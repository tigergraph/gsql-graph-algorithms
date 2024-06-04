/******************************************************************************
 * Copyright (c) 2021, TigerGraph Inc.
 * All rights reserved.
 * Project: TigerGraph Query Language
 *
 * - This library is for defining struct and helper functions that will be used
 *   in the user-defined functions in "tg_ExprFunctions.hpp". Note that functions
 *   defined in this file cannot be directly called from TigerGraph Query scripts.
 *   Please put such functions into "tg_ExprFunctions.hpp" under the same directory
 *   where this file is located.
 *
 * - Please don't remove necessary codes in this file
 *
 * - A backup of this file can be retrieved at
 *     <tigergraph_root_path>/dev_<backup_time>/gdk/gsql/src/QueryUdf/tg_ExprUtil.hpp
 *   after upgrading the system.
 *
 ******************************************************************************/

#ifndef TG_EXPRUTIL_HPP_
#define TG_EXPRUTIL_HPP_

#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <gle/engine/cpplib/headers.hpp>
#include <vector>
#include <chrono>
#include <list>
#include <string>
#include <unordered_map>
#include <tuple>
#include <algorithm>
#include <numeric>
#include <mutex>
#include <condition_variable>
#include <thread>
#include <random>
#include <fstream>
#include <sstream>

namespace tg {

  typedef std::string string; //XXX DON'T REMOVE

  /* ======= START FREQUENT PATTERN MINING ======= */
  const uint64_t BASE = 1ULL << 63;
  const int64_t MOD = 9223372036854775783;
  /* ======= END FREQUENT PATTERN MINING ======== */

  /* ======== START NODE2VEC ==============*/
  typedef std::vector < float > Vector;

  struct Word {
    int32_t index_;
    std::string text_;
    uint32_t count_;
    Word * left_, * right_;

    std::vector < uint8_t > codes_;
    std::vector < uint32_t > points_;

    Word(int32_t index, std::string text, uint32_t count, Word * left = 0, Word * right = 0): index_(index), text_(text), count_(count), left_(left), right_(right) {}
    Word(const Word & ) = delete;
    const Word & operator = (const Word & ) = delete;
  };
  typedef std::shared_ptr < Word > WordP;

  struct Sentence {
    std::vector < Word * > words_;
    std::vector < std::string > tokens_;
  };
  typedef std::shared_ptr < Sentence > SentenceP;

  struct Model {
    std::vector < Vector > syn0_, syn1_;
    std::vector < Vector > syn0norm_;

    //negative sampling
    std::vector < Vector > syn1neg_;
    std::vector < int > unigram_;

    std::unordered_map < std::string, WordP > vocab_;
    std::vector < Word * > words_;

    int layer1_size_;
    int window_;

    //subsampling
    float sample_;

    int min_count_; //minumum count of word (or phrase) appearance to be put into context
    int negative_;

    float alpha_, min_alpha_;

    bool phrase_; //whether consider phrase
    float phrase_threshold_; //threshold for the phrase score to be put into context

    Model(int size = 100, int window = 10, float sample = 0.001, int min_count = 0, int negative = 0, float alpha = 0.025, float min_alpha = 0.0001): layer1_size_(size), window_(window), sample_(sample), min_count_(min_count), negative_(negative), alpha_(alpha), min_alpha_(min_alpha), phrase_(false), phrase_threshold_(100) {}

    bool has(const std::string & w) const {
      return vocab_.find(w) != vocab_.end();
    }

    int build_vocab(std::vector < SentenceP > & sentences) {
      size_t count = 0;
      std::unordered_map < std::string, int > vocab;
      auto progress = [ & count](const char * type,
        const std::unordered_map < std::string, int > & vocab) {
        printf("collecting [%s] %lu sentences, %lu distinct %ss, %d %ss\n", type, count, vocab.size(), type,
          std::accumulate(vocab.begin(), vocab.end(), 0, [](int x,
            const std::pair < std::string, int > & v) {
            return x + v.second;
          }), type);
      }; //show current progress

      // count tokens and phrases, and store the count in vocab
      for (auto & sentence: sentences) {
        ++count;
        if (count % 10000 == 0) progress("word", vocab);

        std::string last_token;
        for (auto & token: sentence -> tokens_) {
          vocab[token] += 1;
          // add bigram phrases
          if (phrase_) {
            if (!last_token.empty()) vocab[last_token + "_" + token] += 1;
            last_token = token;
          }
        }
      }
      progress("word", vocab);

      // if two-word phrases are considered
      if (phrase_) {
        count = 0;
        int total_words = std::accumulate(vocab.begin(), vocab.end(), 0, [](int x,
          const std::pair < std::string, int > & v) {
          return x + v.second;
        }); //total count of words

        std::unordered_map < std::string, int > phrase_vocab;

        //filter the phrases above phrase_threshold, store the count of phrases and words in phrase_vocab, push the token to phrase_tokens
        for (auto & sentence: sentences) {
          ++count;
          if (count % 10000 == 0) progress("phrase", phrase_vocab);

          std::vector < std::string > phrase_tokens;
          std::string last_token;
          uint32_t pa = 0, pb = 0, pab = 0;
          for (auto & token: sentence -> tokens_) {
            pb = vocab[token];
            if (!last_token.empty()) {
              std::string phrase = last_token + "_" + token;
              pab = vocab[phrase];
              float score = 0;
              if (pa >= min_count_ && pb >= min_count_ && pab >= min_count_)
                score = (pab - min_count_) / (float(pa) * pb) * total_words;
              if (score > phrase_threshold_) {
                phrase_tokens.push_back(phrase);
                token.clear();
                phrase_vocab[phrase] += 1;
              } else {
                phrase_tokens.push_back(last_token);
                phrase_vocab[last_token] += 1;
              }
            }
            last_token = token;
            pa = pb;
          }

          if (!last_token.empty()) {
            phrase_tokens.push_back(last_token);
            phrase_vocab[last_token] += 1;
          }
          sentence -> tokens_.swap(phrase_tokens);
        }
        progress("phrase", phrase_vocab);

        printf("using phrases\n");
        vocab.swap(phrase_vocab);
      }

      int n_words = vocab.size();
      if (n_words <= 1) return -1;

      words_.reserve(n_words);
      auto comp = [](Word * w1, Word * w2) {
        return w1 -> count_ > w2 -> count_;
      };

      // populate vocab_ with word (str), [word, count](*Word)
      for (auto & p: vocab) {
        uint32_t count = p.second;
        if (count <= min_count_) continue;

        auto r = vocab_.emplace(p.first, WordP(new Word {
          0,
          p.first,
          count
        }));
        words_.push_back((r.first -> second.get()));
      }
      std::sort(words_.begin(), words_.end(), comp); //sort by count

      int index = 0;
      for (auto & w: words_) w -> index_ = index++; //assign index to all words

      printf("collected %lu distinct words with min_count=%d\n", vocab_.size(), min_count_);

      n_words = words_.size();

      std::vector < Word * > heap = words_;
      std::make_heap(heap.begin(), heap.end(), comp);

      std::vector < WordP > tmp;
      for (int i = 0; i < n_words - 1; ++i) {
        std::pop_heap(heap.begin(), heap.end(), comp);
        auto min1 = heap.back();
        heap.pop_back();
        std::pop_heap(heap.begin(), heap.end(), comp);
        auto min2 = heap.back();
        heap.pop_back();
        tmp.emplace_back(WordP(new Word {
          i + n_words, "", min1 -> count_ + min2 -> count_, min1, min2
        }));

        heap.push_back(tmp.back().get());
        std::push_heap(heap.begin(), heap.end(), comp);
      }

      int max_depth = 0;
      std::list < std::tuple < Word * , std::vector < uint32_t > , std::vector < uint8_t >>> stack;
      stack.push_back(std::make_tuple(heap[0], std::vector < uint32_t > (), std::vector < uint8_t > ()));
      count = 0;
      while (!stack.empty()) {
        auto t = stack.back();
        stack.pop_back();

        Word * word = std::get < 0 > (t);
        if (word -> index_ < n_words) {
          word -> points_ = std::get < 1 > (t);
          word -> codes_ = std::get < 2 > (t);
          max_depth = std::max((int) word -> codes_.size(), max_depth);
        } else {
          auto points = std::get < 1 > (t);
          points.emplace_back(word -> index_ - n_words);
          auto codes1 = std::get < 2 > (t);
          auto codes2 = codes1;
          codes1.push_back(0);
          codes2.push_back(1);
          stack.emplace_back(std::make_tuple(word -> left_, points, codes1));
          stack.emplace_back(std::make_tuple(word -> right_, points, codes2));
        }
      }

      printf("built huffman tree with maximum node depth %d\n", max_depth);

      syn0_.resize(n_words);
      syn1_.resize(n_words);

      std::default_random_engine eng(::time(NULL));
      std::uniform_real_distribution < float > rng(0.0, 1.0);
      for (auto & s: syn0_) {
        s.resize(layer1_size_);
        for (auto & x: s) x = (rng(eng) - 0.5) / layer1_size_;
      }
      for (auto & s: syn1_) s.resize(layer1_size_);

      #if 0
      //TODO: verify
      if (negative_ > 0) {
        syn1neg_.resize(n_words);
        for (auto & s: syn1neg_) s.resize(layer1_size_);

        unigram_.resize(1e8);
        const float power = 0.75;
        float sum = std::accumulate(words_.begin(), words_.end(), 0.0, [ & power](float x, Word * word) {
          return x + ::pow(word -> count_, power);
        });
        float d1 = ::pow(words_[0] -> count_, power) / sum;

        int i = 0;
        for (int a = 0; a < unigram_.size(); ++a) {
          unigram_[a] = i;
          if (float(a) / unigram_.size() > d1) {
            ++i;
            d1 += ::pow(words_[i] -> count_, power) / sum;
          }
          if (i >= words_.size()) i = words_.size() - 1;
        }
      }
      #endif

      return 0;
    }

    int train(std::vector < SentenceP > & sentences, int n_workers) {
      int total_words = std::accumulate(vocab_.begin(), vocab_.end(), 0,
        [](int x,
          const std::pair < std::string, WordP > & p) {
          return (int)(x + p.second -> count_);
        });
      int current_words = 0;
      float alpha0 = alpha_, min_alpha = min_alpha_;

      typedef std::vector < Sentence * > Job;
      typedef std::unique_ptr < Job > JobP;
      std::mutex m;
      std::condition_variable cond_var;
      std::list < JobP > jobs;

      volatile bool done = false;
      auto worker = [ & ]() {
        while (true) {
          JobP job; {
            std::unique_lock < std::mutex > lock(m);
            while (jobs.empty() && !done)
              cond_var.wait(lock);

            if (jobs.empty()) break;

            job = std::move(jobs.front());
            jobs.pop_front();
          }

          if (!job) break;

          auto cstart = std::chrono::high_resolution_clock::now();
          float alpha = std::max(min_alpha, float(alpha0 * (1.0 - 1.0 * current_words / total_words)));
          int words = 0;
          for (auto sentence: * job) {
            words += train_sentence( * sentence, alpha);
          }
          current_words += words;
          auto cend = std::chrono::high_resolution_clock::now();
          auto duration = std::chrono::duration_cast < std::chrono::microseconds > (cend - cstart).count();
          printf("training alpha: %.4f progress: %.2f%% words per thread sec: %.3fK\n", alpha, current_words * 100.0 / total_words, words * 1000.0 / duration);
        }
      };

      auto enqueue_job = [ & ](JobP && job) {
        std::unique_lock < std::mutex > lock(m);
        jobs.push_back(std::forward < JobP > (job));
        cond_var.notify_one();
      };

      std::vector < std::thread > workers;
      for (int i = 0; i < n_workers; ++i)
        workers.push_back(std::thread(worker));

      JobP job(new Job);
      const size_t batch_size = 800;

      std::default_random_engine eng(::time(NULL));
      std::uniform_real_distribution < float > rng(0.0, 1.0);

      for (auto & sentence: sentences) {
        if (sentence -> tokens_.empty())
          continue;
        size_t len = sentence -> tokens_.size();
        sentence -> words_.reserve(len);
        for (size_t i = 0; i < len; ++i) {
          auto it = vocab_.find(sentence -> tokens_[i]);
          if (it == vocab_.end()) continue;
          Word * word = it -> second.get();
          // subsampling
          if (sample_ > 0) {
            float rnd = (sqrt(word -> count_ / (sample_ * total_words)) + 1) * (sample_ * total_words) / word -> count_;
            if (rnd < rng(eng)) continue;
          }
          sentence -> words_.push_back(it -> second.get());
        }

        job -> push_back(sentence.get());
        if (job -> size() == batch_size) {
          enqueue_job(std::move(job));
          job.reset(new Job);
        }
      }

      if (!job -> empty())
        enqueue_job(std::move(job));

      done = true;
      for (int i = 0; i < n_workers; ++i) enqueue_job(JobP());
      for (auto & t: workers) t.join();

      syn0norm_ = syn0_;
      for (auto & v: syn0norm_) unit(v);

      return 0;
    }

    int save(const std::string & file) const {
      std::ofstream out(file, std::ofstream::out);
      out << syn0_.size() << " " << syn0_[0].size() << std::endl;

      std::vector < Word * > words = words_;
      std::sort(words.begin(), words.end(), [](Word * w1, Word * w2) {
        return w1 -> count_ > w2 -> count_;
      });

      for (auto w: words) {
        out << w -> text_;
        for (auto i: syn0_[w -> index_]) out << " " << i;
        out << std::endl;
      }

      return 0;
    }

    int load(const std::string & file) {
      std::ifstream in (file);
      std::string line;
      if (!std::getline( in , line)) return -1;

      int n_words = 0, layer1_size = 0;
      std::istringstream iss(line);
      iss >> n_words >> layer1_size;

      syn0_.clear();
      vocab_.clear();
      words_.clear();
      syn0_.resize(n_words);
      for (int i = 0; i < n_words; ++i) {
        if (!std::getline( in , line)) return -1;

        std::istringstream iss(line);
        std::string text;
        iss >> text;

        auto p = vocab_.emplace(text, WordP(new Word {
          i,
          text,
          0
        }));
        words_.push_back(p.first -> second.get());
        syn0_[i].resize(layer1_size);
        for (int j = 0; j < layer1_size; ++j) {
          iss >> syn0_[i][j];
        }
      }

      layer1_size_ = layer1_size;
      printf("%d words loaded\n", n_words);

      syn0norm_ = syn0_;
      for (auto & v: syn0norm_) unit(v);

      return 0;
    }

    std::vector < std::pair < std::string, float >> most_similar(std::vector < std::string > positive, std::vector < std::string > negative, int topn) {
      if ((positive.empty() && negative.empty()) || syn0norm_.empty()) return std::vector < std::pair < std::string, float >> {};

      Vector mean(layer1_size_);
      std::vector < int > all_words;
      auto add_word = [ & mean, & all_words, this](const std::string & w, float weight) {
        auto it = vocab_.find(w);
        if (it == vocab_.end()) return;

        Word & word = * it -> second;
        saxpy(mean, weight, syn0norm_[word.index_]);

        all_words.push_back(word.index_);
      };

      for (auto & w: positive) add_word(w, 1.0);
      for (auto & w: negative) add_word(w, -1.0);

      unit(mean);

      Vector dists;
      std::vector < int > indexes;
      int i = 0;

      dists.reserve(syn0norm_.size());
      indexes.reserve(syn0norm_.size());
      for (auto & x: syn0norm_) {
        dists.push_back(dot(x, mean));
        indexes.push_back(i++);
      }

      auto comp = [ & dists](int i, int j) {
        return dists[i] > dists[j];
      };
      //              std::sort(indexes.begin(), indexes.end(), comp);

      int k = std::min(int(topn + all_words.size()), int(indexes.size()) - 1);
      auto first = indexes.begin(), last = indexes.begin() + k, end = indexes.end();
      std::make_heap(first, last + 1, comp);
      std::pop_heap(first, last + 1, comp);
      for (auto it = last + 1; it != end; ++it) {
        if (!comp( * it, * first)) continue;
        * last = * it;
        std::pop_heap(first, last + 1, comp);
      }

      std::sort_heap(first, last, comp);

      std::vector < std::pair < std::string, float >> results;
      for (int i = 0, j = 0; i < k; ++i) {
        if (std::find(all_words.begin(), all_words.end(), indexes[i]) != all_words.end())
          continue;
        results.push_back(std::make_pair(words_[indexes[i]] -> text_, dists[indexes[i]]));
        if (++j >= topn) break;
      }

      return results;
    }

    private:
      int train_sentence(Sentence & sentence, float alpha) {
        const int max_size = 1000;
        const float max_exp = 6.0;
        const static std::vector < float > table = [ & ]() {
          std::vector < float > x(max_size);
          for (size_t i = 0; i < max_size; ++i) {
            float f = exp((i / float(max_size) * 2 - 1) * max_exp);
            x[i] = f / (f + 1);
          }
          return x;
        }();

        int count = 0;
        int len = sentence.words_.size();
        int reduced_window = rand() % window_;
        for (int i = 0; i < len; ++i) {
          const Word & current = * sentence.words_[i];
          size_t codelen = current.codes_.size();

          int j = std::max(0, i - window_ + reduced_window);
          int k = std::min(len, i + window_ + 1 - reduced_window);
          for (; j < k; ++j) {
            const Word * word = sentence.words_[j];
            if (j == i || word -> codes_.empty())
              continue;
            int word_index = word -> index_;
            auto & l1 = syn0_[word_index]; //layer1 weight

            Vector work(layer1_size_);
            for (size_t b = 0; b < codelen; ++b) {
              int idx = current.points_[b];
              auto & l2 = syn1_[idx]; //layer2 weight

              float f = dot(l1, l2);
              if (f <= -max_exp || f >= max_exp)
                continue;

              int fi = int((f + max_exp) * (max_size / max_exp / 2.0));

              f = table[fi]; //prediction
              //                              f = sigmoid(f);
              float g = (1 - current.codes_[b] - f) * alpha; //codes_ : one-hot label

              saxpy(work, g, l2);
              saxpy(l2, g, l1);

              //                              work += syn1_[idx] * g;
              //                              syn1_[idx] += syn0_[word_index] * g;
            }

            //negative sampling
            #if 0
            if (negative_ > 0) {
              for (int d = 0; d < negative_ + 1; ++d) {
                int label = (d == 0 ? 1 : 0);
                int target = 0;
                if (d == 0) target = i;
                else {
                  target = unigram_[rand() % unigram_.size()];
                  if (target == 0) target = rand() % (vocab_.size() - 1) + 1;
                  if (target == i) continue;
                }

                auto & l2 = syn1neg_[target];
                float f = dot(l1, l2), g = 0;
                if (f > max_exp) g = (label - 1) * alpha;
                else if (f < -max_exp) g = (label - 0) * alpha;
                else {
                  int fi = int((f + max_exp) * (max_size / max_exp / 2.0));
                  g = (label - table[fi]) * alpha;
                }

                saxpy(work, g, l2);
                saxpy(l2, g, l1);

              }
            }
            #endif

            //                              syn0_[word_index] += work;
            saxpy(l1, 1.0, work);
          }
          ++count;
        }
        return count;
      }

    float similarity(const std::string & w1,
      const std::string & w2) const {
      auto it1 = vocab_.find(w1), it2 = vocab_.find(w2);
      if (it1 != vocab_.end() && it2 != vocab_.end())
        return dot(syn0_[it1 -> second -> index_], syn0_[it2 -> second -> index_]);
      return 0;
    }

    static inline float dot(const Vector & x,
      const Vector & y) {
      int m = x.size();
      const float * xd = x.data(),
        * yd = y.data();
      float sum = 0.0;
      while (--m >= 0) sum += ( * xd++) * ( * yd++);
      return sum;
    }

    static inline void saxpy(Vector & x, float g,
      const Vector & y) {
      int m = x.size();
      float * xd = x.data();
      const float * yd = y.data();
      while (--m >= 0)( * xd++) += g * ( * yd++);
    }

    static inline void unit(Vector & x) {
      float len = ::sqrt(dot(x, x));
      if (len == 0) return;

      int m = x.size();
      float * xd = x.data();
      while (--m >= 0)( * xd++) /= len;
    }
  };

  /* ============ END NODE2VEC =============== */

  /* ============== START Milvus =========== */
  class tg_MilvusUtil {
  public:
    tg_MilvusUtil(const std::string& host, int port) {
        this->host = host;
        this->port = port;
        curl_global_init(CURL_GLOBAL_ALL);
    }

    ~tg_MilvusUtil() {
        curl_global_cleanup();
    }

    std::vector<float> stringToFloatVector(const std::string& str, char delimiter = ',') {
        std::vector<float> result;
        std::stringstream ss(str);
        std::string item;

        while (std::getline(ss, item, delimiter)) {
            try {
            result.push_back(std::stof(item));
            } catch (const std::invalid_argument& ia) {
            std::cerr << "Invalid argument: " << ia.what() << '\n';
            } catch (const std::out_of_range& oor) {
            std::cerr << "Out of Range error: " << oor.what() << '\n';
            }
        }

        return result;
    }

    ListAccum<std::string> search(const std::string& collection_name, const std::string& vector_field_name,
                        const std::string& vertex_id_field_name, const std::vector<float>& query_vector, const std::string& metric_type, int top_k) const {
        ListAccum<std::string> vertexIdList;

        Json::Value search_body;
        search_body["collectionName"] = collection_name;
        
        // Convert query_vector to Json::Value format
        for (const auto& val : query_vector) {
            search_body["vector"].append(val);
        }

        search_body["outputFields"] = Json::arrayValue;
        search_body["outputFields"].append("pk");
        search_body["outputFields"].append(vertex_id_field_name);
        search_body["limit"] = top_k;

        // You may need to adjust 'search_body' to match the exact format expected by your Milvus server version

        CURL* curl = curl_easy_init();
        if (curl) {
            CURLcode res;
            std::string readBuffer;            
            std::string url;
            
            if (host.substr(0, 4) == "http" && host.find(":") != std::string::npos && host.find(std::to_string(port)) != std::string::npos) {
                url = host + "/v1/vector/search";
            } else if (host.substr(0, 4) == "http") {
                url = host + ":" + std::to_string(port) + "/v1/vector/search";
            } else {
                url = "http://" + host + ":" + std::to_string(port) + "/v1/vector/search";
            }

            Json::StreamWriterBuilder writerBuilder;
            std::string requestBody = Json::writeString(writerBuilder, search_body);

            curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
            curl_easy_setopt(curl, CURLOPT_POST, 1L);
            curl_easy_setopt(curl, CURLOPT_POSTFIELDS, requestBody.c_str());
            curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
            curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);

            struct curl_slist *headers = NULL;
            headers = curl_slist_append(headers, "Content-Type: application/json");
            curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);

            res = curl_easy_perform(curl);
            if (res != CURLE_OK) {
                std::cerr << "curl_easy_perform() failed: " << curl_easy_strerror(res) << std::endl;
            } else {
                Json::CharReaderBuilder readerBuilder;
                Json::Value json_response;
                std::unique_ptr<Json::CharReader> const reader(readerBuilder.newCharReader());
                std::string parseErrors;

                bool parsingSuccessful = reader->parse(readBuffer.c_str(), readBuffer.c_str() + readBuffer.size(), &json_response, &parseErrors);
                
                if (parsingSuccessful) {
                    std::cout << "JSON successfully parsed" << std::endl;
                } else {
                    // If parsing was unsuccessful, print the errors encountered
                    std::cerr << "Failed to parse JSON: " << parseErrors << std::endl;
                }

                if (parsingSuccessful) {
                    for (const auto& item : json_response["data"]) {
                        std::string pk = item["pk"].asString();
                        std::string vertex_id_str = item[vertex_id_field_name].asString();
                        std::cout << "Vector ID: " << pk << "\tVertex ID: " << vertex_id_str << std::endl;
                        vertexIdList += vertex_id_str;
                    }
                }
            }

            curl_easy_cleanup(curl);
            curl_slist_free_all(headers);
        }

        return vertexIdList;
    }

  private:
    std::string host;
    int port;

    static size_t WriteCallback(void *contents, size_t size, size_t nmemb, std::string *userp) {
        userp->append((char*)contents, size * nmemb);
        return size * nmemb;
    }
  };

  /* ============== END Milvus =========== */
  
  /* ============== START A STAR =========== */

  inline float rad(float d) {
    return d * 3.1415926535897932384626433832795 / 180.0;
  }

  /* ============== END A STAR =========== */

  /* ============ START APPROXIMATE NEAREST NEIGHBORS =============== */

  template < typename T >
    inline double tg_euclidean_distance_accum(ListAccum < T > & A, ListAccum < T > & B) {
      int n = A.size();
      double euclidean_distance = 0.0;
      for (int i = 0; i < n; i++)
        euclidean_distance += (A.get(i) - B.get(i)) * (A.get(i) - B.get(i));

      euclidean_distance = std::sqrt(euclidean_distance);
      return euclidean_distance;
    }

  template < typename T >
    inline double tg_cosine_similarity_accum(ListAccum < T > & A, ListAccum < T > & B) {
      int n = A.size();
      double mean_A = 0.0, mean_B = 0.0, inner = 0.0, magnitude_A = 0.0, magnitude_B = 0.0;
      for (int i = 0; i < n; i++) {
        inner += A.get(i) * B.get(i);
        magnitude_A += A.get(i) * A.get(i);
        magnitude_B += B.get(i) * B.get(i);
      }

      double cosine_similarity = inner / std::sqrt(magnitude_A * magnitude_B);
      return cosine_similarity;
    }

  template < typename T >
    inline double tg_jaccard_similarity_accum(ListAccum < T > & A, ListAccum < T > & B) {
      std::sort(std::begin(A.data_), std::end(A.data_));
      std::sort(std::begin(B.data_), std::end(B.data_));

      std::vector < T > intersection_list;

      std::set_intersection(
        std::begin(A.data_), std::end(A.data_), std::begin(B.data_), std::end(B.data_), std::back_inserter(intersection_list));

      int cardinality_A = A.size(), cardinality_B = B.size(), cardinality_intersection = intersection_list.size();

      double jaccard_similarity = cardinality_intersection * (1.0 / (cardinality_A + cardinality_B - cardinality_intersection));
      return jaccard_similarity;
    }

  template < typename T >
    inline double tg_overlap_similarity_accum(ListAccum < T > & A, ListAccum < T > & B) {
      std::sort(std::begin(A.data_), std::end(A.data_));
      std::sort(std::begin(B.data_), std::end(B.data_));

      std::vector < T > intersection_list;

      std::set_intersection(
        std::begin(A.data_), std::end(A.data_), std::begin(B.data_), std::end(B.data_), std::back_inserter(intersection_list));

      int cardinality_A = A.size(), cardinality_B = B.size(), cardinality_intersection = intersection_list.size();

      double overlap_similarity = cardinality_intersection * (1.0 / std::min(cardinality_A, cardinality_B));
      return overlap_similarity;
    }

  template < typename T >
    inline double tg_pearson_similarity_accum(ListAccum < T > & A, ListAccum < T > & B) {
      int n = A.size();
      double mean_A = 0.0, mean_B = 0.0, covariance = 0.0, std_dev_A = 0.0, std_dev_B = 0.0;
      for (int i = 0; i < n; i++) {
        mean_A += A.get(i);
        mean_B += B.get(i);
      }
      mean_A /= n;
      mean_B /= n;

      for (int i = 0; i < n; i++) {
        double diff_A = A.get(i) - mean_A, diff_B = B.get(i) - mean_B;
        covariance += diff_A * diff_B;
        std_dev_A += diff_A * diff_A;
        std_dev_B += diff_B * diff_B;
      }

      double pearson_similarity = covariance / std::sqrt(std_dev_A * std_dev_B);
      return pearson_similarity;
    }

  /* ============ END APPROXIMATE NEAREST NEIGHBORS =============== */

  /*
   * Define structs that used in the functions in "ExprFunctions.hpp"
   * below. For example,
   *
   *   struct Person {
   *     string name;
   *     int age;
   *     double height;
   *     double weight;
   *   }
   *
   */
}

#endif /* TG_EXPRUTIL_HPP_ */

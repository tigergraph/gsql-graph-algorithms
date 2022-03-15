/******************************************************************************
 * Copyright (c) 2015-2021, TigerGraph Inc.
 * All rights reserved.
 * Project: TigerGraph Query Language
 * udf.hpp: a library of user defined functions used in queries.
 *
 * - This library should only define functions that will be used in
 *   TigerGraph Query scripts. Other logics, such as structs and helper
 *   functions that will not be directly called in the GQuery scripts,
 *   must be put into "tg_ExprUtil.hpp" under the same directory where
 *   this file is located.
 *
 * - Supported type of return value and parameters
 *     - int
 *     - float
 *     - double
 *     - bool
 *     - string (don't use std::string)
 *     - accumulators
 *
 * - Function names are case sensitive, unique, and can't be conflict with
 *   built-in math functions and reserve keywords.
 *
 * - Please don't remove necessary codes in this file
 *
 * - A backup of this file can be retrieved at
 *     <tigergraph_root_path>/dev_<backup_time>/gdk/gsql/src/QueryUdf/tg_ExprFunctions.hpp
 *   after upgrading the system.
 *
 ******************************************************************************/

#ifndef TG_EXPRFUNCTIONS_HPP_
#define TG_EXPRFUNCTIONS_HPP_

#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <gle/engine/cpplib/headers.hpp>
#include <algorithm>
#include <functional>
#include <chrono>
#include <iostream>
#include <fstream>
#include <sstream>
#include <map>
#include <random>
#include <vector>
#include <math.h>

/**     XXX Warning!! Put self-defined struct in tg_ExprUtil.hpp **
 *  No user defined struct, helper functions (that will not be directly called
 *  in the GQuery scripts) etc. are allowed in this file. This file only
 *  contains user-defined expression function's signature and body.
 *  Please put user defined structs, helper functions etc. in tg_ExprUtil.hpp
 */
#include "tg_ExprUtil.hpp"

namespace UDIMPL {
  typedef std::string string; //XXX DON'T REMOVE

  /* ============== START MAP EQUATION ======================== */

  inline double tg_log_2(double num) {
    return log2(num);
  }

  /* ============== END MAP EQUATION ======================== */


  /* ============== START SPEAKER LISTENER LABEL PROP ================== */

  inline double tg_getVal(ListAccum < double > & list, int64_t i) {
    return list.get(i);
  }

  inline void tg_getVertexesFromEdge(SetAccum < EDGE > & edgeSet, SetAccum < VERTEX > & res) {
    for (auto it = edgeSet.data_.begin(); it != edgeSet.data_.end(); ++it) {
      res += it -> srcVid;
      res += it -> tgtVid;
    }
  }

  inline int64_t tg_rand_int(int minVal, int maxVal) {
    std::random_device rd;
    std::mt19937 e1(rd());
    std::uniform_int_distribution < int > dist(minVal, maxVal);
    return (int64_t) dist(e1);
  }

  /* ============== END SPEAKER LISTENER LABEL PROP ================== */

  /* ============== START FREQUENT PATTERN MINING ===================== */

  inline int64_t tg_get_hash(int64_t id) {
    int64_t hash_val = id % tg::MOD;
    return hash_val;
  }

  template < typename tup >
    inline int64_t tg_get_pattern_key(MaxAccum < tup > t) {
      tup in_data = t;
      return in_data.pattern_key;
    }

  template < typename tup >
    inline int64_t tg_get_suffix_key(MaxAccum < tup > t) {
      tup in_data = t;
      return in_data.suffix_key;
    }
  inline ListAccum < int64_t > tg_initiate_hash_const(int length) {
    ListAccum < int64_t > return_arr;
    __int128_t promoter;

    return_arr += 1;

    for (int i = 1; i < length + 1; i++) {
      promoter = return_arr.get(i - 1);

      promoter *= tg::BASE;
      promoter %= tg::MOD;

      return_arr += static_cast < int64_t > (promoter);
    }

    return return_arr;
  }
  inline int64_t tg_get_hash_without_first_element(int64_t hash_val, int64_t first, int size,
    const ListAccum < int64_t > & HASH_CONST) {
    __int128_t promoter = hash_val;

    __int128_t first_hash = first;
    first_hash *= HASH_CONST.get(size - 1);
    first_hash %= tg::MOD;

    promoter -= first_hash;

    promoter %= tg::MOD;
    promoter += tg::MOD;
    promoter %= tg::MOD;

    promoter *= tg::BASE;
    promoter %= tg::MOD;

    return static_cast < int64_t > (promoter);
  }

  inline int64_t tg_get_hash_without_last_element(int64_t hash_val, int64_t last) {
    __int128_t promoter = hash_val;
    promoter -= last;
    promoter %= tg::MOD;
    promoter += tg::MOD;
    promoter %= tg::MOD;

    return promoter;
  }

  inline int64_t tg_get_hash_concat(int64_t hash_val, int64_t appender) {
    __int128_t promoter = hash_val;

    promoter *= tg::BASE;
    promoter %= tg::MOD;

    promoter += appender;
    promoter %= tg::MOD;

    return static_cast < int64_t > (promoter);
  }

  inline bool tg_is_subset(const ListAccum < int64_t > & subset, int64_t ending, ListAccum < int64_t > & superset) {

    int curr_pos = 0;
    int i = 0;

    for (i = 0; i < superset.size(); ++i) {
      if (superset.get(i) == subset.get(curr_pos)) {
        ++curr_pos;
        if (curr_pos == subset.size()) {
          break;
        }
      }
    }
    if (curr_pos != subset.size()) {
      return false;
    }

    for (int j = i + 1; j < superset.size(); ++j) {
      if (superset.get(j) == ending) {
        return true;
      }
    }

    return false;

  }

  inline ListAccum < int64_t > tg_concat(ListAccum < int64_t > original_list, int64_t appending_element) {
    original_list += appending_element;

    return original_list;
  }
  inline ListAccum < VERTEX > tg_to_vertex_list(const ListAccum < int64_t > & l) {
    ListAccum < VERTEX > v_list;
    for (int i = 0; i < l.size(); ++i) {
      v_list += VERTEX(l.get(i));
    }
    return v_list;
  }
  template < typename tup >
    inline tup tg_get_tup(MaxAccum < tup > val) {
      tup new_tup = val;
      return new_tup;
    }

  /* ============== END FREQUENT PATTERN MINING ===================== */

  /* ============== START EMBEDDING SIMILARITY ===================== */

  inline MapAccum < int, double > tg_cosine_similarity(ListAccum < double > emb1, MapAccum < int, ListAccum < double >> other_vertices, int embeddingDim) {
    std::vector < double > v1(embeddingDim);
    for (int e = 0; e < embeddingDim; e++) {
      v1[e] = emb1.get(e);
    }
    std::vector < double > v2(embeddingDim);

    MapAccum < int, double > results;
    for (auto it = std::begin(other_vertices); it != std::end(other_vertices); it++) {
      for (int e = 0; e < embeddingDim; e++) {
        v2[e] = it -> second.get(e);
      }
      double dot = std::inner_product(std::begin(v1), std::end(v1), std::begin(v2), 0.0);
      double sim = (dot / (
        sqrt(std::inner_product(std::begin(v1), std::end(v1), std::begin(v1), 0.0)) *
        sqrt(std::inner_product(std::begin(v2), std::end(v2), std::begin(v2), 0.0))));
      MapAccum < int, double > temp(it -> first, sim);
      results += temp;
    }
    return results;
  }

  /* ============== END EMBEDDING SIMILARITY ===================== */

  /* ============== START PAIRWISE EMBEDDING SIMILARITY ===================== */

  inline double tg_pairwise_cosine_similarity(ListAccum < double > emb1, ListAccum < double > emb2, int embeddingDim) {
    std::vector < double > v1(embeddingDim);
    std::vector < double > v2(embeddingDim);
    for (int e = 0; e < embeddingDim; e++) {
      v1[e] = emb1.get(e);
      v2[e] = emb2.get(e);
    }
    double dot = std::inner_product(std::begin(v1), std::end(v1), std::begin(v2), 0.0);
    double res = (dot / (
      sqrt(std::inner_product(std::begin(v1), std::end(v1), std::begin(v1), 0.0)) *
      sqrt(std::inner_product(std::begin(v2), std::end(v2), std::begin(v2), 0.0))));
    return res;
  }

  /* ============== END PAIRWISE EMBEDDING SIMILARITY ===================== */

  /* ============== START FAST RP ================= */

  inline ListAccum < float > tg_extract_list(string weights) {
    ListAccum < float > wghts;
    string current_weight;
    std::stringstream s_stream(weights);
    while (s_stream.good()) {
      std::getline(s_stream, current_weight, ',');
      wghts.data_.push_back(std::stof(current_weight));
    }
    return wghts;
  }

  inline float tg_fastrp_rand_func(int64_t v_id, int64_t emb_idx, int64_t seed, int64_t s) {
    std::hash < std::string > hasher;
    auto hash = hasher(std::to_string(v_id) + "," + std::to_string(emb_idx) + "," + std::to_string(seed));

    std::mt19937 gen(hash);
    std::uniform_real_distribution < float > distribution(0.0, 1.0);
    float p1 = 0.5 / s, p2 = p1, p3 = 1 - 1.0 / s;
    float v1 = sqrt(s), v2 = -v1, v3 = 0.0;

    float random_value = distribution(gen);
    if (random_value <= p1)
      return v1;
    else if (random_value <= p1 + p2)
      return v2;
    else
      return v3;
  }

  /* ============== END FAST RP ================= */

  /* ============== START NODE2VEC ================= */

  // node2vec function: given random walk sequence, this function trains vector using skip-gram model
  inline void tg_node2vec_sub(int dimension, string input_file, string output_file) {
    tg::Model model(dimension);
    model.sample_ = 0;
    // model.window = 10;
    int n_workers = 4;
    std::vector < tg::SentenceP > sentences;

    size_t count = 0;
    const size_t max_sentence_len = 200;

    tg::SentenceP sentence(new tg::Sentence);
    std::ifstream in (input_file);
    while (true) {
      std::string s; in >> s;
      if (s.empty()) break;
      ++count;
      sentence -> tokens_.push_back(std::move(s));
      if (count == max_sentence_len) {
        count = 0;
        sentences.push_back(std::move(sentence));
        sentence.reset(new tg::Sentence);
      }
    }

    if (!sentence -> tokens_.empty())
      sentences.push_back(std::move(sentence));

    model.build_vocab(sentences);
    model.train(sentences, n_workers);
    model.save(output_file);

  }

  // random function, generate a random value between 0 and 1
  inline float tg_random() {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution < > dis(0, 1);
    return dis(gen);
  }

  // generate a int random value given a range
  inline int tg_random_range(int start, int end) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution < > dis(start, end);
    return dis(gen);

  }
  // generate a random value based on probability distribution
  // For example: given {0.5,0.3,0.2}, this function will generate {0,1,2} based on its probability
  inline int tg_random_distribution(ListAccum < float > p) {
    std::vector < float > a;
    for (auto it: p.data_) {
      a.push_back(it);
    }
    std::random_device rd;
    std::mt19937 gen(rd());
    std::discrete_distribution < > dis(a.begin(), a.end());
    return dis(gen);
  }

  /* ============== END NODE2VEC ================= */

  /* ============== START A STAR =========== */

  /* ALREADY DEFINED
  inline double getVal (ListAccum<double>& list, int64_t i) {
    return list.get(i);
  }
  */
  
  inline float tg_GetDistance(float lat1, float lng1, float lat2, float lng2) {
    float a;
    float b;
    float radLat1 = tg::rad(lat1);
    float radLat2 = tg::rad(lat2);
    a = radLat1 - radLat2;
    b = tg::rad(lng1) - tg::rad(lng2);
    float s = 2 * asin(sqrt(pow(sin(a / 2), 2) + cos(radLat1) * cos(radLat2) * pow(sin(b / 2), 2)));
    s = s * 6378.137;
    s = s / 1000;
    return s;
  }

  /* ============== END A STAR =========== */

  /* ============== START MAXIMAL INDEPENDENT SET ===== */

  /* ALREADY DEFINED
  inline int64_t rand_int (int minVal, int maxVal) {
    std::random_device rd;
    std::mt19937 e1(rd());
    std::uniform_int_distribution<int> dist(minVal, maxVal);
    return (int64_t) dist(e1);

  }
  */

  /* ============== END MAXIMAL INDEPENDENT SET ===== */

  /* ============== START APPROXIMATE NEAREST NEIGHBORS ===== */

  template < typename T >
    inline double tg_similarity_accum(ListAccum < T > A, ListAccum < T > B,
      const string & similarity_type) {
      double similarity = 0;
      if (similarity_type.compare("COSINE") == 0) {
        similarity = tg::tg_cosine_similarity_accum(A, B);
      } else if (similarity_type.compare("JACCARD") == 0) {
        similarity = tg::tg_jaccard_similarity_accum(A, B);
      } else if (similarity_type.compare("EUCLIDEAN") == 0) {
        similarity = tg::tg_euclidean_distance_accum(A, B);
      } else if (similarity_type.compare("OVERLAP") == 0) {
        similarity = tg::tg_overlap_similarity_accum(A, B);
      } else if (similarity_type.compare("PEARSON") == 0) {
        similarity = tg::tg_pearson_similarity_accum(A, B);
      }
      return similarity;
    }

  /* =========== END APPROXIMATE NEAREST NEIGHBORS ============= */

}

/****************************************/

#endif /* TG_EXPRFUNCTIONS_HPP_ */

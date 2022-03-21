#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <gle/engine/cpplib/headers.hpp>
#include <iostream>
#include <random>
#include <sstream>
#include <string>
#include <math.h>
#include <functional>

inline ListAccum<float> tg_extract_list(string weights){
  ListAccum<float> wghts;
  string current_weight;
  std::stringstream s_stream(weights);
  while (s_stream.good()) {
    std::getline(s_stream, current_weight, ',');
    wghts.data_.push_back(std::stof(current_weight));
  }
  return wghts;
}

inline float tg_fastrp_rand_func(int64_t v_id, int64_t emb_idx, int64_t seed, int64_t s){	  
  std::hash<std::string> hasher;
  auto hash = hasher(std::to_string(v_id) + "," + std::to_string(emb_idx) + "," + std::to_string(seed));

  std::mt19937 gen(hash);
  std::uniform_real_distribution<float> distribution(0.0, 1.0);
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

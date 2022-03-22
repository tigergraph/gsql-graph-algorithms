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


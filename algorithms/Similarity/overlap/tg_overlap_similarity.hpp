#include <stdio.h>
#include <stdlib.h>

#include <algorithm>
// #include <gle/engine/cpplib/headers.hpp>
#include <cmath>
#include <string>
#include <vector>

typedef std::string string;

template <typename T>
inline double tg_overlap_similarity(std::vector<T> A, std::vector<T> B) {
  std::sort(std::begin(A), std::end(A));
  std::sort(std::begin(B), std::end(B));

  std::vector<T> intersection_list;

  std::set_intersection(
      std::begin(A), std::end(A), std::begin(B), std::end(B), std::back_inserter(intersection_list));

  int cardinality_A = A.size(), cardinality_B = B.size(), cardinality_intersection = intersection_list.size();

  double overlap_similarity = cardinality_intersection * (1.0 / std::min(cardinality_A, cardinality_B));
  return overlap_similarity;
}

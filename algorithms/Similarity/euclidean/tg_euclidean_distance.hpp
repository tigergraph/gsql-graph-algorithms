#include <stdio.h>
#include <stdlib.h>

#include <algorithm>
// #include <gle/engine/cpplib/headers.hpp>
#include <cmath>
#include <string>
#include <vector>

typedef std::string string;

template <typename T>
inline double tg_euclidean_distance(std::vector<T> A, std::vector<T> B) {
  int n = A.size();
  double euclidean_distance = 0.0;
  for (int i = 0; i < n; i++)
    euclidean_distance += (A[i] - B[i]) * (A[i] - B[i]);

  euclidean_distance = std::sqrt(euclidean_distance);
  return euclidean_distance;
}
template <>
inline double tg_euclidean_distance(std::vector<string> A, std::vector<string> B) = delete;
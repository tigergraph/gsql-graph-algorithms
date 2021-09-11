#include <stdio.h>
#include <stdlib.h>

#include <algorithm>
// #include <gle/engine/cpplib/headers.hpp>
#include <cmath>
#include <string>
#include <vector>

typedef std::string string;

template <typename T>
inline double tg_cosine_similarity(std::vector<T> A, std::vector<T> B) {
  int n = A.size();
  double mean_A = 0.0, mean_B = 0.0, inner = 0.0, magnitude_A = 0.0, magnitude_B = 0.0;
  for (int i = 0; i < n; i++) {
    inner += A[i] * B[i];
    magnitude_A += A[i] * A[i];
    magnitude_B += B[i] * B[i];
  }

  double cosine_similarity = inner / std::sqrt(magnitude_A * magnitude_B);
  return cosine_similarity;
}
template <>
inline double tg_cosine_similarity(std::vector<string> A, std::vector<string> B) = delete;

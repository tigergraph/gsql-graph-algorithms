#include <stdio.h>
#include <stdlib.h>

#include <algorithm>
// #include <gle/engine/cpplib/headers.hpp>
#include <cmath>
#include <string>
#include <vector>

typedef std::string string;

template <typename T>
inline double tg_pearson_similarity(std::vector<T> A, std::vector<T> B) {
  int n = A.size();
  double mean_A = 0.0, mean_B = 0.0, covariance = 0.0, std_dev_A = 0.0, std_dev_B = 0.0;
  for (int i = 0; i < n; i++) {
    mean_A += A[i];
    mean_B += B[i];
  }
  mean_A /= n;
  mean_B /= n;

  // note both covariance and std_dev are divided by n, therefore not necessary to include
  for (int i = 0; i < n; i++) {
    double diff_A = A[i] - mean_A, diff_B = B[i] - mean_B;
    covariance += diff_A * diff_B;
    std_dev_A += diff_A * diff_A;
    std_dev_B += diff_B * diff_B;
  }

  double pearson_similarity = covariance / std::sqrt(std_dev_A * std_dev_B);
  return pearson_similarity;
}

template <typename T>
inline double tg_pearson_similarity_accum(ListAccum<T>& A, ListAccum<T>& B) {
  int n = A.size();
  double mean_A = 0.0, mean_B = 0.0, covariance = 0.0, std_dev_A = 0.0, std_dev_B = 0.0;
  for (int i = 0; i < n; i++) {
    mean_A += A.get(i);
    mean_B += B.get(i);
  }
  mean_A /= n;
  mean_B /= n;

  // note both covariance and std_dev are divided by n, therefore not necessary to include
  for (int i = 0; i < n; i++) {
    double diff_A = A.get(i) - mean_A, diff_B = B.get(i) - mean_B;
    covariance += diff_A * diff_B;
    std_dev_A += diff_A * diff_A;
    std_dev_B += diff_B * diff_B;
  }

  double pearson_similarity = covariance / std::sqrt(std_dev_A * std_dev_B);
  return pearson_similarity;
}
#include <stdio.h>
#include <stdlib.h>

#include <algorithm>
// #include <gle/engine/cpplib/headers.hpp>
#include <cmath>
#include <string>
#include <vector>

typedef std::string string;

template <typename T>
inline double tg_similarity(std::vector<T> A, std::vector<T> B, const string& similarity_type) {
    double similarity;
    switch (similarity_type) {
        case "cosine":
            int n = A.size();
            double mean_A = 0.0, mean_B = 0.0, inner = 0.0, magnitude_A = 0.0, magnitude_B = 0.0;
            for (int i = 0; i < n; i++) {
                inner += A[i] * B[i];
                magnitude_A += A[i] * A[i];
                magnitude_B += B[i] * B[i];
            }

            double cosine_similarity = inner / std::sqrt(magnitude_A * magnitude_B);
            similarity = cosine_similarity;
            break;
        case "euclidean":
            int n = A.size();
            double euclidean_distance = 0.0;
            for (int i = 0; i < n; i++)
                euclidean_distance += (A[i] - B[i]) * (A[i] - B[i]);

            euclidean_distance = std::sqrt(euclidean_distance);
            similarity = euclidean_distance;
            break;
        case "jaccard":
            std::sort(std::begin(A), std::end(A));
            std::sort(std::begin(B), std::end(B));

            std::vector<T> intersection_list;

            std::set_intersection(
                std::begin(A), std::end(A), std::begin(B), std::end(B), std::back_inserter(intersection_list));

            int cardinality_A = A.size(), cardinality_B = B.size(), cardinality_intersection = intersection_list.size();

            double jaccard_similarity = cardinality_intersection * (1.0 / (cardinality_A + cardinality_B - cardinality_intersection));
            similarity = jaccard_similarity;
            break;
        case "overlap":
            std::sort(std::begin(A), std::end(A));
            std::sort(std::begin(B), std::end(B));

            std::vector<T> intersection_list;

            std::set_intersection(
                std::begin(A), std::end(A), std::begin(B), std::end(B), std::back_inserter(intersection_list));

            int cardinality_A = A.size(), cardinality_B = B.size(), cardinality_intersection = intersection_list.size();

            double overlap_similarity = cardinality_intersection * (1.0 / std::min(cardinality_A, cardinality_B));
            similarity = overlap_similarity;
            break;
        case "pearson":
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
            similarity = pearson_similarity;
            break;
    }

    return similarity;
}




template <typename T>
inline double tg_similarity_accum(ListAccum<T>& A, ListAccum<T>& B, const string& similarity_type) {
    double similarity;
    switch (similarity_type) {
        case "cosine":
            int n = A.size();
            double mean_A = 0.0, mean_B = 0.0, inner = 0.0, magnitude_A = 0.0, magnitude_B = 0.0;
            for (int i = 0; i < n; i++) {
                inner += A.get(i) * B.get(i);
                magnitude_A += A.get(i) * A.get(i);
                magnitude_B += B.get(i) * B.get(i);
            }

            double cosine_similarity = inner / std::sqrt(magnitude_A * magnitude_B);
            similarity = cosine_similarity;
            break;
        case "euclidean":
            int n = A.size();
            double euclidean_distance = 0.0;
            for (int i = 0; i < n; i++)
                euclidean_distance += (A.get(i) - B.get(i)) * (A.get(i) - B.get(i));

            euclidean_distance = std::sqrt(euclidean_distance);
            similarity = euclidean_distance;
            break;
        case "jaccard":
            std::sort(std::begin(A.data_), std::end(A.data_));
            std::sort(std::begin(B.data_), std::end(B.data_));

            std::vector<T> intersection_list;

            std::set_intersection(
                std::begin(A.data_), std::end(A.data_), std::begin(B.data_), std::end(B.data_), std::back_inserter(intersection_list));

            int cardinality_A = A.size(), cardinality_B = B.size(), cardinality_intersection = intersection_list.size();

            double jaccard_similarity = cardinality_intersection * (1.0 / (cardinality_A + cardinality_B - cardinality_intersection));
            similarity = jaccard_similarity;
            break;
        case "overlap":
            std::sort(std::begin(A.data_), std::end(A.data_));
            std::sort(std::begin(B.data_), std::end(B.data_));

            std::vector<T> intersection_list;

            std::set_intersection(
                std::begin(A.data_), std::end(A.data_), std::begin(B.data_), std::end(B.data_), std::back_inserter(intersection_list));

            int cardinality_A = A.size(), cardinality_B = B.size(), cardinality_intersection = intersection_list.size();

            double overlap_similarity = cardinality_intersection * (1.0 / std::min(cardinality_A, cardinality_B));
            similarity = overlap_similarity;
            break;
        case "pearson":
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
            similarity = pearson_similarity;
            break;
    }

    return similarity;
}
/******************************************************************************
 * Copyright (c) 2016, TigerGraph Inc.
 * All rights reserved.
 * Project: TigerGraph Query Language
 *
 * - This library is for defining struct and helper functions that will be used
 *   in the user-defined functions in "ExprFunctions.hpp". Note that functions
 *   defined in this file cannot be directly called from TigerGraph Query scripts.
 *   Please put such functions into "ExprFunctions.hpp" under the same directory
 *   where this file is located.
 *
 * - Please don't remove necessary codes in this file
 *
 * - A backup of this file can be retrieved at
 *     <tigergraph_root_path>/dev_<backup_time>/gdk/gsql/src/QueryUdf/ExprUtil.hpp
 *   after upgrading the system.
 *
 ******************************************************************************/

#ifndef EXPRUTIL_HPP_
#define EXPRUTIL_HPP_

#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <gle/engine/cpplib/headers.hpp>
#include <math.h>
#include <random>
#include <algorithm>
#include <vector>

typedef std::string string; //XXX DON'T REMOVE

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

template <typename T>
 inline double tg_euclidean_distance_accum(ListAccum<T>& A, ListAccum<T>& B) {
   int n = A.size();
   double euclidean_distance = 0.0;
   for (int i = 0; i < n; i++)
     euclidean_distance += (A.get(i) - B.get(i)) * (A.get(i) - B.get(i));

   euclidean_distance = std::sqrt(euclidean_distance);
   return euclidean_distance;
 }

template <typename T>
 inline double tg_cosine_similarity_accum(ListAccum<T>& A, ListAccum<T>& B) {
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

template <typename T>
 inline double tg_jaccard_similarity_accum(ListAccum<T>& A, ListAccum<T>& B) {
   std::sort(std::begin(A.data_), std::end(A.data_));
   std::sort(std::begin(B.data_), std::end(B.data_));

   std::vector<T> intersection_list;

   std::set_intersection(
       std::begin(A.data_), std::end(A.data_), std::begin(B.data_), std::end(B.data_), std::back_inserter(intersection_list));

   int cardinality_A = A.size(), cardinality_B = B.size(), cardinality_intersection = intersection_list.size();

   double jaccard_similarity = cardinality_intersection * (1.0 / (cardinality_A + cardinality_B - cardinality_intersection));
   return jaccard_similarity;
 }

template <typename T>
 inline double tg_overlap_similarity_accum(ListAccum<T>& A, ListAccum<T>& B) {
   std::sort(std::begin(A.data_), std::end(A.data_));
   std::sort(std::begin(B.data_), std::end(B.data_));

   std::vector<T> intersection_list;

   std::set_intersection(
       std::begin(A.data_), std::end(A.data_), std::begin(B.data_), std::end(B.data_), std::back_inserter(intersection_list));

   int cardinality_A = A.size(), cardinality_B = B.size(), cardinality_intersection = intersection_list.size();

   double overlap_similarity = cardinality_intersection * (1.0 / std::min(cardinality_A, cardinality_B));
   return overlap_similarity;
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

   for (int i = 0; i < n; i++) {
     double diff_A = A.get(i) - mean_A, diff_B = B.get(i) - mean_B;
     covariance += diff_A * diff_B;
     std_dev_A += diff_A * diff_A;
     std_dev_B += diff_B * diff_B;
   }

   double pearson_similarity = covariance / std::sqrt(std_dev_A * std_dev_B);
   return pearson_similarity;
 }

#endif /* EXPRUTIL_HPP_ */

#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <gle/engine/cpplib/headers.hpp>
#include <iostream>
#include <map>
#include <random>
#include <sstream>
#include <string>
#include <vector>

inline double pairwise_cosine_similarity(ListAccum<double> emb1, ListAccum<double> emb2, int embeddingDim) {
    Eigen::VectorXd v1(embeddingDim);
    Eigen::VectorXd v2(embeddingDim);
    for (int e = 0; e < embeddingDim; e++) {
        v1[e] = emb1.get(e);
        v2[e] = emb2.get(e);
    }
    double res = (v1.dot(v2))/(v1.norm()*v2.norm());
    return res;
}

inline MapAccum<int, double> cosine_similarity(ListAccum<double> emb1, MapAccum<int, ListAccum<double>> other_vertices, int embeddingDim) {
    Eigen::VectorXd v1(embeddingDim);
    for (int e = 0; e < embeddingDim; e++) {
        v1[e] = emb1.get(e);
    }
    Eigen::VectorXd v2(embeddingDim);

    MapAccum<int, double> results;
    for(auto it = std::begin(other_vertices); it != std::end(other_vertices); it++) {
        for (int e = 0; e < embeddingDim; e++){
            v2[e] = it->second.get(e);
        }
        double sim = (v1.dot(v2))/(v1.norm()*v2.norm());
        MapAccum<int, double> temp(it->first, sim);
        results += temp;
    }
    return results;
}
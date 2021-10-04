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
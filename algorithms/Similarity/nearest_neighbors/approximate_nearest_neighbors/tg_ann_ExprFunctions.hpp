#include <string>
#include <gle/engine/cpplib/headers.hpp>
#include <math.h>
#include <random>

/**     XXX Warning!! Put self-defined struct in ExprUtil.hpp **
 *  *  No user defined struct, helper functions (that will not be directly called
 *   *  in the GQuery scripts) etc. are allowed in this file. This file only
 *    *  contains user-defined expression function's signature and body.
 *     *  Please put user defined structs, helper functions etc. in ExprUtil.hpp
 *      */
#include "ExprUtil.hpp"

namespace UDIMPL {
  typedef std::string string; //XXX DON'T REMOVE

  /****** BIULT-IN FUNCTIONS **************/
  /****** XXX DON'T REMOVE ****************/
  inline int64_t str_to_int (string str) {
    return atoll(str.c_str());
  }

  inline int64_t float_to_int (float val) {
    return (int64_t) val;
  }

  inline string to_string (double val) {
    char result[200];
    sprintf(result, "%g", val);
    return string(result);
  }
  inline double log_2(double num) {
        return log2(num);
  }

  template <typename T>
  inline double tg_similarity_accum(ListAccum<T>& A, ListAccum<T>& B, const string& similarity_type) {
    double similarity = 0;
    if (similarity_type.compare("COSINE") == 0) {
      similarity = tg_cosine_similarity_accum(A, B);
    }
    else if (similarity_type.compare("JACCARD") == 0) {
      similarity = tg_jaccard_similarity_accum(A, B);
    }
    else if (similarity_type.compare("EUCLIDEAN") == 0) {
      similarity = tg_euclidean_similarity_accum(A, B);
    }
    else if (similarity_type.compare("OVERLAP") == 0) {
      similarity = tg_overlap_similarity_accum(A, B);
    }
    else if (similarity_type.compare("PEARSON") == 0) {
      similarity = tg_pearson_similarity_accum(A, B);
    }
    return similarity;
  }

}
/****************************************/

#endif /* EXPRFUNCTIONS_HPP_ */

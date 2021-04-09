/******************************************************************************
 * Copyright (c) 2015-2016, TigerGraph Inc.
 * All rights reserved.
 * Project: TigerGraph Query Language
 * udf.hpp: a library of user defined functions used in queries.
 *
 * - This library should only define functions that will be used in
 *   TigerGraph Query scripts. Other logics, such as structs and helper
 *   functions that will not be directly called in the GQuery scripts,
 *   must be put into "ExprUtil.hpp" under the same directory where
 *   this file is located.
 *
 * - Supported type of return value and parameters
 *     - int
 *     - float
 *     - double
 *     - bool
 *     - string (don't use std::string)
 *     - accumulators
 *
 * - Function names are case sensitive, unique, and can't be conflict with
 *   built-in math functions and reserve keywords.
 *
 * - Please don't remove necessary codes in this file
 *
 * - A backup of this file can be retrieved at
 *     <tigergraph_root_path>/dev_<backup_time>/gdk/gsql/src/QueryUdf/ExprFunctions.hpp
 *   after upgrading the system.
 *
 ******************************************************************************/

#ifndef EXPRFUNCTIONS_HPP_
#define EXPRFUNCTIONS_HPP_

#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <gle/engine/cpplib/headers.hpp>

/**     XXX Warning!! Put self-defined struct in ExprUtil.hpp **
 *  No user defined struct, helper functions (that will not be directly called
 *  in the GQuery scripts) etc. are allowed in this file. This file only
 *  contains user-defined expression function's signature and body.
 *  Please put user defined structs, helper functions etc. in ExprUtil.hpp
 */
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
    sprintf(result, "%d", val);
    return string(result);
  }

  template <typename tuple>
  inline uint64_t getCid (tuple tup) {
    return tup.cid;
  }

  template <typename tuple>
  inline uint64_t getDeltaQ (tuple tup) {
    return tup.deltaQ;
  }

  template <typename MESSAGE>
  inline int64_t louvain_UDF (gpelib4::SingleValueMapContext<MESSAGE>* context,ServiceAPI* serviceapi, EngineServiceRequest& request, SumAccum<int> cid, float weight, VERTEX s, float incident, float sWeight, float totalWeight, float epsilon) {
    enum GVs {GV_SYS_PC, GV_PARAM_v_type, GV_PARAM_e_type, GV_PARAM_wt_attr, GV_SYS_wt_wt_attr_flag, GV_PARAM_iter1, GV_SYS_iter1_flag, GV_PARAM_iter2, GV_SYS_iter2_flag, GV_PARAM_tolerence, GV_SYS_tolerence_flag, GV_PARAM_print_accum, GV_SYS_print_accum_flag, GV_PARAM_result_attr, GV_SYS_result_attr_flag, GV_PARAM_file_path, GV_SYS_file_path_flag,
      GV_GACC_weightToCluster, GV_GACC_currVertex, GV_GACC_maxDeltaQ, GV_GACC_bestCluster, GV_GACC_totIncidentCluster, GV_GACC_totalWeight, GV_GACC_modularity, GV_GACC_modularity2, GV_GACC_weightToClusterMap, GV_GACC_moveComm, GV_GACC_representMap, GV_GACC_representSet, GV_GACC_vertexMap, GV_GACC_clusterDist, GV_GACC_clusterMap, GV_GV_last_modularity, GV_GV_last_modularity2, GV_GV_iteration, GV_GV_Iter1, GV_GV_epsilon, GV_GV_iteration2, GV_GV_partitions, GV_GV_debug, GV_SYS_i11, GV_SYS_i36, GV_SYS_i21, GV_SYS_i57, FE_GV_25, FE_GV_25_NULL, MONITOR, MONITOR_ALL, GV_SYS_OLD_PC, GV_SYS_EXCEPTION, GV_SYS_TO_BE_COMMITTED, GV_SYS_LAST_ACTIVE, GV_SYS_EMPTY_INITIALIZED, GV_SYS_VTs, GV_SYS_S_SIZE, GV_SYS_S_ORDERBY, GV_SYS_S_LASTSET, GV_SYS_Start_SIZE, GV_SYS_Start_ORDERBY, GV_SYS_Start_LASTSET, GV_SYS_T1_SIZE, GV_SYS_T1_ORDERBY, GV_SYS_T1_LASTSET, GV_SYS_represent_SIZE, GV_SYS_represent_ORDERBY, GV_SYS_represent_LASTSET};

    MaxAccum<VERTEX>& currentVertex = context->GetGlobalVariableLocal(GV_GACC_currVertex)->template GetValue<MaxAccum<VERTEX>>();
    MapAccum<int64_t, SumAccum<float>>& comMap = context->GetGlobalVariableLocal(GV_GACC_weightToCluster)->template GetValue<MapAccum<int64_t,SumAccum<float>>>();

    MaxAccum<float>& maxDeltaQ = context->GetGlobalVariableLocal(GV_GACC_maxDeltaQ)->template GetValue<MaxAccum<float>>();
    MaxAccum<int64_t>& bestCluster = context->GetGlobalVariableLocal(GV_GACC_bestCluster)->template GetValue<MaxAccum<int64_t>>();

    // std::cout << "[redrain][udf]" << &currentVertex << ", " << &comMap << ", " << &maxDeltaQ << ", " << &bestCluster << "\n";

    // the first edgeMap (<0 or !=s)
    if (currentVertex.data_ != s) {
      comMap.clear();
      maxDeltaQ = std::numeric_limits<float>::lowest();
    }

    currentVertex = s;
    float edgeWeightSum = 0;
    auto it = comMap.data_.find(cid);
    if (it != comMap.data_.end()) {
      edgeWeightSum = it->second + weight;
      it->second += weight;
    } else {
      edgeWeightSum = weight;
      comMap.data_.insert(std::pair<int64_t,float> (cid, weight));
    }

    //float deltaQ_new = comMap.get(cid) - incident * sWeight / totalWeight;
    float deltaQ_new = edgeWeightSum/totalWeight - incident * sWeight / (2 * totalWeight * totalWeight);
    //std::cout << "deltaQ_new > maxDeltaQ:" << (deltaQ_new > maxDeltaQ) << ", deltaQ_new:" << deltaQ_new << ",comMap.get(cid):" << comMap.get(cid) << ",cid:" << cid << ", incident:" << incident << ", sWeight:" << sWeight << ",totalWeight:" << totalWeight << ",maxDeltaQ:" << maxDeltaQ << ",bestCluster:" << bestCluster << "sourceID:" << s << std::endl;

    if (deltaQ_new > maxDeltaQ || (deltaQ_new == maxDeltaQ  && cid < bestCluster)) {
      maxDeltaQ = deltaQ_new;
      bestCluster = cid;
    }
    return bestCluster;
  }

}
/****************************************/

#endif /* EXPRFUNCTIONS_HPP_ */

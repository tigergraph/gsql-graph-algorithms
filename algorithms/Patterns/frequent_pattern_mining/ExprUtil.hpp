/******************************************************************************
 * Copyright (c) 2021, TigerGraph Inc.
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
#include <vector>

typedef std::string string; //XXX DON'T REMOVE
const uint64_t BASE = 1ULL << 63;
const int64_t MOD = 9223372036854775783;

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



#endif /* EXPRUTIL_HPP_ */

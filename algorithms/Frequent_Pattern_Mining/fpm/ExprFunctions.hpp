/*Copyright (c) 2021, TigerGraph Inc.
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
#include <algorithm>
#include <functional>
#include <iostream>
#include <chrono>
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
	    sprintf(result, "%g", val);
            return string(result);
	}

	inline int64_t get_hash(int64_t id){
	    int64_t hash_val = id % MOD;
	    return hash_val;
	}

	template<typename tup>
	inline int64_t get_pattern_key(MaxAccum<tup> t){
		tup in_data = t;
		return in_data.pattern_key;
	}
	
	template<typename tup>
	inline int64_t get_suffix_key(MaxAccum<tup> t){
		tup in_data = t;
		return in_data.suffix_key;
	}
	inline ListAccum<int64_t> initiate_hash_const(int length){
		ListAccum<int64_t> return_arr;
		__int128_t promoter;

		return_arr += 1;

		for (int i = 1; i < length + 1; i++){
			promoter = return_arr.get(i - 1);
			
			promoter *= BASE;
			promoter %= MOD;
			
			return_arr += static_cast<int64_t>(promoter);
		}
		
		return return_arr;
	}
	inline int64_t get_hash_without_first_element(int64_t hash_val, int64_t first, int size, const ListAccum<int64_t>& HASH_CONST){
	    __int128_t promoter = hash_val;

	    __int128_t first_hash = first;
	    first_hash *= HASH_CONST.get(size - 1);
	    first_hash %= MOD;

	    promoter -= first_hash;

	    promoter %= MOD;
	    promoter += MOD;
	    promoter %= MOD;

	    promoter *= BASE;
	    promoter %= MOD;

	    return static_cast<int64_t>(promoter);
	}

	inline int64_t get_hash_without_last_element(int64_t hash_val, int64_t last){
		__int128_t promoter = hash_val;
		promoter -= last;
		promoter %= MOD;
		promoter += MOD;
		promoter %= MOD;

	    return promoter;
	}

	inline int64_t get_hash_concat(int64_t hash_val, int64_t appender){
	    __int128_t promoter = hash_val;

	    promoter *= BASE;
	    promoter %= MOD;

	    promoter += appender;
	    promoter %= MOD; 

	    return static_cast<int64_t>(promoter); 
	}

	inline bool is_subset(const ListAccum<int64_t>& subset, int64_t ending, ListAccum<int64_t> &superset){

	    int curr_pos = 0;
	    int i = 0;

	    for (i = 0; i < superset.size(); ++i){
		if (superset.get(i) == subset.get(curr_pos)){
		    ++curr_pos;
		    if (curr_pos == subset.size()){
			break;
		    }
		}
	    }
	    if (curr_pos != subset.size()){
	    	return false;
	    }

	    for (int j = i + 1; j < superset.size(); ++j){
		if (superset.get(j) == ending){
		    return true;
		}
	    }

	    return false;

	}

	inline ListAccum<int64_t> concat(ListAccum<int64_t> original_list, int64_t appending_element){
	    original_list += appending_element;

	    return original_list;
	}
	inline ListAccum<VERTEX> to_vertex_list(const ListAccum<int64_t>& l){
		ListAccum<VERTEX> v_list;
		for (int i = 0; i < l.size(); ++i){
			v_list += VERTEX(l.get(i));
		}
		return v_list;
	}
	template<typename tup>
	inline tup get_tup(MaxAccum<tup> val){
		tup new_tup = val;
		return new_tup;
	}
}
/****************************************/

#endif /* EXPRFUNCTIONS_HPP_ */

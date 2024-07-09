#!/bin/bash

rm ~/mem/*.log
mkdir -p ~/mem

sleep 1;

mem_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )" 

sh ${mem_dir}/run_free.sh >> ~/mem/mem.log 2>&1 &

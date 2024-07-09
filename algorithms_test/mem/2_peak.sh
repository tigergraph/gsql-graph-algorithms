#!/bin/bash

grep 'Mem:' ~/mem/mem.log > ~/mem/prof.log; 

mem_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )" 
awk -f ${mem_dir}/peak.awk ~/mem/prof.log >> ~/mem/peak.log;

tail -n 1 ~/mem/peak.log

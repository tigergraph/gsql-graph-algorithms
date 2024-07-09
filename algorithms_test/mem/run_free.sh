#!/usr/bin/bash
# monitor the memory for one week
for i in $(seq 1 604800)
do 
  date
  free | grep Mem
  sleep 1
done

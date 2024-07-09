# initialization for line 1
NR == 1 {
  max_mem = $3;
  min_mem = $3;
} 
# memory
NR > 1 && $3 > max_mem {
  max_mem = $3;
}
NR > 1 && $3 < min_mem {
  min_mem = $3;
}
# sum
{
  sum_mem += $3;
  row_num ++;
}
# print results after processing the file
END {
  if(row_num > 0) avg_mem = sum_mem / row_num / 1024 / 1024;
  max_mem = max_mem / 1024 / 1024;
  min_mem = min_mem / 1024 / 1024;
  diff_mem = max_mem - min_mem;
  printf "row num: %0.0f. max mem: %0.2f GB; min mem: %0.2f GB; avg mem: %0.2f GB; max mem - min mem: %0.2f GB.\n", row_num, max_mem, min_mem, avg_mem, diff_mem;
}

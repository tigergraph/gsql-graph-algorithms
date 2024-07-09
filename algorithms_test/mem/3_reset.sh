#!/bin/bash

# Set up initial variables
check_count=0
max_checks=100
mem_diff_threshold=0.01
mem_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Function to get memory stats and check the difference
check_memory() {
  # Run the memory check commands
  grep 'Mem:' ~/mem/mem.log > ~/mem/prof.log
  awk -f ${mem_dir}/peak.awk ~/mem/prof.log >> ~/mem/peak.log

  # Get the latest memory stats
  latest_stats=$(tail -n 1 ~/mem/peak.log)

  # Extract the max - min memory difference
  mem_diff=$(echo "$latest_stats" | awk -F';' '{print $4}' | awk -F' ' '{print $6}')

  # Convert mem_diff to a number
  mem_diff=$(echo "$mem_diff" | sed 's/GB//')

  # Return the memory difference
  echo "$mem_diff"
}

# Main loop
while [ $check_count -lt $max_checks ]; do
  check_count=$((check_count + 1))

  # Check memory and get the difference
  mem_diff=$(check_memory)

  # Check if the difference is less than the threshold
  if (( $(echo "$mem_diff < $mem_diff_threshold" | bc -l) )); then
    break
  fi

  # Run the reset script and sleep for 1 second
  > ~/mem/mem.log
  sleep 1
done


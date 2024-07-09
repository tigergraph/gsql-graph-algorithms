#!/bin/bash

# Function to run the curl command
run_curl_command() {
  local graph_name=$1
  local query_name=$2
  local para_str=$3
  local timeout_ms=$4
  local result_file_path=$5
  local duration_file_path=$6

  echo "Starting curl command for query: $query_name on graph: $graph_name"

  start_time=$(date +%s%N)
  curl_result=$(curl -s -H "GSQL-TIMEOUT: $timeout_ms" "http://127.0.0.1:14240/restpp/query/${graph_name}/${query_name}?${para_str}")
  end_time=$(date +%s%N)

  # Calculate the duration
  duration=$((end_time - start_time))
  duration_in_milliseconds=$(echo "scale=3; $duration / 1000000" | bc)

  # Create query result directory if it doesn't exist
  mkdir -p "$(dirname "$result_file_path")"

  # Check for errors in the curl result
  error=$(echo "$curl_result" | jq -r '.error')
  message=$(echo "$curl_result" | jq -r '.message')

  if [ "$error" = "true" ]; then
    echo "Error: $message"
  fi

  # Write the result of the curl command to file
  echo "$curl_result" > "$result_file_path"
  echo "Result has been written to $result_file_path"

  # Write the duration to file
  echo "$duration_in_milliseconds" > "$duration_file_path"
  echo "Duration has been written to $duration_file_path"

  echo "Finished curl command for query: $query_name on graph: $graph_name"
}

# Main function
main() {
  # Default config file path
  dir=$(cd "$(dirname "$0")"; pwd) 
  config_file="${dir}/config/3_run.json"

  # Parse command-line arguments
  while getopts "c:f:" opt; do
    case ${opt} in
      c)
        config_file=$OPTARG
        ;;
      f)
        filter=$OPTARG
        ;;
      \?)
        echo "Usage: $0 [-c config_file] [-f filter]"
        exit 1
        ;;
    esac
  done

  # Check if required commands are available
  if ! command -v jq &> /dev/null; then
    echo "Error: jq is not installed."
    exit 1
  fi

  # Check if the configuration file exists
  if [ ! -f "$config_file" ]; then
    echo "Error: Configuration file not found: $config_file"
    exit 1
  fi

  # Read general settings from the configuration file
  default_graph_name=$(jq -r '.general_settings.default_graph_name' "$config_file")
  default_timeout_in_minutes=$(jq -r '.general_settings.default_timeout_in_minutes' "$config_file")
  default_output_directory=$(jq -r '.general_settings.default_output_directory' "$config_file")
  default_output_directory=${default_output_directory/#\~/$HOME}
  summary_file_path=$(jq -r '.general_settings.summary_file_path' "$config_file")
  summary_file_path=${summary_file_path/#\~/$HOME}

  # Write header to the CSV file
  echo "algorithm,run_number,query_run_time_sec,query_peak_memory_gb" > "$summary_file_path"

  # Run the memory monitor
  source "${dir}/mem/1_start.sh"

  # Iterate over each algorithm
  algorithms=$(jq -r '.algorithms | to_entries[] | .key' "$config_file")
  for algorithm in $algorithms; do
    # Apply filter if specified
    if [ -n "$filter" ]; then
      if [[ ! "$algorithm" == *$filter ]]; then
        continue
      fi
    fi

    runs=$(jq -r ".algorithms[\"${algorithm}\"][]" "$config_file" | jq -c .)

    # Calculate total run number for an algorithm
    mapfile -t runs_array <<< "$runs"
    total_runs=${#runs_array[@]}

    # Iterate over each run for the algorithm
    run_index=0
    for run in "${runs_array[@]}"; do

      echo "==================== ${algorithm} run ${run_index} ===================="

      # Reset the memory monitor
      source "${dir}/mem/3_reset.sh"

      # Extract values from the JSON
      graph_name=$(echo "$run" | jq -r '.graph_name // empty')
      query_name=$(echo "$run" | jq -r '.query_name // empty')
      timeout_in_minutes=$(echo "$run" | jq -r '.timeout_in_minutes // empty')
      output_directory=$(echo "$run" | jq -r '.output_directory // empty')
      parameters=$(echo "$run" | jq -r '.parameters')

      # Check if query_name exists
      if [ -z "$query_name" ] || [ "$query_name" == "null" ]; then
        echo "Error: query_name is a must-have key in the algorithm configuration for algorithm: $algorithm; index: $run_index"
        exit 1
      fi

      # Set default values if not provided
      graph_name=${graph_name:-$default_graph_name}
      timeout_in_minutes=${timeout_in_minutes:-$default_timeout_in_minutes}
      if [ "$total_runs" -eq 1 ]; then
        output_directory=${output_directory:-"$default_output_directory/${algorithm}"}
      else
        output_directory=${output_directory:-"$default_output_directory/${algorithm}/${run_index}"}
      fi
      output_directory=${output_directory/#\~/$HOME}
      result_file_path="$output_directory/result.json"
      duration_file_path="$output_directory/duration.txt"
      memory_file_path="$output_directory/memory.txt"

      # Create parameter list string
      para_str=$(echo "$parameters" | jq -r 'to_entries | map("\(.key)=\(.value|tostring)") | join("&")')

      # Calculate timeout in milliseconds
      timeout_ms=$((timeout_in_minutes * 60000))

      # Run the curl command
      run_curl_command "$graph_name" "$query_name" "$para_str" "$timeout_ms" "$result_file_path" "$duration_file_path"

      # Increment run index
      run_index=$((run_index + 1))

      # Save the peak memory to file
      source "${dir}/mem/2_peak.sh" > "$memory_file_path"
      echo "Peak memory has been written to $memory_file_path"

      # Check if duration.txt exists
      if [ -f "$duration_file_path" ]; then
        # Read query run time in ms and convert to seconds
        query_run_time_ms=$(cat "$duration_file_path")
        query_run_time_sec=$(echo "scale=3; $query_run_time_ms / 1000" | bc)
      else
        echo "Warning: $duration_file_path not found."
        continue
      fi

      # Check if memory.txt exists
      if [ -f "$memory_file_path" ]; then
        # Extract query peak memory from memory.txt
        query_peak_memory=$(grep 'max mem - min mem' "$memory_file_path" | awk -F' ' '{print $(NF-1)}')
      else
        echo "Warning: $memory_file_path not found."
        continue
      fi

      # Write the data to the CSV file
      echo "$algorithm,${run_index},$query_run_time_sec,$query_peak_memory" >> "$summary_file_path"
    done
  done

  # Stop the memory monitor
  source "${dir}/mem/4_stop.sh"
}

# Run the main function
main "$@"


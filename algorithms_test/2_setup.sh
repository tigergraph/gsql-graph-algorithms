#!/bin/bash

# Function to run gsql commands
run_gsql_file() {
  local file_path=$1
  local command=$2
  local graph_name=$3

  if [ -e "$file_path" ]; then
    echo "Running: $command $file_path"
    if [ -n "$graph_name" ]; then
      if ! gsql -u "$user_name" -p "$password" -g "$graph_name" "$file_path"; then
        echo "Error: Failed to run $command $file_path for graph $graph_name"
        return 1
      fi
    else
      if ! gsql -u "$user_name" -p "$password" "$file_path"; then
        echo "Error: Failed to run $command $file_path"
        return 1
      fi
    fi
    return 0
  else
    echo "Error: File path $file_path does not exist."
    return 1
  fi
}

# Function to create and install queries
install_queries_for_graph() {
  local graph_name=$1
  local queries_to_install=$2
  local repo_dir=$3

  # Check if there are queries to install
  if [ "$queries_to_install" != "null" ] && [ -n "$queries_to_install" ]; then
    # Drop all queries for the graph
    gsql -u "$user_name" -p "$password" -g "$graph_name" "drop query *"

    # Create the queries
    echo "$queries_to_install" | jq -r '.[]' | while IFS= read -r query_path; do
      gsql_query_path="${repo_dir}/${query_path}"
      # Create the query
      if ! run_gsql_file "$gsql_query_path" "Creating query" "$graph_name"; then
        echo "Error: Failed to create query from $gsql_query_path for graph $graph_name"
        return 1
      fi
    done

    # Install the queries
    echo "Installing queries for graph: $graph_name"
    if ! gsql -u "$user_name" -p "$password" -g "$graph_name" "INSTALL QUERY *"; then
      echo "Error: Failed to install the queries for graph: $graph_name"
      return 1
    fi
  else
    echo "No queries to install for graph: $graph_name"
  fi
  return 0
}

# Main function
main() {
  # Check if required commands are available
  if ! command -v jq &> /dev/null; then
    echo "Error: jq is not installed."
    exit 1
  fi

  if ! command -v gsql &> /dev/null; then
    echo "Error: gsql is not installed."
    exit 1
  fi

  # Read the JSON configuration file
  dir=$(cd "$(dirname "$0")"; pwd) 
  config_file="${dir}/config/2_setup.json"
  gsql_dir="${dir}/gsql"
  repo_dir="${dir}/.."

  # Check if the configuration file exists
  if [ ! -f "$config_file" ]; then
    echo "Error: Configuration file not found: $config_file"
    exit 1
  fi

  # Extract user_name and password
  user_name=$(jq -r '.tigergraph.user_name // empty' "$config_file")
  password=$(jq -r '.tigergraph.password // empty' "$config_file")

  # Check if user_name and password are empty
  if [ -z "$user_name" ]; then
    echo "Error: user_name is not set in the configuration file."
    exit 1
  fi

  if [ -z "$password" ]; then
    echo "Error: password is not set in the configuration file."
    exit 1
  fi

  # Extract execution steps and set default values if not provided
  to_drop_graph=$(jq -r '.execution_steps.drop_graph // empty' "$config_file")
  to_drop_graph=${to_drop_graph:-false}
  to_create_schema=$(jq -r '.execution_steps.create_schema // empty' "$config_file")
  to_create_schema=${to_create_schema:-false}
  to_create_loading_job=$(jq -r '.execution_steps.create_loading_job // empty' "$config_file")
  to_create_loading_job=${to_create_loading_job:-false}
  to_run_loading_job=$(jq -r '.execution_steps.run_loading_job // empty' "$config_file")
  to_run_loading_job=${to_run_loading_job:-false}
  to_install_queries=$(jq -r '.execution_steps.install_queries // empty' "$config_file")
  to_install_queries=${to_install_queries:-false}

  # Iterate over each graph and get its file_path
  graphs=$(jq -r '.graphs | to_entries[] | @base64' "$config_file")

  echo "$graphs" | while IFS= read -r graph_b64; do
    graph=$(echo "${graph_b64}" | base64 --decode)
    graph_name=$(echo "$graph" | jq -r '.key')
    file_path=$(echo "$graph" | jq -r '.value.file_path')
    file_path=${file_path/#\~/$HOME}
    queries_to_install=$(echo "$graph" | jq -r '.value.queries_to_install // empty')

    echo "======================================== ${graph_name} ========================================"

    # Drop the graph
    if [ "$to_drop_graph" = "true" ]; then
      echo "Dropping the graph ${graph_name}..."
      gsql -u "$user_name" -p "$password" -g "$graph_name" "DROP JOB *"
      gsql -u "$user_name" -p "$password" -g "$graph_name" "DROP QUERY *"
      gsql -u "$user_name" -p "$password" "DROP GRAPH ${graph_name}"
      echo "Finished dropping graph ${graph_name}."
      echo "--------------------------------------------------------------------------------"
    fi

    # Create the schema
    if [ "$to_create_schema" = "true" ]; then
      gsql_schema_path="$gsql_dir/$graph_name/1_create_schema.gsql"
      run_gsql_file "$gsql_schema_path" "Creating schema"
      echo "--------------------------------------------------------------------------------"
    fi

    # Create the loading job
    if [ "$to_create_loading_job" = "true" ]; then
      gsql_loading_job_path="$gsql_dir/$graph_name/2_create_loading_job.gsql"
      run_gsql_file "$gsql_loading_job_path" "Creating loading job"
      echo "--------------------------------------------------------------------------------"
    fi

    # Run the loading job
    if [ "$to_run_loading_job" = "true" ]; then
      if [ -e "$file_path" ]; then
        echo "Running loading job for $file_path..."
        if ! gsql -u "$user_name" -p "$password" -g "$graph_name" "RUN LOADING JOB loading_job USING f1=\"$file_path\""; then
          echo "Error: Failed to run loading job for $file_path"
        fi
        echo "Finished running loading job for $file_path."
      else
        echo "Error: File path $file_path does not exist."
      fi
      echo "--------------------------------------------------------------------------------"
    fi

    # Create and install the queries
    if [ "$to_install_queries" = "true" ]; then
      install_queries_for_graph "$graph_name" "$queries_to_install" "$repo_dir"
    fi
  done
}

# Run the main function
main

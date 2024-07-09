#!/bin/bash

# Directory to search for .gsql files
search_dir="../../algorithms"

# Find all .gsql files under the search directory recursively
gsql_files=$(find "$search_dir" -type f -name "*.gsql")

# Check if any .gsql files were found
if [ -z "$gsql_files" ]; then
  echo "No .gsql files found in $search_dir"
else
  echo "Found the following .gsql files:"
  echo "$gsql_files"
fi


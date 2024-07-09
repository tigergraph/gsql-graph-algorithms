#!/bin/bash

# Main function
main() {
  # Check if required commands are available
  if ! command -v jq &> /dev/null; then
    echo "Error: jq is not installed."
    exit 1
  fi

  # Read the JSON configuration file
  dir=$(cd "$(dirname "$0")"; pwd) 
  config_file="${dir}/config/1_dataset.json"

  # Check if the configuration file exists
  if [ ! -f "$config_file" ]; then
    echo "Configuration file not found: $config_file"
    exit 1
  fi

  # Extract general settings
  default_directory=$(jq -r '.general_settings.default_directory' "$config_file")
  default_directory=${default_directory/#\~/$HOME}

  # Iterate over each dataset
  datasets=$(jq -r '.datasets | to_entries[] | @base64' "$config_file")

  # Decode each dataset entry and process it
  echo "$datasets" | while IFS= read -r dataset_b64; do
    dataset=$(echo "${dataset_b64}" | base64 --decode)
    dataset_name=$(echo "$dataset" | jq -r '.key')
    download_link=$(echo "$dataset" | jq -r '.value.download_link')
    directory=$(echo "$dataset" | jq -r '.value.directory // empty')
    directory=${directory/#\~/$HOME}
    directory=${directory:-$default_directory}
    top_level_dir=$(echo "$dataset" | jq -r '.value.top_level_dir')

    echo "======================================== ${dataset_name} ========================================"

    # Create the directory if it doesn't exist
    mkdir -p "$directory"

    # Extract the file name from the download link
    file_name=$(basename "$download_link")

    # Check if the folder exists before downloading the dataset
    dataset_folder="$directory/$top_level_dir"
    if [ ! -d "$dataset_folder" ]; then
      # Download the dataset if it doesn't exist
      if [ ! -f "$directory/$file_name" ]; then
        echo "Downloading $file_name..."
        if ! wget -O "$directory/$file_name" "$download_link"; then
          echo "Failed to download $file_name"
          continue
        fi
      fi

      # Unzip the dataset
      echo "Unzipping $file_name into $directory..."
      if tar -xvjf "$directory/$file_name" -C "$directory" --strip-components=1 --one-top-level="$top_level_dir"; then
        echo "Finished unzipping $file_name."
      else
        echo "Failed to unzip $file_name"
      fi
    else
      echo "Directory $dataset_folder already exists, skipping unzipping."
    fi
  done
}

# Run the main function
main

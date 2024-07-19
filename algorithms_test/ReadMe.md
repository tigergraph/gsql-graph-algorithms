# Introduction

This project contains a set of Bash scripts for automating various tasks related to dataset management, TigerGraph setup, and query execution. The scripts are designed to work with configuration files that specify the details for each task. Below is an overview of each script and the project structure.

## Scripts Overview

### 1. `1_dataset.sh`
This script downloads and extracts datasets as specified in the `config/1_dataset.json` configuration file. It supports downloading files in various formats and ensures that the data is placed in the correct directories.

### 2. `2_setup.sh`
This script sets up TigerGraph graphs by executing tasks such as dropping existing graphs, creating schemas, creating loading jobs, and installing queries. The tasks are defined in the `config/2_setup.json` configuration file.

### 3. `3_run.sh`
This script executes queries on TigerGraph and collects performance metrics such as runtime and peak memory usage. The queries and their parameters are specified in the `config/3_run.json` configuration file.

## File Structure

```
.
├── 1_dataset.sh
├── 2_setup.sh
├── 3_run.sh
├── config
│   ├── 1_dataset.json
│   ├── 2_setup.json
│   └── 3_run.json
├── gsql
│   ├── MyGraph
│   │   ├── 1_create_schema.gsql
│   │   └── 2_create_loading_job.gsql
│   └── MyGraph2
│       ├── 1_create_schema.gsql
│       └── 2_create_loading_job.gsql
├── mem
│   ├── 1_start.sh
│   ├── 2_peak.sh
│   ├── 3_reset.sh
│   ├── 4_stop.sh
│   ├── peak.awk
│   └── run_free.sh
└── ReadMe.md
```

### `config` Directory
Contains JSON configuration files for each script:
- `1_dataset.json`: Configuration for dataset download and extraction.
- `2_setup.json`: Configuration for setting up TigerGraph graphs.
- `3_run.json`: Configuration for running queries and collecting metrics.

### `gsql` Directory
Contains GSQL scripts for defining schemas and loading jobs for different graphs:
- `MyGraph/1_create_schema.gsql`: Schema definition for `MyGraph`.
- `MyGraph/2_create_loading_job.gsql`: Loading job for `MyGraph`.
- `MyGraph2/1_create_schema.gsql`: Schema definition for `MyGraph2`.
- `MyGraph2/2_create_loading_job.gsql`: Loading job for `MyGraph2`.

The folder names `MyGraph` and `MyGraph2` represent graph names. You can add more graphs by creating new folders, each containing a `1_create_schema.gsql` file to create the schema and a `2_create_loading_job.gsql` file to create the loading job.

### `mem` Directory
Contains scripts and utilities for monitoring memory usage during query execution. These scripts are used automatically when you run 3_run.sh, but they can also be used manually if needed.
- `1_start.sh`: Starts memory monitoring.
- `2_peak.sh`: Captures peak memory usage.
- `3_reset.sh`: Resets memory monitoring.
- `4_stop.sh`: Stops memory monitoring.
- `peak.awk`: AWK script for processing memory data.
- `run_free.sh`: Utility script for running `free` command.

## Usage

1. **Download and extract datasets**:
   ```sh
   ./1_dataset.sh
   ```

2. **Set up TigerGraph**:
   ```sh
   ./2_setup.sh
   ```

3. **Run queries and collect metrics**:
   ```sh
   ./3_run.sh [-c config_file] [-f filter]
   ```

Ensure you have the necessary permissions to execute these scripts (`chmod +x script_name.sh`) and that the required tools (`jq`, `curl`, `gsql`) are installed on your system.

# Dataset Download and Extraction Script

This script downloads and extracts datasets specified in a JSON configuration file.

## Prerequisites

- Install `jq` (e.g., `sudo apt-get install jq`).

## Configuration

Place a JSON configuration file at `config/1_dataset.json`:

```json
{
  "general_settings": {
    "default_directory": "~/data/public"
  },
  "datasets": {
    "LiveJournal": {
      "download_link": "https://snap.stanford.edu/data/soc-LiveJournal1.txt.gz",
      "top_level_dir": "livejournal"
    },
    "Facebook": {
      "download_link": "https://snap.stanford.edu/data/facebook_combined.txt.gz",
      "directory": "~/data/tmp",
      "top_level_dir": "facebook"
    }
  }
}
```

## Usage

1. Ensure `jq` is installed.
2. Place the configuration file at `config/1_dataset.json`.
3. Run the script:
   ```sh
   ./1_dataset.sh
   ```

## Script Details

- Checks for `jq`.
- Reads `config/1_dataset.json`.
- Iterates over each dataset, creating directories, downloading, and extracting files.

## Example Output

```
======================================== LiveJournal ========================================
Created directory: /home/tigergraph/data/public/livejournal
Downloading soc-LiveJournal1.txt.gz...
--2024-07-19 06:49:47--  https://snap.stanford.edu/data/soc-LiveJournal1.txt.gz
Resolving snap.stanford.edu (snap.stanford.edu)... 171.64.75.80
Connecting to snap.stanford.edu (snap.stanford.edu)|171.64.75.80|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 259619239 (248M) [application/x-gzip]
Saving to: ‘/home/tigergraph/data/public/soc-LiveJournal1.txt.gz’

/home/tigergraph/data/public/soc-LiveJournal1.txt 100%[=============================================================================================================>] 247.59M  28.9MB/s    in 9.2s

2024-07-19 06:49:56 (26.8 MB/s) - ‘/home/tigergraph/data/public/soc-LiveJournal1.txt.gz’ saved [259619239/259619239]

Unzipping soc-LiveJournal1.txt.gz into /home/tigergraph/data/public...
Finished unzipping soc-LiveJournal1.txt.gz.
======================================== Facebook ========================================
Created directory: /home/tigergraph/data/tmp/facebook
Downloading facebook_combined.txt.gz...
--2024-07-19 06:50:03--  https://snap.stanford.edu/data/facebook_combined.txt.gz
Resolving snap.stanford.edu (snap.stanford.edu)... 171.64.75.80
Connecting to snap.stanford.edu (snap.stanford.edu)|171.64.75.80|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 218576 (213K) [application/x-gzip]
Saving to: ‘/home/tigergraph/data/tmp/facebook_combined.txt.gz’

/home/tigergraph/data/tmp/facebook_combined.txt.g 100%[=============================================================================================================>] 213.45K   539KB/s    in 0.4s

2024-07-19 06:50:04 (539 KB/s) - ‘/home/tigergraph/data/tmp/facebook_combined.txt.gz’ saved [218576/218576]

Unzipping facebook_combined.txt.gz into /home/tigergraph/data/tmp...
Finished unzipping facebook_combined.txt.gz.
```

# TigerGraph Setup Script

This script automates the setup and management of TigerGraph graphs by executing various tasks such as dropping graphs, creating schemas, creating and running loading jobs, and installing queries based on a configuration file.

## Prerequisites

- Ensure `jq` and `TigerGraph` are installed on your system.
- Place the JSON configuration file at `config/2_setup.json`.

## Configuration File

The configuration file `config/2_setup.json` should have the following structure:

```json
{
  "tigergraph": {
    "user_name": "tigergraph",
    "password": "tigergraph"
  },
  "graphs": {
    "MyGraph": {
      "file_path": "/home/tigergraph/data/public/livejournal/soc-LiveJournal1.txt",
      "execution_steps": {
        "drop_graph": true,
        "create_schema": true,
        "create_loading_job": true,
        "run_loading_job": true,
        "install_queries":true
      },
      "queries_to_install": [
        "algorithms/Community/connected_components/weakly_connected_components/small_world/tg_wcc_small_world.gsql",
        "algorithms/Centrality/pagerank/global/unweighted/tg_pagerank.gsql"
      ]
    },
    "MyGraph2": {
      "file_path": "/home/tigergraph/data/tmp/facebook/facebook_combined.txt",
      "execution_steps": {
        "drop_graph": false,
        "create_schema": false,
        "create_loading_job": false,
        "run_loading_job": false,
        "install_queries":false
      },
      "queries_to_install": [
        "algorithms/Community/louvain/tg_louvain.gsql"
      ]
    }
  }
}
```

## Usage

1. Ensure `jq` and `gsql` are installed.
2. Place the configuration file at `config/2_setup.json`.
3. Run the script:
   ```sh
   ./2_setup.sh
   ```

## Script Details

### Functions

- `run_gsql_file(file_path, command, graph_name)`: Executes a GSQL file.
- `install_queries_for_graph(graph_name, queries_to_install, repo_dir)`: Installs queries for a graph.

### Main Workflow

- Checks for required commands (`jq` and `gsql`).
- Reads the configuration file.
- Extracts and processes each graph's details:
  - Drops the graph if specified.
  - Creates the schema if specified.
  - Creates the loading job if specified.
  - Runs the loading job if specified.
  - Installs queries if specified.

## Example Output

```
======================================== MyGraph ========================================
Dropping the graph MyGraph...
Graph 'MyGraph' does not exist.
Graph 'MyGraph' does not exist.
The graph MyGraph could not be dropped!
Finished dropping graph MyGraph.
--------------------------------------------------------------------------------
Running: Creating schema /home/tigergraph/gsql-graph-algorithms/algorithms_test/gsql/MyGraph/1_create_schema.gsql
Stopping GPE GSE RESTPP
Successfully stopped GPE GSE RESTPP in 16.598 seconds
Starting GPE GSE RESTPP
Successfully started GPE GSE RESTPP in 0.068 seconds
The graph MyGraph is created.
Successfully created schema change jobs: [change_schema_of_MyGraph].
WARNING: When modifying the graph schema, reinstalling all affected queries is required, and the duration of this process may vary based on the number and complexity of the queries. To skip query reinstallation, you can run with the '-N' option, but manual reinstallation of queries will be necessary afterwards.
Kick off schema change job change_schema_of_MyGraph
Doing schema change on graph 'MyGraph' (current version: 0)
Trying to add local vertex 'MyNode' to the graph 'MyGraph'.
Trying to add local edge 'MyEdge' and its reverse edge 'rev_MyEdge' to the graph 'MyGraph'.

Graph MyGraph updated to new version 1
The job change_schema_of_MyGraph completes in 0.643 seconds!
Local schema change succeeded.
Successfully dropped jobs on the graph 'MyGraph': [change_schema_of_MyGraph].
--------------------------------------------------------------------------------
Running: Creating loading job /home/tigergraph/gsql-graph-algorithms/algorithms_test/gsql/MyGraph/2_create_loading_job.gsql
Using graph 'MyGraph'
Successfully created loading jobs: [loading_job].
--------------------------------------------------------------------------------
Running loading job for /home/tigergraph/data/public/livejournal/soc-LiveJournal1.txt...
[Tip: Use "CTRL + C" to stop displaying the loading status update, then use "SHOW LOADING STATUS <jobid>" to track the loading progress again]
[Tip: Manage loading jobs with "ABORT/RESUME LOADING JOB <jobid>"]
Running the following loading job:
  Job name: loading_job
  Jobid: MyGraph.loading_job.file.m1.1721373808522
  Log directory: /home/tigergraph/tigergraph/log/fileLoader/MyGraph.loading_job.file.m1.1721373808522
Job "MyGraph.loading_job.file.m1.1721373808522" loading status
Current timestamp is 2024-07-19 07:23:34.03
Loading status was last updated at 2024-07-19 07:23:30.272.
[FINISHED] m1 ( Finished: 1 / Total: 1 )
  +-----------------------------------------------------------------------------------------------+
  |            FILENAME |   LINES |   OBJECTS |   ERRORS |   AVG SPEED |   DURATION |   PERCENTAGE|
  |soc-LiveJournal1.txt |       3 |         6 | 68993776 |      <1 l/s |     1.58 s |        100 %|
  +-----------------------------------------------------------------------------------------------+
[WARNING] bad data in m1 /home/tigergraph/data/public/livejournal/soc-LiveJournal1.txt: 68993773 line(s) do not have enough number of tokens.
[WARNING] bad data in m1 /home/tigergraph/data/public/livejournal/soc-LiveJournal1.txt:MyEdge: 3 object(s) have invalid attributes.
Sampling error data can be viewed by executing the 'SHOW LOADING ERROR MyGraph.loading_job.file.m1.1721373808522'.
LOAD SUCCESSFUL for loading jobid: MyGraph.loading_job.file.m1.1721373808522
  Job ID: MyGraph.loading_job.file.m1.1721373808522
  Elapsed time: 2 sec
  Log directory: /home/tigergraph/tigergraph/log/fileLoader/MyGraph.loading_job.file.m1.1721373808522
  Summary: /home/tigergraph/tigergraph/log/fileLoader/MyGraph.loading_job.file.m1.1721373808522/summary

Finished running loading job for /home/tigergraph/data/public/livejournal/soc-LiveJournal1.txt.
--------------------------------------------------------------------------------
All queries are dropped.
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Community/connected_components/weakly_connected_components/small_world/tg_wcc_small_world.gsql
Successfully created queries: [tg_wcc_small_world].
Running: Creating query /home/tigergraph/gsql-graph-algorithms/algorithms_test/../algorithms/Centrality/pagerank/global/unweighted/tg_pagerank.gsql
Successfully created queries: [tg_pagerank].
Installing queries for graph: MyGraph
Start installing queries, about 1 minute ...
tg_wcc_small_world query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_wcc_small_world?v_type=VALUE&e_type=VALUE&[threshold=VALUE]&[print_results=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
tg_pagerank query: curl -X GET 'http://127.0.0.1:9000/query/MyGraph/tg_pagerank?v_type=VALUE&e_type=VALUE&[max_change=VALUE]&[maximum_iteration=VALUE]&[damping=VALUE]&[top_k=VALUE]&[print_results=VALUE]&[result_attribute=VALUE]&[file_path=VALUE]&[display_edges=VALUE]'. Add -H "Authorization: Bearer TOKEN" if authentication is enabled.
Select 'm1' as compile server, now connecting ...
Node 'm1' is prepared as compile server.

[========================================================================================================] 100% (2/2)
Query installation finished.
======================================== MyGraph2 ========================================
```

# TigerGraph Query Execution Script

This script automates the execution of queries on TigerGraph and collects performance metrics such as runtime and peak memory usage.

## Prerequisites

- Ensure `jq` and `curl` are installed on your system.
- Place the JSON configuration file at `config/3_run.json`.

## Configuration File

The configuration file `config/3_run.json` should have the following structure:

```json
{
  "general_settings": {
    "default_graph_name": "MyGraph",
    "default_timeout_in_minutes": "15",
    "default_output_directory": "~/data/algos",
    "summary_file_path": "~/data/algos/summary.csv"
  },
  "algorithms": {
    "community/tg_wcc_small_world": [
      {
        "query_name": "tg_wcc_small_world",
        "parameters": {
          "v_type": "MyNode",
          "e_type": "MyEdge",
          "threshold": 100000,
          "print_results": false
        }
      }
    ]
  }
}
```

## Usage

1. Ensure `jq` and `curl` are installed.
2. Place the configuration file at `config/3_run.json`.
3. Run the script:
   ```sh
   ./3_run.sh [-c config_file] [-f filter]
   ```

### Options

- `-c config_file`: Specify a custom configuration file (default: `config/3_run.json`).
- `-f filter`: Filter algorithms to run based on a substring match.

## Script Details

### Functions

- `run_curl_command(graph_name, query_name, para_str, timeout_ms, result_file_path, duration_file_path)`: Executes a query and collects runtime.
- `main()`: Main function to read configuration, execute queries, and collect metrics.

### Main Workflow

- Parses command-line arguments.
- Checks for required commands (`jq` and `curl`).
- Reads the configuration file.
- Iterates over each algorithm and its runs:
  - Applies filters if specified.
  - Executes the query using `curl`.
  - Measures runtime and peak memory usage.
  - Writes results to the specified output files and summary CSV.

## Example Output

```
==================== community/tg_wcc_small_world run 0 ====================
Starting curl command for query: tg_wcc_small_world on graph: MyGraph
Result has been written to /home/tigergraph/data/algos/community/tg_wcc_small_world/result.json
Duration has been written to /home/tigergraph/data/algos/community/tg_wcc_small_world/duration.txt
Finished curl command for query: tg_wcc_small_world on graph: MyGraph
Peak memory has been written to /home/tigergraph/data/algos/community/tg_wcc_small_world/memory.txt
```


from genericpath import isdir
import os
import git
import time
TIGERGRAPH_DOCUMENTATION_LINK = 'https://docs.tigergraph.com/tigergraph-platform-overview/graph-algorithm-library#'
# Readme shields for working versions of TG,
# write something about benchmarking (open-source testing)
# benchmark -> CLI tester

Documentation = {
    'betweenness_centrality': 'betweenness-centrality',
    'closeness': 'closeness-centrality',
    'connected_components': 'connected-components',
    'cosine': 'cosine-similarity-of-neighborhoods-batch',
    'cycle_detection': 'cycle-detection',
    'estimated_diameter': 'estimated-diameter',
    'greedy_graph_coloring': 'greedy-graph-coloring',
    'jaccard': 'jaccard-similarity-of-neighborhoods-batch',
    'k_core': 'k-core-decomposition',
    'k_means': 'https://raw.githubusercontent.com/tigergraph/gsql-graph-algorithms/master/algorithms/schema-free/kmeans.gsql',
    'k_nearest_neighbors': 'k-nearest-neighbors-cosine-neighbor-similarity-all-vertices-batch',
    'label_propagation': 'label-propagation',
    'local_clustering_coefficient': 'local-clustering-coefficient',
    'louvain_distributed': 'louvain-method-with-parallelism-and-refinement',
    'louvain': 'louvain-method-with-parallelism-and-refinement',
    'maximal_independent_set': 'maximal-independent-set',
    'minimum_spanning_forest': 'minimum-spanning-forest-msf',
    'minimum_spanning_tree': 'minimum-spanning-tree-mst',
    'pagerank': 'pagerank',
    'strongly_connected_components': 'strongly-connected-components-1',
    'shortest_path': 'single-source-shortest-path-weighted',
    'triangle_counting': 'triangle-counting',
    'Node2Vec': 'node-2-vec',
    'FastRP': 'N/A'
    }



# find last directory
def recursvie_dir(path, set_dirs):
    for item in os.listdir(path):
        new_path = os.path.join(path, item)
        if os.path.isdir(new_path):
            if not has_subdirectories(new_path):
                set_dirs.add(new_path)
            recursvie_dir(new_path,set_dirs)

def recursvie_gsql_algos(path, set_algos):
    for item in os.listdir(path):
        new_path = os.path.join(path, item)
        is_gsql_file = '.gsql' in new_path
        if os.path.isfile(new_path) and is_gsql_file:
            set_algos.add(new_path)
        elif os.path.isdir(new_path):
            recursvie_gsql_algos(new_path, set_algos)


def has_subdirectories(path):
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            return True
    return False

def fetch_change_log(algo_lib_dir, title):
    change_log = f'\n# {title} Change Logs\n'
    gsql_git = git.Git('~/Documents/GitHub/gsql-graph-algorithms')
    for file in os.listdir(algo_lib_dir):
        if '.gsql' in file:
            gsql_path = os.path.join(algo_lib_dir, file)
            gsql_algo_name = file.replace('.gsql','')
            
            change_log += f'\n## `{gsql_algo_name}` Logs\n'
            gsql_logs = gsql_git.log('--follow', '--pretty=format:%h!!%an!!%as!!%s', f'{gsql_path}')
            # change_log += f'\n```\n{gsql_logs}\n```\n'

            for log in gsql_logs.splitlines():
                hashid, author, date, message = log.split('!!')
                change_log += f'> ## {date}\n> #### ({hashid}) {author} : {message}\n'
        
    return change_log



def write_readme_files(paths):
    for dir in paths:
        specific_readme = ['algorithms/GraphML/Embeddings/Node2Vec', 'algorithms/GraphML/Embeddings/FastRP']
        title = dir.split('/')[-1]
        doc_title = title.replace('_',' ').title()
        link = TIGERGRAPH_DOCUMENTATION_LINK + Documentation[title]
        if dir not in specific_readme:
            with open(os.path.join(dir, 'README.md'), 'w') as handler:
                template = f'# {doc_title}\n## [TigerGraph {doc_title} Documentation]({link})\n'
                for algo in os.listdir(dir):
                    if algo.endswith('.gsql'):
                        algo_name = algo.replace('.gsql','')
                        template += f'\n### Install {algo_name} via Tigergraph CLI\n'
                        template += f'\n```bash\n$ tg box algos install {algo_name}\n```\n'
                        template += f'\n### Install {algo_name} via GSQL terminal\n'
                        template += f'\n```bash\n$ BEGIN\n# Paste {algo_name} code after BEGIN command\n$ END \n$ INSTALL QUERY {algo_name}\n```'
                handler.write(template)
        with open(os.path.join(dir, 'CHANGELOG.md'), 'w') as handler:
            handler.write(fetch_change_log(dir,doc_title))



if __name__ == "__main__":
    set_dirs = set()
    recursvie_dir('algorithms', set_dirs)
    write_readme_files(set_dirs)

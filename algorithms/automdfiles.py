from genericpath import isdir
import os
import git
import time
import datetime


TIGERGRAPH_DOCUMENTATION_LINK = 'https://docs.tigergraph.com/graph-algorithm-library/'
TIGERGRAPH_DISCORD_LINK = 'https://discord.gg/vFbmPyvJJN'
TIGERGRAPH_COMMUNITY_LINK = 'https://community.tigergraph.com'

## CHANGE (once official)
TIGERGRAPH_STARTERKIT_LINK = 'https://github.com/zrougamed/TigerGraph-Starter-Kits-Parser'

TIGERGRAPH_GSQL_REPO_LINK = 'https://github.com/tigergraph/gsql-graph-algorithms/blob/master/'
TIGERGRAPH_COMMITS_LINK = 'https://github.com/tigergraph/gsql-graph-algorithms/commit/'

# CHANGE TO DESIRED VERSION
TIGERGRAPH_CURRENT_GSQL_VERSION = 'v3.2.1'  

TIGERGRAPH_CURRENT_VERSION_DATE_READABLE = datetime.date.today().strftime("%B %d, %Y")
centrality = 'centrality'
similarity = 'similarity'
community = 'community'
path = 'path'
node = 'node-embeddings'
classification = 'classification'

Documentation = {
    'betweenness': f'{centrality}/betweenness-centrality',
    'closeness': f'{centrality}/closeness-centrality',
    'weakly_connected_components': f'{community}/connected-components',
    'strongly_connected_components': f'{community}/connected-components',
    'cosine': f'{similarity}/cosine-similarity-of-neighborhoods-batch',
    'cycle_detection': f'{path}/cycle-detection',
    'estimated_diameter': f'{path}/estimated-diameter',
    'greedy_graph_coloring': f'{classification}greedy-graph-coloring',
    'jaccard': f'{similarity}/jaccard-similarity-of-neighborhoods-batch',
    'k_core': f'{community}/k-core-decomposition',
    'k_means': 'https://raw.githubusercontent.com/tigergraph/gsql-graph-algorithms/master/algorithms/schema-free/kmeans.gsql',
    'k_nearest_neighbors': f'{classification}/k-nearest-neighbors-cosine-neighbor-similarity-all-vertices-batch',
    'label_propagation': f'{community}/label-propagation',
    'local_clustering_coefficient': f'{community}/local-clustering-coefficient',
    'louvain_distributed': f'{community}/louvain-method-with-parallelism-and-refinement',
    'louvain': f'{community}/louvain-method-with-parallelism-and-refinement',
    'maximal_independent_set': f'{path}/maximal-independent-set',
    'minimum_spanning_forest': f'{path}/minimum-spanning-forest-msf',
    'minimum_spanning_tree': f'{path}/minimum-spanning-tree-mst',
    'pagerank': f'{centrality}/pagerank',
    'strongly_connected_components': f'{community}/strongly-connected-components-1',
    'shortest_path': f'{path}/single-source-shortest-path-weighted',
    'triangle_counting': f'{community}/triangle-counting',
    'Node2Vec': f'{node}/node-2-vec',
    'harmonic': f'{centrality}/harmonic-centrality',
    'FastRP': 'N/A',
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
    change_log = f'\n## {TIGERGRAPH_CURRENT_GSQL_VERSION} {title} Change Logs - {TIGERGRAPH_CURRENT_VERSION_DATE_READABLE}\n'
    # CHANGE THIS
    gsql_git = git.Git('~/Documents/GitHub/gsql-graph-algorithms')
    for file in os.listdir(algo_lib_dir):
        if '.gsql' in file or '.cpp' in file or '.hpp' in file:
            gsql_path = os.path.join(algo_lib_dir, file)
            gsql_algo_name = file.replace('.gsql','').replace('.cpp','').replace('.hpp','')
            
            change_log += f'\n### `{gsql_algo_name}`\n'
            gsql_logs = list(gsql_git.log('-m','--follow', '--date=iso', '--pretty=format:%H!!%h!!%an!!%as!!%s', f'--since="{get_last_merge_date_iso()}"', f'{gsql_path}').splitlines())
            gsql_logs += list(gsql_git.log('--full-history','--follow','--date=iso', '--pretty=format:%H!!%h!!%an!!%as!!%s', f'--since="{get_last_merge_date_iso()}"', f'{gsql_path}').splitlines())
            gsql_logs = set(gsql_logs)

            if not gsql_logs:
                continue
            for log in gsql_logs:
                hashid_long, hashid_short, author, date, message = log.split('!!')
                commit_link = TIGERGRAPH_COMMITS_LINK + hashid_long
                change_log += f'\n> [`{hashid_short}`]({commit_link}) {message}\n'
        
    return change_log

def get_last_merge_date_iso():
    gsql_git = git.Git('~/Documents/GitHub/gsql-graph-algorithms')
    last_merge = list(gsql_git.log('--merges', '--pretty=format:%aI').splitlines())[0]
    return last_merge



def write_md_files(paths):
    for dir in paths:
        specific_readme = ['algorithms/GraphML/Embeddings/Node2Vec', 'algorithms/GraphML/Embeddings/FastRP']
        title = dir.split('/')[-1]
        changelog_link = dir + '/CHANGELOG.md'
        doc_title = title.replace('_',' ').title()
        link = TIGERGRAPH_DOCUMENTATION_LINK + Documentation[title] if title in Documentation.keys() else TIGERGRAPH_DOCUMENTATION_LINK
        previous_changelog = ''
        if os.path.exists(os.path.join(dir, 'CHANGELOG.md')):
            with open(os.path.join(dir, 'CHANGELOG.md'), 'r') as handler:
                previous_changelog = handler.read()
        with open(os.path.join(dir, 'CHANGELOG.md'), 'w') as handler:
            handler.write(fetch_change_log(dir,doc_title) + previous_changelog)
        if dir not in specific_readme:
            with open(os.path.join(dir, 'README.md'), 'w') as handler:
                template = f'\n# {doc_title}\n'
                template += f'\n#### [{doc_title} Changelog]({TIGERGRAPH_GSQL_REPO_LINK+changelog_link}) | '
                template += f'[Discord]({TIGERGRAPH_DISCORD_LINK}) | '
                template += f'[Community]({TIGERGRAPH_COMMUNITY_LINK}) | '
                template += f'[TigerGraph Starter Kits]({TIGERGRAPH_STARTERKIT_LINK})\n'
                template += f'\n## [TigerGraph {doc_title} Documentation]({link})\n'
                template += f'\n## Available {doc_title} Algorithms \n'
                for algo in os.listdir(dir):
                    if algo.endswith('.gsql'):
                        algo_name = algo.replace('.gsql','')
                        algo_link = TIGERGRAPH_GSQL_REPO_LINK + dir + '/' + algo
                        template += f'\n* [`{algo_name}`]({algo_link})\n'
                template += f'\n## Installation \n'
                template += f'\n### Replace `<{doc_title} Algorithm>` with desired algorithm listed above \n'
                template += f'\n#### Via TigerGraph CLI\n'
                template += f'\n```bash\n$ tg box algos install <{doc_title} Algorithm>\n```\n'
                template += f'\n#### Via GSQL terminal\n'
                template += f'\n```bash\nGSQL > BEGIN\n# Paste <{doc_title} Algorithm> code after BEGIN command\nGSQL > END \nGSQL > INSTALL QUERY <{doc_title} Algorithm>\n```'
                handler.write(template)




if __name__ == "__main__":
    set_dirs = set()
    recursvie_dir('algorithms', set_dirs)
    write_md_files(set_dirs)
from genericpath import isdir
import os
r = 'algorithms'
s = set()
def recursvie_dir(path):
    for item in os.listdir(path):
        new_path = os.path.join(path, item)
        if os.path.isdir(new_path):
            if not has_subdirectories(new_path):
                s.add(new_path)
            recursvie_dir(new_path)

def has_subdirectories(path):
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            return True
    return False

recursvie_dir('algorithms')
for dir in s:
    ignore_dir = ['algorithms/GraphML/Embeddings/Node2Vec']
    if dir not in ignore_dir :
        with open(os.path.join(dir, 'README.md'), 'w') as handler:
            title = dir.split('/')[-1]
            link = f'https://docs.tigergraph.com/tigergraph-platform-overview/graph-algorithm-library#'
            template = f'## {title}\n### Documentation : {link}\n'
            template += f'### Install {title} via Tigergraph CLI\n'
            template += f'```bash\n$ tg box algos install {title}\n```\n'
            template += f'### Install {title} via GSQL terminal\n'
            template += f'```bash\n$ BEGIN \n\n# Paste query code after BEGIN command\n\n$ <{title}_gsql_code>\n$ END \n$ INSTALL QUERY {title}\n```'

            handler.write(template)



    
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
    with open(os.path.join(dir, 'README.md'), 'w') as handler:
        title = (dir.split('/')[-1]).capitalize()
        template = f'## {title}\nDocumentation : link'
        handler.write(template)
    
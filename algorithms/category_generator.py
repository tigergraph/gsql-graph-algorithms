import os


dir = next(os.walk(os.getcwd()))

print(dir[0], dir[1])

for d in dir[1]:
    f_name = os.path.join(dir[0], d, f"tg_category_{'_'.join(d.lower().split())}.yml")
    with open(f_name, "w") as f:
        pass

"""
for subdir, dirs, files in os.walk(os.getcwd()):
    print(dirs)
"""

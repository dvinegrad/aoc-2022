class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = {}
        self.subdirs = {}

    def add_file(self, fname, fsize):
        self.files[fname] = fsize

    def add_subdir(self, dirname):
        self.subdirs[dirname] = Dir(dirname, self)

    def get_subdir(self, dirname):
        return self.subdirs[dirname]

def compute_file_sizes(dir, size_map, path):
    total_size = sum(dir.files.values())
    
    if len(dir.subdirs) > 0:
        total_size += sum(map(lambda entry: compute_file_sizes(entry[1], size_map, path + entry[0] + '/'), dir.subdirs.items()))

    size_map[path + dir.name] = total_size
    return total_size


with open('input.txt') as f:
    lines = f.read().splitlines()

root = Dir('/', None)
cur = root
size_map = {}

for line in lines:
    if line.startswith("$ cd"):
        dirname = line.split("$ cd ")[1]
        if dirname == "/":
            cur = root
        elif dirname == "..":
            cur = cur.parent
        else:
            cur = cur.get_subdir(dirname)
    elif line.startswith("$ ls"):
        continue
    elif line.startswith("dir"):
        dirname = line.split(" ")[1]
        cur.add_subdir(dirname)
    elif line[0].isdigit():
        size_str, fname = line.split(" ")
        cur.add_file(fname, int(size_str))

compute_file_sizes(root, size_map, '/')

res = sum(filter(lambda s: s <= 100000, size_map.values()))
print(res)
import hashlib


def hash(file):
    with open(file, 'r') as f:
        for line in f.readlines():
            yield hashlib.md5(line.encode('utf-8')).hexdigest()


for link in hash('links_list.txt'):
    print(link)

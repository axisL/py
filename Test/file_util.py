import os


def write_file(path, seq):
    f = open(path, 'w', encoding='utf-8')
    f.write(''.join(seq))
    f.close()


def file_walk(path, file_type, func):
    for root, dirs, files in os.walk(path):
        for file_name in files:
            file, typ = os.path.splitext(file_name)
            if typ == file_type:
                func(file_name, root)

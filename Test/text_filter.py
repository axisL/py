import os

from file_util import file_walk, write_file


def read_txt(name, path):
    full_name = os.path.join(path, name).replace("\\", "/")
    content = open(full_name, 'r', encoding='utf-8').read()
    log = ''
    for i in replace:
        if content.__contains__(i.split(",")[0]):
            log += i.split(",")[0]+"\n"
            print(i.split(",")[0])
        content = content.replace(i.split(",")[0], i.split(",")[1])
    write_file(os.path.join(path, ("done_" + name).replace(extension, ".conf")), content)
    write_file(os.path.join(path, ("log_" + name).replace(extension, ".log")), log)


replace = open("D:/recv/fileFilter/replace.txt", 'r', encoding='utf-8').readlines()
extension = ".txt"
file_walk("D:/recv/fileFilter/source", extension, read_txt)

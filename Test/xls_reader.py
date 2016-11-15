import os
import xlrd
from file_util import write_file, file_walk


def read_xls(name, path):
    full_name = os.path.join(path, name).replace("\\", "/")
    table = xlrd.open_workbook(full_name).sheet_by_index(0)
    c = map(lambda x, y, z: x + y + z + "\n\n", table.col_values(4), table.col_values(14), table.col_values(2))
    c = filter(lambda x: list((filter(lambda y: str(x).__contains__(y.replace('\n', '')), ignore))).__len__() == 0, c)
    c = filter(lambda x: list((filter(lambda y: not str(x).__contains__(y.replace('\n', '')), contain))).__len__() == 0,
               c)

    # c = filter(lambda x: not str(x).__contains__("玩家列表更新"), c)
    # for i in c:
    #     print(i + "\n")
    write_file(os.path.join(path, ("c_" + name).replace(extension, ".txt")), c)


ignore = open("D:/recv/bug/new/ignore.txt", 'r', encoding='utf-8').readlines()
contain = open("D:/recv/bug/new/contain.txt", 'r', encoding='utf-8').readlines()
extension = ".xls"
file_walk("D:/recv/bug/new", extension, read_xls)

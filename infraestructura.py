# import pandas as pd
import re
# import numpy
import sys

listSearch = ['LAR412_13.2', 'CS 275-2 ', 'CS 276', 'LAR306']
strFile = []

if sys.argv[1] is not None:
    def replace_str(line):
        line_filtered = ""
        for x in listSearch:
            count_ini = len(line)
            line_filtered = remove_repeated(line, x, count_ini)
            print(line_filtered)
        return line


    def remove_repeated(line, x, count_ini):
        line = line.replace('{}/{}'.format(x, x), x)
        if len(line) == count_ini:
            print("returned line: " + line)
            return line
        else:
            remove_repeated(line, x, len(line))


    print('route is:' + sys.argv[1])
    with open(sys.argv[1]) as fp:
        line = fp.readline()
        columns = len(line.split(';'))
        while line:
            listStr = line.split(';')
            if listStr[0] == "":
                del listStr[0]
                line = ';'.join(listStr)

            if len(listStr) == columns:
                # replace_str(line)
                strFile.append(replace_str(line))
            line = fp.readline()

    with open('D:/TestFileDestination/Infraestructura_modified.csv', 'w') as f:
        for item in strFile:
            f.write(item)

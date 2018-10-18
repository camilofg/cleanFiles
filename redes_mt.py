#import pandas as pd
import re
#import numpy
import sys


if sys.argv[1] is not None:
    print('route is:' + sys.argv[1])
    with open(sys.argv[1]) as fp:
        line = fp.readline()
        cnt = 0
        error_count = 0
        columns = len(line.split(';'))
        str_file = []
        uncompleted_line = ""
        prefix = ""
        while line:
            if line != "" and line != "\n":
                listStr = line.split(';')
                if listStr[0] == "":
                    del listStr[0]
                    line = ';'.join(listStr)
                if len(listStr) < columns:
                    if uncompleted_line != "":
                        prefix = ';'
                    else:
                        prefix = ''
                    uncompleted_line += prefix + re.sub(r'[\n]', '', line, flags=re.MULTILINE | re.DOTALL)

                    print("line: ", cnt)
                    print("uncompleted line: ", uncompleted_line)
                    print("actual line: ", line)
                    if len(uncompleted_line.split(';')) == columns:
                        print("completed Line", uncompleted_line)
                        str_file.append(uncompleted_line + '\n')
                        uncompleted_line = ""
                    error_count += 1
                else:
                    x = 'prn'
                    line = line.replace('"{}"{}'.format(x, x), ' ' + x)
                    x = 'PRN'
                    line = line.replace('"{}"{}'.format(x, x), ' ' + x)
                    line = re.sub(r'["  "]', ' ', line, flags=re.MULTILINE | re.DOTALL)
                    line = line.replace('"', '')
                    line = line = re.sub(r'[\t]', '', line, flags=re.MULTILINE | re.DOTALL)
                    str_file.append(line)
            cnt += 1
            line = fp.readline()
            #line = re.sub(r'[\t]', '', fp.readline(), flags=re.MULTILINE | re.DOTALL)
        with open('D:/TestFileDestination/REDES_MT_modified.csv', 'w') as f:
            for item in str_file:
                f.write(item)

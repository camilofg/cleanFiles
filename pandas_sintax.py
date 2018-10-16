#import pandas as pd
import re
#import numpy
import sys


if sys.argv[1] is not None:
    print('route is:' + sys.argv[1])
    with open(sys.argv[1]) as fp:
            #'D:/08102018/REDES_BT/REDES_BT.csv') as fp:
        line = fp.readline()
        cnt = 0
        error_count = 0
        str_file = []
        uncompleted_line = ""
        while line:
            cnt += 1
            line = fp.readline()
            listStr = line.split(';')
            if listStr[0] == "":
                del listStr[0]
            if len(listStr) < 22:
                uncompleted_line += re.sub(r'[\n]', '', line, flags=re.MULTILINE | re.DOTALL)
                print("uncompleted line: ", uncompleted_line)
                print("actual line: ", line)
                if len(uncompleted_line.split(';')) == 22:
                    print("completed Line", uncompleted_line)
                    str_file.append(uncompleted_line + '\n')
                    uncompleted_line = ""
                error_count += 1
                print("line {}".format(cnt))
            if len(listStr) == 22:
                str_file.append(line)

        with open('D:/TestFileDestination/REDES_BT_modified.csv', 'w') as f:
            for item in str_file:
                f.write(item)

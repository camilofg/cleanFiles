# import pandas as pd
import re
# import numpy
import sys
import postgres_conn as pgConn
import codecs

listSearch = ['LAR412_13.2', 'CS 275-2 ', 'CS 276', 'LAR306']
strFile = []
columns = ""
numColumns = 0

if sys.argv[1] is not None:
    line_str = ""
    cntLine = 0

    def replace_str(line):
        line_filtered = ""
        for x in listSearch:
            count_ini = len(line)
            line_filtered = remove_repeated(line, x, count_ini)
        return line_filtered


    def remove_repeated(line, x, count_ini):
        ret_line = line.replace('{}/{}'.format(x, x), x)
        if len(ret_line) == count_ini:
            ret_line = line
            return ret_line
        else:
            return remove_repeated(ret_line, x, len(ret_line))


    print('route is:' + sys.argv[1])
    with codecs.open(sys.argv[1], 'r', encoding='utf-8', errors='ignore') as fp:
        line = fp.readline()
        numColumns = len(line.split(';'))
        while line:
            listStr = line.split(';')
            if listStr[0] == "":
                del listStr[0]
                line = ';'.join(listStr)

            if len(listStr) == numColumns:
                if cntLine > 0:
                    new_line = replace_str(line)
                    new_line = line.replace('"CASERIO"', 'CASERIO')
                    x = 'prn'
                    line = line.replace('"{}"{}'.format(x, x), ' ' + x)
                    x = 'PRN'
                    line = line.replace('"{}"{}'.format(x, x), ' ' + x)
                    line = re.sub(r'["  "]', ' ', line, flags=re.MULTILINE | re.DOTALL)
                else:
                    dataType = " character varying(5000)"
                    strQuery = "CREATE TABLE Infraestructura_original("
                    columnsCreate = ""
                    columns = ""
                    prefix = ""
                    for item in listStr:
                        columnsCreate += prefix + item + dataType
                        columns += prefix + item
                        if columnsCreate != "":
                            prefix = ","
                    strQuery += columnsCreate + ")"
                    db = pgConn.DbConn()
                    db.execute_query(strQuery)
                    new_line = line
                strFile.append(new_line)
            print(cntLine)
            cntLine += 1
            line = fp.readline()

    with codecs.open('D:/TestFileDestination/Infraestructura_modified.csv', 'w', 'utf-8') as f:
        print(len(strFile))
        for item in strFile:
            f.write(item)
        insertQuery = "COPY Infraestructura_original(" + columns + ") FROM 'D:/08102018/Infraesctrutura/infraestructura.csv' " \
                      " DELIMITER ';' CSV HEADER;"
        db.execute_query(insertQuery)

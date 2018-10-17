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
                if (len(listStr) < columns) or (line[:1] == '|'):
                    if uncompleted_line != "" and line[:1] != '|':
                        prefix = ';'
                    else:
                        prefix = ''
                    uncompleted_line += prefix + re.sub(r'[\n]', '', line, flags=re.MULTILINE | re.DOTALL)
                    print("uncompleted line: ", uncompleted_line)
                    print("actual line: ", line)
                    if len(uncompleted_line.split(';')) == columns:
                        print("completed Line", uncompleted_line)
                        str_file.append(uncompleted_line + '\n')
                        uncompleted_line = ""
                    error_count += 1
                    print("line {}".format(cnt))
                if len(listStr) == columns and (line[:1] != '|'):
                    if cnt == 0:
                        str_file.append("TM_NOM; CD_NOM_GENERAL; UTM_X_I; UTM_Y_I; UTM_X_F; UTM_Y_F; TIPO_UBICACION; SEG_LONG_REAL; ID_CARTO; " \
                        "SECTOR; ARCO; TCBT_IDINT; LINEA_BT; CUBT_TENSION; CUBT_TENSION_NOMINAL; CONDUCTOR_DESCRIPTOR; MATERIAL; " \
                        "INFR_I; INFR_F; ID_APOYO_I; ID_APOYO_F; TRAFO")
                    else:
                        str_file.append(line)
            cnt += 1
            line = re.sub(r'[\t]', '', fp.readline(), flags=re.MULTILINE | re.DOTALL)
        with open('D:/TestFileDestination/REDES_BT_modified.csv', 'w') as f:
            for item in str_file:
                f.write(item)

import postgres_conn as pgConn


db = pgConn.DbConn()
columns = '"ID_CARTOGRAFICO", "NOM_APOYO", "ALTURA", "MATERIAL", "ESTRUCTURA", "CLASE_APOYO", "FORMA_CONST", ' \
          '"TENSION_MECANICA", "BRAZO_VAL", "DESCR_CAMARA", "USO_APOYO", "CANT_BRAZOS", "ID_APOYO", "TIPO_APOYO", ' \
          '"TIPO_CAMARA", "DIRECCION", "MAX_NIVEL_TENS", "COORDENADAS_X", "COORDENADAS_Y", "PROPIETARIO", ' \
          '"INFR_FECHA_BAJA", "MUNICIPIO", "POBLACION", "INFR_ESTRUCTURA_AP", "INFR_FUNCION_AP", "INFR_MAXIMO_NT_AP", ' \
          '"INFR_F_PUESTA_SERVICIO", "INFR_NORMA", "VALOR_ESFUERZO", "INFR_PERTENENCIA"'

insertQuery = "COPY Infraestructura_original(" + columns + ") FROM 'D:/08102018/Infraesctrutura/infraestructura.csv' " \
                      " DELIMITER ';' CSV HEADER ENCODING 'ISO_8859_5';"
db.execute_query(insertQuery)

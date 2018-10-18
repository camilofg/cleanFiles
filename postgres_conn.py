import psycopg2


class DbConn:
    def __init__(self):
        self.conn = psycopg2.connect("dbname='Informacion_Activos' user='postgres' password='Qwerty123' host='localhost' port='5432'")
        self.conn.autocommit = True

    def execute_query(self, query: object) -> object:
        try:
            cur = self.conn.cursor()
            cur.execute(query)
        except Exception as err:
            print(err.pgcode)

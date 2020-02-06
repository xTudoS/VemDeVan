import psycopg2
from psycopg2.extras import DictCursor

class DB:

    def conexao(self):
        conn = psycopg2.connect("dbname='vemdevan' user='postgres' host='localhost' password='senha'")
        return conn
    
    def execute(self, query, insert=False):
        data = None
        error = True
        try:
            conn = self.conexao()
            cur = conn.cursor(cursor_factory=DictCursor)
            cur.execute(query)
            if insert:
                conn.commit()
            else:
                data = cur.fetchall()
            error = False
        except Exception:
            conn.rollback()
        finally:
            conn.close()

        return data, error

import psycopg2
from srcs.config import Config


class DataBase:
    def __init__(self):
        self.conn = None
        self.cursor = None
        pass

    def getDataBaseConnection(self):
        self.conn = psycopg2.connect(dbname=Config.DATABASE_DBNAME,
                                     user=Config.DATABASE_USER,
                                     port=Config.DATABASE_PORT,
                                     host=Config.DATABASE_HOST,
                                     password=Config.DATABASE_PASSWORD
                                     )
        self.cursor = self.conn.cursor()
        return self.cursor

    def stopDataBaseConnection(self):
        self.conn.close()
        self.cursor.close()

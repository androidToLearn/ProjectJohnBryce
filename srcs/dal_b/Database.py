import psycopg2


class DataBase:
    def __init__(self):
        self.conn = None
        self.cursor = None
        pass

    def getDataBaseConnection(self):
        self.conn = psycopg2.connect(dbname='postgres',
                                     user='postgres',
                                     port='5432',
                                     host='localhost',
                                     password="newpassword"
                                     )
        self.cursor = self.conn.cursor()
        return self.cursor

    def stopDataBaseConnection(self):
        self.conn.close()
        self.cursor.close()

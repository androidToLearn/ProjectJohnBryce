import psycopg2

IS_TEST = True

conn = psycopg2.connect(dbname='postgres',
                        user='postgres',
                        port='5432',
                        host='localhost',
                        password="newpassword"
                        )
cursor = conn.cursor()

conn2 = psycopg2.connect(dbname='test_db',
                         user='postgres',
                         port='5432',
                         host='localhost',
                         password="newpassword"
                         )
cursor2 = conn2.cursor()


def getDataBaseConnection():
    if not IS_TEST:
        global cursor
        global conn
        conn = psycopg2.connect(dbname='postgres',
                                user='postgres',
                                port='5432',
                                host='localhost',
                                password="newpassword"
                                )
        cursor = conn.cursor()
        return cursor
    global cursor2
    conn2 = psycopg2.connect(dbname='test_db',
                             user='postgres',
                             port='5432',
                             host='localhost',
                             password="newpassword"
                             )
    cursor2 = conn2.cursor()
    return cursor2


def stopDataBaseConnection():
    if not IS_TEST:
        global conn
        global cursor
        cursor.close()
        conn.close()
    else:
        global conn2
        global cursor2
        cursor2.close()
        conn2.close()

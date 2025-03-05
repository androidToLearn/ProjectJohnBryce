from srcs.dal_b.Database import DataBase
from modules1.Like import Like


class Like_dao:
    COLUMN_ID_USER = "id_user"
    COLUMN_ID_VACATION = "id_vacation"
    TABLE_NAME = "likes"

    def __init__(self):
        dataBase = DataBase()
        cur = dataBase.getDataBaseConnection()
        script = """CREATE TABLE IF NOT EXISTS likes (
                    id_user INTEGER,
                    id_vacation INTEGER
                )"""
        cur.execute(script)
        dataBase.conn.commit()
        dataBase.stopDataBaseConnection()

    def insertLike(self, like):
        dataBase = DataBase()
        cursor = dataBase.getDataBaseConnection()
        cursor.execute(f"""INSERT INTO {Like_dao.TABLE_NAME} ({Like_dao.COLUMN_ID_USER} , {Like_dao.COLUMN_ID_VACATION}) VALUES (%s , %s)""", (
            like.id_user, like.id_vacation, ))
        dataBase.stopDataBaseConnection()

    def deleteLikeByLike(self, like):
        dataBase = DataBase()
        cursor = dataBase.getDataBaseConnection()
        cursor.execute("DELETE FROM " + Like_dao.TABLE_NAME + " WHERE " + Like_dao.COLUMN_ID_USER +
                       "=" + str(like.id_user) + " AND " + Like_dao.COLUMN_ID_VACATION + "=" + str(like.id_vacation))
        dataBase.stopDataBaseConnection()

    def getAll(self):
        dataBase = DataBase()
        cursor = dataBase.getDataBaseConnection()
        cursor.execute("SELECT * FROM " + Like_dao.TABLE_NAME)
        results = cursor.fetchall()
        dataBase.stopDataBaseConnection()

        allLikes = []
        for result in results:
            allLikes.append(Like(results[0], result[1]))
        return allLikes

    def deleteAll():
        dataBase = DataBase()
        cursor = dataBase.getDataBaseConnection()
        deleteTable = "DROP TABLE IF EXISTS " + Like_dao.TABLE_NAME
        createTable = f"""CREATE TABLE IF NOT EXISTS {Like_dao.TABLE_NAME} ({Like_dao.COLUMN_ID_USER} "INTEGER," {Like_dao.COLUMN_ID_VACATION} INTEGER)"""
        cursor.execute(deleteTable)
        cursor.execute(createTable)

        dataBase.stopDataBaseConnection()

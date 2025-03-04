import srcs.dal_b.Database as Database
from modules1 import Like


class Like_dao:
    COLUMN_ID_USER = "id_user"
    COLUMN_ID_VACATION = "id_vacation"
    TABLE_NAME = "likes"

    def __init__(self):
        createTable = f"""CREATE TABLE IF NOT EXISTS {Like_dao.TABLE_NAME} ({Like_dao.COLUMN_ID_USER} "INTEGER," {Like_dao.COLUMN_ID_VACATION} INTEGER)"""
        cursor = Database.getDataBaseConnection()
        cursor.execute(createTable)
        Database.stopDataBaseConnection()

    def insertLike(self, like):
        cursor = Database.getDataBaseConnection()
        cursor.execute(f"""INSERT INTO {Like_dao.TABLE_NAME} ({Like_dao.COLUMN_ID_USER} , {Like_dao.COLUMN_ID_VACATION}) VALUES (%s , %s)""", (
            like.id_user, like.id_vacation, ))
        Database.stopDataBaseConnection()

    def deleteLikeByLike(self, like):
        cursor = Database.getDataBaseConnection()
        cursor.execute("DELETE FROM " + Like_dao.TABLE_NAME + "WHERE" + Like_dao.COLUMN_ID_USER +
                       "=" + like.id_user + "AND" + Like_dao.COLUMN_ID_VACATION + "=" + like.id_vacation)
        Database.stopDataBaseConnection()

    def getAll(self):
        cursor = Database.getDataBaseConnection()
        cursor.execute("SELECT * FROM " + Like_dao.TABLE_NAME)
        results = cursor.fetchall()
        Database.stopDataBaseConnection()

        allLikes = []
        for result in results:
            allLikes.append(Like(results[0], result[1]))
        return allLikes

    def deleteAll():
        cursor = Database.getDataBaseConnection()
        deleteTable = "DROP TABLE IF EXISTS " + Like_dao.TABLE_NAME
        createTable = f"""CREATE TABLE IF NOT EXISTS {Like_dao.TABLE_NAME} ({Like_dao.COLUMN_ID_USER} "INTEGER," {Like_dao.COLUMN_ID_VACATION} INTEGER)"""
        cursor.execute(deleteTable)
        cursor.execute(createTable)

        Database.stopDataBaseConnection()

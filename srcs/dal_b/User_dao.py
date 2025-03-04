import srcs.dal_b.Database as Database


class User_dao:
    COLUMN_ID = "id"
    COLUMN_NAME = "name"
    COLUMN_SECOND_NAME = "second_name"
    COLUMN_PASSWORD = "password"
    COLUMN_EMAIL = "email"
    COLUMN_ID_ROLE = "id_role"
    TABLE_NAME = "users"

    def __init__(self):
        createTable = f"""CREATE TABLE IF NOT EXISTS {User_dao.TABLE_NAME} ({User_dao.COLUMN_ID} SERIAL INTEGER KEY,
        {User_dao.COLUMN_NAME} VARCHAR(225),
        {User_dao.COLUMN_SECOND_NAME} VARCHAR(225),
        {User_dao.COLUMN_PASSWORD} VARCHAR(225),
        {User_dao.COLUMN_EMAIL} VARCHAR(225),
        {User_dao.COLUMN_ID_ROLE} INTEGER
        )"""
        cursor = Database.getDataBaseConnection()
        cursor.execute(createTable)
        Database.stopDataBaseConnection()

    def insertUser(self, user):
        cursor = Database.getDataBaseConnection()
        cursor.execute(f"""INSERT INTO {User_dao.TABLE_NAME} ({User_dao.COLUMN_NAME, User_dao.COLUMN_SECOND_NAME,
                                                               User_dao.COLUMN_PASSWORD, User_dao.COLUMN_EMAIL, User_dao.COLUMN_ID_ROLE})VALUES (%s , %s , %s , %s , %S) RETURNING {User_dao.COLUMN_ID}""", (user.name, user.second_name, user.password, user.email, user.id_role,))
        user.id = cursor.fetchone()[0]
        Database.stopDataBaseConnection()

    def getAll(self):
        cursor = Database.getDataBaseConnection()
        cursor.execute("SELECT * FROM " + User_dao.TABLE_NAME)
        users = cursor.fetchall()
        Database.stopDataBaseConnection()
        return users

    def deleteUserById(self, id):
        cursor = Database.getDataBaseConnection()
        cursor.execute(
            f"""DELETE FROM {User_dao.TABLE_NAME} WHERE {User_dao.COLUMN_ID} = {id}""")
        Database.stopDataBaseConnection()

    # def __init__(self, id: int, name: str, second_name: str, password: str, email: str, id_role: int):

    def getUserById(self, id):
        cursor = Database.getDataBaseConnection()
        cursor.execute(
            f"""SELECT * FROM {User_dao.TABLE_NAME} WHERE {User_dao.COLUMN_ID} = {id}""")
        result = cursor.fetchone()
        Database.stopDataBaseConnection()
        return User(id, result[1], result[2], result[3], result[4], result[5])

    def updateUserById(self, user):
        cursor = Database.getDataBaseConnection()
        cursor.execute(f"""UPDATE {User_dao.TABLE_NAME} 
                        SET {User_dao.COLUMN_NAME} = '{user.name}', 
                            {User_dao.COLUMN_SECOND_NAME} = '{user.second_name}', 
                            {User_dao.COLUMN_PASSWORD} = '{user.password}', 
                            {User_dao.COLUMN_EMAIL} = '{user.email}', 
                            {User_dao.COLUMN_ID_ROLE} = {user.id_role} 
                        WHERE {User_dao.COLUMN_ID} = {user.id}""")
        Database.stopDataBaseConnection()

    def deleteAll():
        cursor = Database.getDataBaseConnection()
        deleteTable = "DROP TABLE IF EXISTS " + User_dao.TABLE_NAME
        createTable = f"""CREATE TABLE IF NOT EXISTS {User_dao.TABLE_NAME} ({User_dao.COLUMN_ID} SERIAL INTEGER KEY,
        {User_dao.COLUMN_NAME} VARCHAR(225),
        {User_dao.COLUMN_SECOND_NAME} VARCHAR(225),
        {User_dao.COLUMN_PASSWORD} VARCHAR(225),
        {User_dao.COLUMN_EMAIL} VARCHAR(225),
        {User_dao.COLUMN_ID_ROLE} INTEGER
        )"""
        cursor.execute(deleteTable)
        cursor.execute(createTable)

        Database.stopDataBaseConnection()

from srcs.dal_b.Database import DataBase


class User_dao:
    COLUMN_ID = "id"
    COLUMN_NAME = "name"
    COLUMN_SECOND_NAME = "second_name"
    COLUMN_PASSWORD = "password"
    COLUMN_EMAIL = "email"
    COLUMN_ID_ROLE = "id_role"
    TABLE_NAME = "users"

    def __init__(self):
        print("created")

    def insertUser(self, user):
        dataBase = DataBase()
        cursor = dataBase.getDataBaseConnection()
        cursor.execute(f"""INSERT INTO {User_dao.TABLE_NAME} ({User_dao.COLUMN_NAME}, {User_dao.COLUMN_SECOND_NAME}, 
                                                            {User_dao.COLUMN_PASSWORD}, {User_dao.COLUMN_EMAIL}, {User_dao.COLUMN_ID_ROLE}) 
                            VALUES (%s, %s, %s, %s, %s) RETURNING {User_dao.COLUMN_ID}""",
                       (user.name, user.second_name, user.password, user.email, user.id_role))

        user.id = cursor.fetchone()[0]
        dataBase.stopDataBaseConnection()

    def getAll(self):
        print("get all")
        dataBase = DataBase()
        cursor = dataBase.getDataBaseConnection()
        print("get connection")
        cursor.execute("SELECT * FROM " + User_dao.TABLE_NAME)
        print("do execute")
        users = cursor.fetchall()
        print("fetch all")

        allUsers = []
        if cursor.fetchone() is None:
            return allUsers

        for user in users:
            allUsers.append(
                User(user[0], user[1], user[2], user[3], user[4], user[5]))
        dataBase.stopDataBaseConnection()
        return allUsers

    def deleteUserById(self, id):
        dataBase = DataBase()
        cursor = dataBase.getDataBaseConnection()
        cursor.execute(
            f"""DELETE FROM {User_dao.TABLE_NAME} WHERE {User_dao.COLUMN_ID} = {id}""")
        dataBase.stopDataBaseConnection()

    # def __init__(self, id: int, name: str, second_name: str, password: str, email: str, id_role: int):

    def getUserById(self, id):
        dataBase = DataBase()
        cursor = dataBase.getDataBaseConnection()
        cursor.execute(
            f"""SELECT * FROM {User_dao.TABLE_NAME} WHERE {User_dao.COLUMN_ID} = {id}""")
        result = cursor.fetchone()
        dataBase.stopDataBaseConnection()
        return User(id, result[1], result[2], result[3], result[4], result[5])

    def updateUserById(self, user):
        dataBase = DataBase()
        cursor = dataBase.getDataBaseConnection()
        cursor.execute(f"""UPDATE {User_dao.TABLE_NAME} 
                        SET {User_dao.COLUMN_NAME} = '{user.name}', 
                            {User_dao.COLUMN_SECOND_NAME} = '{user.second_name}', 
                            {User_dao.COLUMN_PASSWORD} = '{user.password}', 
                            {User_dao.COLUMN_EMAIL} = '{user.email}', 
                            {User_dao.COLUMN_ID_ROLE} = {user.id_role} 
                        WHERE {User_dao.COLUMN_ID} = {user.id}""")
        dataBase.stopDataBaseConnection()

    def deleteAll():
        dataBase = DataBase()
        cursor = dataBase.getDataBaseConnection()
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

        dataBase.stopDataBaseConnection()

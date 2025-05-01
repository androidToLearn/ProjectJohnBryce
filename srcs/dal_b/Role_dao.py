from srcs.dal_b.Database import Database
import modules1.Role as Role


class Role_dao:
    COLUMN_ID = "id"
    COLUMN_NAME = "name"
    TABLE_NAME = "roles"

    def __init__(self):
        pass

    def insertRole(self, role):
        dataBase = Database()
        cursor = dataBase.getDataBaseConnection()
        cursor.execute(
            f"""INSERT INTO {Role_dao.TABLE_NAME} ({Role_dao.COLUMN_NAME}) VALUES (%s) RETURNING {role.id}""", (role.name,))
        role.id = cursor.fetchone()[0]
        dataBase.stopDataBaseConnection()

    def deleteRoleById(self, id):
        dataBase = Database()
        cursor = dataBase.getDataBaseConnection()
        cursor.execute(
            f"""DELETE FROM {Role_dao.TABLE_NAME} WHERE {Role_dao.COLUMN_ID} = {id}""")
        dataBase.stopDataBaseConnection()

    def updateRoleById(self, role):
        dataBase = Database()
        cursor = dataBase.getDataBaseConnection()
        cursor.execute(
            f"""UPDATE {Role_dao.TABLE_NAME} SET {Role_dao.COLUMN_NAME} = {role.name} WHERE {Role_dao.COLUMN_ID} = {role.id}""")
        dataBase.stopDataBaseConnection()

    def getRoleById(self, id):
        dataBase = Database()
        cursor = dataBase.getDataBaseConnection()
        cursor.execute("SELECT * FROM " +
                       Role_dao.TABLE_NAME + "WHERE = " + id)
        result = cursor.fetchone()
        dataBase.stopDataBaseConnection()
        return Role(result[0], result[1])

    def getAll(self):
        dataBase = Database()
        cursor = dataBase.getDataBaseConnection()
        cursor.execute("SELECT * FROM " + Role_dao.TABLE_NAME)
        results = cursor.fetchall()
        dataBase.stopDataBaseConnection()
        allRoles = []
        for result in results:
            allRoles.append(Role(result[0], result[1]))
        return allRoles

    def deleteAll(self):
        dataBase = Database()
        cursor = dataBase.getDataBaseConnection()
        deleteTable = "DROP TABLE IF EXISTS " + Role_dao.TABLE_NAME
        createTable = f"""CREATE TABLE IF NOT EXISTS {Role_dao.TABLE_NAME} ({Role_dao.COLUMN_ID} SERIAL PRIMARY KEY,
        {Role_dao.COLUMN_NAME} VARCHAR(225))"""
        cursor.execute(deleteTable)
        cursor.execute(createTable)

        dataBase.stopDataBaseConnection()

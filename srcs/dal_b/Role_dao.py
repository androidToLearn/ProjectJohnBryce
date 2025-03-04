import Database
import modules1.Role as Role


class Role_dao:
    COLUMN_ID = "id"
    COLUMN_NAME = "name"
    TABLE_NAME = "roles"

    def __init__(self):
        createTable = f"""CREATE TABLE IF NOT EXISTS {Role_dao.TABLE_NAME} ({Role_dao.COLUMN_ID} SERIAL PRIMARY KEY,
        {Role_dao.COLUMN_NAME} VARCHAR(225))"""
        cursor = Database.getDataBaseConnection()
        cursor.execute(createTable)
        Database.stopDataBaseConnection()

    def insertRole(self, role):
        cursor = Database.getDataBaseConnection()
        cursor.execute(
            f"""INSERT INTO {Role_dao.TABLE_NAME} ({Role_dao.COLUMN_NAME}) VALUES (%s) RETURNING {role.id}""", (role.name,))
        role.id = cursor.fetchone()[0]
        Database.stopDataBaseConnection()

    def deleteRoleById(self, id):
        cursor = Database.getDataBaseConnection()
        cursor.execute(
            f"""DELETE FROM {Role_dao.TABLE_NAME} WHERE {Role_dao.COLUMN_ID} = {id}""")
        Database.stopDataBaseConnection()

    def updateRoleById(self, role):
        cursor = Database.getDataBaseConnection()
        cursor.execute(
            f"""UPDATE {Role_dao.TABLE_NAME} SET {Role_dao.COLUMN_NAME} = {role.name} WHERE {Role_dao.COLUMN_ID} = {role.id}""")
        Database.stopDataBaseConnection()

    def getRoleById(self, id):
        cursor = Database.getDataBaseConnection()
        cursor.execute("SELECT * FROM " +
                       Role_dao.TABLE_NAME + "WHERE = " + id)
        result = cursor.fetchone()
        Database.stopDataBaseConnection()
        return Role(result[0], result[1])

    def getAll():
        cursor = Database.getDataBaseConnection()
        cursor.execute("SELECT * FROM " + Role_dao.TABLE_NAME)
        results = cursor.fetchall()
        Database.stopDataBaseConnection()
        allRoles = []
        for result in results:
            allRoles.append(Role(result[0], result[1]))
        return allRoles

    def deleteAll():
        cursor = Database.getDataBaseConnection()
        deleteTable = "DROP TABLE IF EXISTS " + Role_dao.TABLE_NAME
        createTable = f"""CREATE TABLE IF NOT EXISTS {Role_dao.TABLE_NAME} ({Role_dao.COLUMN_ID} SERIAL PRIMARY KEY,
        {Role_dao.COLUMN_NAME} VARCHAR(225))"""
        cursor = Database.getDataBaseConnection()
        cursor.execute(deleteTable)
        cursor.execute(createTable)

        Database.stopDataBaseConnection()

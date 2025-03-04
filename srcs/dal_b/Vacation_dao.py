import srcs.dal_b.Database as Database
import modules1.Vacation as Vacation


class Vacation_dao:
    COLUMN_ID = "id"
    COLUMN_ID_COUNTRY = "id_country"
    COLUMN_DESCRIPTION = "description"
    COLUMN_DATE_START = "date_start"
    COLUMN_DATE_END = "date_end"
    COLUMN_PRICE = "price"
    COLUMN_IMAGE_NAME = "image_name"
    TABLE_NAME = "vacations"

    #    def __init__(self, id: int, id_country: int, description: str, date_start: str, date_end: str, price: int, image_name: str):

    def __init__(self):
        createTable = f"""CREATE TABLE IF NOT EXISTS {Vacation_dao.TABLE_NAME} ({Vacation_dao.COLUMN_ID} SERIAL PRIMARY KEY,
        {Vacation_dao.COLUMN_ID_COUNTRY} "INTEGER",
        {Vacation_dao.COLUMN_DESCRIPTION} VARCHAR(225),
        {Vacation_dao.COLUMN_DATE_START} VARCHAR(225),
        {Vacation_dao.COLUMN_DATE_END} VARCHAR(225),
        {Vacation_dao.COLUMN_PRICE} INTEGER,
        {Vacation_dao.COLUMN_IMAGE_NAME} VARCHAR(225))"""
        cursor = Database.getDataBaseConnection()
        cursor.execute(createTable)
        Database.stopDataBaseConnection()

    def insertVacation(self, vacation):
        cursor = Database.getDataBaseConnection()
        cursor.execute(
            f"""INSERT INTO {Vacation_dao.TABLE_NAME} ({Vacation_dao.COLUMN_DESCRIPTION, Vacation_dao.COLUMN_DATE_START, Vacation_dao.COLUMN_DATE_END, Vacation_dao.COLUMN_PRICE, Vacation_dao.COLUMN_ID_COUNTRY, Vacation_dao.COLUMN_IMAGE_NAME}) VALUES (%s , %s , %s , %s , %s, %s) RETURNING {Vacation_dao.COLUMN_ID}""", (vacation.description, vacation.date_start, vacation.date_end, vacation.price, vacation.id_country, vacation.image_name))
        vacation.id = cursor.fetchone()[0]
        Database.stopDataBaseConnection()

    def deleteVacationById(self, id):
        cursor = Database.getDataBaseConnection()
        cursor.execute(
            f"""DELETE FROM {Vacation_dao.TABLE_NAME} WHERE {Vacation_dao.COLUMN_ID} = {id}""")
        Database.stopDataBaseConnection()

    def getAll(self):
        cursor = Database.getDataBaseConnection()
        cursor.execute("SELECT * FROM" + Vacation_dao.TABLE_NAME)
        results = cursor.fetchall()
        Database.stopDataBaseConnection()
        allVacations = []
        for result in results:
            allVacations.append(Vacation(
                [result[0], result[1], result[2], result[3], result[4], result[5], result[6]]))
        return allVacations

    def getVacationById(self, id):
        cursor = Database.getDataBaseConnection()
        cursor.execute("SELECT * FROM" + Vacation_dao.TABLE_NAME +
                       "WHERE" + Vacation_dao.COLUMN_ID + "=" + id)
        result = cursor.fetchone()
        Database.stopDataBaseConnection()
        return Vacation([result[0], result[1], result[2], result[3], result[4], result[5], result[6]])

    #    def __init__(self, id: int, id_country: int, description: str, date_start: str, date_end: str, price: int, image_name: str):

    def updateVacationById(self, vacation):
        cursor = Database.getDataBaseConnection()
        cursor.execute(f"""UPDATE {Vacation_dao.TABLE_NAME} 
                        SET {Vacation_dao.COLUMN_ID_COUNTRY} = '{vacation.id_country}', 
                            {Vacation_dao.COLUMN_DESCRIPTION} = '{vacation.description}', 
                            {Vacation_dao.COLUMN_DATE_START} = '{vacation.date_start}', 
                            {Vacation_dao.COLUMN_DATE_END} = '{vacation.date_end}',
                            {Vacation_dao.COLUMN_IMAGE_NAME} = '{vacation.image_name}', 
                            {Vacation_dao.COLUMN_PRICE} = {vacation.price} 
                        WHERE {Vacation_dao.COLUMN_ID} = {vacation.id}""")
        Database.stopDataBaseConnection()

    def deleteAll():
        cursor = Database.getDataBaseConnection()
        deleteTable = "DROP TABLE IF EXISTS " + Vacation_dao.TABLE_NAME
        createTable = f"""CREATE TABLE IF NOT EXISTS {Vacation_dao.TABLE_NAME} ({Vacation_dao.COLUMN_ID} SERIAL PRIMARY KEY,
        {Vacation_dao.COLUMN_ID_COUNTRY} "INTEGER",
        {Vacation_dao.COLUMN_DESCRIPTION} VARCHAR(225),
        {Vacation_dao.COLUMN_DATE_START} VARCHAR(225),
        {Vacation_dao.COLUMN_DATE_END} VARCHAR(225),
        {Vacation_dao.COLUMN_PRICE} INTEGER,
        {Vacation_dao.COLUMN_IMAGE_NAME} VARCHAR(225))"""
        cursor = Database.getDataBaseConnection()
        cursor.execute(deleteTable)
        cursor.execute(createTable)

        Database.stopDataBaseConnection()

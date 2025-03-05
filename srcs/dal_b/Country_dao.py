import Database
import modules1.Country as Country


class Country_dao():
    NAME_TABLE = 'country'
    COLUMN_NAME = 'name'
    COLUMN_ID = 'id'

    def __init__(self):
        print("created")

    def insertCountry(self, country):
        cursor = Database.getDataBaseConnection()
        cursor.execute(
            f"""INSERT INTO {Country_dao.NAME_TABLE}({Country_dao.COLUMN_NAME}) VALUES (%s) RETURNING {Country_dao.COLUMN_ID}""", (country.name,))
        country.id = cursor.fetchone()[0]
        Database.stopDataBaseConnection()

    def getAll(self):
        cursor = Database.getDataBaseConnection()
        cursor.execute(f"""SELECT * FROM {Country_dao.NAME_TABLE}""")
        countries = cursor.fetchall()
        Database.stopDataBaseConnection()

        allCountries = []
        for country in countries:
            allCountries.append(Country(country[0], country[1]))

        return allCountries

    def updateById(self, country):
        cursor = Database.getDataBaseConnection()
        cursor.execute(
            f"""UPDATE {Country_dao.NAME_TABLE} SET {Country_dao.COLUMN_NAME} = %s WHERE {Country_dao.COLUMN_ID} = %s""", (country.name, country.id))
        Database.stopDataBaseConnection()

    def getById(self, id):
        cursor = Database.getDataBaseConnection()
        cursor.execute(
            f"""SELECT * FROM {Country_dao.NAME_TABLE} WHERE {Country_dao.COLUMN_ID} = %s""", (id, ))
        result = cursor.fetchone()
        Database.stopDataBaseConnection()
        return Country(result[0], result[1])

    def deleteCountryById(self, id):
        cursor = Database.getDataBaseConnection()
        cursor.execute(
            f"""DELETE FROM {Country_dao.NAME_TABLE} WHERE {Country_dao.COLUMN_ID} = {id}""")
        Database.stopDataBaseConnection()

    def deleteAll():
        cursor = Database.getDataBaseConnection()
        deleteTable = "DROP TABLE IF EXISTS " + Country_dao.NAME_TABLE
        create_table = f"""CREATE TABLE IF NOT EXISTS {Country_dao.NAME_TABLE} (
        {Country_dao.COLUMN_ID} SERIAL PRIMARY KEY, 
        {Country_dao.COLUMN_NAME} VARCHAR(225))"""
        cursor.execute(deleteTable)
        cursor.execute(create_table)

        Database.stopDataBaseConnection()

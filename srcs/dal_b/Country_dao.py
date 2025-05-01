from srcs.dal_b.Database import Database
from modules1.Country import Country


class Country_dao():
    NAME_TABLE = 'country'
    COLUMN_NAME = 'name'
    COLUMN_ID = 'id'

    def __init__(self):
        pass

    def insertCountry(self, country):
        dataBase = Database()
        cursor = dataBase.getDataBaseConnection()
        cursor.execute(
            f"""INSERT INTO {Country_dao.NAME_TABLE}({Country_dao.COLUMN_NAME}) VALUES (%s) RETURNING {Country_dao.COLUMN_ID}""", (country.name_country,))
        country.id = cursor.fetchone()[0]
        dataBase.stopDataBaseConnection()

    def getAll(self):
        dataBase = Database()
        cursor = dataBase.getDataBaseConnection()
        cursor.execute(f"""SELECT * FROM {Country_dao.NAME_TABLE}""")
        countries = cursor.fetchall()
        dataBase.stopDataBaseConnection()

        allCountries = []
        for country in countries:
            allCountries.append(Country(country[0], country[1]))

        return allCountries

    def updateById(self, country):
        dataBase = Database()
        cursor = dataBase.getDataBaseConnection()
        cursor.execute(
            f"""UPDATE {Country_dao.NAME_TABLE} SET {Country_dao.COLUMN_NAME} = %s WHERE {Country_dao.COLUMN_ID} = %s""", (country.name_country, country.id))
        dataBase.stopDataBaseConnection()

    def getById(self, id):
        dataBase = Database()
        cursor = dataBase.getDataBaseConnection()
        cursor.execute(
            f"""SELECT * FROM {Country_dao.NAME_TABLE} WHERE {Country_dao.COLUMN_ID} = %s""", (id, ))
        result = cursor.fetchone()
        dataBase.stopDataBaseConnection()
        return Country(result[0], result[1])

    def deleteCountryById(self, id):
        dataBase = Database()
        cursor = dataBase.getDataBaseConnection()
        cursor.execute(
            f"""DELETE FROM {Country_dao.NAME_TABLE} WHERE {Country_dao.COLUMN_ID} = {id}""")
        dataBase.stopDataBaseConnection()

    def deleteAll(self):
        dataBase = Database()
        cursor = dataBase.getDataBaseConnection()
        deleteTable = "DROP TABLE IF EXISTS " + Country_dao.NAME_TABLE
        create_table = f"""CREATE TABLE IF NOT EXISTS {Country_dao.NAME_TABLE} (
        {Country_dao.COLUMN_ID} SERIAL PRIMARY KEY, 
        {Country_dao.COLUMN_NAME} VARCHAR(225))"""
        cursor.execute(deleteTable)
        cursor.execute(create_table)

        dataBase.stopDataBaseConnection()

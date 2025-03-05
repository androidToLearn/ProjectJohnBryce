import asyncio
from modules1.Vacation import Vacation
from srcs.dal_b.Vacation_dao import Vacation_dao


def getAllVacationsInBackground():
    return asyncio.run(getAllVacations1())


async def getAllVacations1():
    task = asyncio.create_task(getAllVacations())
    return await task


async def getAllVacations():
    #    def __init__(self, id: int, id_country: int, description: str, date_start: str, date_end: str, price: int, image_name: str):

    keepVacation = Vacation(-1, 1, "", "", "", 1, "")
    vacation_dao = Vacation_dao()
    allVacations = vacation_dao.getAll()
    b = True
    while b:
        b = False
        for i in range(0, len(allVacations) - 1):
            if isVacationNewer(allVacations[i], allVacations[i + 1]):
                v1 = allVacations[i]
                v2 = allVacations[i + 1]
                b = True
                keepVacation.id = v1.id
                keepVacation.id_country = v1.id_country
                keepVacation.description = v1.description
                keepVacation.date_start = v1.date_start
                keepVacation.date_end = v1.date_end
                keepVacation.price = v1.price
                keepVacation.image_name = v1.image_name

                v1.id = v2.id
                v1.id_country = v2.id_country
                v1.description = v2.description
                v1.date_start = v2.date_start
                v1.date_end = v2.date_end
                v1.price = v2.price
                v1.image_name = v2.image_name

                v2.id = keepVacation.id
                v2.id_country = keepVacation.id_country
                v2.description = keepVacation.description
                v2.date_start = keepVacation.date_start
                v2.date_end = keepVacation.date_end
                v2.price = keepVacation.price
                v2.image_name = keepVacation.image_name
    return allVacations


def isVacationNewer(v1, v2):
    day = v1.date_start[0:2]
    month = v1.date_start[3:5]
    year = v1.date_start[6:10]

    day2 = v2.date_start[0:2]
    month2 = v2.date_start[3:5]
    year2 = v2.date_start[6:10]

    if year > year2:
        return True
    elif year < year2:
        return False

    if month > month2:
        return True
    elif month < month2:
        return False

    if day > day2:
        return True
    elif day < day2:
        return False
    return False

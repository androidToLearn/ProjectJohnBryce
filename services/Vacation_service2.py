import asyncio
from datetime import datetime


def insertVacationsInBackground(id_country, description, date_start, date_end, price):
    return asyncio.run(insertVacations1(id_country, description, date_start, date_end, price))


async def insertVacations1(id_country, description, date_start, date_end, price):
    task = asyncio.create_task(insertVacations(
        id_country, description, date_start, date_end, price))
    return await task


async def insertVacations(id_country, description, date_start, date_end, price):
    if len(str(id_country)) > 0 and len(description) > 0 and len(date_start) > 0 and len(date_end) > 0 and len(str(price)) > 0:
        if price < 0 or price > 10000:
            raise Exception("bad price")
        else:
            if isBigger(date_start, date_end):
                raise Exception("bad date!")
            else:
                now = datetime.now().strftime("%d/%m/%Y")
                if isBigger(now, date_start) or isBigger(now, date_end):
                    raise Exception("bad start date")

    else:
        raise Exception("fill all fields")


def isBigger(date_start, date_end):
    day = date_start[0:2]
    month = date_start[3:5]
    year = date_start[6:10]

    day2 = date_end[0:2]
    month2 = date_end[3:5]
    year2 = date_end[6:10]

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

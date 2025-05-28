import asyncio
from datetime import datetime
from srcs.dal_b.Vacation_dao import Vacation_dao
from modules1.Vacation import Vacation


def insertVacations(id_country, description, date_start, date_end, price, filename, isInOther):
    print('--------------------')
    print('date_start:', date_start)
    print('date_end:', date_end)
    b = False
    try:
        int(date_start[0:4])
        int(date_end[0:4])
    except Exception:
        # רק אם הפורמאט לא הפוך תוסיף את ה0
        b = True

    if b:
        date_start = addZeros(date_start, isRevers=isInOther)
        date_end = addZeros(date_end, isRevers=isInOther)
    price = int(price)
    if len(str(id_country)) > 0 and len(description) > 0 and len(date_start) > 0 and len(date_end) > 0 and len(str(price)) > 0:
        if price < 0 or price > 10000:
            raise Exception("bad price")
        else:
            if isBigger(date_start, date_end, isInOther) or (len(date_start) != 10 or len(date_end) != 10):
                raise Exception("bad date!")
            else:
                now = datetime.now().strftime("%d/%m/%Y")

                if isBigger(now, date_start, isInOther, True) or isBigger(now, date_end, isInOther, True):
                    raise Exception("bad start date")
                vacation_dao = Vacation_dao()
                if isInOther:
                    vacation_dao.insertVacation(
                        Vacation(-1, id_country, description, date_start[::-1], date_end[::-1], int(price), filename))
                    print('date end', date_end[::-1])
                else:
                    vacation_dao.insertVacation(
                        Vacation(-1, id_country, description, date_start, date_end, int(price), filename))
                    print('date end', date_end)

    else:
        raise Exception("fill all fields")


def addZeros(date, isRevers):
    if isRevers:
        try:
            int(date[0:2])
            isWithZero = True
        except Exception:
            isWithZero = False
        if not isWithZero:
            date = date[0:1] + '0' + date[1:]

        try:
            int(date[3:5])
            isWithZero = True
        except Exception:
            isWithZero = False
        if not isWithZero:
            date = date[0:4] + '0' + date[4:]
    else:
        try:
            int(date[0:2])
            isWithZero = True
        except Exception:
            isWithZero = False
        if not isWithZero:
            date = '0' + date[0:]

        try:
            int(date[3:5])
            isWithZero = True
        except Exception:
            isWithZero = False
        if not isWithZero:
            date = date[0:3] + '0' + date[3:]
    print(date)
    return date


def isBigger(date_start, date_end, isInOther, isDate=False):
    if isInOther:
        try:
            if not isDate:
                day = int(date_start[0:2][::-1])
                month = int(date_start[3:5][::-1])
                year = int(date_start[6:10][::-1])
            else:
                day = int(date_start[0:2])
                month = int(date_start[3:5])
                year = int(date_start[6:10])

            day2 = int(date_end[0:2][::-1])
            month2 = int(date_end[3:5][::-1])
            year2 = int(date_end[6:10][::-1])
        except Exception:
            return True
    else:
        day = int(date_start[0:2])
        month = int(date_start[3:5])
        year = int(date_start[6:10])

        day2 = int(date_end[0:2])
        month2 = int(date_end[3:5])
        year2 = int(date_end[6:10])

    print('day', day)
    print('month', month)
    print('year', year)

    print('day2', day2)
    print('month2', month2)
    print('year2', year2)
    if year > year2:
        return True
    elif year < year2:
        return False

    if month > month2:
        return True
    elif month < month2:
        return False

    print('start day: ', day)
    print('end day: ', day2)
    if day > day2:
        return True

    elif day < day2:
        return False
    return False

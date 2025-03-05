import asyncio
from srcs.dal_b.User_dao import User_dao
from modules1.User import User

#    def __init__(self, id: int, name: str, second_name: str, password: str, email: str, id_role: int):


def userRegisterInBackground(name, second_name, password, email):
    asyncio.run(userRegister(name, second_name, password, email))


async def userRegister(name, second_name, password, email):
    asyncio.create_task(
        inUserRegister(name, second_name, password, email))


async def inUserRegister(name, second_name, password, email):

    if len(name) > 0 and len(second_name) > 0 and len(password) > 0 and len(email) > 0:

        if '@gmail.com' in email or '@gov.co.il' in email:
            if len(password) >= 4:
                user_dao = User_dao()
                users = user_dao.getAll()
                if isExistsUser(users, name, second_name, password, email):
                    return True
                else:
                    raise Exception("failed , gmail appear , try again!")
            else:
                raise Exception("password must be with less four length")
        else:
            raise Exception("email wrong")
    else:
        raise Exception("fill all fields")


def isExistsUser(users, name, second_name, password, email):
    for user in users:
        if user.email == email and user.password == password:
            return True
    return False

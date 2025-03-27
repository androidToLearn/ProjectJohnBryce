import asyncio
from srcs.dal_b.User_dao import User_dao
from modules1.User import User

#    def __init__(self, id: int, name: str, second_name: str, password: str, email: str, id_role: int):


def userLoginInBackground(name, second_name, password, email):
    asyncio.run(userLogin(name, second_name, password, email))


async def userLogin(name, second_name, password, email):
    asyncio.create_task(inUserLogin(name, second_name, password, email))


async def inUserLogin(name, second_name, password, email):
    """"login new user"""
    if len(name.strip()) > 0 and len(second_name.strip()) > 0 and len(password.strip()) > 0 and len(email.strip()) > 0:
        if '@gmail.com' in email or '@gov.co.il' in email:
            if len(password) >= 4:

                print("do...")
                user_dao = User_dao()
                print("after")
                users = user_dao.getAll()

                if not isGmailAppear(users, email):
                    user_dao.insertUser(
                        User(-1, name, second_name, password, email, 1))
                    print("login!")
                else:
                    raise Exception("failed , gmail appear , try again!")
            else:
                raise Exception("password must be with less four length")
        else:
            raise Exception("email wrong")
    else:
        raise Exception("fill all fields")


def isGmailAppear(users, email):
    for user in users:
        if user.email == email:
            return True
    return False

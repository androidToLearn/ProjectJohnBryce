import asyncio
from srcs.dal_b.User_dao import User_dao
from modules1.User import User

#    def __init__(self, id: int, name: str, second_name: str, password: str, email: str, id_role: int):


def isUserLogin(name, second_name, password, email, isAdmin):
    """"login new user"""
    if len(name.strip()) > 0 and len(second_name.strip()) > 0 and len(password.strip()) > 0 and len(email.strip()) > 0:
        if '@gmail.com' in email or '@gov.co.il' in email:
            if len(password) >= 4:

                print("do...")
                user_dao = User_dao()
                print("after")
                users = user_dao.getAll()

                if not isGmailAppear(users, email):
                    if isAdmin:
                        id = 0
                    else:
                        id = 1
                    user = User(-1, name, second_name, password, email, id)
                    user_dao.insertUser(user)
                    print("login!")
                    return user
                else:
                    return "failed , gmail appear , try again!"
            else:
                return "password must be with less four length"
        else:
            return "email pattern wrong"
    else:
        return "fill all fields"


def isGmailAppear(users, email):
    for user in users:
        print(user)
        if user.email == email:
            return True
    return False

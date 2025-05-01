import asyncio
from srcs.dal_b.User_dao import User_dao
from modules1.User import User

#    def __init__(self, id: int, name: str, second_name: str, password: str, email: str, id_role: int):


def isUserRegister(name, second_name, password, email, isAdmin):
    """enter with exists user"""
    if len(name) > 0 and len(second_name) > 0 and len(password) > 0 and len(email) > 0:

        if '@gmail.com' in email or '@gov.co.il' in email:
            if len(password) >= 4:
                user_dao = User_dao()
                users = user_dao.getAll()
                user = isExistsUser(users, name, second_name, password, email)
                if user != None:
                    if isAdmin:
                        id = 0
                    else:
                        id = 1
                    user.id_role = id
                    user_dao.updateUserById(user)
                    return user
                else:
                    return "failed , gmail or password wrong , try again!"
            else:
                return "password must be with less four length"
        else:
            return "email wrong"
    else:
        return "fill all fields"


def isExistsUser(users, name, second_name, password, email):
    """check if is user exists"""
    for user in users:
        if user.email == email and user.password == password:
            return user
    return None

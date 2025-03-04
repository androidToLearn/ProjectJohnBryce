import asyncio
import srcs.dal_b.Like_dao as Like_dao
import srcs.dal_b.User_dao as User_dao
import srcs.dal_b.Vacation_dao as Vacation_dao

#    def __init__(self, id: int, name: str, second_name: str, password: str, email: str, id_role: int):


def insertLikeInBackground(like):
    asyncio.run(insertLikeBack(like))


async def insertLikeBack(like):
    asyncio.create_task(
        insertLikeBack1(like))


async def insertLikeBack1(like):
    vacation_dao = Vacation_dao()
    user_dao = User_dao()
    vacations = vacation_dao.getAll()
    users = user_dao.getAll()
    if not isIdAppear(like.id_vacation, vacations):
        raise Exception("bad vacation id!")
    if not isIdAppear(like.id_user, users):
        raise Exception("bad user id")
    like_dao = Like_dao()
    like_dao.insertLike(like)


async def isIdAppear(id, objects):
    for o in objects:
        if o.id == id:
            return True
    return False

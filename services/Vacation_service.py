import asyncio
from srcs.dal_b.Vacation_dao import Vacation_dao
from srcs.dal_b.Like_dao import Like_dao


def deleteVacationsInBackground(id_vacation):
    return asyncio.run(deleteVacations1(id_vacation))


async def deleteVacations1(id_vacation):
    task = asyncio.create_task(deleteVacations(
        id_vacation))
    return await task


async def deleteVacations(id_vacation):
    vacation_dao = Vacation_dao()
    vacation_dao.deleteVacationById(id_vacation)
    like_dao = Like_dao()
    likes = like_dao.getAll()
    for like in likes:
        if like.id_vacation == id_vacation:
            like_dao.deleteLikeByLike(like)

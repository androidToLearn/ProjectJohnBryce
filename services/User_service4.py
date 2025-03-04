import asyncio
import srcs.dal_b.Like_dao as Like_dao

#    def __init__(self, id: int, name: str, second_name: str, password: str, email: str, id_role: int):


def deleteLikeInBackground(like):
    asyncio.run(deleteLikeBack(like))


async def deleteLikeBack(like):
    asyncio.create_task(
        deleteLikeBack1(like))


async def deleteLikeBack1(like):
    like_dao = Like_dao()
    like_dao.deleteLikeByLike(like)

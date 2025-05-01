import asyncio
from srcs.dal_b.Like_dao import Like_dao

#    def __init__(self, id: int, name: str, second_name: str, password: str, email: str, id_role: int):


def deleteLikeBack1(like):
    """delete some like"""
    like_dao = Like_dao()
    like_dao.deleteLikeByLike(like)

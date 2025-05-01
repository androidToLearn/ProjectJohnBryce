import unittest
from services import User_service
from services import User_service2
from services import User_service3
from services import User_service4
from services import Vacation_service
from services import Vacation_service1
from services import Vacation_service2
from services import Vacation_service3
from srcs.dal_b.Database import Database
from modules1.User import User
from modules1.Like import Like


class Test1(unittest.TestCase):
    def test_all(self):
        print("start....")
        dataBase = Database()
        conn = dataBase.getDataBaseConnection()
        with open('srcs/init_db.sql', 'r', encoding='utf8') as file:
            sql_script = file.read()
        conn.execute(sql_script)

        dataBase.stopDataBaseConnection()
        print("start services....")

        self.test_user_service()
        self.test_user_service2()
        self.test_user_service3()
        self.test_user_service4()
        self.test_user_vacation()
        self.test_user_vacation1()
        self.test_user_vacation2()
        self.test_user_vacation3()

    def test_user_service(self):
        User_service.isUserLogin(
            "yishay", "racmut", "123456", "rachmut@gmail.com", False)

       # User_service.isUserLogin(
        #    "yishay", "", "123456", "rachmut@gmail.com", False)

    def test_user_service2(self):
        User_service2.isUserRegister(
            "yishay", "racmut", "123456", "rachmut@gmail.com", False)
       # User_service2.isUserRegister(
        #    "yishay", "", "123456", "rachmut@gmail.com", False)

    def test_user_service3(self):
        like = Like(1, 1)
        User_service3.insertLikeBack1(like)
        like = Like(1, 100000000)
        User_service3.insertLikeBack1(like)

    def test_user_service4(self):
        like = Like(1, 1)
        User_service4.deleteLikeBack1(like)
        #    def __init__(self, id: int, name: str, second_name: str, password: str, email: str, id_role: int):

        # user = User(-1, "", "", "", "", 1)
        # User_service4.deleteLikeInBackground(user)

    def test_user_vacation(self):
        Vacation_service.deleteVacations(1)
        Vacation_service.deleteVacations(10000)

    def test_user_vacation1(self):
        print(Vacation_service1.getAllVacations())
       # self.assertEqual(
        #  Vacation_service1.getAllVacationsInBackground(), 8)  # בשביל שגיאה

    def test_user_vacation2(self):
        Vacation_service2.insertVacations(
            1, "חופשת הפירות", "10/10/2027", "10/11/2027", 100)
       # Vacation_service2.insertVacationsInBackground(
        #    1, "חופשת הפירות", "10/10/2027", "10/11/2027", 10000000)

    def test_user_vacation3(self):
        Vacation_service3.updateVacations(
            1, "חופשת הפירות", "10/10/2027", "10/11/2027", 100)
       # Vacation_service3.updateVacationsInBackground(
       #     1, '', "10/10/2027", "10/11/2027", 100)


if __name__ == "__name__":
    unittest.main()

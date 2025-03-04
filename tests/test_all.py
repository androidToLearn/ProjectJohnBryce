import unittest
import services.User_service as User_service
import services.User_service2 as User_service2
import services.User_service3 as User_service3
import services.User_service4 as User_service4
import services.Vacation_service as Vacation_service
import services.Vacation_service1 as Vacation_service1
import services.Vacation_service2 as Vacation_service2
import services.Vacation_service3 as Vacation_service3
import srcs.dal_b.Database as Database
from modules1.User import User
from modules1.Like import Like


class Test1(unittest.TestCase):
    def test_all(self):
        Database.IS_TEST = True
        conn = Database.getDataBaseConnection()
        with open('srcs/init_db.sql', 'r', encoding='utf8') as file:
            sql_script = file.read()
            conn.execute(sql_script)
        Database.stopDataBaseConnection()

        self.test_user_service()
        self.test_user_service2()
        self.test_user_service3()
        self.test_user_service4()
        self.test_user_vacation()
        self.test_user_vacation1()
        self.test_user_vacation2()
        self.test_user_vacation3()

        Database.IS_TEST = False
        conn = Database.getDataBaseConnection()
        with open('src/init_db.sql', 'r', encoding='utf8') as file:
            sql_script = file.read()
            conn.execute(sql_script)
        Database.stopDataBaseConnection()

    def test_user_service(self):
        User_service.userLoginInBackground(
            "yishay", "racmut", "123456", "rachmut@gmail.com")
        User_service.userLoginInBackground(
            "yishay", "", "123456", "rachmut@gmail.com")

    def test_user_service2(self):
        User_service2.userRegisterInBackground(
            "yishay", "racmut", "123456", "rachmut@gmail.com")
        User_service2.userRegisterInBackground(
            "yishay", "", "123456", "rachmut@gmail.com")

    def test_user_service3(self):
        like = Like(1, 1)
        User_service3.insertLikeInBackground(like)
        like = Like(1, 100000000)
        User_service3.insertLikeInBackground(like)

    def test_user_service4(self):
        like = Like(1, 1)
        User_service4.deleteLikeInBackground(like)
        user = User()
        User_service4.deleteLikeInBackground(user)

    def test_user_vacation(self):
        Vacation_service.deleteVacationsInBackground(1)
        Vacation_service.deleteVacationsInBackground(10000)

    def test_user_vacation1(self):
        print(Vacation_service1.getAllVacationsInBackground())
        self.assertEqual(Vacation_service1.getAllVacationsInBackground(), 8)

    def test_user_vacation2(self):
        Vacation_service2.insertVacationsInBackground(
            1, "חופשת הפירות", "10/10/2027", "10/11/2027", 100)
        Vacation_service2.insertVacationsInBackground(
            1, "חופשת הפירות", "10/10/2027", "10/11/2027", 10000000)

    def test_user_vacation3(self):
        Vacation_service3.updateVacationsInBackground(
            1, "חופשת הפירות", "10/10/2027", "10/11/2027", 100)
        Vacation_service3.updateVacationsInBackground(
            1, '', "10/10/2027", "10/11/2027", 100)


if __name__ == "__name__":
    unittest.main()

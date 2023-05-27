from selenium import webdriver
import unittest
from pages.sign_up_page1 import ZalandoLoginTest
from pages.short_password_page2 import ZalandoShortPassword
from pages.registration_page3 import ZalandoRegisterPassword
import test_data.data as td


class TestsZalando(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(td.mainpage)

    def test_sign(self):
        sign = ZalandoLoginTest(self.driver)
        sign.testcorrectpassword()

    def test_short(self):
        short_pass = ZalandoShortPassword(self.driver)
        short_pass.testshortpassword()

    def test_register(self):
        register = ZalandoRegisterPassword(self.driver)
        register.testinvalidregistration()

    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main(verbosity=2)

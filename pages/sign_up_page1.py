from locators import SignUpLocators
from pages.base_page import BasePage
import test_data
import time
import test_data.data as td


class ZalandoLoginTest(BasePage):
    def testcorrectpassword(self):
        # Zamknięcie ciasteczek
        time.sleep(8)
        window = self.driver.find_element(*SignUpLocators.WINDOW_BUTTON)
        window.click()
        # Kliknięcie na ikonę logowania
        login_button = self.driver.find_element(*SignUpLocators.LOGIN_BUTTON)
        login_button.click()
        time.sleep(2)
        # Logowanie na konto
        e_mail_input = self.driver.find_element(*SignUpLocators.EMAIL_BUTTON)
        e_mail_input.send_keys(*test_data.data.e_mail)
        time.sleep(2)
        password_input = self.driver.find_element(*SignUpLocators.PASSWORD_BUTTON)
        password_input.send_keys(*test_data.data.password)
        time.sleep(2)
        login_button2 = self.driver.find_element(*SignUpLocators.LOGIN_BUTTON2)
        login_button2.click()
        time.sleep(5)

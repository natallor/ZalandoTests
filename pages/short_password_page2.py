from locators import ShortPasswordLocators
from pages.base_page import BasePage
import test_data
import time
import test_data.data as td


class ZalandoShortPassword(BasePage):
    def testshortpassword(self):
        # Zamknięcie ciasteczek
        time.sleep(8)
        window = self.driver.find_element(*ShortPasswordLocators.WINDOW_BUTTON)
        window.click()
        # Kliknięcie na ikonę logowania
        login_button = self.driver.find_element(*ShortPasswordLocators.LOGIN_BUTTON)
        login_button.click()
        time.sleep(2)
        # Logowanie na konto
        e_mail_input = self.driver.find_element(*ShortPasswordLocators.EMAIL_BUTTON)
        e_mail_input.send_keys(*test_data.data.e_mail)
        time.sleep(2)
        short_password_input = self.driver.find_element(*ShortPasswordLocators.PASSWORD_BUTTON)
        short_password_input.send_keys(*test_data.data.short_password)
        time.sleep(2)
        login_button2 = self.driver.find_element(*ShortPasswordLocators.LOGIN_BUTTON2)
        login_button2.click()
        time.sleep(5)

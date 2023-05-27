from locators import RegistrationLocators
from pages.base_page import BasePage
import test_data
import time
import test_data.data as td


class ZalandoRegisterPassword(BasePage):

    def testinvalidregistration(self):
        # Zamknięcie ciasteczek
        time.sleep(8)
        window = self.driver.find_element(*RegistrationLocators.WINDOW_BUTTON)
        window.click()
        # Kliknięcie na ikonę logowania
        login_button = self.driver.find_element(*RegistrationLocators.LOGIN_BUTTON)
        login_button.click()
        time.sleep(2)
        # Kliknięcie na "Zarejestruj się"
        registration_button = self.driver.find_element(*RegistrationLocators.REGISTRATION_BUTTON)
        registration_button.click()
        time.sleep(2)

        # Wpisanie danych
        name_input = self.driver.find_element(*RegistrationLocators.NAME_BUTTON)
        name_input.send_keys(test_data.data.name)
        time.sleep(2)
        last_name_input = self.driver.find_element(*RegistrationLocators.LAST_NAME_BUTTON)
        last_name_input.send_keys(test_data.data.last_name)
        time.sleep(2)
        e_mail_input = self.driver.find_element(*RegistrationLocators.REGISTER_EMAIL_BUTTON)
        e_mail_input.send_keys(test_data.data.e_mail)
        time.sleep(2)
        register_password_input = self.driver.find_element(*RegistrationLocators.REGISTER_PASSWORD_BUTTON)
        register_password_input.send_keys(test_data.data.register_password)

        # Zaznaczamy modę
        fashion = self.driver.find_element(*RegistrationLocators.FASHION_BUTTON)
        fashion.click()
        time.sleep(2)

        # Klikamy zarejestruj się
        registration_button2 = self.driver.find_element(*RegistrationLocators.REGISTRATION_BUTTON2)
        registration_button2.click()
        time.sleep(5)

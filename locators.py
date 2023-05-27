from selenium.webdriver.common.by import By


WINDOW_XPATH = "//button[@id='uc-btn-accept-banner']"
LOGIN_BUTT_XPATH = "//a[@title='Zaloguj się']//*[name()='svg']"
EMAIL_ID = 'login.email'
PASSWORD_ID = 'login.secret'
LOGIN_BUTT2_XPATH = '//*[@id="sso"]/div/div[2]/main/div/div[2]/div/div/div/form/button'
REGISTRATION_BUTT_XPATH = "//*[@id='sso']/div/section/div/div[2]/div/button"
NAME_XPATH = "//input[@id='register.firstname']"
LAST_NAME_XPATH = "//input[@id='register.lastname']"
REGISTER_EMAIL_XPATH = "//input[@id='register.email']"
REGISTER_PASSWORD_XPATH = "//input[@id='register.password']"
FASHION_BUTT_XPATH = "//*[@id='register.fashion_preference']/div[2]/div/div[1]/div/label"
REGISTRATION_BUTT2_XPATH = "//*[@id='section-register']/div/form/div[7]/button"


class SignUpLocators:
    WINDOW_BUTTON = (By.XPATH, WINDOW_XPATH)
    LOGIN_BUTTON = (By.XPATH, LOGIN_BUTT_XPATH)
    EMAIL_BUTTON = (By.ID, EMAIL_ID)
    PASSWORD_BUTTON = (By.ID, PASSWORD_ID)
    LOGIN_BUTTON2 = (By.XPATH, LOGIN_BUTT2_XPATH)


class ShortPasswordLocators:
    WINDOW_BUTTON = (By.XPATH, WINDOW_XPATH)
    LOGIN_BUTTON = (By.XPATH, LOGIN_BUTT_XPATH)
    EMAIL_BUTTON = (By.ID, EMAIL_ID)
    PASSWORD_BUTTON = (By.ID, PASSWORD_ID)
    LOGIN_BUTTON2 = (By.XPATH, LOGIN_BUTT2_XPATH)


class RegistrationLocators:
    WINDOW_BUTTON = (By.XPATH, WINDOW_XPATH)
    LOGIN_BUTTON = (By.XPATH, LOGIN_BUTT_XPATH)
    REGISTRATION_BUTTON = (By.XPATH, REGISTRATION_BUTT_XPATH)
    NAME_BUTTON = (By.XPATH, NAME_XPATH)
    LAST_NAME_BUTTON = (By.XPATH, LAST_NAME_XPATH)
    REGISTER_EMAIL_BUTTON = (By.XPATH, REGISTER_EMAIL_XPATH)
    REGISTER_PASSWORD_BUTTON = (By.XPATH, REGISTER_PASSWORD_XPATH)
    FASHION_BUTTON = (By.XPATH, FASHION_BUTT_XPATH)
    REGISTRATION_BUTTON2 = (By.XPATH, REGISTRATION_BUTT2_XPATH)

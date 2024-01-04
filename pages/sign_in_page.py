from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class SignInPage(Page):

    EMAIL_FIELD = (By.CSS_SELECTOR, "[type='email']")
    PWD_FIELD = (By.CSS_SELECTOR, "[type='password']")

    LOGIN_BTN = (By.CSS_SELECTOR, "[class*='login-button']")

    def sign_in(self):
        sleep(5)
        self.click(*self.EMAIL_FIELD)
        self.input('usahleb@gmail.com', *self.EMAIL_FIELD)
        self.click(*self.PWD_FIELD)
        self.input('Intern1587!@', *self.PWD_FIELD)
        self.click(*self.LOGIN_BTN)

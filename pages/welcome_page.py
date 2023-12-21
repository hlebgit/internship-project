from pages.base_page import Page
from selenium.webdriver.common.by import By

class WelcomePage(Page):

    OPEN_IN_BROWSER_BTN = (By.CSS_SELECTOR, "[class='button-block-home'] [href*='soft.reelly.io']")

    def open_welcome_page(self):
        self.open_url('https://www.reelly.io/')

    def click_open_main_page(self):
        self.click(*self.OPEN_IN_BROWSER_BTN)


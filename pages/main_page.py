from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class MainPage(Page):

    OFF_PLAN = (By.CSS_SELECTOR, "[class*='menu'] address")

    def open_off_plan_page(self):
        self.click(*self.OFF_PLAN)



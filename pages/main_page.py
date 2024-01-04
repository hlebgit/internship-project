from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class MainPage(Page):


    OFF_PLAN = (By.CSS_SELECTOR, "[class*='menu'] address")
    OFF_PLAN_MOBILE = (By.XPATH, "//*[@wized='mobileMenuForVerifiedUsers'] //*[text()='Off-plan']")

    def open_off_plan_page(self):
        sleep(5)
        #WEB
        # self.click(*self.OFF_PLAN)
        #Mobile
        self.click(*self.OFF_PLAN_MOBILE)



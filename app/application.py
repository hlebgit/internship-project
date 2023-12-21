from pages.base_page import Page
from pages.welcome_page import WelcomePage
from pages.main_page import MainPage
from pages.sign_in_page import SignInPage
from pages.off_plan_page import OffPlanPage

class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.welcome_page = WelcomePage(driver)
        self.main_page = MainPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.off_plan_page = OffPlanPage(driver)




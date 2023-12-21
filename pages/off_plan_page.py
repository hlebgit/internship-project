from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class OffPlanPage(Page):

    OPEN_IN_BROWSER_BTN = (By.CSS_SELECTOR, "[class='button-block-home'] [href*='soft.reelly.io']")
    FILTER_BTN = (By.CSS_SELECTOR, "form [class*='filter-button']")
    FUTURE_LAUNCH_FILTER = (By.XPATH, "//*[@class='filters-tags'] //*[text()='Future Launch']")
    TOTAL_LISTINGS = (By.CSS_SELECTOR, "[wized='cardOfProperty']")
    LISTINGS_WITH_FUTURE_LAUNCH_TAG = (By.XPATH, "//a[@wized='cardOfProperty'] //*[text()='Future Launch']")

    def verify_off_plan_opened(self):
        assert "off-plan" in self.driver.current_url,\
            f"Expected page should contain 'off-plan', but opened {self.driver.current_url}"

    def filter_by_future_launch(self):
        sleep(5)
        self.click(*self.FILTER_BTN)
        sleep(5)
        self.click(*self.FUTURE_LAUNCH_FILTER)
        sleep(5)

    def verify_each_future_launch_tag(self):
        total_listings_loaded = self.find_elements(*self.TOTAL_LISTINGS)
        listings_with_future_launch_tag = self.find_elements(*self.LISTINGS_WITH_FUTURE_LAUNCH_TAG)

        assert len(total_listings_loaded) == len(listings_with_future_launch_tag), \
            f"Some listings do not show 'Future Launch' tag." \
            f"Actual count of listings {len(total_listings_loaded)}," \
            f"while count of listings with tag {len(listings_with_future_launch_tag)}"


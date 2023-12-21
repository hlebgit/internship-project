from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_url(self, url):
        self.driver.get(url)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
         return self.driver.find_elements(*locator)

    def input(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text,\
            f"Expected text '{expected_text}' did not match actual '{actual_text}'"

    def get_current_window(self):
        return self.driver.current_window_handle

    def get_all_windows(self):
        return self.driver.window_handles

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)

    def close_page(self):
        self.driver.close()

    def switch_to_window(self, window_id):
        self.driver.switch_to.window(window_id)

    def wait_for_element_visible(self, *locator):
        element = self.wait.until(
            EC.visibility_of_element_located(*locator),
            message=f'Element by {locator} not visible'
        )
        return element


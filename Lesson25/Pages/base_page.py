from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
# from pytest_bdd import scenarios, given, when, then, parsers


class BasePage:
    def __init__(self, driver, url):
        self.chrome = driver
        self.url = url
        self.chrome.implicitly_wait(5)
        self.chrome.maximize_window()

    def open(self):
        self.chrome.fullscreen_window()
        self.chrome.get(self.url)

    def is_element_present(self, locator):
        try:
            if self.chrome.find_element(*locator):
                return True
        except NoSuchElementException:
            return False

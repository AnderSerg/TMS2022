from Lesson25.Pages.base_page import BasePage
from Lesson25.Locators.main_page_loc import MainPageLoc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class MainPage(BasePage):

    locator = ''

    def open_login_page(self):
        time.sleep(1)
        WebDriverWait(self.chrome, 60).until(EC.presence_of_element_located(MainPageLoc.login_loc))
        login_link = WebDriverWait(self.chrome, 20).until(EC.element_to_be_clickable(MainPageLoc.login_loc))
        login_link.click()

    # def verify_login_url(self):

    def verify_login_link(self):
        assert self.is_element_present(MainPageLoc.login_loc), "Login link is not present!"

    def verify_basket_is_empty(self):
        assert self.is_element_present(MainPageLoc.basket_empty_loc), "Basket is not empty"

    def go_to_dresses_page(self):
        time.sleep(1)
        # dresses = WebDriverWait(self.chrome, 20).until(EC.element_to_be_clickable(MainPageLoc.dresses_loc))
        dresses = self.chrome.find_elements(*MainPageLoc.dresses_loc)[1]
        dresses.click()

    def go_to_contact_page(self):
        time.sleep(1)
        # dresses = WebDriverWait(self.chrome, 20).until(EC.element_to_be_clickable(MainPageLoc.dresses_loc))
        contact = self.chrome.find_element(*MainPageLoc.contact_us_loc)
        contact.click()




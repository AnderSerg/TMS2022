from Lesson25.Pages.base_page import BasePage
from Lesson25.Locators.contact_us_loc import ContactUsLoc
from selenium.webdriver.support import expected_conditions as EC


class ContactUsPage(BasePage):

    def contact_us_is_present(self):
        assert self.is_element_present(ContactUsLoc.contact_us_loc)

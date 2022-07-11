from Lesson25.Pages.base_page import BasePage
from Lesson25.Locators.dresses_loc import DressesLoc


class DressesPage(BasePage):

    def verify_women_is_present(self):
        assert self.is_element_present(DressesLoc.women_loc), 'Element Women is not present!'

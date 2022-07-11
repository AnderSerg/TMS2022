from Lesson25.Pages.base_page import BasePage
from Lesson25.Locators.login_page_loc import LoginPageLoc


class LoginPage(BasePage):

    def input_email(self, loc):
        pass

    def input_password(self):
        pass

    def login(self):
        self.input_email(LoginPageLoc.input_email_loc)
        self.input_password()







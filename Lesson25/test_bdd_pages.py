import pytest
from Lesson25.Pages.login_page import LoginPage
from Lesson25.Pages.main_page import MainPage
from Lesson25.Pages.dresses_page import DressesPage
from Lesson25.Pages.contact_us_page import ContactUsPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pytest_bdd import scenarios, given, when, then, parsers


scenarios('Lesson25/test_bdd_page.feature')


@pytest.fixture
def open_browser():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


@given('We open main page')
def open_site(open_browser):
    link = "http://automationpractice.com/index.php"
    global main_page
    main_page = MainPage(open_browser, link)
    main_page.open()


@when('we check login link')
def verify_login_link(open_browser):
    main_page.verify_login_link()


@then('We open login page')
def open_login_page():
    main_page.open_login_page()

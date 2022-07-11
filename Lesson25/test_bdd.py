import pytest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Constants

DUCKDUCKGO_HOME = 'https://duckduckgo.com/'


# Fixtures

@pytest.fixture
def browser():
    b = webdriver.Chrome('/Users/marinasmirnova/PycharmProjects/pytestProject/chromedriver')
    b.implicitly_wait(10)
    yield b
    b.quit()


def ddg_home(browser):
    browser.get(DUCKDUCKGO_HOME)


def search_phrase(browser, phrase):
    search_input = browser.find_element_by_id('search_form_input_homepage')
    search_input.send_keys(phrase + Keys.RETURN)


def search_results(browser, phrase):
    # Check search result list
    # (A more comprehensive test would check results for matching phrases)
    # (Check the list before the search phrase for correct implicit waiting)
    links_div = browser.find_element_by_id('links')
    assert len(links_div.find_elements_by_xpath('//div')) > 0
    # Check search phrase
    search_input = browser.find_element_by_id('search_form_input')
    assert search_input.get_attribute('value') == phrase
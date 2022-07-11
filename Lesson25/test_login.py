import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def open_login_page():
    login_link = browser.find_element(By.CSS_SELECTOR, ".login")
    login_link.click()



def test_login():
    global browser
    browser = webdriver.Chrome('./chromedriver')
    browser.implicitly_wait(5)
    link = "http://automationpractice.com/index.php"


    try:
        browser.get(link)
        open_login_page()
    finally:
        browser.quit()


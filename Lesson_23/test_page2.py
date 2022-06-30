from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import math
from selenium.webdriver.support.ui import WebDriverWait


def test_wiki_search_field():
    chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        url = 'http://suninjuly.github.io/alert_accept.html'
        chrome.get(url)
        chrome.maximize_window()
        # chrome.fullscreen_window()
        button = chrome.find_element(By.CLASS_NAME, "btn.btn-primary")
        button.click()
        time.sleep(5)

        confirm = chrome.switch_to.alert
        confirm.accept()
        time.sleep(5)

    finally:
        chrome.quit()

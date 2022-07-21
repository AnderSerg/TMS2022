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
        url = 'http://the-internet.herokuapp.com/windows'
        chrome.get(url)
        chrome.maximize_window()
        # chrome.fullscreen_window()
        button = chrome.find_element(By.XPATH, '//*[@target="_blank"]')
        tab1 = chrome.current_window_handle
        button.click()
        time.sleep(5)

        tab2 = chrome.window_handles[1]
        chrome.switch_to.window(tab2)
        new_window_text = chrome.find_element(By.XPATH, '//h3[text()="New Window"]').text
        assert new_window_text == "New Window"

        time.sleep(5)

    finally:
        chrome.quit()

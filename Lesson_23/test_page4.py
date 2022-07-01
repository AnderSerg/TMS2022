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
        url = 'http://demo.guru99.com/test/guru99home/'
        chrome.get(url)
        chrome.maximize_window()
        # chrome.fullscreen_window()

        chrome.switch_to.frame(chrome.find_element(By.ID, "a077aa5e"))
        time.sleep(5)
        src_jmeter = chrome.find_element(By.TAG_NAME, "img")
        src_jmeter.click()
        time.sleep(5)

        tab2 = chrome.window_handles[1]
        chrome.switch_to.window(tab2)
        time.sleep(10)
        check = chrome.find_element(By.XPATH, "//h1[@class='entry-title']").text
        assert check == "Selenium Live Project: FREE Real Time Project for Practice"

    finally:
        chrome.quit()

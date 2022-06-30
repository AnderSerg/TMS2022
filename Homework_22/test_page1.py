from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_wiki_search_field():
    chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        url = 'https://ultimateqa.com/complicated-page/'
        chrome.get(url)
        chrome.maximize_window()
        # chrome.fullscreen_window()
        button_click1 = chrome.find_element(By.XPATH, "//a[@class='et_pb_button et_pb_button_4 et_pb_bg_layout_light']")
        button_click1.click()
        time.sleep(5)

        button_click2 = chrome.find_element(By.CSS_SELECTOR, "[class='et_pb_button et_pb_button_4 et_pb_bg_layout_light']")
        button_click2.click()
        time.sleep(5)

        button_click3 = chrome.find_element(By.CLASS_NAME, "et_pb_button.et_pb_button_4.et_pb_bg_layout_light")
        button_click3.click()
        time.sleep(5)

    finally:
        chrome.quit()

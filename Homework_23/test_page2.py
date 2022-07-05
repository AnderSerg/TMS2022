from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_wiki_search_field():
    chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        url = 'http://the-internet.herokuapp.com/frames'
        chrome.get(url)
        chrome.maximize_window()
        # chrome.fullscreen_window()

        chrome.find_element(By.XPATH, "//*[@id='content']/div/ul/li[2]/a").click()

        chrome.switch_to.frame(chrome.find_element(By.XPATH, "//*[@id='mce_0_ifr']"))

        check_text = WebDriverWait(chrome,10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='tinymce']/p"))).text
        assert check_text == "Your content goes here."
        time.sleep(5)

    finally:
        chrome.quit()

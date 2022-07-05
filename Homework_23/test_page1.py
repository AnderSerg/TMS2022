import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


def test_wiki_search_field():
    chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    chrome.implicitly_wait(5)
    try:
        url = 'http://the-internet.herokuapp.com/dynamic_controls'
        chrome.get(url)
        chrome.maximize_window()
        # chrome.fullscreen_window()

        button_remove = chrome.find_element(By.XPATH, "//*[@id='checkbox-example']/button")
        button_remove.click()
        mesage1 = WebDriverWait(chrome, 10).until(EC.visibility_of_element_located((By.ID, "message")))

        try:
            checkbox_check = chrome.find_element(By.XPATH, "//*[@id='checkbox']/input")
        except:
            print("no checkbox")

        disable_inp = chrome.find_element(By.XPATH, "//*[@id='input-example']/input")
        if disable_inp.get_attribute("disabled") == "true":
            print("input disabled")
        else:
            print("input enabled")

        button_enable = chrome.find_element(By.XPATH, "//*[@id='input-example']/button").click()

        mesage2 = WebDriverWait(chrome, 10).until(EC.visibility_of_element_located((By.ID, "message")))

        disable_inp = chrome.find_element(By.XPATH, "//*[@id='input-example']/input")
        if disable_inp.get_attribute("disabled") == "true":
            print("input disabled")
        else:
            print("input enabled")

    finally:
        chrome.quit()

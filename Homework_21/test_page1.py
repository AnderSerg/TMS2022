from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_wiki_search_field():
    chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        url = 'https://demoqa.com/select-menu'
        chrome.get(url)
        chrome.fullscreen_window()
        drop_open1 = chrome.find_element(By.XPATH, "//*[contains(text(), 'Select Option')]")
        drop_open1.click()
        time.sleep(2)

        drop_check1 = chrome.find_element(By.XPATH, "//*[contains(text(), 'Group 1, option 2')]")
        drop_check1.click()
        time.sleep(2)

        drop_open2 = chrome.find_element(By.XPATH, "//*[contains(text(), 'Select Title')]")
        drop_open2.click()
        time.sleep(2)

        drop_check2 = chrome.find_element(By.XPATH, "//*[contains(text(), 'Dr.')]")
        drop_check2.click()
        time.sleep(2)

        drop_open3 = chrome.find_element(By.ID, "oldSelectMenu")
        drop_open3.click()
        time.sleep(2)

        drop_check3 = chrome.find_element(By.XPATH, "//*[contains(text(), 'Blue')]")
        drop_check3.click()
        time.sleep(5)

        drop_open4 = chrome.find_element(By.XPATH, "//*[contains(text(), 'Select...')]")
        time.sleep(5)
        drop_open4.click()
        time.sleep(2)

        drop_check4 = chrome.find_element(By.XPATH, "//*[contains(text(), 'Blue')]")
        time.sleep(2)
        drop_check4.click()
        time.sleep(2)

    finally:
        chrome.quit()

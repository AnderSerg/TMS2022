from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_wiki_search_field():
    chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        url = 'http://demo.guru99.com/test/newtours/register.php'
        chrome.get(url)
        chrome.fullscreen_window()
        drop_open1 = chrome.find_element(By.NAME, "firstName")
        drop_open1.send_keys('asd')
        time.sleep(2)

        drop_open2 = chrome.find_element(By.NAME, "lastName")
        drop_open2.send_keys('qwe')
        time.sleep(2)

        drop_open3 = chrome.find_element(By.NAME, "phone")
        drop_open3.send_keys('123')
        time.sleep(2)

        drop_open3 = chrome.find_element(By.NAME, "userName")
        drop_open3.send_keys('asd@mail.ru')
        time.sleep(2)

        drop_open3 = chrome.find_element(By.NAME, "address1")
        drop_open3.send_keys('asd')
        time.sleep(2)

        drop_open3 = chrome.find_element(By.NAME, "city")
        drop_open3.send_keys('asd')
        time.sleep(2)

        drop_open3 = chrome.find_element(By.NAME, "state")
        drop_open3.send_keys('asd')
        time.sleep(2)

        drop_open3 = chrome.find_element(By.NAME, "postalCode")
        drop_open3.send_keys('123456')
        time.sleep(2)

        drop_open1 = chrome.find_element(By.XPATH, "//*[contains(text(), 'ANGOLA')]")
        drop_open1.click()
        time.sleep(2)

        drop_open99 = chrome.find_element(By.ID, "email")
        user_name = 'zxc'
        drop_open3.send_keys(user_name)
        time.sleep(2)

        drop_open100 = chrome.find_element(By.NAME, "password")
        password = 'asd'
        drop_open100.send_keys(password)
        time.sleep(2)

        drop_open101 = chrome.find_element(By.NAME, "confirmPassword")
        drop_open101.send_keys('asd')
        time.sleep(2)

        drop_open_10 = chrome.find_element(By.NAME, "submit")
        drop_open_10.click()
        time.sleep(5)

        url1 = 'https://demo.guru99.com/test/newtours/login.php'
        chrome.get(url1)

        time.sleep(2)

        drop_open1000 = chrome.find_element(By.NAME, "userName")
        drop_open1000.send_keys(user_name)
        time.sleep(2)

        drop_open1001 = chrome.find_element(By.NAME, "password")
        drop_open1001.send_keys(password)
        time.sleep(2)

        drop_open999 = chrome.find_element(By.NAME, "submit")
        drop_open999.click()

    finally:
        chrome.quit()

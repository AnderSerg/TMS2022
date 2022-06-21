from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_wiki_search_field():
    chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        # url = 'https://ru.wikipedia.org/wiki/'
        # word = 'Автоматизация'
        # # chrome = webdriver.Chrome(ChromeDriverManager().install())
        #
        # chrome.maximize_window()
        # chrome.get(url)
        # time.sleep(3)
        #
        # search_input = chrome.find_element(By.ID, "searchInput")
        # search_input.send_keys(word)
        # search_input.submit()
        # time.sleep(5)
        #
        # title = chrome.find_element(By.ID, "firstHeading").text
        # assert word == title, f"{title} is not eq {word}"
        url = 'https://demoqa.com/text-box'
        chrome.get(url)
        search_input1 = chrome.find_element(By.ID, "userName")
        search_input1.send_keys("word")
        search_input2 = chrome.find_element(By.ID, "userEmail")
        search_input2.send_keys("asdasd@tut.by")
        search_input3 = chrome.find_element(By.ID, "currentAddress")
        search_input3.send_keys("asdasdasd")
        search_input4 = chrome.find_element(By.ID, "permanentAddress")
        search_input4.send_keys("Asdasd")
        time.sleep(10)
        search_button = chrome.find_element(By.ID, "submit")
        search_button.click()

        check_input1 = chrome.find_element(By.CSS_SELECTOR, '[id=name][class=mb-1]')
        assert check_input1 == search_input1
        check_input2 = chrome.find_element(By.CSS_SELECTOR, '[id=email][class=mb-1]')
        assert check_input2 == search_input2
        check_input3 = chrome.find_element(By.CSS_SELECTOR, '[id=currentAddress][class=mb-1]')
        assert check_input3 == search_input3
        check_input4 = chrome.find_element(By.CSS_SELECTOR, '[id=permanentAddress][class=mb-1]')
        assert check_input4 == search_input4

        time.sleep(10)

        time.sleep(50)

    finally:
        chrome.quit()

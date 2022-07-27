import allure
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import math
from selenium.webdriver.support.ui import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


@allure.story("Test open wiki page")
def test_wiki_search_field():
    chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        url = 'http://suninjuly.github.io/math.html'
        chrome.get(url)
        chrome.maximize_window()
        # chrome.fullscreen_window()
        var_x = chrome.find_element(By.ID, "input_value").text
        answer_x = calc(var_x)
        input_x = chrome.find_element(By.ID, "answer")
        with allure.step("Send Keys"):
            input_x.send_keys(answer_x)

        checkbox = chrome.find_element(By.ID, "robotCheckbox")
        with allure.step("click"):
            checkbox.click()
        radio = chrome.find_element(By.ID, "robotsRule")
        with allure.step("click"):
            radio.click()
        button = chrome.find_element(By.CLASS_NAME, "btn.btn-default")
        with allure.step("click"):
            button.click()
        time.sleep(5)

    finally:
        chrome.quit()

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest_check as check
# pip install pytest-check


def test_wiki_search_field():
    chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        url = 'https://ultimateqa.com/filling-out-forms/'
        chrome.get(url)
        chrome.maximize_window()
        # chrome.fullscreen_window()
        form_name = chrome.find_element(By.ID, "et_pb_contact_name_0")
        form_name.send_keys("AAA")
        time.sleep(5)

        form_mess = chrome.find_element(By.ID, "et_pb_contact_message_0")
        form_mess.send_keys("BBB")
        time.sleep(5)

        button_sub = chrome.find_element(By.CLASS_NAME, "et_pb_contact_submit.et_pb_button")
        button_sub.click()
        time.sleep(5)

        message1 = chrome.find_element(By.CLASS_NAME, "et-pb-contact-message")
        assert message1.text == "Thanks for contacting us"
        # assert message1.text == "Form filled out successfully"
        # check.equal(message1, 'Thanks for contacting us')
        # check.equal(message1, "Form filled out successfully")

        chrome.get(url)
        time.sleep(5)

        form_name = chrome.find_element(By.ID, "et_pb_contact_name_0")
        form_name.send_keys("AAA")
        button_sub = chrome.find_element(By.CLASS_NAME, "et_pb_contact_submit.et_pb_button")
        button_sub.click()
        time.sleep(5)
        message2 = chrome.find_element(By.CLASS_NAME, "et-pb-contact-message")
        check.equal(message2, 'Please, fill in the following fields:')
        # assert message2 == "Please, fill in the following fields:"

        chrome.get(url)
        time.sleep(5)

        form_mess = chrome.find_element(By.ID, "et_pb_contact_message_0")
        form_mess.send_keys("BBB")
        time.sleep(5)
        button_sub = chrome.find_element(By.CLASS_NAME, "et_pb_contact_submit.et_pb_button")
        button_sub.click()
        time.sleep(5)
        message3 = chrome.find_element(By.CLASS_NAME, "et-pb-contact-message")
        check.equal(message3, 'Please, fill in the following fields:')
        # assert message3 == "Please, fill in the following fields:"

    finally:
        chrome.quit()

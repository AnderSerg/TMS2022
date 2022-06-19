from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def test_wiki_search_field():
    url = 'https://ru.wikipedia.org/wiki/'
    word = 'Автоматизация'
    chrome = webdriver.Chrome(ChromeDriverManager().install())
    chrome.get(url)
    time.sleep(3)

    search_input = chrome.find_element(By.ID, "searchInput")
    search_input.send_keys(word)
    search_input.submit()
    time.sleep(5)

    title = chrome.find_element(By.ID, "firstHeading").text
    assert word == title, f"{title} is not eq {word}"

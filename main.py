from selenium import webdriver
import time
from selenium import webdriver
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
import time


path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)

def getText(driver, url):
    driver.get(url)
    text = driver.find_element_by_class_name('td-post-content')
    text = text.text
    return text


def removeSymbol(text):
    flag = True
    while flag:
        if "\u20b9" in text:
            text = text.replace("\u20b9", "Rs.")
        elif "\u2248" in text:
            text = text.replace("\u2248", "approximately ")
        else:
            flag = False
    return text

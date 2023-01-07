from main import getText, removeSymbol
from selenium import webdriver
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
import time


path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)

data = pd.read_excel("Input.xlsx", sheet_name="Sheet1")
urlID = data["URL_ID"]
urls = data["URL"]

for i in range(0, 170):
    text = getText(driver, urls[i])
    filename = urlID[i]
    filename = "Final\\" + str(int(filename)) + ".txt"
    file = open(filename, 'w')
    if "\u20b9" in text:
        text = removeSymbol(text)
    elif "\u2248" in text:
        text = removeSymbol(text)
    file.write(text)
    file.close()
    print("Extraction of", urlID[i], "Finished")
driver.quit()


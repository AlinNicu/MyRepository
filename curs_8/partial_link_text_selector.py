''''
Aici nu trebuie sa se mai potriveasca 100% textul respectiv precum am precizat la 'id' poate sa se potriveasca 99% cu textul respectiv



'''

#Vom lua prima parte

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# initializam chrome-ul
chrome = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com")



chrome.find_element(By.PARTIAL_LINK_TEXT,"Enabled").click()
time.sleep(3)
chrome.find_element(By.ID, 'logo').click()
time.sleep(3)
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Auto').click()

time.sleep(3)

chrome.quit()






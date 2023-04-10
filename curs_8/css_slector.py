import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# initializam chrome-ul
chrome = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com/form")

chrome.find_element(By.CSS_SELECTOR, 'input#first-name').send_keys('TESTjjkllll')
time.sleep(2)

# chrome.find_element(By.CSS_SELECTOR, 'select#select-menu').click()
time.sleep(2)
chrome.find_element(By.CSS_SELECTOR, 'select.form-control').click()
chrome.find_element(By.CSS_SELECTOR,'input[placeholder="Enter last name"]').send_keys('PRENUME')

# <input type="text" class="form-control" id="job-title" placeholder="Enter your job title">
chrome.find_element(By.CSS_SELECTOR,'input[placeholder*="job title"]').send_keys('JOB')#intre *si = *= nu trebuie sa fie spatiu altfel nu merge

time.sleep(4)
chrome.quit()
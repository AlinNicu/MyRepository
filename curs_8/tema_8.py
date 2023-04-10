'''
Alege-ți unuul sau mai multe din sugestiile de site-uri de mai jos

https://formy-project.herokuapp.com/

Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
● Id'''

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# chrome = webdriver.Chrome()
# chrome.get('https://formy-project.herokuapp.com/form')
#
# prenume = chrome.find_element(By.ID, "first-name")
#
# prenume.send_keys('Nicusor Alin')
#
# chrome.find_element(By.ID,'last-name').send_keys('Vaduva')
# chrome.find_element(By.ID, 'job-title').send_keys('Software Tester')
#
# time.sleep(3)
# chrome.quit()

#Link Text

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
chrome.get('https://formy-project.herokuapp.com')


chrome.find_element(By.ID, 'logo').click()

time.sleep(3)
chrome.find_element(By.LINK_TEXT,'Checkbox').click()
time.sleep(3)

try:
    chrome.find_element(By.LINK_TEXT, 'Drag and Drop').click()
except:
    print('Nu exista text')



# ------------------------------------By Partial Link Text---------------------------------
chrome = webdriver.Chrome()
chrome.get('https://formy-project.herokuapp.com/')
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Key and Mouse Press').click()
time.sleep(3)
chrome.find_element(By.ID, 'logo').click()
time.sleep(3)
chrome.find_element(By.PARTIAL_LINK_TEXT,'Modal').click()
time.sleep(3)
chrome.find_element(By.ID, 'logo').click()
time.sleep(3)
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Form').click()
time.sleep(3)

# ------------------------------------By Class Name -------------------------------------

chrome.get('https://formy-project.herokuapp.com/autocomplete')
element = chrome.find_elements(By.CLASS_NAME,"form-control")
element[2].send_keys("Flat 1, 34")
element[3].send_keys("Malton")
element[4].send_keys("North Yorkshire")
time.sleep(3)

# ------------------------------------By CSS -------------------------------------
#dupa ID

chrome.get('https://formy-project.herokuapp.com/autocomplete')
chrome.find_element(By.CSS_SELECTOR, 'input#autocomplete').send_keys('Alin')

#dupa clasa
chrome.get('https://www.phptravels.net/signup')
chrome.find_element(By.CSS_SELECTOR, 'input.form-control').send_keys('Vaduva')






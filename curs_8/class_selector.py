import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# initializam chrome-ul
chrome = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com/form")

chrome.find_element(By.CLASS_NAME, 'form-control').send_keys('FIRSTNAME_BY_CLASS')
chrome.find_elements(By.CLASS_NAME, 'form-control')[2].send_keys('JOB_BY_CLASS')

#Pot sa selectez o obtiune dintr-un drop down

chrome.find_elements(By.CLASS_NAME,'form-control')[3].click()

# Ca sa putem selecta aceste valori in din drop down avem nevoie de o calsa speciala din selenium care se numeste SELECT:
# from selenium.webdriver.support.ui import Select

#prin clasa Select selectam o obtiune dintr-un drop-down din textul vizibil de pe site al obtiunii ex 0-1 , 2-3
# sau din patele cosului html value=1, value=2 etc
Select(chrome.find_elements(By.CLASS_NAME,'form-control')[3]).select_by_visible_text('5-9')# class == form control
time.sleep(2)
Select(chrome.find_elements(By.CLASS_NAME,'form-control')[3]).select_by_index(1) # ma asteopts a fie 0-1
time.sleep(2)
Select(chrome.find_elements(By.CLASS_NAME,'form-control')[3]).select_by_value('4') # value=4

#atributul este calss- valoarea difera de la site la site

time.sleep(4)
chrome.quit()
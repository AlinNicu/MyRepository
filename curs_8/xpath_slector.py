
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# initializam chrome-ul
chrome = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com/form")

'''
// -> va cauta in tot HTML-ul arbore
//input -> va da rezltate cu nr de input din HTML
//[@type='text']                         #daca deschid paranteze patrate pot sa introduc un atribut cu @ in fata
(//[@type='text'])  #Daca ii deschid paranteze ma pot folosi de le ca si o lista
(//[@type='text'])[4] # asa imi va selecta si va aduce in prim plan imputul cu nr 4 - numaratoarea incepe de la 1
//form/div/div/input[@type='text'] - toate elelmentele au ceais treuctura form -div-div-input
//*[@type='text'
//'[@id ='job-title']
(//input[@type = 'text'])
//form/input[@type='text']
//form/div/div/input[@type='text']


//label[contains(text(),'Sub']
//label(text()='First name'


'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome  = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com/form")

#selector by XPATH -> atribut=valoare
chrome.find_element(By.XPATH,"//input[@id='first-name']").send_keys("atribut=valoare")
sleep(2)
#selector by XPATH -> * (toate elementele care respecta regula data (ce este scris intre parantezele patrate))
chrome.find_element(By.XPATH,"//*[@id='first-name']").send_keys("*")
sleep(2)
#selector by XPATH -> navigare in jos - trecem prin fiecare element
chrome.find_element(By.XPATH,"//form/div/div/input[@id='last-name']").send_keys("navigare in jos")
sleep(2)
#selector by XPATH -> navigare in jos - skip tags- cautam sub form un input care respecta regula
chrome.find_element(By.XPATH,"//form//input[@id='last-name']").send_keys("navigare in jos-skip tags")
sleep(2)
#selector by XPATH ->selectam elemente din lista - index-ul incepe de la 1
chrome.find_element(By.XPATH,"(//input[@class='form-control'])[3]").send_keys("Al treilea elemente")
sleep(2)
#selector by XPATH -> OR primul element gasit dintre variabile
chrome.find_element(By.XPATH,"//input[@id='last'] | //input[@id='last-name'] | //input[@id='first-name']").send_keys("OR")
sleep(2)
#selector by XPATH -> in functie de textul partial (sau complet) + luam textul de pe el cu proprietatea text
text  = chrome.find_element(By.XPATH,"//a[contains(text(),'Sub')]").text
sleep(2)
#selector by XPATH -> in funcite de textul vizibil
chrome.find_element(By.XPATH,"//a[text()='Submit']").click()

sleep(2)

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# initializam chrome-ul
chrome = webdriver.Chrome()
chrome.get("https://www.seleniumframework.com/Practiceform")
chrome.find_element(By.NAME, 'country').send_keys('Romania')
chrome.find_element(By.NAME,'company').send_keys('IT Factory')
#Am gasit 2 elelmente cu name = email
#Daca exista mai multe elemente cu acelasi criteriu (name="email") si flolosim metoda find_element, va fii luat primul element gasit pe pagina tot timpul
# Dar exista modalitati in care putem lucra cu cazuri de acet gen

# chrome.find_element(By.NAME,'email').send_keys('asasa@mail.com') #La primul elelmet gasit cu name= email a introdus valaoare - la celalat nu a introdus

#Exista o metoda care se numeste find_elements ->
# cu find elelemets facem rost de toate elementele care respecta un anumit criteriu (ex: name = "email")
# Se aleaza la fel (BY.NAME, "email") - aici nu pot folosi send.keys... oei a;ltceva -
# find_elelmets imi rerurneaza o lista de web element - in cazul acesta am doar metode pe care le pot folosii asupra unei liste cursul 3 sau 4 - incers , invers , copy etc
# dar pot sa fac asa- ii zic elementul 0 primul elelemt gasit  zic send_keys
#EX: chrome.find_elements(By.NAME, "email")[0].send_keys('asasass@mail.com')

chrome.find_elements(By.NAME, "email")[0].send_keys('asasass1@mail.com') # A introdus tot in acel cum singur - primul
                                                           #Dar daca ii dau copy paste aici jos  si ii zic de[1] si asasass2@mail.com
chrome.find_elements(By.NAME, "email")[1].send_keys('asasass2@mail.com')
                                             #In felul acesta putem sa cream elemente cu acesiasi caracteristica name- email - la fel si daca aveam By ID
                                             # Atunci cand avem mai multe elemente trebuie sa ne comportam cu elel ca si cu niste LISTE folosind find element

                                            #Daca ne referim doar la primul element de pe pagina e deajuns find_element
                                            
time.sleep(5)
chrome.quit()



'''
Ex element HTML:
<input type="text" class="form-control" id="first-name" placeholder="Enter first name">

elemetul HTML este format din tag <input - dupa atribute si valori
ce tip de lelemt este? - este un element de tip input

id = atributul
'first-name' - valoarea atributului

(
class = atribut
'form-control' - valoarea atributului acestuia

)
'''

'''
Selectia elelmetelor in pagina cu linkText identifica  hyperlinkurile <a> din HTML folosid textul afisat in pagina

Textul trebuie sa se potrivesca 100% cu textul de la <a> folosit in codul HTML al paginii pe care o testam 
 se refera la 'Autocomplete'
 
Se poate lua din spate mai sigur - in cazul in care este un spatiu pierdut


EX:
<a class="btn btn-lg" href="/autocomplete">Autocomplete</a>


a = este tagul care defineste un element de tip ancora (adica link catre alta pagina)
href = link-ul efectiv catre care se navigheaza. (De obicei nu se pune link-ul complet(cum vedem in browser))
Link complet - https://formy-project.herokuapp.com/autocomplete
Link domeniu - https://formy-project.herokuapp.com/
extensia - /autocomplete

'''

import time

from selenium import webdriver
from selenium.webdriver.common.by import By


#Am o variabila in care voi salva un driver de chrome pe care sa mi-l deschida atunci cand vreu sa execut acest program


#initializam chrom-ul aici
#Acest lucru ne va deschide un nou browser de Chrome cu care vom interactiona
chrome = webdriver.Chrome()
chrome.get('https://formy-project.herokuapp.com/form') # cu metoda .get navigam cu link-ul pus intre ghilimele

time.sleep(5) # asteptam 5 secunde pentru a putea vizulaliza ce se intampla
              # (codul executandu-se prea repede pentru a putea observa cu ochiul liber)

chrome.find_element(By.LINK_TEXT,'Atutocomplete').click()

time.sleep(3)
chrome.find_element(By.ID, 'logo').click()

time.sleep(3)
try:
    chrome.find_element(By.LINK_TEXT,'Atutocomplete').click()
except:
    print('Elementul nu a fost gasit')

chrome.quit()

#Daca tagul  incepe cu <a- acela este un link - hiperlink este un link ascuns in text




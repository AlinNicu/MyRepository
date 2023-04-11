###### Dictionare #######

'''
* Dictionarele sunt structuri de date built-in Phyton
* Sunt folosite petru a stoca mai multe valori intr-o singura variabila
* Crearea unui dictionar se face cu {}
'''

### Crearea unui dictionar ####

# dictionar_gol = dict()
# print(type(dictionar_gol))
# dictionar_gol_2 = {}
# print(type(dictionar_gol_2))

# dummy_dict = dict(nume = 'Vald', varsta = 22, tara ='Romania')
# print(dummy_dict)

###Echivalent cu
# dummy_dict_2 = {
#     'nume': "Vald",
#     'varsta': 22,
#     'tara': ["Romania", "Ungaria"]
# }
# print(dummy_dict_2)

### Caracteristicile unui dictionar ###
'''
-> Ordonate (Incepnd cu Python 3.7) (Ca la liste)
-> Mutablie (Ca la liste)
-> Cheile nu accepta duplicate
-> Cheie: VALOARE
-> Neindexate -> Valorile se pot cauta in functie de numele cheilor la care se afla.
'''

### Nu accepta duplicate ####
# dictionar = {
#     'marca': 'skoda',
#     'an':1999,
#     'an':2010 #Valoarea de la cheia an va fi suprascrisa
# }
# print(dictionar)

#### Accesarea elementelor intr-un dictionar ###

capitale = {
    'Romania': 'Bucuresti',
    'Ungaria': 'Budapesta',
    'Italia' : 'Roma'
}
# capitala_Romania= capitale.get('Romania')
# print(capitala_Romania)

### SAU
# capitala_Ungariei = capitale["Ungaria"]
# print(capitala_Ungariei)
#
# # Accesarea tuturor cheilor dintr-un dictionar
#
# print(capitale.keys())
#
# ### Accesarea tururor valorilor dintr-un dictionar
#
# print(capitale.values())
#
# ### Accesarea tururor elementelor (cheie,valoare) dintr-un dictionar
# print(capitale.items())


### Schimbarea unei valori
# capitale = {
#     "Romania": "Bucuresti",
#     "Ungaria": "Budapesta",
#     "Italia":   "Roma"
# }
#
# capitale['Romania'] = 'Iasi'
# print(capitale)
#
# ### SAU
#
# capitale.update({'Romania':'Cluj-Napoca'})
# print(capitale)

### Adaugarea unui nou element :

# capitale = {
#     "Romania": "Bucuresti",
#     "Ungaria": "Budapesta",
#      "Italia": "Roma"
#  }
#
# capitale['Bulgaria'] = 'Sofia'
# print(capitale)
#
# ### SAU
# capitale.update({'Franta':'Paris'})
# print(capitale)
#
# ### Stergerea elementeleor dintr-un dictionar
# capitale.pop('Italia')
# print(capitale)
#
# #### Lungimea dictionarului
# print(len(capitale))
#
# #### Stergerea tuturor elemntelor (Ca la liste)
# capitale.clear()
# print(capitale)
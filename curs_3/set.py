##### Set-uri #######
'''
* Sterurile sunt structuri de date buit-in Python
*Sunt folosite pentru a stoca mai multe valori unice intr-o singura variabila
* Crearea unu set se face cu cu set() sau folosind element{}
'''

###### Crearea uni set #####

# set_gol = {}# Atentie se screaza un dictionar
# print(type(set_gol))

# set_gol = set()
# print(type(set_gol))
# set_fructe = {'mere','pere','struguri'}
# print(type(set_fructe))

#### Caracteristicile unui set ####
'''
->Neordonate
->Imutalbile- se pot adauga sau sterge valori, dar nu se pot schimba valori
->Nu accepta duplicate
->Neindexate
'''
#### Neordonate

# fructe = {'mere','pere','struguri'}
# print(fructe)

##### Fara Dupliocate
# fructe = {'mere','pere','struguri', 'struguri', 'pere'}
# print(fructe)

##### Adaugare elemente in set ####
#
# set1 = {1,2,3,4}
# print(set1)
# set1.add(5)
# print(set1)
# set1.add(5)
# print(set1)

#### Stergerea unui element dintr-un set ####

# set1 = {1,2,3,4,5,6,7,8,9,10}
# print(set1)
# set1.remove(4)
# print(set1)
# # set1.remove(20) # # Arunca eroarea daca nu exista elementul dorit
# # print(set1)
# set1.discard(20)  # # Daca elementul nu exista, discard nu arunca nici o eroare
# print(set1)

### Adaugarea unui set intr-un alt set ####

set1 ={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set2 ={10,20,30,40}
set1.update(set2) # # In set1 se adauga set2
print(set1)

set1.update(['ana', 'vlad', 'flavius']) # # update accepta si alta strctura de date, nu doar set-uri
print(set1)
print(set1.difference(set2))
print(set2.difference(set1))
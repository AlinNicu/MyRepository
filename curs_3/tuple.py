
'''

Sunt structuri de date built in Python
Sunt folosite pentru a stoca mai multe valori intr-o singura variabila
Createa unei tupe se face cu () sau folosind tupe()
'''
# #### Crearea unei Tuple ####
# tupla_goala = ()
# print(type(tupla_goala))
# tupla_goala = tuple()
# print(type(tupla_goala))

# prima_tupla = (1,2,3,4,5)
# prima_tupla = (True, 1,2,3,4,5,.43412, 'Strinng')
# print(prima_tupla)
# ## ATENTIE, Crearea unei Tuple ci o singura valoare trebuie adaugat o virgula dupa prima/singura valoare
# m_tupla = ('para',)
# print(m_tupla)


#### CARACTERISTICILE UNEI TUPLE #####
'''
-> Ordonate
-> Imutabile (nu se pot adauga/ sterge/ modifica valori din tupla deja creata
-> Accepta duplicate
-> Valorile sunt indexate (primul index este [0])

'''
##### Accesare elemente #### (Ca la liste)
# fructe = ('Mere', 'Pere', 'Striguri', 'Ananas', 'Banane')
# print('fructe [0]=', fructe [0])
# print('fructe[::-1]=',fructe [::-1])
#
# #### Adaugare elemente ####
#
# fructe = fructe + ('Banane',) ### In mod normal nu se pot adauga elemnte noi in tuple, dar Pyhton permite acest lucru
# print(fructe)

### Stergere elemente ###
## Nu putem sterge elemente din tupla
# Workaround-> Tranformam tupla in lista
# fructe = list(fructe)
# fructe.remove("Banane")
# fructe = tuple(fructe)
# print(type(fructe))
# print(fructe)

####Nu se pot modifica elementele dintr-o tupla 3#### (Workaround -> Transform tup in lista

#### Unpac Tuple

# fructe = ("Mere","Pere","Struguri","Ananas","Banane")
# mere,pere,struguri,ananas,banane = fructe
# print(ananas)
# print(mere,pere,struguri,ananas,banane)
#
# ### Lungimea unei tuple ##
# print(len(fructe))

'''
Structuri repetitive = blocuri de cod care se vor executa
in mod repetitiv pana cand  o anumita conditie nu mai este
respectata (este falsa)

*in cazul lui while (while conditie: - se va executa pana cand conditia va fii falsa
                    <corpul while-ului>
*in czul lui for (...)
Iteratie = de fiecare data cand reinta in while este iteratie(ciclu)
Interatie = procesul prin care un bloc de cod este executat
in cadrul structurii repetitive

'''

####______________________________________________
#### While/Ehile esle ####

'''
while = 'cat timp' - ne permite sa repetam executarea unui cod, cat timp condiitia este adevarata.

- Controlul de control (de exemplu 'i') al  structurii repetitive trebuie declarat inainte de structura reptitiva
 (while) si modificat in interiorul structurii repetitive (while).

!!!!!ATENTIE!!!! Daca nu modificam valoarea contorului in interiorul structurii repetitive
 vom crea un loop (ciclu)infinit
 
'''
# i = 0
# while i <= 3:
#     print(f'Valoarea lui i inainte de incrementare : {i}')
#     i += 1 #<=> i = i + 0
'''
i = 0 => i <=3 ? Da => Se executa codul din interiorul ciclului.
i = 1 => i <=3 ? Da => Se executa codul din interiorul ciclului.
i = 2 => i <=3 ? DA => se executa codul din interiorul ciclului
i = 3 => i <=3 ? DA => se executa codul din interiorul ciclului
i = 4 => i <=3 ? NU => se iese din ciclu

'''


# i = 0
# while i <= 50:
#     print(f'Valoarea lui i inainte de incrementare: {i}')
#     i += 1
#
# print('Done')
# print('Done2')

# Exemple de cicluri infinite

# i = 0
# while i <=3:
#     print(f'INFINITY: {i}')
    #Daca Nu incrementam valoarea lui (i) niciodata,
    # iar astfel conditia va ramane mereu True (0<=3)
# Facem un ciclu infinit in mod voit.
# Cele mai doua uszuale moduri are (while True: print(ciclu infinit)
#
# while True:
#     print('Ciclu infinit')
#     # Merge in mai multe moduri, de exemplu
# while 1:
#     print('Ciclu infinit')
# Daca adaug ca while orice timp de data, chiar si o lista goala , atata timp cat exista
# el reurneaza True si va fii infinit.
# while 'Samanta':
#     print("Ciclu infinit")

# Mai putin : while None , care va returna False iar ciclul se ca orpii

# while None:
#     print('Ciclu infinit')
# print('None returneaza False')

# i = 100
# while i >= 0:
#     print(f'valoarea lui i este {i}')
#     i -= 1

# i = 0
# while i <= 50:
#     print(f'Valoarea lui i inainte de incrementare: {i}')
#     i += 1
# else:
#     print(f'Valoarea lui i este {i}, astfel conditia i<=50 este falsa')
'''
Folosim WHILE ELSE (Referinta la exemplul de mai sus)

WHILE = tipul structurii repetive
i<=50: = conditia care se evalueaza
else = setul de instructiuni care se va executa dupa ce se iese
din structura repetitiva
'''
# i = 0
# while i <= 20:
#     print(f'i = {i}')
#     i += 1
# else:
#     print(f'i nu mai este mai mic sau egal cu 20, i = {i}')

# i = 0
# while i<=37:
#     print(f'i = {i}')
#     i += 1
# else:
#     print(f'i nu mai este mai mic sau egal cu 37, i ={i}')
#
# i = 37
# while i >= 0:
#     print(f'Anii lui Alin sunt: {i}')
#     i -= 1
# else:
#     print(f'`Ani de acum nu mai sunt aceiasi cu ani de anul viitor:{i}')

"""
Debugging = Depanare = procesul prin care gasim 
                    si rezolvam probleme in cod (bugs)
                    = punem pauza in cod ca sa vedem cum se parcurge
                    codul pas cu pas
"""

#Parcurgerea listelor cu while
#
# lista_fructe = ['mere', 'pere', 'banane', 'struguri']
#
# i = 0
# while i < len(lista_fructe):
#     print(f'fruct={lista_fructe[i]}')
#     i += 1
# print('Am iesit din while')



'''
Exercitiu:
Type a one-letter command and hit enter:
A to add a name to your list
R to remove a name from your list
S to show all the names in your list
Q to quit 
'''
# names =[]
# ALLOW_COMMANDS = ['A','R','S','Q']
# continue_loop = True
#
# while True:
#
#
#     command = input("Introduceti comanda [a,r,s,q] ").upper()
#     if command not in ALLOW_COMMANDS:
#         print("Comanda diferita")
#     else:
#
#         if command == 'A':
#             nume = input('Introduceti nume:' )
#             names.append(nume)
#         elif command == 'R':
#             nume = input('Sterge nume' )
#             names.remove(nume)
#         elif command == 'S':
#             print(names)
#
#         else:
#             # continue_loop - False
#             break

#########_____________________________________________>>>>><<<<<<<<<<<<<<<<<<<
#
# while continue_loop:# Se va iesi din while atunci cand: continue_loop = False
#     command = input("Introduceti comanda ['A','R','S','Q']: ").lower()
#     if command in ALLOW_COMMANDS:
#         if command == 'a':
#             name = input('Introduceti un nume pentru a-l adauga: ')
#             names.append(name) ### SAU names = names + name
#         elif command == 'r':
#             name = input('Introduceti un nume pentru a-l sterge: ')
#             names.remove(name)
#         elif command == 's':
#             print(f'Lista actuala este: {names} ')
#             continue# or break
#     else:
#         print(f"Introduceti o comanda valida, alegeti intre ['A','R','S','Q'] ")


#### Break #### opreste executia ciclului repetitiv
# ****Break Se poate folosii doare intr-un while sau intr-un  for
# break EX

# i= 0
# while i <=3:
#     print(i)
#     if i == -10:
#         break ## Asa am scapat de un ciclu infnit - prin acest break ciclul se va oprii la -10
#     i -= 1 # <=> i = i -1

# # funtioneaza la fel si pentru while ---- nu se mai executa interatiile de dupa



#### Continue in while
##### Continue ------ Va sari peste iteratia actuala--- E un fel de skip
#**** Se va sari peste clocl de cod de dupa skip, care tine de for/while
# Exemplu

# i = 0
# while i <= 10:
#     if i == 5:# Aici sa sari peste 5, 5 nu va fi afisat in print
#        i += 1
#        continue
#     print(i)
#     i += 1


#### FOR/FOR ELSE ####

### RANGE ------- ###### este o functie care defineste un interval (A,B,C)
'''
range ->  range este o functie care defineste un interval
       range (A,B,C)
       A = de unde incepem **** Daca nu punem nimic, atunci va fii default 0 exmplu: range(4) <=> 0,1,2,3
       B = pana unde mergem. *** Daca nu punem, atunci va fii limita superioara -1 exemplu: range(4) <=> 0,1,2,3
       C = pasul - optional (default 1) - adica creste, incrementeaza din 1 in 1          
'''

# for i in range(3,12): # Aici C nu exista si by defalut va incrementa din 1 in 1 de la 3 pana la 12 - 1 ADICA 11 ,
#                      # 'for' stie sa faca asta fara a mai scrie i +=
#     print(i)
# for i in range(2,26,2):# Aici C exista si va incrementa din 2 in 2 - interam de la 2 pana la 24
#     print(i)
# for i in range(14,0,-1):# se incepe intodeuna de la valoarea cea mai mare - in acest caz de la 14 in jos cu -1 pana la 1
#     print(i)
# for i in range(14,0,1 ):# Aici nu va merge pentru ca nu are cum sa plece de la 14 si adunand cu 1 sa ajunga la 0.
#                         # dar dca ii punem -1 funcioneaza pentru ca va pleca de la 14 si va ajuge pana la 0 + 1 adica 1
#     print(i)

# for i in range(33):# By default porneste de la 0 pana la numarul pe care il introducem noi in paranteza -1 adica 32
#     print(i)



##### FOR EACH ---
# Se creaza o variabila la fiecare valoare din lista noastra-------si se ia fiecare in parte

#**** Se foloseste in Liste Dictionare sau in orice alta structura de date

### For va merge ordonat, rand pe rand- de la inceput pana la final infdiferent de lungimea ei

# culori = ['rosu','albastru','verde','galben','mov']
# for alin in culori:
#     print(f'Culoarea mea preferata este: {alin}')

# for i in [3,4,6, 'mere',7, True]:
#     print(i)

# lista_fructe = ['mere', 'pere', 'banane', 'struguri']
# lista_numere = [1,2,3,4] # For  ech merge pe toata lista de numere
#
# for fruct in lista_fructe:
#     print(fruct)
# for numar in lista_numere:
#     print(numar)
# Putem face si in felul de mai sus cu (Range) si ma gandesc la indexi
# for i in range(len(lista_fructe)): # range by default porneste de la 0 pana la 4 -1 = 3, iar noi avem index-ul 3 la lsita_fructe
#     print(lista_fructe[i])

##### ----------------

# Calculeaza numerele pare pana la 101
# suma = 0
# for i in range(0,102,2):
#     suma+=i
#     print(suma)
# print(suma)

######----------Inverseaza texul folosit for-------
#
# text = 'Ana are mere'# indexul aici este 11 si reprezinta i
# text_inversat = ''
# print(text[::-1])
# range (A,B,C)

# for i in range(len(text)-1,-1,-1): ### i = 11,,10.9....0 ---- (-1,-1,-1) pt ca atunci cand mergem descescator
#                                    # trebuie sa punem toti parametri (A,B,C)
#     text_inversat += text[i]
#
# print(text_inversat)


"""
Exercitiu:
avem o lista de culori: ["roz","albastru","rosu","alb","galben"]
Parcurg lista iar cand ajung la valoarea culoarea alb dau skip 
"""

# lista_culori = ['roz','albastru','rosu','alb','galben',]
#
# for culoare in lista_culori:
#     if culoare == 'alb':
#         continue
#     print(culoare)
"""
Avem lista de mai sus. Stergem din lista toate nonculorile (Alb,Gri,Negru)
"""

# lista_culori = ['roz','gri','albastru','rosu','alb','galben', 'negru']
# for nonculoare in lista_culori:
#     if nonculoare == "alb" or nonculoare == "negru" or nonculoare =="gri":
#         lista_culori.remove(nonculoare)
#         print(f'{nonculoare} este este culoare')
# print(f'culori sunt: {lista_culori}')

###### Cum iteream cheie in valoare intr-un dictionar?


# note_elevi = {
#     'Andrei':10,
#     'Elena' :8,
#     'Marina': 10,
# }
# #print(note_elevi.items())
#
# for elev, nota in note_elevi.items():
#     print(f'{elev} a luat nota: {nota}')


####### Cum iteram printr-un dictionar in dictionar etc...

# dict1 = {
#     "HR":{
#         "1":{
#             'Andrei':4532,
#             'Matei':2364,
#             'Florin':12353,
#         },
#         '2':{
#             'Iulia':56435,
#             'Georgiana':1235323,
#             'Luca': 1634523,
#             'Andrei': 653224
#         }
#     }
# }
# # print(dict1.items())
# for cheie, valoare in dict1.items():
#     print("------------------------------")
#     print(cheie,valoare)
#     print('-------------------------')
#     for cheie_din_hr, valori_din_hr in valoare.items():
#         print('--------------------------')
#         print(cheie_din_hr,)
#         print('---------------------------')
#         print(valori_din_hr,)
#         for chei_din_1_2, valori_din_1_2 in valori_din_hr.items():
#             print('!!!!-----------------!!!!')
#             print(chei_din_1_2,)
#             print('!!!__________________________!!!')
#             print(valori_din_1_2,)
#             print("!!!_____________________________!!!")
#






# for i in range(5):
#     if i == 3:
#         continue
#         print(i)


###### Exemple din Teme:
'''

2. Aceeași listă: Folosește un for else În for
  
 - Modifică elementele din listă astfel încât să fie scrie cu majuscule, exceptând primul și ultimul.
În else:
- Printează lista.
'''

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
#
# for masina in range(1, len(masini)-1):
#     masini[masina] = masini[masina].upper()
#     print(masini)
#
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for i, masina in enumerate(masini): # cu enumerate iteram prin fiecare element si indexul acestuia /
#     # masina = variabila egala cu fiecare element din lista
#     if i == 0 or i == len(masini) - 1: # verificam indexul daca este primul sau ultimul
#         continue
#     else:
#         masini[i] = masina.upper() # capitalizam fiecare element din variabila
# else:
#     print(masini)

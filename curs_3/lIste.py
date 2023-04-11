##### Liste  ######

'''
Listele sunt structuri de date buit -in Python
Listele sunt folosite pentru a stoca mai multe valori intr- o singura varialbila
Crearea unei liste se face cu  []  sau folosinfd  list()
'''

#### Crearea unei liste ####

# lista_goala = []
# print(lista_goala)
# print(type(lista_goala))

# SAU
# lista_goala = list ()
# print(lista_goala)
# print(type(lista_goala))
#index      0       1        2        3        4              5
# lista = ['Masina', 45, 'Caractere', True, [1,2,3,4,], [1,2,3,4,5,6,7,8,9]]
#
# print(lista)
# print(lista [5] [4])

#### CARACTERISTICILE UNEI LISTE #####
'''
-> Ordonate
-> Mutabile (putem adauga, putem sterge sau schimba elemente)
-> Accepta duplicate
-> Valorile listei sunt indexate(!!!! Primul index este zero)

'''

#### Listele sunt ordonate ####

'''
Acest lucru inseamna ca valorile listei au o anumita ordine, ordine care nu se schimba.
Daca adaugi o valoare noua in lista, valoarea va fii adaugata la final de lista.
!!!! Atentie, exista anumite metode in liste care pot schimba ordinea valorilor din lista, dar in general 
ordinea valorilor nu se schimba.

'''

# masini = ['Audi', 'VW', 'BMW', 'Skoda', 'Mercedes']

#### Accesare element ####

#(Ca si la String, Curs 1 )

# print('masini [0] =', masini [0])
# print('masini[2::]=', masini[2::])
# print('masini[::-1]=', masini[::-1])
# print('masini[-1:-4]=', masini[-4:-1])
#                                   \ echivalent cu -> masini [1:4]
# print('masini [1:4]=', masini[1:4])

#### Listele  sunt ####

'''
Putem schimba, adauga sau sterge valori din lista dupa ce acesta a fost creata.
'''
#### Adaugare de elemente ####
# masini = ['Audi', 'VW', 'BMW', 'Skoda', 'Mercedes']
#
# masini = masini + ['Toyota']
# print(masini)
#
# # adaugare cu append
# masini.append('Hyundai')
# print(masini)
#
# masini2 = ['Audi', 'Toyota', 'Prius', 'Porche', 'Logan']
# masini.extend(masini2) # extinde lista de masini cu lista de masini2
# print(masini)
# masini.append(masini2)# flosind append se introduce masini2 ca element in lista masini.
# print(masini)

#### Stergere element ####

#

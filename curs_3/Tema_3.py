
# 1. Declara o lista note_muzicale in care sa pui do re mi etc pana la do

# note_muzicale = ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si', 'Do']
# a. Afiseaz-o
# print(note_muzicale)
#b. Inversează ordinea folosind slicing si suprascrie aceasta lista, apoi printeaza
#varianta actuala (inversata)
#
# note_muzicale = note_muzicale [::-1]
# print(note_muzicale)
#c. Pe aceasta lista, aplica o metoda care banuiesti ca face același lucru, adica sa ii
#inverseze ordinea (Nu trebuie sa o suprascrii în acest caz, deoarece metoda face
#asta automat) si apoi printeaza varianta actuala a listei. Practic ai ajuns înapoi la
#varianta inițială

# note_muzicale.reverse()
# print(note_muzicale)

# note_muzicale = note_muzicale[::-1]
# print(note_muzicale)

# 2. Afiseaza pe ecran de cate ori apare nota ‘do’ in lista.
# print(note_muzicale.count('Do'))

#3. Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4], gaseste 2 variante sa le unesti intr-o singura lista.
#
# list1 = [3, 1, 0, 2]
# list2 = [6, 5, 4]
# list1.extend(list2)
# print(list1)
# list1 = list1 +[6, 5, 4]
# print(list1)
# lista_noua = list1 + list2
# print(lista_noua)

#4. Sorteaza si afiseaza lista generata la exercitiul anterior. Sterge numarul 0 din lista
#folosind o functie si apoi afiseaza din nou lista
# lista_noua.sort()
# print(f'Lista sortata este {lista_noua}')
# lista_noua.remove(0)
# print(lista_noua)

#5. Folosind un if, verifica lista generata la exercitiul 3 si afiseaza pe fiecare ramura
#urmatoarele:
#- Lista este goala (IF)
#- Lista nu este goala (ELSE)

# if len(lista_noua) <=0:
#     print('Lista este goala')
# else:
#     print('Lista nu este goala')
# #6. Foloseste o lista care sa goleasca lista de la exercitiul 3
# lista_noua.clear()
# print(lista_noua)

#7. Rescrie if-ul de la exercitiul 5 si verifica inca o data rezultatul. Acum ar trebui sa se
#afiseze ca lista e goala.

# if len(lista_noua)<=0:
#     print('Lista este goala')
# else:
#     print('Lista nu este goala')

#8. Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}, foloseste o functie ca sa
#afisezi Elevii (cheile)

# dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
# print(dict1.keys())

#9 Printeaza cei 3 elevi din dictionarul de mai sus si respectiv notele lor
#Ex: ‘Ana a luat nota {x}’.
#Doar nota o vei lua folosindu-te de cheie

#print(f'Ana a luat nota: {dict1['Ana']}')  #!??de ce nu merge, este la fel, care este eroarea?

##### Trebue sa ai ggilimele duble intre parantezele patrate
#
# print(f'Ana a luat nota: {dict1["Ana"]}')
# print(f'Gigel a luat nota:{dict1["Gigel"]}')
# print(f'Dorel a luat nota:{dict1["Dorel"]}')
#
# #10. Imagineaza-ti ca Dorel a facut contestatie si a primit nota 6.
# #             - Modifica nota lui Dorel in 6
# #             - Printeaza nota lui dupa modificare
#
# dict1['Dorel']= 6
# print(f'Nota lui Dorel dupa modificare este: {dict1["Dorel"]}')
#
# #11. Imagineaza-ti ca Gigel se transfera din clasa.
# #- Cauta o functie care sa il stearga
# #Vine un coleg nou.
# #- Adaugati-l in lista pe Ionica, cu nota 9
# #- Printati dictionarul cu noii elevi
#
# dict1.pop("Gigel")
# print(dict1.keys())
# print(f'Dictionarul fara Gigel: {dict1}')
# dict1['Ionica'] = 9
# print(f'Dictionarul dupa venirea lui Ionel: {dict1}')

#12. Ai urmatoarele seturi:
#zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
#weekend = {'sambata', 'duminica'}
#- Incearca sa adaugi in setul zilele_sapt ziua de ‘luni’ si observa ce se intampla.

# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri','sambata', 'duminica' }
# weekend = {'sambata', 'duminica'}
# zile_sapt.add('luni')
# print(f'Lista a ramas identica pentru ca nu se pot afisa duplicate in seturi: {zile_sapt}')
#
# #13. Foloseste un if si verifica daca:
# #- Weekend este un subset al zilelor din sapt (adica daca elementele din setul weekend se
# #regasesc intre elementele din setul zile_sapt)
# #- Weekend nu este un subset al zilelor din sapt
# #Hint: Va puteti folosi fie de operatorul de comparatie fie de o functie. Rezultatul fiecarui
# #punct de mai sus va fi un boolean
#
# if weekend.issubset(zile_sapt):
#     print('weekend ESTE un subset al zileleor saptamani')
# else:
#     print('Weekend NU este un subsent al zilelor saptamanii')
#
# #14. Afiseaza diferentele dintre aceste 2 seturi (adica elementele care sunt in zile_sapt si nu
# #sunt in weekend si invers)
#
# diferenta1=zile_sapt.difference(weekend)
# print(f'Diferenta dintre zilele_spat si weekend este: {diferenta1}')
# diferenta2 = weekend.difference(zile_sapt)
# print(f'Diferenta dintre week-end si zilele_sapt este: {diferenta1}')
#
# #15 15. Afiseaza intersectia elementelor din aceste 2 seturi (adica elementele care exista in
# #ambele seturi). Hint: Va puteti folosi de o functie
#
# intersectia=zile_sapt.intersection(weekend)
# print(intersectia)
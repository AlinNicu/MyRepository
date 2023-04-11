

# # 1.
#
# # Ce este o variabil?
# # O variabila este
#
# # alin = '36 de ani'
#
# '''
# O variabila in Python este o locatie de memorie rezervata pentru a salva valori.
# Cu alte cuvinte, o variabila in programul Phyton da date computerului, ca sa le proceseze.
#
# O variabila in Python este un nume simbolic care este o referinta a unui obiect.
#  Odata ce obectul este asignat la variabila, te poti adresa obiectul prin numele pe care-l detine
#
# '''
#
#
# #2.
#
# '''
# Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
# variabilă :
#
# - string
# - int
# - float
# - bool
#
# '''
#
# george='are aceiasi varsta ca Raluca'
# raluca=32.7
# ionut=27
# camelia=13>=27
# # print(george)
# # print(raluca)
# # print(ionut)
# # print(camelia>raluca)
#
# #3 Utilizeaza funcia type pentru a verifica daca au tipul de date asteptat.
#
# # print(type(george))
# # print(type(raluca))
# # print(type(ionut))
# # print(type(camelia>raluca))
#
# #4 Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
# # aceeași variabilă (suprascriere):
# #- Verifică tipul acesteia.
#
#
# raluca=32.7
# print('The age of raluca is:', raluca)# 32.7
# # Rotunjește ‘float’-ul folosind funcția round()
# print('The rounded age of raluca is:', round(raluca))# 33
# # #suprascriere
# raluca=33
# print(raluca)
# print(type(raluca))
#
# # 5.Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
# print('George', george)
# print('Raluca are varsta de', raluca)
# print('Ionut are varsta de', ionut)
# print('Camelia este mai mare sau de aceiasi vartsa cu cellati?', camelia)

'''
6. Citește de la tastatură:
- numele;
- prenumele.
Afișează: 'Numele complet are x caractere'.

'''
# nume_prenume='Dumitrescu Ionica'
# nume='Dumitrescu'
# prenume='Ionica'
# prezentare= f'Numele complet este {nume} {prenume}'
# print(prezentare)

# string:         D  u  m  i  t  r  e  s  c  u     I  o  n  i  c  a
# index negativ:  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16
# index negativ: -17-16-15-14-13-12-11-10-9 -8 -7 -6  -5 -4 -3 -2 -1

# print(len(prenume+nume))

'''
7. Citește de la tastatură:
- lungimea;
- lățimea.
Afișează: 'Aria dreptunghiului este x'.

'''

# lungimea= 7
# latimea=5
# aria_dreptunghiului=f'Aria dreptunghiului este:'
# print(aria_dreptunghiului,7*5)


'''
8.Având stringul: 'Coral is either the stupidest animal or the smartest rock':

- afișează de câte ori apare cuvântul 'the';

'''
# str = 'Coral is either the stupidest animal or the smartest rock'
# print(len(str))
# print(str.upper())
# print(str.count('the'))

'''
9. Același string.
● Afișează de câte ori apare cuvântul 'the';
● Printează rezultatul.

'''
# print('Cuvantul the apare de', str.count('the'))

'''
10. Același string.
● Folosiți un assert ca să verificați dacă acest string conține doar numere.

'''
# print('Contine numere acest string?')
# assert str==int

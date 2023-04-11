from utils.utils import say_hi_name_and_age, print_hi
# import utils.utils
'''
* O functie este o modalitate prin care putem sa economisim un cod.

* O functie putem sa o definim o singura data s apoi sa facem ceea ce se numeste apelare a functiei.

* Apelarea funtiei inseamna trimiterea sistemului catre adresa de memorie care poarta numele funtiei
     si la care este stocat codul pe care vrem sa-l executam.

* Definirea unei functii se poate face pe baza keyword-ului def

* O functie POATE sa abia PARAMETRI, dar nu este obligatoriy sa abiba.

* Chiar daca functia NU are parametri ,Parantezele De Dupa numele Functiei
    sunt Obligatorii atat la definire cat si la apelare.

* Un parametru reprezinta o informatie de care functia are nevoie din exeterior
     pentru a executa toate instructiunile.

* Putem alege sa parametrizam atunci cand vrem ca functia noastra sa poata
    sa fie rulata pentru o plaja mai mare de valori.
    ex: suma intre doua numere, putem avea alte doua numere la fiecare rulare

* O functie POATE sa aiba optiune de return, dar nu este obligatoriu sa aiba.

Vom alege sa punem o optiune de return pe functie atunci cand vrem sa salvam rezultatul
    acelei functii  intr-o variabila sau sa trimitem acel rezultat catre un sistem extern.

'''

# # Definirea functiei, fara parametri si fara return
# def say_hi():
#     print('Hi')
#     print('Salutari din functia say_Hi()')
#     print('Inca un Hi')# putem adauga cat vrem aici, va fii afisat in momentul accesarii functiei.


#apelarea functiei de mai sus (!!!! Atentie !!!) Daca nu este apelata acesta nu se va exexuta.
# Parametru reprezinta datele de intrare (ex o variabila), uneori functiile au nevoie de acesti parametri
# Functia poate avea oricati paramentri ne dorim, in funtie de conventie-
# Parametri sunt optionali pt functie, daca avem mai multi Paramentri se despart prin virgula.
# SUnt ca niste variabile care nu sunt initializate, daca nu apelam acesta functie userul nu are nici o valoare
# in cazul respetiv si voi fii initaliazate dor atunci cand apelam.
# say_hi()
# say_hi()
# say_hi()
# say_hi()
# say_hi()

# Def unei functii cu parametru

# def printt_hi(nume):
#     print(f'Hi {nume}')

# Apalearea functiei cu parametru: (1 parametru) (din fisierul utils.py care se afla in directorul utils (vezi import de la lina 1_

# print_hi("Vali")
# print_hi('Fanica')
#
# #say_hi_name_and_age este o functie care se afla in uitls.py
# say_hi_name_and_age('Vali', 24)
# say_hi_name_and_age('Fanica',30)

# in situatia in care folosim doar utils, vezi ex la lina 2 va trebuii sa folosim utils la inceput,
# dar situatia se complica si este rocomandat ca sa folosim expemplul de la linia 1
# utils.utils.print_hi()
# utils.utils.print_hi()

# say_hi_name_and_age('Vali', 24)
# say_hi_name_and_age('Fanica',30)

# def say_hi():
#     print('Hi')
#     print('Salutari din functia say_Hi()')
#     print('Inca un Hi')# putem adauga cat vrem aici, va fii afisat in momentul accesarii functiei.
'''
def -> keyword-ul care anunta inceptul definirii unei functii

say_hi -> numele funtiei care este dat de noi si care poate fii orice in general (free text)
 !!! Atrentie!!! Numele functiei, trebuie sa fie sugestiv cu actiunea pea care o desfasoara
 
 () -> Zona in care putem specifia parametri, In cazul functiei say_hi nu aavem nici un parametru,
  insa in cazul functiei say_hi_name_and_age avem definiti 2 parsmetri (name, age)
 : -> reperezinta inceputul functiei ca si la (if, for , while)
 apoi 
 
 Corpul functiei (Atentie: Indentat, catre dreapta  ca la if , for, while.
  
'''

'''
definim functia  -> parametrii (ex: say_hi_nume_and_age (nume, age)) (nume si age sunt parametrii)
apelam functia -> argumente (ex: (say_hi_name_and_age('Fanica', 30)) ('Fanica' si 30 sunt argumente)
ex: Parametru = Nume
    Argument = Fanica
    
'''
# In acest caz, parametrul va fii 15
# say_hi_name_and_age('Tudor')
# In acest caz parametrul va fii 56 ______
# Practic ia valoarea argumentului pe care il transmitem noi in functia noarstra
# say_hi_name_and_age('Andrei',56) # Daca scriu acelasi lucru si scriu by default 56, va luta valoarea 56


### Foarte mare Atentie - daca am pun un paramentru si nu am pus valoare default (vezi age din say_hi_name_and_age),
# ne va da eroare. Suntem obligatI SA O INITIALIZAM CAND APELAM FUNCTIA

#Ex: TypeError: print_hi() missing 1 required positional argument: 'nume'
# - adica lipseste un argument pozitional si va arunca o eroare

# print_hi() # Arunca o eroare- Pentru ca nu are by default si suntem obligati sa-i dam noi o valoare.




####___________RETURN__________####

'''
By default o functie care nu are RETURN va returna  valoarea de NONE

'''

# Ne va afisa doua valori - prima va fii 'Hi my name is Tudor, I am 45' si
# a doua va fii 'None' si este valoarea variabilei valoare_returnata -
# Ea doar printeaza mesajul dar nu are nici o valoare in  ea
# valoarea_returnata = say_hi_name_and_age('Tudor', 45)
# print(valoarea_returnata)

# Acum putem sa definim o funtie in care sa scriem:

# def numar_par(numar):
#     if numar % 2 == 0:
#         return  f'Numarul {numar} este par'
#     else:
#         return f'Numarul {numar} este impar'
# Acum daca apelez numar par de 4
#Ex

# numar_par(4)

# o sa-mi apleze funcia mea numar par dar nu o sa afiseze nimic
# (Tot none va fii). De ce?! Pentru ca eu nu am facut un Print absolut nicaieri,
# doar am returnat un string

### in  acest caz, declar o noua variabila :
#Ex:

# valoare = numar_par(4) # In acest caz daca fac print la valoare
# print(valoare)

# Aici este vorba de o noanta importanta si anume -
# # daca pun aici print la line 131 -133 in loc de retun
# def numar_par(numar):
#     if numar % 2 == 0:
#         print (f'Numarul {numar} este par')
#     else:
#         print (f'Numarul {numar} este impar')
#
# valoare = numar_par(4)
# print(valoare)
# Amterior am vazut ca Nea afisat Numarl 4 este par.
# Dar daca in loc de return pun print ne va afisa Numarul 4 este par
# si imediat dupa el None, pentru ca nu imi retuneaza nimci functia mea.
# Insa daca pun return in loc de print imi va afisa Numarul 4 este par deoarce am flosit  print,
# dar valoare este None pentru ca nu imi returneaza nimic functia mea.

## Daca folosec retun imi va arata exact valoarea Numarul 4 este par.

# De aceia retun se pun intotdeuna la final,
# deoarece orice cod de dupa nu mai este executat, pentru ca iese din functie.
# Vezi acest print de dupa retrun
#Ex:
# def numar_par(numar):
#     if numar % 2 == 0:
#         return  f'Numarul {numar} este par'
#         print('Sunt aici')
#     else:
#         return f'Numarul {numar} este impar'

###### Ce este un Retun?############

'''
* Se foloseste cand functia ne si expune un raspuns  (output)
* Acest raspuns se poate salva in Variabile
* Return este Optional
* Se poate returna orice timp de date cunoscut
* In gereral , return e ultimul lucru in fu'nctie,
  deoarece aici se iese din functie.
* In general avem un singur return.
  Exceptie cand folosim  is else, 
  atunci puten acea mai multe dar oricum la rulare se va ajunge doar
  intr-un singur caz.

'''

# Vrem sa calculam suna tuturor numerelor pare dintr-un anumit interval si sa returnam suma.
# Functia primeste ca si paratmetru  limita superioara din intervalul nostru (by defalut incepe de la 0)

# def suma_numere_pare(limita_superioara):
#     suma= 0
#     for numar in range (limita_superioara + 1):
#         if numar % 2 == 0:
#             suma += numar
#     return suma # fara acest return nu funcioneaza exeplul cu  50 de mai jos -
                # pentru ca suma din acesta sunctie va fi NONE
               # si nu va avea cu ce sa compare acel 50 din functia de mai jos-
               # Prin return si aceasta functie ne putem da mai departe valoarea pe care am folosit-o

##### ATENTIE!!!!! variabila suma  este diferita de variabila din interiorul functiei noastre

# suma = suma_numere_pare(32)# fara print nu arata nimic aici
#
# # Folosind  suma calculata mai sus, folosind o alta functie verifica daca este mai mare decat 50.
# suma = suma + 10 # Prin acesta va creste de la 272 la 282
# def verificare_suma(suma):# toate aceste suma sunt diferite unele de altele, nu au nimic in comun
#     if suma > 50:
#         print(f'Suma este mai mare decar 50, suma fiind {suma}')
#     else:
#         print(f'Suma este mai mica decar 50, suma fiind {suma}')


#Ex: daca nu am folosi acest return si ii dam run, nu va functiona

# verificare_suma(suma) #Suma este mai mare decar 50, suma fiind 272


# print(suma) # 272 = suma tuturor numerelor pare dintre 0 si 32 = 272

#
# def variabila_in_functie():
#     nume = 'Andrei'
#     print(suma)
# print(nume) # aici va da eroare - nu vede variabila de nume din interiorul
            # functiei
            # Adica variabila ( nume = Andrei) exista doar in interiorul functiei noastre
            # Insa daca facem un prin sunt variabila (nume=Andrei) si o apelam prin variabila_in_functie.
            # Variabila exista doar in interiorul functiei nostre si doar atat.
#


# O functie care are return este o functie care ne returneaza ceva.

'''
Scrieti o functie care primeste ca parametru un string si calculeaza numarul de litere mari si litere mici din el

Si printeaza numerele respective

'''

# def calculator_de_litere(text):
#     upper_case = 0
#     lower_case = 0
#     for litera in text:
#         if litera.isupper() == True:
#             upper_case += 1
#         elif litera.islower() == True:
#             lower_case += 1
#
#     print(f'Textul a fost {text}')
#     print(f'Numarul de litere mici este : {lower_case}')
#     print(f'Numarul de litere mari estee {upper_case}')
#
# text_tastatura = input('Introduceti un text')
# #apelam functia
# calculator_de_litere(text_tastatura)
# calculator_de_litere('Am trei ani')


def exemplu_multiple_parameters(nume = None, prenume= None, varsta = 0, cnp= '0', sex= None): # Aici nu vreau sa setez toti parametri ci doar ce doresc
    print(nume,prenume,varsta,cnp, sex)

exemplu_multiple_parameters(None, 'Vasile', 0, "0233455677")

exemplu_multiple_parameters(cnp = "0233455677", prenume = 'Vasile', nume = 'Petrescu') # Dupa cum observati nu ma mai
# intereseaza pozitia sau valoarea celorlati paramentri si nu trebuie sa-i rescriu.
#Dar cand nu am setat la by defalut None atunci trebuei sa-i dau o valoare la nume Obligatoruiu

# ACesttea sunt functii fara RETURN

nume, prenume, varsta, cnp, sex = exemplu_multiple_parameters(None, "Vasile", 0, "0233455677" )
print(cnp)
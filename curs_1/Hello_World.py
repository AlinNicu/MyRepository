# print("Hello World")
# print("Hello World")
# print('Jesus Christ')
# print("Is the King of Kings")
# print("Alin Nicu Vaduva il va slujii si-L va uma cu adevarat")
#
# ######## Comentarii ########
#
# # Comentarii pe o linie (#)
#
#
# '''
# Comentarii
# pe
# mai
# multe
# linii
#
# '''
#
# '''
#
# Comentarii
# pe
# mai
# multe
# linii
#
# Comentariu = linie/linii din  codul sursa care nu sunt executate. Sunt menite deobicei pentru anumite adnotari sau
# explicatii
#
#     Comentariu pe o linie se face cu #
#     Comentarii pe mai multe linii se face """""" (3 ghilimele la inceput si la final)
#     sau '''''' (3 apostrof la inceput si la final)
# """
#
# #sau
# """
# Comentarii
# pe
# mai
# multe
# linii
# '''''''''''
#
# print("Al 3-lea Hello world")
#
# ######Variabile######
#
# print("**Variable**")
#
# """
# 1. O variabla este un spatiu rezervat in memoria sistemului (calculatorului)
# care poate stoca informatii si poate fi modificata in timp.
#
# 2 O variabila trebuie sa fie definita de un nume ( cat mai sugestiv posibil)
# x=1998 (not good practice), an 1998 (good practice)
# 3. Variabila este creata doar dupa ce I se asigneaza o valoare.
# 4. Reguli de denumire a unei variablie:
# - Nu pot contine spatii
# - Nu pott fi denumite cu denumiri rezervate (de exemplu "print")
# - trebuie sa fie unice
# - Nu pot incepe cu un numar dar pot contine numere in compozitie:
# expemplu: var5=5 ->good - (5var=5->gresit)
# - Case sensitive (o variablia cu numele de camelcase nu este tot una cu camelCase)
# 5. Conventii de denumire in general in python
# - Pentru nume de cale (Sesiuna 7): pascalCase
# - Pentru nume variablie/metode/functii (Sesiunea 5+): snake_case
# - Pentru constante: NUME_CONSTANTA (cu uppercase
#
# """
#
# #5var=5
#
# # Declararea si initializarea unei variabile
#
# model_masina="60"
# model_Masina="V10"
# print("model_masina")
# print(model_Masina)# variabilele sunt case senzitive
#
# # Suprascriere
#
# model_masina="V70"
# print(model_masina)
#
# #Constante -> In python este conceptual. Se scrie cu uppercase si teoretic valoarea nu trebuie sa se modifice.
#
# NUME_CONSTANTA=500
# print(NUME_CONSTANTA)
# NUME_CONSTANTA=70
# print(NUME_CONSTANTA)# este doar conceptul
#
# # Putem modifca tipul unei variabile
#
# model_masina= 90
# print(model_masina)
# # declarare pe o singura linie
#
# mar, para, portocala = "mar", "para", "portocala"
# print(mar,para,portocala)
#
# x=y=z=100
# print(x,y,z)
#
# ##### Tipuri de Date (DATA TYPES) ######
#
#
# """
# Un tip de date este o informatie care ii spune sistemului ce tip de informatie putem stoca intr-o variabila
#
#
# Cele mai folosite tipuri de date
# - int(short for integer)-> Poate stoca doar valori intregi  (1,2,5,10000000,4500000, etc)
# - float-> poate stoca numere cu virgula (1.42 2.8)
# - bool (short for Boolean) -> True or False
# - String-> poate stoca text (sir de caractere)
#
# """
#
# a=3
# b=3.3
# c=False
# d="string"
#
# print("a este de tipul", type(a))
# print("b este tipul",type(b))
# print("c este tipul",(c))
# print("d este de tipul",type(d))
#
# ###### TYPE si TYPE CASTING ######
# exemplu =30
# print("exemplul este tipul", type(exemplu))
#
# exemplu="text"
# print("exemplu este tipul", type(exemplu))
#
#
# exemplu= True
# print("exemplu este de tipul", type(exemplu))
#
# exemplu_2="100"
# print(type(exemplu_2))
# tip_de_data_intreg=int(exemplu_2)
# print(type(tip_de_data_intreg))
#
# a='text'
# #print(int(a))#-> ne da erroare
#
# number= 1.9999 #float- aici ne da valoarea 1
# print(int(number))
#
# ##### Functia print() #####
# nume="Vali"
# varsta=24
# print("Ma numesc " + nume + " si am varsta de " + str(varsta) + " ani")
# print(f"Ma numesc {nume} si a varsta de {varsta} ani") # Recomandat sa scriem asa
#
# ##### STRING-URI #####
# print("Mc Donald's")
# print('Mc Donald"s')
#
# # SAU putem folosi escape mechanism
# # # Caracterul "escape" este backslashul\= va face escape la caracterul ilegal
#
# #print('Mc donald\'s') # o sa ia tot ca un caracter si o sa mearga daca pun \
#
#
#
# nume="Popescu"
# prenume="Elena"
# prezentare= "Numele meu este " + nume + " "+ prenume
# print(prezentare)
#
# prezentare_varianta_2=f"Numele meu este {nume} {prenume}"
# print(prezentare_varianta_2)
#
# ##### String (index, slicing, len(), metode) #####
#
# string_example="Ana are mere"
# print(string_example[0])
# print(string_example[1:4])# pozitia de start este indexul 1  iar ultima pozitie luata in considerare este 3
# print(string_example[-1])# ultimul caracter
# print(string_example[-4])
#
# #string  A n a   a r e   m e  r e
# #index   0 1 2 3 4 5 6 7 8 9   10 11
# #index negativ: -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
#
#print(string_example[-12])
#
#
# p)rint(len(string_example))# rezultatul este de -12
# print(string_example.upper())# returneaza de cate ori apare "ANA ARE MERE"
# print(string_example.count("are")# returneaza de cate ori apare
# #caracterul/sub-string introdus intre () in string-ul nostru
# print(string_example.replace("a","9"))# schimba caracterul din stanga->a cu 9

# string_example.lower()

##### INPUT #####
#
# a = input("introduceti date de la tastatura")
# print(f"Ai introdus {a}")# care este problema aici de ce nu apre {a} ca sapuns? de ce este incomplet?

# nume= input ("introduceti numele")
# varsta= input("Introduceti varsta ") #varsta = "24"
# varsta= int(input("Introduceti varsta"))

# varsta_peste_10_ani = varsta + 10
# print(f"Varsta peste 10 ani: {varsta_peste_10_ani}")

# nume, varsta, gen = input("introduceti numele varsta genul:").split()# se ia ca si separator spatiu
# print(nume, varsta, gen)
# nume, varsta, gen = input("introduceti numele|varsta|genul:").split("|") # se ia "|" ca separator
# print(nume, varsta, gen)
#

##### ASSERT #####
#
# a=1
# #
# assert a==1,"A nu este egal cu 1"#  == vreifica daca a = 1
# print("Am ajuns aici deoarece a este egal cu 1")
# assert a==2, "A nu este egal cu 2"
# # nu ami am ajuns- deoarece asertul a fdat ca fals
# print("Oare mai ajung aici daca verific ca a este egal cu 2")
# #
# user_name=input("Username:")
#
# #
# assert user_name =="user2015", "User inexistent"
# password=input("Password:")
# assert password == "parola123", "parola incorecta"
# print("Autentificare reusita")

assert 1=="1"# False pentru ca 1 intre "" este considerat sting ( litera) si nu type adica cifra casa poata face comparatia
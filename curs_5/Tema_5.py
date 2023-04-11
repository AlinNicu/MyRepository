
#1.Funcție care să calculeze și să returneze suma a două numere
#
# numar1 = 25
# numar2 = 45
#
# def calc_num(numar1,numar2):
#     sum = numar2 + numar1;
#     return sum;
# print('Suma celor doua numere este:',calc_num(numar2,numar1))


#2.Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
# def par_impar():
#    numar = int(input("Enter a number: "))
#    if (numar % 2) == 0:
#     print("{0} True, numarul este par".format(numar))
#    else:
#     print("{0} False, numarul este impar".format(numar))
#
#
# par_impar()

# 3 Funcție care returnează numărul total de caractere din numele tău complet. (nume, prenume, nume_mijlociu)

# def get_number_of_chars_from_name(nume, prenume, nume_mijlociu = ''):
#     nr_chars = 0
#     concatenate_strings = nume + prenume + nume_mijlociu
#     return len(concatenate_strings)
#
#
# get_nr_chr_alin = get_number_of_chars_from_name('Slavescu', 'Alin')
# print(get_nr_chr_alin)
# get_nr_chr_vali = get_number_of_chars_from_name('Chiras', 'Valentin', 'Fanica')
# print(get_nr_chr_vali)

# 4. Funcție care returnează aria dreptunghiului

# def aria_dreptungiului(L,l):
#     aria = lungime * latime
#     return aria
# print(aria_dreptungiului(10, 5))
# print(aria_dreptungiului(20,10))

# lungime=10
# latime=5
# def get_rectangle(x):
#     return latime * lungime
# for i in 'x':
#     # function call
#     result = get_rectangle(i)
#     print('Aria lui',i, '=',result)

# 5 Funcție care returnează aria cercului

# def aria_cercului(raza):
#     aria = raza * raza * 3.14
#     return aria
#
# print(aria_cercului(10))
# print(aria_cercului(5))

# def findArea(r):
#     PI = 3.14
#     return PI * (r*r);
# print("Aria cercului este = %.6f" % findArea(6));


#6. 6. Funcție care returnează True dacă un caracter x se găsește într-un string dat și Talse dacă nu găsește.

# def check_character(string, x):
#     if x in string:
#         return True
#     else:
#         return False
#
# print(check_character('pui de porumb', 'catel'))
# print(check_character('x-ray', 'x'))

#### 7. Funcție fără return, primește un string și printează pe ecran:
# ● Nr de caractere lower case este x
#● Nr de caractere upper case este y

# def nr_caractere_up_and_low(string):
#     x_low = 0
#     y_up = 0
#     for caracater in string:
#         if caracater.isupper():
#             x_low = x_low + 1
#         elif caracater.islower():
#              y_up = y_up + 1
#     print(f'Numarul de caractere mari este: {x_low}')
#     print(f'Numarul de catactere mai mici este: {y_up}')
#
# nr_caractere_up_and_low('asdAAA1aaA')

# 8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive.


# lista = [4,  3, 2, 1 - 3, -7, -10]
#
# def numere_pozitive(numere):
#     lista =[]
#     for numar in numere:
#         if numar > 0:
#             lista.append(numar)
#     return lista

# print(numere_pozitive(lista))



#9
'''. Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
Primul numar x este mai mare decat al doilea nr y
Al doilea nr y este mai mare decat primul nr x
Numerele sunt egale. '''

# def numere(x,y):
#     if x == y:
#         print(f'Numerele sunt egale')
#     elif x > y:
#         print(f'Primul numar {x} este mai mare decat al doilea numar {y}')
#     else:
#         print(f'Al doilea nr {y} este mai mare decat primul numar {x}')
#
# numere(17, -2)
# numere(19, 20)


#10
# '''10. Functie care primeste un numar si un set de numere.
# Printeaza ‘am adaugat numarul nou in set’ + returneaza True
# Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False'''
#
# set_numere1 = {3, 5, 7, 78, -8, 25}
# set_numere2 = {2, 10, 3, 28, -6, 57}
#
# def adaugare_numar(set_de_numere, numar_now):
#     if numar_now in set_de_numere:
#         print(f'Nu am pus numarul {numar_now} in set, exista deja')
#         return False
#     else:
#         set_de_numere.add(numar_now)
#         print(f'Am adaugat numarul {numar_now} in set')
# print(adaugare_numar(set_numere1, 30))
# print(adaugare_numar(set_numere2, 57))
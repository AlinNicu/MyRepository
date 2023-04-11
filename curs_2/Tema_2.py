# 1 Explica cu cuvintele tale in cadrul unui comentariu cum functioneaza un if else
'''
Instrucțiunea if-else este folosită pentru a executa atât partea adevărată, cât și partea falsă a unei anumite condiții.
Dacă condiția este adevărată, codul de bloc if este executat și dacă condiția este falsă,
codul de bloc else este executat.
'''

# 2. Verifica si afiseaza daca x este numar natural sau nu (un numar se considera natural
# daca este numar intreg mai mare ca 0)

# x = int(input('Introduceti numar natural:'))
#
# if x % 8 == 2:
#     print('Numarul este natural')
# # else:
#     print('Numarul nu este natural')


#3. Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru


# x = int(input('Introduceti numar pozitiv:'))
#
# if x >= 1:
#     print('Numarul este pozitiv')
# else:
#     print('Numarul nu este pozitiv')
#
# x = int(input('Introduceti numar neutru:'))
# if x == 0:
#     print('Numarul este neutru')
# else:
#     print('Numarul nu este neutru')
#
# x = int(input('Introduceti numar negativ:'))
# if x < 0:
#     print('Numarul este negativ')
# else:
#     print('Numarul nu este negativ')

#4. Verifica si afiseaza daca x este intre -2 si 13 (incluzand captele de interval).

# x = 5
# if x  >= -2 and x <= 13:
#    print('Acest numar este cuprins intre -2 si 13.')
# else:
#    print('Acest numar este cuprins intre -2 si 13 ')

#5.Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5
# x = 18
# y = 11
#
# if x-y < 5:
#     print('Diferenta este mai mica decat 5')
# else:
#     print('Diferenta este mai mare decat 5')

#6. Verifica daca x NU este intre 5 si 27, incluzand capetele de interval. (a se folosi ‘not’)
#
# x = 2
#
# if not (5 <= x <= 27):
#     print( 'X nu este intre 5 si 27')
# else:
#     print('Numarul este intre 5 si 27')

#7. - Declara o noua variabila y de tip int si apoi verifica si afiseaza daca x si y sunt egale,
#daca nu, afiseaza care din ele este mai mare

# x = 4
# y = 4
#
# if x == y:
#     print('x and y sunt egale')
# elif x > y:
#     print(f'{x} este x si este mai mare decat y')
# else:
#     print(f'{y} este y si este mai mare decat x')

#8. - Presupunand ca x, y, z (toate de tip int) - reprezinta laturile unui triunghi,
                    # afiseaza daca triunghiul este isoscel (doua laturi sunt egale),
                    # echilateral (toate laturile sunt egale)
                    # sau oarecare (nicio latura nu e egala).
# x = 10
# y = 10
# z = 10
#
# if (x == y and x != z) or (x == z and x != z) or (y==z and y != z):
#     print('Triunghiul este isoscel')
# elif x == y == z:
#     print('Triunghiul este cu laturile egale')
# else:
#     print('Triunghiul este orarecare')

# 9. Citeste o litera de la tastatura apoi verifica si afiseaza daca este vocala sau nu

# letter = input('Introduceti o litera:')
# letter = letter.lower()
# if letter.isdigit():
#     print('Nu ai introdus o litera ci altceva')
# elif letter.upper() == 'a' or letter.upper() == 'e' or letter.upper() == 'i' or letter.upper() == 'o' or letter.upper() == 'u':
#     print('Litera este vocala.')
# else:
#     print('Nu este vocala')

#10. # Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza:
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F

# nota = float(input('Ce nota a primit?'))
# if 9 <= nota <=10:
#     nota='A'
#     print(f'Nota din sistemul american este {nota}')
# elif 8 <= nota <=9:
#     nota='B'
#     print(f'Nota din sistemul american este {nota}')
# elif 7 <= nota <=8:
#     nota='C'
#     print(f'Nota din sistemul american este {nota}')
# elif 6 <= nota <=7:
#     nota='D'
#     print(f'Nota din sistemul american este {nota}')
# elif 5 <= nota <=6:
#     nota='E'
#     print(f'Nota din sistemul american este {nota}')
# elif 4 <= nota <=5:
#     nota='F'
#     print(f'Nota din sistemul american este {nota}')
# else:
#     print('Valoarea introdusa nu este de la 1 la 10')



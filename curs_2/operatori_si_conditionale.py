##### Operatori de atribuire #####

'''
Atribuire/Asignare = proces prin care salvam informatii la adresa de
 memorie indentificarea cu un nume al variabilei
'''

'''
= --> x=5
+= --> x + = 1 <=> x = x+1
-= --> x - = 1 <=> x = x-1
*= --> x * = 3 <=> x = x*3
/= --> x / = 3 <=> x = x/3
'''

# print('*' * 5, 'Operatori de atribuire', 'x' * 5)

# x = 3
# print('x=3-->', x)
# x++3
# print('x+=3-->', x)
# x -= 3
# print('x-=3-->', x)
#
# x *= 3
# print('x*=3-->', x)
# x /= 3
# print('x/=3-->', x)

#####	Operatori aritmetici    #####
"""
+   Adunare        --> x+y
-   Scadere        --> x-y
*   Inmultire      --> x*y
/   Impartire      --> x/y
//  Floor division --> x//y (Rotunjeste rezultatul la cel mai apropriat numar intreg inferior)
%   Modulo         --> x%y (Returneaza Restul impartirii)
**  Exponential    --> x**y ( Ridica la putere
"""
# print("*"*5,"Operatori aritmetici","*"*5)
#
# x = 9
# y = 3
#
# print('x+y=', x+y)
# print('x-y=', x-y)
# print('x*y=', x*y)
# print('x/y=', x/y)
# print('x//y=', x//y)
# print('x%y=', x%y)
# print('x**y=', x**y)

#-----------------------------------------------------------------------------------------------------------------------

#####	Operatori Logici    #####

'''
and --> Returneaza True dsca ambele conditii sunt adevarate --> x > 5 and x < 10

or  --> Returneaza True daca cel putin o conditie este adevarata --> x > 5 or x == 2

not --> Returneaza True daca rezultatul conditiei este Fals si vice- versa --> nor  (x<5), not ((x> 5 and  x < 10)

'''

# print("*"*5,"Operatori logici","*"*5)
#
# x = 2
# print('and-->', x > 5 and x < 10)
# print('or->>', x > 5 or x == 2)
# print('not->>', not ( x < 5 and x < 10 ))

# ------------------------------------------------------------------------------------- #
#####	Operatori de comparare    #####
"""
==  --> Equal                       --> x == y
!=  --> Not Equal                   --> x != y
>   --> Greater then                --> x > y
<   --> Less then                   --> x < y
>=  --> Greater then or equal to    --> x >= y
<=  --> Less then or equal to       --> x <= y
Oridinea prioritatii NOT > AND > OR
"""
# print("*"*5,"Operatori de comparare","*"*5)
#
# x = 2
# y = 10
#
# print(f'{x} == {y} -->', x == y)
# print(f'{x} != {y}-->', x != y)
# print(f'{x} > {y}-->', x > y)
# print(f'{x} < {y}-->', x < y)
# print(f'{x} >= {y}-->', x >= y)
# print(f'{x} <= {y}-->', x <= y)

# NOT > And > OR

# a = 10
# b = 20
# c = 30
#
# #       F    or  F   and    T   => F
# print( a > b or b > c and c == 30)     # inseamna  a > b or ( b > c  and   c == 30)
# #       F    and   F   or  F     and    T
# #             F        or         F      => F
# print( a > b and b > c or a == 15 and c == 30 )   # inseamna (a > b and b > c) or (a == 15 and c == 30)
# #     not   F    and   F    or    T
# #       T       and    F    or     T
# #                F          or     T     => T
# print( not a > b and a == 15 or c == 30 )  # inseamna ((not a > b) and a == 15) or c == 30

# -------------------------------------------------------------------------------------#

 ##### Flow Control #####
# print('*'*5, 'Flow Control', '*'*5)
# print('*'*3, 'If simplu', '*'*3)
# #If simplu
# x=5
# if x > 10:
#     print(f'Valoarea lui x este mai mare decat 10')
# print(' Am iesit din if')
# if x < 10:
#     print(f'Valoarea lui x este mai mica decat 10')
# print('Am iesit din if')
#
#
#if else
# print('-' * 20)
# numar = int(input('Introducere numar:'))
#
# if numar % 2 == 0:
#     print('Numarul este par')
# else:
#     print('Numarul este impar')
# print('Cod de dupa if elese')

#if elif else
# print("-" * 20)
# optiunea = int(input("Alege o optiune [0, 1, 2]: "))
#
# if optiunea == 0:
#     print('Ai ales 0')
# elif optiunea == 1:
#     print('Ai ales 1')
# elif optiunea == 2:
#     print('Ai ales 2')
# else:
#     print('Ai ales altceva in afara de  0, 1, 2')
#
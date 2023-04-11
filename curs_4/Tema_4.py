
#1
'''
 Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi; ● ‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while.
'''
from operator import index

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
#
# for masina in range(len(masini)):
#     print(f' Masina mea preferata este:{masini[masina]}')

# for masina in masini:
#     print(f'masina mea preferata este:{masina}')

# masina = 9
#
# while masina < len(masini):
#     print(f'Masina mea preferata este: {masini[masina]}')
#     masina = masina + 1

#2
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
# else:
#     print(masini)

#3
'''
3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes. Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘

'''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for masina in masini:
#     if masina == "Mercedes":
#         print(f'Am gasit masina dorita de dumneavoastra {masina} ')
# else:
#     print(f'Am gasit masina {masina}.Mai cautam')

#4.

'''
4. Aceași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
else).
- Printează S-ar putea să vă placă mașina x.

'''

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#
# for masina in masini:
#     if masina == "Trabant" or masina == "Lastun":
#         continue
#     print(f'S-ar putea sa va placa masina:{masina}')


#5
'''
5. Modernizează parcul de mașini:
● Crează o listă goală,masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
● Printează Modele vechi:x.
● Modelenoi:x. 
'''

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# masini_vechi = []
#
# for masina in masini:
#     if masina == 'Trabant' or masina =='Lastun':
#         masini_vechi.append(masina)
#         index = masini.index(masina)
#         masini[index] = 'Tesla'
#
# print('Modele vechi:', masini_vechi)
# print('Modele noi:', masini)

#6
'''. Având dict: pret_masini = {
                       'Dacia': 6800,
                       'Lăstun': 500,
                       'Opel': 1100, 
                       'Audi': 19000, 
                       'BMW': 23000
}
Vine un client cu un buget de 15000 euro.
● Prezintă doar mașinile care se încadrează în acest buget.
● Itereaza pri ndict.items() și accesează mașina și prețul.
● Printează Pentru un buget de sub 15000 euro puteți alege mașină
xLastun
● Itereazăprinlistă.

'''
# pret_masini = {
#             'Dacia': 6800,
#             'Lăstun': 500,
#             'Opel': 1100,
#             'Audi': 19000,
#             'BMW': 23000
# }
# buget = 15000
#
# for masina, pret in pret_masini.items():
#     if pret <= buget:
#         print(f'In bugetul de pana la 15000 {buget} euro puteti alege masina: {masina}')

#7. Având lista:

'''
● Iterează prin ea.
● Afișează decâte ori apare 3(nu ai voie să folosești count).
'''
# numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# x = 0
#
# for numar in numere:
#      if numar == 3:
#          x = x + 1
# print(f'Numarul 3 apare de: {x}' )

#8
'''
 Aceeași listă:
● Itereazăprinea
● Calculeazășiafișeazăsumanumerelor(nuaivoiesăfoloseștisum).
'''
# numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# suma = 0
#
# for numar in numere:
#     suma = suma + numar
# print(f'Suma numerelor din lista este:{suma}')

#9
'''
Aceeași listă:
● Iterează prin ea.
● Afișază cel mai mare număr(nu ai voie să folosești max).

'''

# numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# maxim = numere[0]
# for numar in numere:
#     if numar > maxim:
#         maxim = numar
# print(f'Cel mai mare numar din lista este: {maxim}')

#10. Aceeași listă:
'''
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
Ex: dacă e 3, să devină -3 
● Afișază noua listă.
'''
# numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#
# lista_neg = []
# for numar in numere:
#     if numar > 0:
#         # numar = numar - numar*2
#         numar = -(abs(numar)) # alta solutie
#     lista_neg.append(numar)
# print(f'Lista a devenit: {lista_neg}')


#####_______________________ Optinonale__________#########

'''
1.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3] numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere
Populează corect celelalte liste
Afișeaza cele 4 liste la final

'''
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare =[]
# numere_impare = []
# numere_pozitive = []
# numere_negative = []

# for numar in alte_numere:
#     if numar % 2 == 0:
#         numere_pare.append(numar)
#     else:
#         numere_impare.append(numar)
#     if numar > 0:
#         numere_pozitive.append(numar)
#     else:
#         numere_negative.append(numar)
#
# print(f'lista cu numerele pare este:{numere_pare}')
# print(f'lista cu numerele impare este:{numere_impare}')
# print(f'lista cu numere pozitive este:{numere_pozitive}')
# print(f'lista cu numere negative:{numere_negative}')


'''
2. Aceeași listă:
Ordonează crescător lista fară să folosești sort.
Te poți inspira vizual de aici. https://www.youtube.com/watch?v=lyZQPjUT5B4
'''

# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
#
# for i in range(len(alte_numere)):
#     for j in range(i+1, len(alte_numere)):
#         if alte_numere[i] > alte_numere[j]:
#             alte_numere[j], alte_numere[i] = alte_numere[i], alte_numere[j]
# print(alte_numere)

#3.
'''
 Ghicitoare de număr:
numar_secret = Generați un număr random între 1 și 30
Numar_ghicit = None
Folosind un while
User alege un număr
'''

# import random
#
# numar_secret=random.randint(1,30)
# numar_ghicit = None
#
# while numar_ghicit is None:
#     nr = int(input('Introduceti numarul:'))
#     if nr > numar_secret:
#         print('Numarul secret este mai mic')
#     elif nr < numar_secret:
#         print('Numarul secret este mai mare')
#     else:
#         print('Felicitari ati ghicit numarul')
#         break
#
'''
4. Alege un număr de la tastatură
Ex: 7
Scrie un program care să genereze în consolă următoarea piramidă
1
22
333
4444
55555
666666
7777777

Ex:3
1
22
333
'''

# nr = int(input('Scrie un numar:'))
# i = 1
#
# while i <= nr:
#     print('')
#     for j in range(i):
#         j = i
#         print(j, end ='')
#         j =  i + 1
#     i = i + 1

5.
# Iterează prin listă 2d
# Printează ‘Cifra curentă este x’ (hint: nested for - adică for în for)
# tastatura_telefon = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
# for i in range(len(tastatura_telefon)):
#     for j in range(len(tastatura_telefon[i])):
#         print(f'Cifra curenta este: {tastatura_telefon[i][j]}')
# sau cu for each
for row in tastatura_telefon:
    for column in row:
        print(f'FOR EACH: Cifra curenta este {column}')











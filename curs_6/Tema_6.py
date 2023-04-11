# 1.
'''
Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()

'''

class Cerc:

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare
        self.PI = 3.14

    def descrie_cerc(self):
        print(f'Raza cercului este: {self.raza}')
        print(f'Culoarea cercului este: {self.culoare}')

    def aria(self):
        aria = self.raza * self.raza *3.14
        return aria

    def diametru(self):
        diametru = self.raza * 2
        return diametru
    def circumferinta_cerc(self):
        circumferinta = 2 * 3.14 * self.raza
        return circumferinta

cer = Cerc(50, "Argintiu")
cer.descrie_cerc()
print(cer.raza)
print(cer.aria())
print(cer.circumferinta_cerc())


#2
'''
2. Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
'''


class Dreptunghi():

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere_dreptunhi(self):
        print(f'Dreptunghiul are lungimea {self.lungime} si latimea {self.latime}, iar culoarea {self.culoare}')

    def get_aria_dreptunghi(self):
        aria = self.lungime * self.latime



#3
#
'''
3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)
# '''
class Angajat:

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f'Numele anagajatului este {self.nume}')
        print(f'Prenumele anagajatului este {self.prenume}')
        print(f'Salariul anagajatului este {self.salariu}')

    def nume_complet(self):
        print(f'Numele meu este {self.nume} {self.prenume}')

    def salariu_lunar(self):
        print(f'Salariul meu lunar este {self.salariu}')

    def salariu_anual(self):
        salariu_anual = self.salariu * 12
        print(f'Salariul meu anual este: {salariu_anual} Ron')

    def marire_salariu(self):
        marire = 500
        marire_salariu =+ 500
        print(f'Marirea de salariu este de {marire_salariu} Ron ')

alin = Angajat ('Vaduva', 'Alin', 2500)
alin.descrie()
alin.salariu_lunar()
alin.salariu_anual()
alin.marire_salariu()
class Angajat:

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f'Numele anagajatului este {self.nume}')
        print(f'Prenumele anagajatului este {self.prenume}')
        print(f'Salariul anagajatului este {self.salariu}')

    def nume_complet(self):
        print(f'Numele meu este {self.nume} {self.prenume}')

    def salariu_lunar(self):
        print(f'Salariul meu lunar este {self.salariu}')

    def salariu_anual(self):
        salariu_anual = self.salariu * 12
        print(f'Salariul meu anual este: {salariu_anual} Ron')

    def marire_salariu(self):
        marire = 500
        marire_salariu =+ 500
        print(f'Marirea de salariu este de {marire_salariu} Ron ')

alin = Angajat ('Vaduva', 'Alin', 2500)
alin.descrie()
alin.salariu_lunar()
alin.salariu_anual()
alin.marire_salariu()



#4
'''
# 4.Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate atributele
# Metode:
# ● afisare_sold() - Titularul x are în contul y suma de n lei
# ● debitare_cont(suma)
# ● creditare_cont(suma)
'''


class Cont:

    def __init__(self, iban, titular_cont, sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold

    def descriere(self):
        print(f'IBAN-ul dumneavoastra este: {self.iban}')
        print(f'Numele titulatului al acestui cont este: {self.titular_cont}')
        print(f'Soldul dumneavoastra este: {self.sold}')

    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} !')

    def debitare_cont(self, suma):
        suma = 4000
        if suma >= self.sold:
            self.sold -= suma
        else:
            print('Fonduri insuficiente')

    def creditare_cont(self, suma):
        # suma = 700
        self.sold += sum
        print(f'Suma creditata in cont este {suma}')

beneficiar = Cont(122334, 'Alin', 200)
beneficiar.descriere()
debitare = Cont(122334, 'Alin', 4000)
debitare.afisare_sold()
creditare = Cont(122334, 'Alin', 700)
creditare.afisare_sold()


class Persoana:
    # nume = ""
    # prenume = "" daca scriu aceste atribute in acest fel la prnt nu va arata nimic ,
                   # insa daca incep cu constructorul __init__ , va fii obligat sa-mi dea valorile precizate.
    # age = 0
    def __init__(self,nume,prenume,age): # acest __init__ ne ajuta sa construim obiectul nostru
       self.nume = nume  ### self.nume =! (diferit de) nume (ca sa accesam field-urile clasei trebuie sa le sctiem cu self. inainte
       self.prenume = prenume
       self.age = age
# Constructorul ne ajuta sa dam valori, sa initializam variabilele,
# Cand avem None la atribute __init__ ne ajuta sa initializam aceste atribute sa le dam valori.

    '''
    Care este diferenta dintr-e o Functie si o metoda?:

    Functia - este chiar la inceput, indentata la stanga, nu detine nici o clasa acesta functie
    
    # In Clasa Persoana, daca definim o functie def prezentare(self): urmata de print. vezi in exemplu mai jos.
    - Acesta se numeste Metoda - care nu este decat o functie in interiorul unei calse.
    
    
    self-> daca sterg self. si voi avea doar nume fara self. nu voi avea nimic afisat,
     insa doar cand adaug self pot accesa field-urile unei calse. Va stii ca se refera la numele declarat.
    Ex self.nume = nume:   self.nume este total diferit != de nume.
    
    '''
    def prezentare(self):
       print(f' Salut, ma numesc {self.nume} {self.prenume}. Si am {self.age} ani')

    def get_vasrta_peste_10_ani (self):
        return self.age + 10


# Pentru a aapela functia prezentare - trebuie sa scriu  numele obiectului ., adaug numele metodei (functiei siu self)
# vali.prezentare()
# ##### Aiici vei vedea in bulinele galbene si roz:
# un 'f' care vine de la functie si un 'm' care vine de la metoda
'''
Scriu functia  vali.prezentare()\\\\ or alina.prezentare() ,
                asa o apelez -, si ii dau run -> fiecare apeleaza functia fiecare, cu valorile field-urilor lor 
*Aceasta este o metoda

Putem sa facem cate metode avem nevoie, nu avem o limita
EX :  def get_vasrta_peste_10_ani (self):
        return self.age + 10
        
        
 Ca sa o apelam ii dam print(alina.get_varsta_peste_10_ani())
'''
eu = Persoana('Vaduva', 'Alin', 37)
print(eu.prenume)

eu.prenume = 'Nicusor'
print(eu.prenume)

alina = Persoana('Dobrescu', 'Alina', 23)
print(alina.prenume)
alina.prenume = 'Dobrescu'
print(alina.nume)

eu.prezentare()
alina.prezentare()

print(alina.get_vasrta_peste_10_ani())


'''
Asa se acesteaza importul unei calse din alte fisiere
from folder.folder.fisier import nume_clasa

'''
# from Curs_6_Class import Persoana
from masina import Masina
# eu = Persoana('Vaduva', 'Alin', 37)
# eu.prezentare()

audi = Masina('A6', 'Audi')#Modelul masinii este Audi, marca A6 si are culoarea alb
audi.prezentare_masina()

bmw = Masina('BMW', '118D')
bmw.prezentare_masina()
bmw.culoare = 'negru'
bmw.prezentare_masina()

audi.accelereaza(50)
audi.start()
audi.accelereaza(50)
audi.accelereaza(30)
# print(audi.viteza)
audi.stop()
# print(audi.viteza)
audi.accelereaza(10)

audi.start()
audi.accelereaza(40)
audi.incetineste(30)
audi.incetineste(30)
audi.stop()
# audi.culoare='Verde' # Sunt destul de putine momente cand atribuim in acest fel unei valori
# dintr-o calse. Fiecare clasa are metodele ei, si e mai simplu este metoda de jos pentru un programator.
audi.vopseste('Verde')
print(audi.culoare)

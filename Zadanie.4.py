from math import *
import sys

class NaZakupy:
    nazwa="buła"
    ilosc=1
    miara="sztuka"
    koszt=2.30
    def __init__(self, nazwa, ilosc, miara, koszt):
        self.nazwa=nazwa
        self.ilosc=ilosc
        self.miara=miara
        self.koszt=koszt
    def wyswietl_produkt(self):
        print('nazwa ',self.nazwa)
        print("ilosc ",self.ilosc)
        print("miara ",self.miara)
        print("cena za sztukę ",self.koszt)
    def ile(self):
        print(self.nazwa," ",self.ilosc)
    def rachunek(self):
        print(self.koszt*self.ilosc)


Parówa=NaZakupy("Parówka",4,"sztuka",5)
print(Parówa)
Parówa.wyswietl_produkt()
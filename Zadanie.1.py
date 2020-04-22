from math import *
import sys

lista = []
for x in range(0,101,4):
    lista += [x]


plik = open("dane.txt","w")
plik.writelines(str(lista))
plik.close()

from math import *
import sys

with open("zadanie3.txt", "w") as plik:
    plik.write("costam fajnego")


with open("zadanie3.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")
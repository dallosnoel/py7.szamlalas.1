'''
1. Feladat
Készíts egy programot, amely [1;10] intervallumon generál 5 darab véletlen egész számot és ezeket tárolja el egy listában! A program számolja össze, és képernyőre írja ki a listában tárolt páros számok számát, valamint a lista elemeit!
'''

import random

lista = [random.randint(1, 10) for i in range(5) ]

paros_lista = [i for i in lista if i % 2 == 0]

print(f"Páros számok száma: {len(paros_lista)} ")
print(f"A lista elemei: {lista} ")
print(paros_lista)
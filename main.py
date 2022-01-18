'''
1. Feladat
Készíts egy programot, amely [1;10] intervallumon generál 5 darab véletlen egész számot és ezeket tárolja el egy listában! A program számolja össze, és képernyőre írja ki a listában tárolt páros számok számát, valamint a lista elemeit!
'''

import random
lista = []
paros_lista = []

for i in range(5):
  veletlen = random.randint(1, 10)
  lista.append(veletlen)

for x in lista:
  if x % 2 == 0:
    paros_lista.append(x)

print(f"Páros számok száma: {len(paros_lista)} ")
print(f"A lista elemei: {lista} ")
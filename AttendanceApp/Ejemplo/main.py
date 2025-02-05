#!/usr/bin/env python3

from personaje import Personaje
from guerrero import Guerrero
from mago import Mago

input('Bienvenido. Presione enter para continuar...')
goku = Personaje('Goku', 20, 15, 10, 100)
guts = Guerrero('Guts', 20, 15, 10, 100, 5)
vanessa = Mago('Vanessa', 20, 15, 10, 100, 5)

goku.atacar(guts)
guts.atacar(vanessa)
vanessa.atacar(goku)

goku.atributos()
print()
guts.atributos()
print()
vanessa.atributos()
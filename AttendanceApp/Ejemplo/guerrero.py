#!/usr/bin/env python3

from personaje import Personaje

class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiarArma(self):
        opcion = int(input('Elige un arma:\n (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10.'))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print('Número de arma incorrecto.')

    def atributos(self):
        super().atributos()
        print('-Espada:', self.espada)

    def daño(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa

"""
miGuerrero = Guerrero('Guts', 20, 10, 10, 100, 5)

miGuerrero.atributos()
miGuerrero.cambiarArma()
miGuerrero.atributos()
"""
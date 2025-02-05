#!/usr/bin/env python3



class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        self.sexo = 'Null'
        self.genero = 'Null'
        self.aguante = fuerza * vida
        self.turno = False

    def atributos(self):
        print(self.nombre, ':', sep='')
        print('-Fuerza:', self.fuerza)
        print('-Inteligencia', self.inteligencia)
        print('-Defensa:', self.defensa)
        print('-Vida:', self.vida)

    def oneAttribute(self, atributo:str):
        #print(getattr(mi_personaje, 'fuerza'))
        print(getattr(self, atributo))

    def subirNivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def estaVivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, 'ha muerto, gracias por jugar.')

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, 'ha realizado', daño, 'puntos de daño a', enemigo.nombre)
        if enemigo.estaVivo():
            print('La vida de', enemigo.nombre, 'es', enemigo.vida)
        else:
            enemigo.morir()

    def getFuerza(self):
        return self.fuerza
    
    def setFuerza(self, fuerza):
        if fuerza < 0:
            print('Error: introdujo un valor negativo')
        else:
            self.fuerza = fuerza

"""
miPersonaje = Personaje('H4K0', 10, 10, 10, 100)
personajito = Personaje('Muñeco', 1, 1, 1, 8)

print(miPersonaje.getFuerza())
miPersonaje.setFuerza(-20)
print(miPersonaje.getFuerza())
"""
#!/usr/bin/env python3



class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida
        self.__sexo = 'Null'
        self.__genero = 'Null'
        self.__aguante = fuerza*vida
        self.__turno = False

    def atributos(self):
        print(self.__nombre, ':', sep='')
        print('-Fuerza:', self.__fuerza)
        print('-Inteligencia', self.__inteligencia)
        print('-Defensa:', self.__defensa)
        print('-Vida:', self.__vida)

    def oneAttribute(self, atributo:str):
        print(getattr(self, atributo))
        #print(getattr(mi_personaje, 'fuerza'))

    def subirNivel(self, fuerza, inteligencia, defensa):
        self.__fuerza = self.__fuerza + fuerza
        self.__inteligencia = self.__inteligencia + inteligencia
        self.__defensa = self.__defensa + defensa

    def estaVivo(self):
        return self.__vida > 0

    def __morir(self):
        self.__vida = 0
        print(self.__nombre, 'ha muerto, gracias por jugar.')

    def daño(self, enemigo):
        return self.__fuerza - enemigo.__defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.__vida = enemigo.__vida - daño
        print(self.__nombre, 'ha realizado', daño, 'puntos de daño a', enemigo.__nombre)
        if enemigo.estaVivo():
            print('La vida de', enemigo.__nombre, 'es', enemigo.__vida)
        else:
            enemigo.__morir()

    def getFuerza(self):
        return self.__fuerza
    
    def setFuerza(self, fuerza):
        if fuerza < 0:
            print('Error: introdujo un valor negativo')
        else:
            self.__fuerza = fuerza

miPersonaje = Personaje('H4K0', 10, 10, 10, 100)
personajito = Personaje('Muñeco', 1, 1, 1, 8)

print(miPersonaje.getFuerza())
miPersonaje.setFuerza(-20)
print(miPersonaje.getFuerza())




""" 
miPersonaje.sexo = input('¿Cuál es el sexo del personaje? ')

miPersonaje.subirNivel(5,10, 15)
personajito.subirNivel(1,1, 10)

miPersonaje.oneAttribute('fuerza')
personajito.oneAttribute('fuerza')

personajito = Personaje('Muñeco', 1, 1, 1, 3)

print(miPersonaje.estaVivo())
print(personajito.estaVivo())

personajito.morir()
personajito.getAtributos()

print(miPersonaje.daño(personajito))
miPersonaje.atacar(personajito)
personajito.getAtributos()

Python no tiene atributos ni métodos privados. TODOS son públicos.
Así se accede a los método o atributos __ :
    miPersonaje._Personaje__fuerza = -5
    miPersonaje.atributos()
    miPersonaje._Personaje__morir()



"""
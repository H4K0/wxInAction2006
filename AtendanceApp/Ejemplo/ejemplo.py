#!/usr/bin/env python3

class Personaje:
    nombre = 'Default'
    sexo = 'Null'
    genero = 'Null'
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0

mi_personaje = Personaje()

mi_personaje.nombre = input("¿Cuál es el nombre del personaje? ")


print("El nombre de mi personaje es ", mi_personaje.nombre)
print("El sexo de mi personaje es ", mi_personaje.sexo)
print("El genero de mi personaje es ", mi_personaje.genero)
print("La fuerza de mi personaje es ", mi_personaje.fuerza)
print("La inteligencia de mi personaje es ", mi_personaje.inteligencia)
print("La defensa de mi personaje es ", mi_personaje.defensa)
print("La vida de mi personaje es ", mi_personaje.vida)
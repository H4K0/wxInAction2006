#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-
# Original example:
#  https://pythones.net
# Now on: 
#  www.github.com/H4k0/GP/wxInAction2006
#

'''
También podemos hacerlo, utilizando super(). De esta forma es casi el mismo código
pero no necesitamos especificar la clase padre, por lo que podremos cambiarle el
nombre en cualquier momento y nuestro código seguirá funcional, fíjate:
'''

class Padre(object): #Creamos la clase Padre
    def __init__(self, ojos, cejas): #Definimos los Atributos
        self.ojos = ojos
        self.cejas = cejas
        
class Hijo(Padre): #Creamos clase hija que hereda de Padre
    def __init__(self, ojos, cejas, cara): #creamos el constructor de la clase especificando atributos
        super().__init__(ojos, cejas)#Solicitamos a super llamar de la clase padre esos atributos
        self.cara = cara #Especificamos el nuevo atributo para Hijo
        
Tomas = Hijo('Marrones', 'Negras', 'Larga')
print (Tomas.ojos, Tomas.cejas, Tomas.cara)
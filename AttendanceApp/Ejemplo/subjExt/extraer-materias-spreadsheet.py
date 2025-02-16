#!/usr/bin/env python3

import openpyxl
import os.path

myPath = 'AttendanceApp/Ejemplo/strg/9° A.xlsx'
filas = ['B','C','D','E','F','G','N','P','R','T','V','X','Z','AB','AD','AF','AH','AJ','AL','AN','AP','AR','AT','AV']
filasImp = ['D','N','P','R','T','V','X','Z','AB','AD','AF','AH','AJ','AL','AN','AP','AR','AT','AV']
sl = ['Álgebra', 'Arts', 'Biology', 'Citizenship', 'Computer Science', 'Desarrollo Humano', 'English', 'Estadística', 'Filosofía', 'Física', 'Geography', 'Geometría', 'Historia', 'Lenguaje', 'Ortografía', 'Physical Education', 'Química']
columnas = [9, 67]
superior = []
paso =[]
alto = []
bajo = []
superior_fin = ""
alto_fin = ""
bajo_fin = ""

if os.path.isfile(myPath):
    print('.:. Archivo encontrado .:.')
else:
    print('El archivo no debe ser creado.')
    exit(1)

wb = openpyxl.load_workbook(filename=myPath)

sheet = wb.active
entrada = wb['Hoja1']
salida = wb['Salida']

for j in range(columnas[0], columnas[1], 4):
    temp = []
    for i in filasImp:
        k = str(entrada[i+str(j)].value) if entrada[i+str(j)].value is not None else ""
        temp.append(k)
    paso.append(temp)

print(paso)

wb.save(filename=myPath)
wb.close
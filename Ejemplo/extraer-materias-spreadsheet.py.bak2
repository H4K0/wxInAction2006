#!/usr/bin/env python3

import os.path
import openpyxl
from openpyxl.styles import Font
from openpyxl.styles import Alignment

myPath = 'Ejemplo/strg/9° A.xlsx'
print("Ruta absoluta de myPath:", os.path.abspath(myPath))

filas =     ['B','C','D','E','F','G','N','P','R','T','V',
            'X','Z','AB','AD','AF','AH','AJ','AL','AN',
            'AP','AR','AT','AV'
            ]
filasImp =  ['D','N','P','R','T','V','X','Z','AB','AD',
            'AF','AH','AJ','AL','AN','AP','AR','AT'
            ]
sl =        ['','Álgebra', 'Arts', 'Biology', 'Citizenship', 'Computer Science',
            'Desarrollo Humano', 'English', 'Estadística', 'Filosofía', 'Física',
            'Geography', 'Geometría', 'Historia', 'Lenguaje', 'Ortografía',
            'Physical Education', 'Química'
            ]
columnas = [10, 77]
paso =[]

if os.path.isfile(myPath):
    print('.:. Archivo encontrado .:.')
else:
    print('El archivo no debe ser creado.')
    exit(1)

wb = openpyxl.load_workbook(filename=myPath)

sheet = wb.active
entrada = wb['Hoja1']
#Si salida existe, asignarla, de lo contrario crearla.
salida = wb['Salida']


for j in range(columnas[0], columnas[1], 4):
    temp = []
    for i in filasImp:
        k = str(entrada[i+str(j)].value) if entrada[i+str(j)].value is not None else ""
        temp.append(k)
    paso.append(temp)

for i in range(len(paso)):
    print(paso[i])
#print(len(paso))
###################
###################
#print(len(paso))


salida['A1'] = 'ESTUDIANTE'
salida['B1'] = 'BAJO'
salida['C1'] = 'ALTO'
salida['D1'] = 'SUPERIOR'

salida['A1'].font = Font(bold = True)
salida['B1'].font = Font(bold = True)
salida['C1'].font = Font(bold = True)
salida['D1'].font = Font(bold = True)

salida.column_dimensions['A'].width = 20
salida.column_dimensions['B'].width = 30
salida.column_dimensions['C'].width = 30
salida.column_dimensions['D'].width = 30

for l in range(0, len(paso)):
    superior_fin = ""
    alto_fin = ""
    bajo_fin = ""
    
    nt = paso[l]

    superior = []
    alto = []
    bajo = []

    for i in range(1,18):
        m = nt[i].replace(",",".")
        nt[i] = float(m)
        if nt[i] <= 2.9:
            bajo.append(sl[i])
        if nt[i] >= 3.8 and nt[i] <= 4.49:
            alto.append(sl[i])
        if nt[i] >= 4.5:
            superior.append(sl[i])

    for i in range(len(bajo)):
        if i == len(bajo)-1:
            bajo_fin = bajo_fin + bajo[i] + "."
        else:
            bajo_fin = bajo_fin + bajo[i] + ", "

    for i in range(len(alto)):
        if i == len(alto)-1:
            alto_fin = alto_fin + alto[i] + "."
        else:
            alto_fin = alto_fin + alto[i] + ", "

    for i in range(len(superior)):
        if i == len(superior)-1:
            superior_fin = superior_fin + superior[i] + "."
        else:
            superior_fin = superior_fin + superior[i] + ", "

    print("Bajo: " + bajo_fin)
    print("Alto: " + alto_fin)
    print("Superior: " + superior_fin)
    print('##########################')
    salida[f'A{l+2}'] = nt[0]
    salida[f'B{l+2}'] = bajo_fin
    salida[f'C{l+2}'] = alto_fin
    salida[f'D{l+2}'] = superior_fin
    
    salida[f'B{l+2}'].alignment = Alignment(wrap_text = True)
    salida[f'C{l+2}'].alignment = Alignment(wrap_text = True)
    salida[f'D{l+2}'].alignment = Alignment(wrap_text = True)



###################
###################

wb.save(filename=myPath)
wb.close
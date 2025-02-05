#!/usr/bin/env python3

import openpyxl
import os.path

#Create a workbook
if os.path.isfile('strg/9° A.xlsx'):
    print('El archivo ya existe no se sobreescribirá.')
    pass
else:
    print('El archivo no debe ser creado.')
    exit()

wb = openpyxl.load_workbook(filename='strg/9° A.xlsx')
print(wb.sheetnames)

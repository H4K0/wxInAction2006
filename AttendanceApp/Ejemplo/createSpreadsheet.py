#!/usr/bin/env python3

import openpyxl

ssBook = openpyxl.Workbook()
sheet = ssBook.active

data = [
    ('Nombre', 'Edad', 'Compañía'),
    ('John', 21, 'Facebook'),
    ('Hannah', 21, 'Apple'),
    ('Camila', 27, 'Toyota'),
    ('Steve', 32, 'Google')
]

for i, j in enumerate(data):
    sheet[f'A{i+1}'] = j[0]
    sheet[f'B{i+1}'] = j[1]
    sheet[f'c{i+1}'] = j[2]

ssBook.save('strg/ssFile.xlsx')
ssBook.close
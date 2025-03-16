#!/usr/bin/env python3
from openpyxl.utils import get_column_letter

n = 0
estado = "Positivo" if n > 0 else "Negativo" if n < 0 else "Cero"
print(estado)



celdas_en_negrita = hoja_tres["A1":"D1"]
fuente = Font(bold=True)


for row in celdas_en_negrita:
    for cell in row:
        cell.font = fuente
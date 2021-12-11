# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 08:59:10 2021

@author: Jheronimo
"""

nombre=str(input("Ingrese el nombre del obrero:    "))
valor=int(input("Ingrese el valor pagado por hora:  "))
horas=int(input("Ingrese el numero de horas trabajadas "))

Valor_final= valor*horas

print()
print("El valor total a pagar al obrero", nombre, "es", Valor_final)
print("Jerónimo Bedoya")
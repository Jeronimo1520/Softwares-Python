# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 08:25:45 2021

@author: Jheronimo
"""

nombre=str(input("Ingrese el nombre del estudiante:    "))
nota1=float(input("Ingrese la primera nota  "))
nota2=float(input("Ingrese la segunda nota  "))
nota3=float(input("Ingrese la tercera nota  "))
nota4=float(input("Ingrese la cuarta nota   "))
nota5=float(input("Ingrese la quinta nota   "))


nota_Final = nota1 * 0.20 + nota2 * 0.20 + nota3 * 0.20 + nota4 * 0.20+ nota5 *0.20
#correccion = (nota1+nota2+nota3+nota4+nota5)/5

print()
print("La nota final del estudiante ", nombre, "es", nota_Final)


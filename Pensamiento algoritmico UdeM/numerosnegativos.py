# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 09:01:46 2021

@author: jeron
"""

N=int(input("Ingrese la cantidad de numeros : "))

contador=1
connegat=0

while contador <= N:
    numero=int(input("Ingrese numero"))
    if numero <0:
        connegat=connegat+1
    #endif
    contador=contador+1
#endwhile
print("Se leyeron ", N ,"numeros, de los cuales ", connegat, "Son negativos")
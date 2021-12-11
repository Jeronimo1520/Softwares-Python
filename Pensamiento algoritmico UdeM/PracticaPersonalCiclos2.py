# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 20:55:52 2021

@author: jeron
"""

Ningresados=int(input("Cuantos numeros va a validar? "))
cont=0
contpares=0
contimpares=0

while cont < Ningresados:
    N=int(input("Ingrese numero a validar: "))
    
    if N % 2 == 0:
        contpares=contpares+1
    else:
        contimpares=contimpares+1
    #endif
    cont=cont+1
#endWhile

print("Los numeros pares son: ",contpares)
print("Los numeros impares son: ",contimpares)
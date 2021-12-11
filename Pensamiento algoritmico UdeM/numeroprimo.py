# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 09:22:00 2021

@author: jeron
"""

N=int(input("Ingrese un numero: "))

primo="si"
cont=2
while cont < N and primo=="si":
    if N % cont ==0:
        primo="no"
    #endif
    print(cont,"", primo)
    cont=cont+1
#endwhile
if primo == "si":
    print("El numero ",N, "Es primo")
else:
    print("El numero ",N, "No es primo")
    
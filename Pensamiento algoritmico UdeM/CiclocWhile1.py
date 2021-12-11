# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 19:02:32 2021

@author: Jheronimo
"""

total=0
contador=1
cont1=0
cont2=0
n=int(input("Ingrese el numero de casas: "))

while contador <= n:
    estrato=int(input("ingrese su estrato: "))
    nrkv=int(input("Ingrese su numero de kilovatios:" ))
    
    if estrato <= 3:
        vlrkv=1000
        cont1=cont1+1
    else:
        vlrkv=2000
        cont2=cont2+1
    #endif
    
    pago = vlrkv * nrkv
    total=total + pago
    contador=contador+1
#endWhile
print()
print("El total recaudado es: ", total)
print("El numero de casas iguales o menores a estrato 3 son: ", cont1)
print("El numero de casas mayores a estrato 3 son: ", cont2)

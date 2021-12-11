# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 09:02:12 2021

@author: jeron
"""
#ejercicio1 buses

n=int(input("Ingrese el numero de tiempos de rutas: "))
a=[0]*n

import random

for i in range(0,n,1):
    a[i]=(random.randint(0,100))

for i in range(0,n):
    print(a[i],end=" ")
    
sum=0
for i in range(0,n):
    sum=sum+a[i]
#endforsum
print()
prom=round(sum/n,2)
print ("El promedio de los elementos del Vector es   ",prom )

tiemposMoI=0
for i in range(0,n):
    if a[i]>=prom:
        tiemposMoI+=1
print("EL numero de tiempos que son mayores o iguales al promedio son: ", tiemposMoI)
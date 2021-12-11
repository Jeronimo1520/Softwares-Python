# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 09:06:07 2021

@author: jeron
"""

N=int(input("Ingrese cantidad de numeros: "))
connum=1
conprim=0
sumapri=0
while connum <= N:
    nro=int(input("Ingrese un numero: "))
    primo=True
    i=2
    while i < nro and primo==True:
      if nro % i ==0:
        primo=False
      #endif
      i=i+1
    if primo == True:
        conprim=conprim+1
        sumapri=sumapri+nro
    #endif
    connum=connum+1
#endwhile
print("La suma de los  ",conprim,"numeros primos es ",sumapri)

    

    
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 08:57:03 2021

@author: jeron
"""

def ejercicio1():
    import random
    n=int(input("Ingrese númeo de elementos del vector "))
    vec=[0]*n
    def llenarvector(v,w):
        for i in range (0,w,1):
            v[i]=random.randint(1,100)
        #endfor
        return
    #endllenarvector
    
    def imprimirvector(v,w):
        for i in range (0,w,1):
            print (v[i], end=" ")
        #endfor
        return
    #endimprimivector
    
    def promedio(v,w):
        acum=0
        for i in range (0,w,1):
            acum=acum+v[i]
        #endfor
        prom = round(acum/n,2)
        return prom
    def menores(v,w):
        acumen=0
        for i in range(0,w,1):
            if v[i]<5:
                acumen+=1
            #endif
        #endfor
        return acumen
    def elementos(v,w):
        mayor=v[0]
        menor=v[0]
        for i in range(0,w,1):
            if v[i]>mayor:
                mayor=v[i]
            #endif
            if v[i]<menor:
                menor=v[i]
            #endif
        #endfor
        print("EL numero mayor es: ",mayor)
        print("EL numero menor es: ",menor)

    
    c=str(input("Presione enter para imprimir el vector inializado"))
    imprimirvector(vec,n)
    c=str(input("Presione enter para llenar el vector"))
    llenarvector(vec,n)
    c=str(input("Presione enter para imprimir el vector con los valores ingresados"))
    imprimirvector(vec,n)
    c=str(input("Presione enter para calcular el promedio"))
    x=promedio(vec,n)
    print("El promedio de los elementos del vector es ",x)
    c=str(input("Presione enter para calcular los numeros menores a 5"))
    y=menores(vec,n)
    print("Los numeros menores a 5 son", y)
    c=str(input("Presione enter para calcular el numero mayor y menor"))
    elementos(vec, n)

    
    
ejercicio1()
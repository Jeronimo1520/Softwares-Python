# -*- coding: utf-8 -*-
"""
Created on Fri May 21 07:55:30 2021

@author: jeron
"""

def principal():
    import random
    m=int(input("Ingrese la cantidad de FILAS a procesar......:"))
    n=int(input("Ingrese la cantidad de COLUMNAS a procesar...:"))
    a=[]
    for i in range(0,m,1):
        a.append([0]*n)
    #endfor
    vec=["??"]*m
    
    def LlenarMatriz(ma,z,w):
        for i in range(0,z):
            vec[i]=str(input(f"Ingrese nombre del vendedor{i+1}  "))
            for j in range(0,w):
                ma[i][j] = random.randint(100,1000);
            #endfor
        #endfor
        return
    def ImprimirMatriz(ma,z,w):
        for i in range(0,z):
            print()
            print(vec[i],'\t',end="  ")
            for j in range(0,w):
                print(ma[i][j],'\t',end="")
        return
    def totalComisiones(ma,z,w):
        for i in range(0,m,1):
                acufila=0
                vendedor=""
                for j in range(0,n,1):
                    acufila=acufila+ma[i][j]  
                #endfor
                vendedor+=vec[i]
                print("El total de comisiones del vendedor: ",vendedor,"es: ",acufila)
        #endfori
        return       
    def comisionesDias(ma,z,w):
        mayordia=0
        dia=0
        for j in range(0,w):
            acumdia=0
            for i in range(z):
                acumdia+=a[i][j]
            #endfor
            if acumdia>mayordia:
                mayordia=acumdia
                dia=j+1
            print()
            print(f"El  total del dia: {j+1} es",acumdia)
        print()
        print("El dia con mayor ventas es el:",dia,"con un total de:",mayordia)
        return
    
    def totalempresa(ma,z,w):
        summatriz=0
        for i in range(0,z):
            for j in range(0,w):
                summatriz=summatriz+ma[i][j]
        return summatriz
    print()
    print ("MATRIZ INICIALIZADA")
    ImprimirMatriz(a,m,n)
    c=str(input("Presione enter para continuar...:"))
    LlenarMatriz(a,m,n)
    print()
    print("MATRIZ ORIGINAL")
    ImprimirMatriz(a,m,n)
    print()
    totalComisiones(a,m,n)
    print()
    comisionesDias(a,m,n)
    print()
    x=totalempresa(a,m,n)
    print("El total de comisiones de cada vendedor son")
    totalComisiones(a,m,n)
    print("Y el total de comisiones pagadas son: ",x)
principal()
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 08:11:26 2021

@author: jeron
"""
"""leer los nombres de los M estudiantes del grupo y guardarlos. Por cada estudiante leer , las 4 notas de la asignatura arreglos paralelos

se desea mostrar en pantalla
1. vector y matriz inicializado
2. inicilizar los vectores con los nombres y las notas.Pueden geenrar numeros aleatorios
3.Mostrar el nombre de los estudiante y las notas definitivas de cada uno
4.promedio general y estudiantes que perdieron
"""

import random
m=int(input("Ingrese la cantidad de FILAS a procesar......:  "))
n=int(input("Ingrese la cantidad de COLUMNAS a procesar...:  "))
mat=[]
for i in range(0,m):
    mat.append([0]*n)
#endfor
vec=["??"]*m

for i in range(0,m,1):
    print()
    print(vec[i],'\t',end="  ")
    for j in range(0,n,1):
            print(mat[i][j], '\t',end=" ")     
     #endfor
 #endfor
c=str(input("Presione enter para llenar los arreglos  "))
            
for i in range(0,m,1):
    vec[i]=str(input(f"Ingrese nombre del estudiante {i+1}  "))
    for j in range(0,n,1):
        mat[i][j]=round(random.random()*5,2)  
                                      

    #endfor
 #endfor
for i in range(0,m,1):
    print()
    print(vec[i],'\t',end="  ")
    for j in range(0,n,1):
            print(mat[i][j], '\t',end=" ")     
     #endfor
print()

acumdefin=0
for i in range(0,m,1):
    acufila=0
    for j in range(0,n,1):
        acufila=acufila+mat[i][j]     
    #endfor
    defin= round(acufila/n,2)
    acumdefin+=defin
    print  ("La nota definitiva del estudiante ",vec[i], " es ", defin)
    promgeneral=round(acumdefin/m,2)
 #endfor
print("Acumulado def:", acumdefin)
print("El promedio general es:", promgeneral)
 



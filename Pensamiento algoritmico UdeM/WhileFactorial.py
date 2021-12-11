# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 08:18:13 2021

@author: jeron
"""
#"Leer N numeros y mostrar el factorial de cada uno de ellos"
N=int(input("Ingrese cantidad de numeros a calcular su factorial   "  ))
i=1
while i <= N:
    nro = int (input("Ingrese numero    "))
    con=1
    fact=1
    while (con <= nro):
        fact=fact*con
        con=con+1
    #endwhile
    print ("El factorial de ",nro, " es ", fact)
    i=i+1
#endwhile

#endwhile
    

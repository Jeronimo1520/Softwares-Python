# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 20:44:15 2021

@author: jeron
"""

total=0
monto=float(input("Ingrese monto de una venta: "))

while monto !=0:
    if monto < 0:
        print("Monto no valido")
    else:
        total=total+monto
    #endif
    monto=float(input("Ingrese monto de una venta: "))
#endWhile
if total > 1000:
    total=total-(total*0.1)
print("EL monto total a pagar es:", total)
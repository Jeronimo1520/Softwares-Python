# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 08:31:21 2021

@author: Jheronimo
"""

estrato=int(input("ingrese estrato: "))
m3consumidos=int(input("ingrese metros cubicos consumidos: "))
cargofijo1=25000
cargofijo2=42000

if estrato <=3:
    consumo= m3consumidos*2000+cargofijo1
else:
    consumo=m3consumidos*3500+cargofijo2
#endif

if estrato <=3:
    impuesto = int(consumo*0.05)
else:
    impuesto = int(consumo*0.07)
#endif


if estrato >=4:
    m3extras=m3consumidos-50
    recargo=m3extras*1000
else:
    m3extras=0
    recargo=0
#endif
    
pagototal=int(consumo+impuesto+recargo)

print()
print("Su consumo es: ", consumo)
print("Su impuesto es de: ", impuesto)
print("Su recargo es de :", recargo)
print("Su totol a pagar es: ", pagototal)
print("Practica hecha por Jerónimo Bedoya B")

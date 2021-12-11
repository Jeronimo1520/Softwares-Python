# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 09:32:26 2021

@author: Jheronimo
"""

nombre=str(input("Ingrese su nombre: "))
pago_dia=int(input("Ingrese su pago por dia: "))
ndias=int(input("Ingrese el numero de dias trabajados: "))

totalpagos= pago_dia*ndias

if totalpagos < 2000000:
    dsso =0.0774
else:
    dsso=0.10
#endif

dsso_total= int(totalpagos*dsso)

if totalpagos < 1000000:
    retencion= 0
else:
   if totalpagos <= 3000000:
        retencion= 0.05
   else:
     if totalpagos <= 5000000:
        retencion= 0.07
     else:
       retencion = 0.09
#endif #endif #endif

retencion_total = totalpagos * retencion
totaldeducciones= int(dsso_total + retencion_total)
netorecibido = totalpagos - totaldeducciones

print()
print("Su nombre es: ", nombre)
print("Su total de pagos es: ", totalpagos)
print("Sus deducciones de seguridad social son: ", dsso_total)
print("Sus deducciones por retencion en la fuente es ", retencion_total)
print("Su total de deducciones es: ", totaldeducciones)
print("Su neto recibido es: ", netorecibido)


# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 15:49:59 2021

@author: Jheronimo
"""

nombre=str(input("Ingrese su nombre: "))
ValorHoraDiurna=int(input("Ingrese el valor de la hora diurna: "))
HoraDiurna=int(input("Ingrese las horas diurnas trabajadas: "))
HoraNocturna=int(input("Ingrese las horas nocturnas trabajadas: "))
HorasFestivas=int(input("Ingrese las horas festivas trabajadas: "))
HorasExDiurna=int(input("Ingrese las horas extras diurnas trabajadas: "))
HorasExNocturnas=int(input("Ingrese las horas extras nocturnas trabajadas: "))
HorasExFestivas=int(input("Ingrese las horas extras festivas trabajadas: "))


 
PagoHoraNormal=int(ValorHoraDiurna * HoraDiurna)
PagoHoraNocturna=int(HoraNocturna * ValorHoraDiurna* 1.35)
PagoHoraFestiva=int(HorasFestivas * ValorHoraDiurna *2)
PagoHoraExDiurna=int(HorasExDiurna * ValorHoraDiurna*1.25)
PagoHoraExNocturna=int(HorasExNocturnas * ValorHoraDiurna*1.75)
PagoHoraExFestiva=int(HorasExFestivas* ValorHoraDiurna *2.25  )

totalpagos= PagoHoraNormal+PagoHoraNocturna+PagoHoraFestiva+PagoHoraExDiurna+PagoHoraExNocturna+PagoHoraExFestiva 


if totalpagos > 1000000:
    retencion= totalpagos*0.5
else:
    retencion = 0
#endif

dedsegsoc= int(totalpagos * 0.074)
totaldeducciones=int(dedsegsoc+retencion)
netoarecibir= int(totalpagos -totaldeducciones)

print()
print("Nombre del trabajador: ", nombre)
print("Su pago por horas diurnas es:  ", PagoHoraNormal)
print("Su pago por horas nocturnas es:  ", PagoHoraNocturna)
print("Su pago por horas festivas es: ",  PagoHoraFestiva)
print("Su pago por horas extras diurnas es: ",  PagoHoraExDiurna)
print("Su pago por horas extras nocturnas es: ", PagoHoraExNocturna)
print("Su pago por horas extras festivas es: ", PagoHoraExFestiva)
print("Su total de pagos es: ", totalpagos)
print("Deducciones por seguridad social son: ", dedsegsoc)
print("Si sus ingresos son mayores a 1000000 se le retendra 5% en la fuente")
print("El neto que recibe es: ", netoarecibir)
print("Practica hecha por Jeronimo Bedoya B")

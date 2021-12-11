# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 11:59:19 2021

@author: Jheronimo
"""

nombre=str(input("Ingrese el nombre del estudiante "))
seg1_1=float(input("Ingrese la nota uno del primer seguimiento "))
seg1_2=float(input("Ingrese la nota dos del segundo seguimiento "))
parcial=float(input("Ingrese la nota del parcial "))
seg2_1=float(input("Ingrese la nota uno del segundo seguimiento "))
seg2_2=float(input("Ingrese la nota dos del segundo seguimiento "))
seg2_3=float(input("Ingrese la nota tres del segundo seguimiento "))
final=float(input("Ingrese la nota del final"))

seguimiento1=(seg1_1*0.125+seg1_2*0.125)/0.25
seguimiento2=(seg2_1*0.10+seg2_2*0.05+seg2_3*0.10)/0.25

definitiva=(seguimiento1+seguimiento2+parcial+final)/4

if definitiva<3:
    estado= "reprobado"
else:
    estado= "aprobado"
    
print()
print("Nombre", nombre)
print("Seguimiento1: ", seguimiento1)
print("Seguimiento2: ",seguimiento2)
print("parcial: ", parcial)
print("final: ",final )
print("definitiva es: ",definitiva )
print("estado: ",estado)

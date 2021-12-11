# -*- coding: utf-8 -*-

nombre=str(input("Ingrese nombre del estudiante:   "))
d=float(input("ingrese el numero 1                 "))
c=float(input("ingrese el numero 2                 "))

e = d//c #div
f = d % c #mod
g = d/c #division
g = round (g,2) #redondear
h = d ** c; #potencia
i = d + c
j = d - c
k = d * c

print()
print("la potencia de                ", d, "a la  ", c, " es ", h)
print("la division entera de         ", d, "en    ", c, " es ", e)
print("El residuo de la division de  ", d, "en    ", c, " es ", f)
print("La divison normal de          ", d, "en    ", c, " es ", g)
print("la suma de                    ", d, "mas   ", c, " es ", i)
print("La resta de                   ", d, "menos ", c, " es ", j)
print("El producto de                ", d, "por   ", c, " es ", k)
print()
print("Practica realizada por       ", nombre)
    
    
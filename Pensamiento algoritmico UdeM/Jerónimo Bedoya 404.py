# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 11:28:02 2021

@author: jeron
"""

n=int(input("Ingrese numero de aspirantes: "))
congen=1
conmuj=0
conhom1620=0
conpub=0
conpar=0
confuemed=0
conhommed=0

while congen <= n:
    
 nombre=str(input("Ingrese el nombre: "))
 edad=int(input("Ingrese la edad: "))
 colegio=int(input("Ingrese la procendencia del colegio, 1:particular, 2:publico: "))
 sexo=int(input("Ingrese el sexo, 1:Femenino, 2:Masculino: "))
 ciudad=int(input("Ingrese el origen de la ciudad, 1:Medellin, 2:Otras ciudades: "))
 
 if sexo == 1:
     conmuj=conmuj+1
 else:
     if edad >= 16 and edad <=20:
         conhom1620= conhom1620+1
     #endif
     if ciudad == 1:
         conhommed= conhommed+1
     #endif
 #endif
 if ciudad == 2:
	 confuemed= confuemed+1
 #endif
 if colegio == 1:
	  conpar= conpar+1
 else:
     conpub=conpub+1
 #endif
 congen=congen+1
#finMQ

pormuj=	conmuj*100/n
porhom1620=	conhom1620*100/n
porfuemed=	confuemed*100/n
porhommed= 	conhommed*100/n

if conpar >conpub:
    print("El mayor numero de aspirantes es de colegio particular")
else:
    if conpub> conpar:
        print("El mayor numero de aspirantes es de colegio público")
    else:
        print("el numero de A. de particulares es iguaL al de A.de publicos")
    #endif
#endif

print("	El porcentaje de aspirantes del sexo femenino es: ", pormuj)
print("	El porcentaje de aspirantes masculinos con edades entre 16 y 20 años es: ", porhom1620)
print("	El porcentaje de aspirantes de fuera de Medellín es: ", porfuemed)
print("	El porcentaje de aspirantes masculinos de la ciudad de Medellín es: ",porhommed)
     
     
     


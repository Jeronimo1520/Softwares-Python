# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 09:44:04 2021

@author: Jheronimo
"""

contraseña=str(input("Ingrese la contraseña:  "))

if contraseña == ("gato"):
    print("Coincide")
else:
    print("No coincide")
#endif
N1=int(input("Ingrese el primer numero:  "))
N2=int(input("Ingrese el segundo numero: "))

if N2 == 0:
    print("ERROR")
else:
    print("el resultado es: ",(N1/N2))
#endif
    
  
letra=str(input("Ingrese una vocal:  ")).lower()
  
if letra == ("a") or letra == ("e") or letra == ("i") or letra == ("o") or letra == ("u"):
      print("Su letra es una vocal")
else:
    print("Su letra no es una vocal")
#endif
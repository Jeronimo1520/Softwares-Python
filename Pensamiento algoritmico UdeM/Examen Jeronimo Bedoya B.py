# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 08:04:13 2021

@author: jeron
"""

Ngrupos=int(input("Ingrese el numero de grupos de pensamiento algoritmico: "))
contN=1
PromedioFacu=0
EstPerdidosFacu=0
mejorNotaFacu=0
AcumPromedio=0
while contN<=Ngrupos:
    codigo=int(input(f"Ingrese el codigo del grupo {contN}:"))
    Nestudiante=int(input(f"Ingrese el numero de estudiantes del grupo {codigo}:"))
    print("Grupo: ", codigo, "Estudiantes: ", Nestudiante)
    promedioGrupo=0
    AcumNotas=0
    EstPerdidosGrupo=0
    mejorNotaGrupo=0
    contEstudiantes=1
    while contEstudiantes<=Nestudiante:
        nota=float(input(f"Ingrese la nota del estudiantes {contEstudiantes}:"))
        AcumNotas=AcumNotas+nota
        if nota < 3:
            EstPerdidosGrupo=EstPerdidosGrupo+1
        if nota >=mejorNotaGrupo:
            mejorNotaGrupo=nota
        contEstudiantes=contEstudiantes+1
    #endwhile
        if mejorNotaGrupo>mejorNotaFacu:
            mejorNotaFacu=mejorNotaGrupo
        promedioGrupo=AcumNotas/Nestudiante
        AcumPromedio=AcumPromedio+promedioGrupo
    print("Grupo: ",codigo,"Promedio grupal: ",promedioGrupo,"Estudiantes que perdieron: ",EstPerdidosGrupo,"La mejor nota es: ",mejorNotaGrupo)
    contN=contN+1
#endwhile
    PromedioFacu=(AcumPromedio/Ngrupos)
    EstPerdidosFacu=EstPerdidosFacu+EstPerdidosGrupo
    

print("Promedio facultad :",PromedioFacu,"Estudiantes que perdieron totales: ",EstPerdidosFacu,"Mejor nota facultad es :",mejorNotaFacu)
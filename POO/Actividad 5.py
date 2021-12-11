from statistics import median_grouped
class Estudiante:

    SIN_NOTA = -1

    def __init__(self, identificacion: str, nombre: str, nota: float = SIN_NOTA):
        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self._nota: float =  nota

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nueva_nota: float):
        if 0 <= nueva_nota <= 5:
            self._nota = nueva_nota

class Curso:

    def __init__(self):
        """
        La clase que contiene el conjunto de estudiantes. Tener presente que los estudiantes se manejan como una lista.
        """
        self.estudiantes = list()

    def agregar_estudiante(self, id: str, nombre: str, nota: float):
        # TODO: Implementar requisito R1. El método debe arrojar una excepción si ya están los 50 estudiantes

            if len(self.estudiantes)<50:
             nuevo_estudiante= Estudiante(id,nombre,nota)
             self.estudiantes.append(nuevo_estudiante)


    def cambiar_nota(self, id_estudiante: str, nueva_nota: float):
        for estudiante in self.estudiantes:
            if id_estudiante == self.estudiantes[estudiante].identificacion:
                self.estudiantes[estudiante].nota=nueva_nota



    def calcular_promedio(self) -> float:
        # TODO: Implementar el requisito R3

        suma_notas = 0
        acumulado_estudiante_con_nota=0
        for estudiante in self.estudiantes:
            if self.estudiantes[estudiante].nota != -1:
                suma_notas += self.estudiantes[estudiante].nota
                acumulado_estudiante_con_nota += 1
        promedio = suma_notas / acumulado_estudiante_con_nota

        return promedio

    def estudiantes_por_encima_del_promedio(self) -> int:

        promedio= self.calcular_promedio()
        acum_est=0
        for estudiante in self.estudiantes:
            if self.estudiantes[estudiante].nota > promedio:
                acum_est += 1
        return acum_est

    def cambiar_notas(self):
        """
        Modificar las notas de los estudiantes de la siguiente manera: a todos los que obtuvieron más de 4.0,
        les quita 0.5. A todos los que obtuvieron menos de 2.0, les aumenta 0.5. A todos los demás,
        les deja la nota sin modificar.
        """
        for estudiante in self.estudiantes:
            if self.estudiantes[estudiante].nota > 4.0:
                self.estudiantes[estudiante].nota = self.estudiantes[estudiante].nota - 0.5
            elif self.estudiantes[estudiante].nota < 2.0:
                self.estudiantes[estudiante].nota = self.estudiantes[estudiante].nota + 0.5


    def menor_nota(self) -> float:
        """
        Retornar la menor nota del curso
        :return: float la menor nota del curso
        """
        menor_nota=self.estudiantes[0].nota
        for estudiante in self.estudiantes:
            if self.estudiantes[estudiante].nota < menor_nota:
                menor_nota = self.estudiantes[estudiante].nota

        return menor_nota

    def rango_con_mas_notas(self) -> tuple:
        """
        Escriba un método que indique en qué rango hay más notas en el curso: rango 1 de 0.0 a 1.99,
        rango 2 de 2.0 a 3.49 y rango 3 de 3.5 a 5.0.
        :return: tupla con dos valores: el primero indica el rango con más notas (1, 2 o 3), el segundo la cantidad
                 de notas del rango
        """
        acum_rang1 = 0
        acum_rang2=0
        acum_rang3=0

        for estudiante in self.estudiantes:
            if 0.0 <= self.estudiantes[estudiante].nota <= 1.99:
                acum_rang1 += 1
            if 2.0 <= self.estudiantes[estudiante].nota <= 3.49:
                acum_rang2 += 1
            if 3.5 <= self.estudiantes[estudiante].nota <= 5.0:
                acum_rang3 += 1

        rango_mas_notas = -1
        cant_notas=0
        if acum_rang1 > acum_rang2 and acum_rang1 > acum_rang3:
            rango_mas_notas=1
            cant_notas = acum_rang1
        if acum_rang2 > acum_rang3 and acum_rang2 > acum_rang1:
            rango_mas_notas=2
            cant_notas=acum_rang2
        if acum_rang3 > acum_rang1 and acum_rang3 > acum_rang2:
            rango_mas_notas = 3
            cant_notas = acum_rang3

        return rango_mas_notas, cant_notas
    def notas_a_cero(self):
        """
        Reemplazar todas las notas del curso por 0.0 hasta que aparezca la primera nota superior a 3.0.
        """
        for estudiante in self.estudiantes:
            if self.estudiantes[estudiante].nota < 3.0:
                self.estudiantes[estudiante].nota = 0


    def sumadas_dan_treinta(self) -> int:
        """
        Calcular el número mínimo de notas del curso necesarias para que la suma supere el valor 30, recorriéndolas
        desde la primera nota en adelante. Si al sumar todas las notas no se llega a ese valor,
        él método debe retornar -1.
        :return: int. El número de notas mínimo que sumadas dan 30
        """
        num_minimo=0
        suma=0
        for estudiante in self.estudiantes:
            if self.estudiantes[estudiante].nota != -1:
                suma += self.estudiantes[estudiante].nota
                num_minimo+=1
                if suma > 30:
                    return num_minimo
                else:
                    return -1

    def nota_mediana(self) -> float:
        """
        Calcular la nota del curso (si hay varias que lo cumplan, puede retornar cualquiera) tal que la mitad
        de las notas sean menores o iguales a ella.
        :return: float. La nota mediana del curso.
        """
        notas=[]
        for estudiante in self.estudiantes:
            if self.estudiantes[estudiante].nota != -1:
                notas+= self.estudiantes[estudiante].nota
        mediana= median_grouped(notas)
        return mediana
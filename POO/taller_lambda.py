# Ejercicio 1. Escriba una función lambda que recibe un parámetro x y retorna el valor x + 5.
# Asigne la función a una variable llamada suma_5
# TODO: Escriba la solución aquí
suma_5 = lambda x: x+5

# Ejercicio 2. Escriba una función lambda que recibe un parámetro x y retorna el valor de x elevado al cuadrado
# Invoque la función inmediatamente y guarde el resultado una variable llamada res
# TODO: Escriba la solución aquí
res = (lambda x: x ** 2)(2)

# Ejercicio 3. Escriba una función lambda que reciba dos parámetro a y b y retorne True si a es mayor o igual a
# b, o False en caso contrario.
# Invoque la función inmediatamente e imprima el resultado por consola
# TODO: Escriba la solución aquí
res_3 = (lambda a, b: a >= b and True or False)(7,5)
print(res_3)

# Ejercicio 4. Usando el método sort() de los objetos lista ordene la siguiente lista en orden descendente.
# Debe usar una función lambda en vez de usar el parámetro reverse de la función sort().
# Al finalizar, imprima la lista ordenada
# Pista: La función lambda se pasa como el parámetro key del método sort()
numeros_1 = [100, 10, 10000, 1, 9 , 999, 99]
# TODO: Escriba la solución aquí
numeros_1.sort(key= lambda numero: 100/numero)
print(numeros_1)

# Ejercicio 5. Usando la función sorted() y una función lambda ordene las palabras en la siguiente lista, con
# base en su segunda letra de la 'a' a la 'z'.
# Al finalizar, imprima la lista ordenada
palabras = ["perro", "gallina", "gorilla", "avestruz", "abeja", "tiburón", "iguana", "oso"]
# TODO: Escriba la solución aquí
palabras_ordenados= sorted(palabras, key= lambda p: p[1])
print(palabras_ordenados)

# Ejercicios 6. Usando la función sorted() y una función lambda ordene las tuplas de la siguiente lista con base
# en los segundos items de cada tupla.
# Al finalizar, muestra la lista de tuplas ordenada
lista_1 = [(7743955, "Bogotá"), (2280908, "Santander"), (6677930, "Antioquia"), (1339998, "Tolima"), (359127, "Putumayo")]
# TODO: Escriba la solución aquí
lista_ordenada = sorted(lista_1, key= lambda t: t[1])
print(lista_ordenada)

# Ejercicios 7. Usando la función sorted(), su parámetro reverse y una función lambda ordene inversamente las tuplas de
# la siguiente lista con base en el último caracter de los segundos items de cada tupla.
# Al finalizar, muestra la lista de tuplas ordenada
lista_2 = [(3743955, "Valle"), (2280908, "Santander"), (6677930, "Antioquia"), (1339998, "Tolima"), (359127, "Putumayo")]
# TODO: Escriba la solución aquí
lista_ordenada_2 = sorted(lista_2, key= lambda t: t[1][-1], reverse=True)
print(lista_ordenada_2)

# Ejercicio 8. Usando la función filter() y una función lambda, filtre la siguiente lista para que solo queden números
# negativos.
# Al finalizar, muestra la lista resultante
numeros_2 = [12, -1, 9, 8, -0.5, -0.2, -100]
# TODO: Escriba la solución aquí
numero_negativos = list(filter(lambda n: n < 0, numeros_2))
print(numero_negativos)

# Ejercicio 9. Usando la función filter(), list(), una función lambda y el método lower() de los strings, filtre todas las vocales
# de un string dado
# Pista 1: como filter() retorna un objeto iterable, se puede utilizar list() para convertir dicho objeto en una lista
# Pista 2: Una función lambda con expresiones lógicas puede tener una expresión del tipo
#          lambda x: True if x in ... else False
texto = "Los olímpicos the invierno de 2022 se llevarán a cabo en Beijing, China"

vocales = list(filter(lambda v: True if v in 'aeiou' else False, texto.lower()))
print(vocales)

# Ejercicio 10. Usando las funciones map(), filter() y una función lambda sume 2000 a todos los valores menores que 8000
# en la lista.
# Imprima la lista al final
# Pista: Se puede usar la función filter() dentro de la función map()
numeros_3 = [1000, 500, 600, 700, 5000, 90000, 17500]
lista = list(filter(lambda x: True if x < 8000 else False, map(lambda x: x+2000,numeros_3)))
print(lista)






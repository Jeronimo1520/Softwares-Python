"""def numero_impar(numero):
    if numero % 2 != 0:
        return True

numeros= [2,3,4,5,6,7,8,9,10,11,12,13]

print(list(filter(numero_impar, numeros)))
"""
"""class Libro:
    def __init__(self,nombre ,precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"El libro {self.nombre} tiene un precio de {self.precio}"

lista_libros= [
    Libro("Harry Potter",25000),
    Libro("100 años de soledad",50000),
    Libro("La Odisea",75000),
    Libro("Romeo y Julieta",10000),

]
def preciosAltos(libro):
    if libro.precio >= 50000:
        return libro.precio

precios_altos = list(filter(preciosAltos,lista_libros))

for precio in precios_altos:
    print(precio)
"""
class Libro:
    def __init__(self,nombre ,precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"El libro {self.nombre} tiene un precio de {self.precio}"

lista_libros= [
    Libro("Harry Potter",25000),
    Libro("100 años de soledad",50000),
    Libro("La Odisea",75000),
    Libro("Romeo y Julieta",10000),

]

def precio_iva(libro):
    libro.precio = libro.precio * 1.19
    return libro

lista_libros_iva = map(precio_iva, lista_libros)

for libro in lista_libros_iva:
    print(libro)

class ClaseA:
    hola=1
    def __init__(self):
        self.attr_1 : str = "attr_1"
        self.attr_2: int = 10
        self.attr_3: str = "attr_3"

    def metodo_1(self):
        print(f"Este es el método 1 de la ClaseA {self.attr_2}")

class ClaseB(ClaseA):
    def __init__(self):
        super().__init__()
        self.attr_4 = "attr_4"

    def metodo_1(self):
        print("antes del método de la clase Padre")
        super().metodo_1()
        print("después del método de la clase Padre")

    def metodo_2(self):
        print("Este método es solo de la clase B")
        print(self.hola)

class ClaseD(ClaseB):
    def __init__(self):
        super(ClaseD, self).__init__()
    def metodo_1(self):
        print(f"Este es el metodo 1 de la clase D")
        super(ClaseB,self).metodo_1()

if __name__ == "__main__":
    d = ClaseD()
    b=ClaseB()
    d.metodo_1()
    b.metodo_2()


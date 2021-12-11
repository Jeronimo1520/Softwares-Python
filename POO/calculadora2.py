def main():
    def suma_modular():
            n = 0
            try:
                n = int(input("Ingrese el número base: "))
            except ValueError:
                int(input("Por favor ingrese un nuevo número: "))
            if n <= 0:
                print("Ingrese una base mayor a cero: ")

            else:
                a = 0
                b = 0
                try:
                    a = int(input("Ingrese un número A: "))
                except ValueError:
                    int(input("Por favor ingrese un nuevo número: "))
                if a <= 0:
                    print("Ingrese un número A positivo: ")
                else:
                    if a >= n:
                        a = a % n

                    try:
                        b = int(input("Ingrese un número b: "))
                    except ValueError:
                        int(input("Por favor ingrese un nuevo número: "))
                    if b <= 0:
                        print("Ingrese un número B postivo: ")
                    else:
                        if b >= n:
                            b = b % n
                        resultado = (a + b) % n
                        print("El resultado de la suma modular es:" , resultado)


    def resta_modular():
            n = 0
            try:
                n = int(input("Ingrese el número base: "))
            except ValueError:
                int(input("Por favor ingrese un nuevo número: "))
            if n <= 0:
                print("Ingrese una base mayor a cero: ")
            else:
                a = 0
                b = 0
                try:
                    a = int(input("Ingrese un número A: "))
                except ValueError:
                    int(input("Por favor ingrese un nuevo número:"))
                if a <= 0:
                    print("Ingrese un número A positivo: ")
                else:
                    if a >= n:
                        a = a % n
                    try:
                        b = int(input("Ingrese un número B: "))
                    except ValueError:
                        int(input("Por favor ingrese un nuevo número: "))
                    if b <= 0:
                        print("Ingrese un número B positivo: ")
                    else:
                        if b >= n:
                            b = b % n
                        resultado = (a - b) % n
                        print("El resultado de la resta modular es:" ,resultado)


    def producto_modular():
            n = 0
            try:
                n = int(input("Ingrese el número base: "))
            except ValueError:
                int(input("Por favor ingrese un nuevo número: "))
            if n <= 0:
                print("Ingrese una base mayor a cero: ")
            else:
                a = 0
                b = 0
                try:
                    a = int(input("Ingrese un número A: "))
                except ValueError:
                    int(input("Por favor ingrese un nuevo número: "))
                if a <= 0:
                    print("Ingrese un número A positivo: ")
                else:
                    if a >= n:
                        a = a % n
                    try:
                        b = int(input("Ingrese un número B: "))
                    except ValueError:
                        int(input("Por favor ingrese un nuevo número: "))
                    if b <= 0:
                        print("Ingrese un número B positivo: ")
                    else:
                        if b >= n:
                            b = b % n
                        resultado = (a * b) % n
                        print("El resultado del producto modular es: ",resultado)

    def inverso_numero(n, b):
        try:
            inverso = pow(b, -1, n)
        except ValueError:
            print("El número no tiene inverso modular")
        else:
            return int(inverso)

    def inverso_modular():
        try:
            n = int(input("Ingrese el numero base: "))
            b = int(input("Ingrese el numero a sacar inverso: "))
        except ValueError:
            print("Por favor ingrese un nuevo número: ")
        else:
            inverso = 0
            try:
                inverso = pow(b, -1, n)
            except ValueError:
                print("El número no tiene inverso modular")

            return print(f"El inverso del numero es: {int(inverso)}")

    def division_modular():
            n = 0
            try:
                n = int(input("Ingrese el número base: "))
            except ValueError:
                int(input("Por favor ingrese un nuevo número: "))
            if n <= 0:
                print("Ingrese una base mayor a cero: ")
            else:
                a = 0
                b = 0

                try:
                    a = int(input("Ingrese un número A: "))
                except ValueError:
                    int(input("Por favor ingrese un nuevo número: "))
                if a <= 0:
                    print("Ingrese un número A positivo: ")
                else:
                    if a >= n:
                        a = a % n
                    try:
                        b = int(input("Ingrese un número B: "))
                    except ValueError:
                        int(input("Por favor ingrese un nuevo número: "))
                    if b <= 0:
                        print("Ingrese un número B positivo")
                    try:
                        b_inverso = inverso_numero(n, b)
                    except:
                        print("Error")
                    else:
                        if b_inverso >= n:
                            b_inverso = b_inverso % n
                        resultado = (a * b_inverso) % n
                        print("El resultado de la división modular es: ",resultado)


    def potencia_modular():
        a = int(input('Ingrese la base: '))
        b = int(input('Ingrese el exponente'))
        n= int(input('Ingrese el módulo'))
        res= ((a**b) % n)
        return print(res)

    def raiz_modular():
        a = int(input('Ingrese el número al cual le quiera sacar la raíz modular: '))
        n = int(input('Ingrese el número del modulo'))
        if a > n or a < 0:
            a = a % n

        cuadradoss = []
        for i in range(0, n, 1):
            cuadp = (i * i) % n
            if cuadp == a:

                cuadradoss.append(i)
        if len(cuadradoss) != 0:
            print("Las raices de", a, "son", cuadradoss)
        else:
            print("El numero", a, "no tiene raiz modular en z", n)

    def cuadrados_perfectos():
        n = int(input('Ingrese el módulo'))
        listaCP = []
        for i in range(0, n - 1):
            listaCP.append((i * i) % n)
        list(set(listaCP))
        return print(len(listaCP))

    def cantInvZn(n):
        inv = []
        lisinv = []
        for i in range(0, n + 1):
            ops = modInvers(i, n)
            if ops != None:
                lisinv.append(i)
                inv.append(ops)
        print("La cantidad de inversos en Zn es: ", inv)
        print("Con estos numeros como b:         ", lisinv)
        print("La cantidad de invertibles es: ", len(inv))

    def modInvers(a, n):
        for x in range(1, n):
            if ((a % n) * (x % n) % n == 1):
                return x
    cantInvZn(5416)


    def menu():

        opt = 0
        while opt not in range(1, 10):
            print("Bienvenido a la calculadora modular")
            print("1. Suma modular")
            print("2. Resta modular")
            print("3. Producto modular")
            print("4. Inverso modular")
            print("5. División modular")
            print("6. Potencia modular")
            print("7. Raíz cuadrada modular")
            print("8. Cuadrados perfectos")
            print("9. Salir")

            opt = int(input("\nIngrese una opción: "))

            if opt not in range(1, 10):
                print("\nERROR")

        return opt

    opcion = 0
    while opcion != 8:
        opcion = menu()

        if opcion == 1:
            suma_modular()
        elif opcion == 2:
            resta_modular()
        elif opcion == 3:
            producto_modular()
        elif opcion == 4:
            inverso_modular()
        elif opcion == 5:
            division_modular()
        elif opcion == 6:
            potencia_modular()
        elif opcion == 7:
            raiz_modular()
        elif opcion == 8:
            cuadrados_perfectos()
        elif opcion == 9:
            print("Ha finalizado el programa")


main()
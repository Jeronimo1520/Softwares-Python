def main():
    from matplotlib import pyplot as plt
    from matplotlib_venn import venn3

    A = {17, 31, 3, 25}
    B = {25, 8, 31, 10}
    C = {6, 3, 31, 10}
    U = {17, 31, 3, 25, 8, 10, 6}

    resultado1 = ((C & B) - A)
    resultado2 = ((A ^ C) & U - B)
    v = venn3((1,1,1,1,1,1,1))

    v.get_label_by_id("100").set_text(A - (B | C))
    v.get_label_by_id("110").set_text((A & B) - C)
    v.get_label_by_id("111").set_text(A & B & C)
    v.get_label_by_id("011").set_text((B & C) - A)
    v.get_label_by_id("101").set_text((A & C) - B)
    v.get_label_by_id("001").set_text(C - (A | B))
    v.get_label_by_id("010").set_text(B - (A | C))


    def resultado21():
        print(f"El resultado del punto 2.1 es n{resultado1} = 10%")
        v.get_label_by_id("011").set_text((B & C) - A)
        v.get_label_by_id("011").set_color("#FF0000")
        plt.show()



    def resultado22():
        print(f"El resultado del punto 2.2 es n{resultado2} = 23%")
        v.get_label_by_id("100").set_text(A - (B | C))
        v.get_label_by_id("100").set_color("#FF0000")
        v.get_label_by_id("001").set_text(C - (A | B))
        v.get_label_by_id("001").set_color("#FF0000")
        plt.show()

    def menu():
        opt = 0
        while opt not in range(1, 4):
            print("\n====== MENU DE OPCIONES")
            print("1. Resultado del punto 2.1")
            print("2.Resultado punto 2.2")
            print("3.Salir")



            opt = int(input("\nIngrese una opción: "))

            if opt not in range(1, 4):
                print("\nERROR: OPCIÓN NO VÁLIDA")

        return opt

    opcion = 0
    while opcion != 3:
        opcion = menu()

        if opcion == 1:
            print(resultado21())
        elif opcion == 2:
            print(resultado22())
        elif opcion == 3:
            print("\n===============")
            print("FIN DEL PROGRAMA")
            print("===============")


main()

from club_social.mundo.errores import SocioExistenteError, SocioNoExistenteError
from club_social.mundo.mundo import Club


def menu():
    opt = 0
    while opt not in range(1, 6):
        print("\n====== MENU DE OPCIONES - CLUB SOCIAL ======")
        print("1. Afiliar un socio al club")
        print("2. Registrar persona autorizada")
        print("3. Registrar consumo")
        print("4. Pagar factura")
        print("5. Salir")

        opt = int(input("\nIngrese una opción: "))

        if opt not in range(1, 6):
            print("\nERROR: OPCIÓN NO VÁLIDA")

    return opt


if __name__ == "__main__":
    club = Club()
    opcion = 0
    while opcion != 5:
        opcion = menu()
        if opcion == 1:
            print("\n>> AFILIAR UN SOCIO AL CLUB")
            cedula = input("Cédula del nuevo socio: ")
            nombre = input("Nombre del nuevo socio: ")
            try:
                club.afiliar_socio_a_club(cedula, nombre)
            except SocioExistenteError as err:
                print(f"\nERROR: {err.msg}")
            else:
                print("\nINFO: El socio se afilió exitosamente")

        elif opcion == 2:
            print("\n>> REGISTRAR PERSONA AUTORIZADA")
            cedula_socio = input("Cédula del socio: ")
            nombre_autorizado = input("Nombre de la persona autorizada: ")
            try:
                club.registrar_autorizado_por_socio(nombre_autorizado, cedula_socio)
            except SocioNoExistenteError as err:
                print(f"\nERROR: {err.msg}")
            else:
                print("\nINFO: El autorizado se registró exitosamente")

        elif opcion == 3:
            print("\n>> REGISTRAR UN CONSUMO")
            cedula_socio = input("Cédula del socio: ")
            concepto = input("Concepto del consumo: ")
            valor_valido = False
            while not valor_valido:
                try:
                    valor = float(input("Valor del consumo: "))
                except ValueError:
                    print("\nERROR: El valor no es numérico")
                else:
                    valor_valido = True

            nombre_autorizado = input("Nombre de la persona autorizada (opcional): ")
            try:
                club.registrar_consumo_a_la_cuenta_del_socio(cedula_socio, concepto, valor, nombre_autorizado)
            except SocioNoExistenteError as err:
                print(f"\nERROR: {err.msg}")
            else:
                print("\nINFO: El consumo se registró exitosamente.")

        elif opcion == 4:
            print("\n>> PAGAR FACTURA")
            cedula_socio = input("Cédula del socio: ")
            socio = club.buscar_socio(cedula_socio)
            if socio is not None:
                print("\nLISTADO DE FACTURAS")
                for idx, factura in enumerate(socio.facturas, start=1):
                    print(f"{idx} - {factura}")
                idx_factura = int(input("\nIngrese la factura a pagar: "))
                factura = socio.facturas[idx_factura - 1]

                try:
                    club.pagar_factura(cedula_socio, factura)
                except SocioNoExistenteError as err:
                    print(f"\nERROR: {err.msg}")
                else:
                    print("\nINFO: la facturase pagó existosamente.")

        elif opcion == 5:
            print("\n===============")
            print("FIN DEL PROGRAMA")
            print("===============")

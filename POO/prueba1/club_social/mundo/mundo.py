from club_social.mundo.errores import SocioNoExistenteError, SocioExistenteError


class Factura:
    """
    Representa una factura de los consumos de un socio o sus autorizados

    Attributes:
        concepto: un str que describe el concepto del consumo
        valor: un float que indica el valor del consumo
        nombre: un str que indica el nombre del autorizado que hizo el consumo
    """
    def __init__(self, concepto: str, valor: float, autorizado: str = ""):
        """
        Inicializa una factura de un socio

        Args:
             concepto: un str que describe el concepto del consumo
             valor: un float que indica el valor consumo
             autorizado: un str, opcional, que indica el nombre del autorizado que hizo el consumo
        """
        self.concepto: str = concepto
        self.valor: float = valor
        self.nombre: str = autorizado

    def __str__(self):
        return f"{self.concepto} - valor: {self.valor} - autorizado: {self.nombre}"

class Socio:
    """
    Representa un socio del club social

    Attributes:
        cedula: un str que indica la identificación del socio
        nombre: un str que indica el nombre del socio
        facturas: una lista de objetos de la clase Factura que contiene todas las facturas asociadas a los consumos del
                  socio y sus autorizados
        autorizados: una lista de str que contiene los nombres de los autorizados del socio
    """

    def __init__(self, cedula: str, nombre: str):
        """
        Inicializa un objeto de la clase Socio

        Args:
             cedula: un str con la identificación del socio
             nombre: un str con el nombre del socio
        """
        self.cedula: str = cedula
        self.nombre: str = nombre
        self.autorizados = list()
        self.facturas = list()

    def agregar_autorizado(self, nombre_autorizado: str):
        """
        Agrega un autorizado a la lista del autorizados del socio

        Args:
            nombre_autorizado: un str con el nombre del autorizado que se va a agregar
        """
        self.autorizados.append(nombre_autorizado)

    def cancelar_factura_pendiente(self, factura: Factura):
        """
        Elimina una factura de la lista de facturas pendientes del socio

        Args:
            factura: Objeto de la clase factura que se quiere eliminar
        """
        self.facturas.remove(factura)

    def agregar_factura(self, concepto: str, valor: float, autorizado: str):
        """
        Crea una factura y la agrea al listado de facturas del socio

        Args:
         concepto: str que indica el concepto del consumo
         valor: float con el valor del consumo
         autorizado: str opcional del autorizado que realizo el consumo
        """
        factura= Factura(concepto, valor,autorizado)
        self.facturas.append(factura)
    def __str__(self):
        return f"({self.cedula}) {self.nombre}"


class Club:
    """
    Clase que representa el club social

    Attributes:
        socios: un diccionario que contiene la lista de socios, donde la cédula es la clave
    """

    def __init__(self):
        self.socios = dict()

    def registrar_autorizado_por_socio(self, nombre_autorizado: str, cedula_socio: str):
        """
        Agrega un autorizado a la lista de autorizados del socio con la cedula dada

        Args:
            nombre_autorizado: un str con el nombre del autorizado que se va a agregar
            cedula_socio: un str con la cédula del socio al que se le va a agregar el autorizado

        Raises:
            SocioNoExistenteError: si la cédula dada como parámetro no pertenece a ningún socio del club
        """
        socio = self.buscar_socio(cedula_socio)
        if socio is not None:
            socio.agregar_autorizado(nombre_autorizado)
        else:
            raise SocioNoExistenteError(cedula_socio, f"No existe un socio con la cédula {cedula_socio}")

    def buscar_socio(self, cedula: str) -> Socio:
        """
        Busca un socio con una cédula dada

        Args:
             cedula: un str con la cédula del socio que se quiere buscar

        Returns:
            Un objeto de la clase Socio o None si no existe ningún socio con la cédula dada
        """
        if cedula in self.socios.keys():
            return self.socios[cedula]
        else:
            return None

    def pagar_factura(self, cedula_socio: str, factura: Factura):
        """
        Elimina una factura de la lista de facturas pendientes del socio con la cédula dada

        Args:
            cedula_socio: un str con la cédula del socio al que se le quiere eliminar la factura
            factura:: Objeto de la clase Factura que se quiere eliminar

        Raises:
            SocioNoExistenteError: si la cédula dada como parámetro no pertenece a ningún socio del club
        """
        socio = self.buscar_socio(cedula_socio)
        if socio is not None:
            socio.cancelar_factura_pendiente(factura)
        else:
            raise SocioNoExistenteError(cedula_socio, f"No existe un socio con la cédula {cedula_socio}")

    def afiliar_socio_a_club(self, cedula_socio:str, nombre_socio: str):
        """
        Agrega un nuevo socio al diccionaio de socios del club

        Args:
            cedula_socio: un str que contiene la identificacion del socio
            nombre_socio: un str con el nombre del socio

        Raises:
            SocioExistenteError: Si ya existe un socio con la misma cedula

        Returns;
            El socio que se agrego al club
        """
        socio = self.buscar_socio(cedula_socio)
        if socio is None:
            socio = Socio(cedula_socio, nombre_socio)
            self.socios[cedula_socio]=socio
            return socio
        else:
            raise SocioExistenteError(cedula_socio, f"Ya existe un socio con la cedula {cedula_socio}")

    def registrar_consumo_a_la_cuenta_del_socio(self, cedula: str, concepto: str, valor: float, autorizado:""):
        """
        Agrega una factura al socio con la cedula dada

        Args:
             cedula: un str con la id del socio
             concepto: str que indica el concepto del consumo
             valor: float con el valor del consumo
             autorizado: str opcional del autorizado que realizo el consumo

        Raises:
            SocioNoExistenteError: Si no existe ningun socio con la cedula dada
        """
        socio = self.buscar_socio(cedula)
        if socio is not None:
            socio.agregar_factura(concepto, valor, autorizado)
        else:
            raise SocioNoExistenteError(cedula, f"No existe un socio con la cedula {cedula}")
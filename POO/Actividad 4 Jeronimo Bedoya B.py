class Jugador:
    GOLES =-1
    TARJETAS_AMARILLAS =-1
    TARJETAS_ROJAS =-1
    ASISTENCIAS =-1

    def __init__(self, nombre: str, numero: str):
        self._nombre: str = nombre
        self._numero : str = numero
        self._goles_anotados: int = Jugador.GOLES
        self._tarjetas_amarillas: int = Jugador.TARJETAS_AMARILLAS
        self._tarjetas_rojas: int = Jugador.TARJETAS_ROJAS
        self._asistencias: int = Jugador.ASISTENCIAS

    @property
    def goles_anotados(self):
        return self._goles_anotados
    @goles_anotados.setter
    def goles_anotados(self, valor):
        self._goles_anotados = valor

    @property
    def tarjetas_amarillas(self):
        return self._tarjetas_amarillas

    @tarjetas_amarillas.setter
    def tarjetas_amarillas(self, valor):
        self._tarjetas_amarillas= valor

    @property
    def tarjetas_rojas(self):
        return self._tarjetas_rojas

    @tarjetas_rojas.setter
    def tarjetas_rojas(self, valor):
        self._tarjetas_rojas = valor

    @property
    def asistencias(self):
        return self._asistencias

    @asistencias.setter
    def asistencias(self, valor):
        self._asistencias = valor

    def tiene_tarjetas_amarillas(self):
        return self._tarjetas_amarillas != Jugador.TARJETAS_AMARILLAS
    def tiene_goles(self):
        return self._goles_anotados != Jugador.GOLES
    def tiene_tarjetas_rojas(self):
        return self._tarjetas_rojas != Jugador.TARJETAS_ROJAS
    def tiene_asistencias(self):
        return self._asistencias != Jugador.ASISTENCIAS

class Equipo:

    def __init__(self):

        self.jugador1 = Jugador("Roberto", "5")
        self.jugador2 = Jugador("Juan", "2")
        self.jugador3 = Jugador("James", "25")
        self.jugador4 = Jugador("Jaime", "10")
        self.jugador5 = Jugador("Andres", "6")

    def promedio_tarjetas_amarillas(self):
        suma_tarjetas_amarillas=0
        total_jugadores_con_tarjetas_amarillas=0
        jugadores = (self.jugador1, self.jugador2, self.jugador3, self.jugador4, self.jugador5)

        for jugador in jugadores:
            if jugador.tiene_tarjetas_amarillas():
                suma_tarjetas_amarillas += jugador.tarjetas_amarillas
                total_jugadores_con_tarjetas_amarillas += 1
        return suma_tarjetas_amarillas / total_jugadores_con_tarjetas_amarillas
    def promedio_tarjetas_rojas(self):
        suma_tarjetas_rojas=0
        total_jugadores_con_tarjetas_rojas=0
        jugadores = (self.jugador1, self.jugador2, self.jugador3, self.jugador4, self.jugador5)

        for jugador in jugadores:
            if jugador.tiene_tarjetas_rojas():
                suma_tarjetas_rojas += jugador.tarjetas_rojas
                total_jugadores_con_tarjetas_rojas +=1
    def relacion_goles_asistencias(self):
        total_goles=0
        total_asistencias=0
        jugadores = (self.jugador1, self.jugador2, self.jugador3, self.jugador4, self.jugador5)
        for jugador in jugadores:
            if jugador.tiene_goles():
                total_goles += jugador.goles_anotados
            if jugador.tiene_asistencias():
                total_asistencias += jugador.asistencias
        return total_goles / total_asistencias

    """def comparacion(self,j1):
        if j1 == self.jugador1:
            print(Equipo.jugador1.goles_anotados)"""
if __name__ == "__main__":
    Equipo=Equipo()

    Equipo.jugador1.tarjetas_amarillas = 6
    Equipo.jugador2.tarjetas_amarillas = 2
    Equipo.jugador1.goles_anotados=2
    Equipo.jugador2.goles_anotados=2
    Equipo.jugador1.asistencias=2
    Equipo.jugador2.asistencias=2
    print(f"El promedio de tarjetas amarillas del equipo son:{Equipo.promedio_tarjetas_amarillas()}")
    print(f"La relacion entre goles y asistencias es: {Equipo.relacion_goles_asistencias()}")





class Jugador:

    def __init__(self, nombre: str, numero: int):
        self.nombre = nombre
        self.numero = numero
        self.goles = 0
        self.asistencias = 0
        self.tarjetas_amarillas = 0
        self.tarjetas_rojas = 0

    def registrar_estadisticas(self, goles, asistencias, amarillas, rojas):
        self.goles += goles
        self.asistencias += asistencias
        self.tarjetas_amarillas += amarillas
        self.tarjetas_rojas += rojas


class Equipo:

    TOTAL_JUGADORES: int = 5

    def __init__(self):
        self.jugador_1 = Jugador("Pepe", 10)
        self.jugador_2 = Jugador("Luis", 5)
        self.jugador_3 = Jugador("Hugo", 2)
        self.jugador_4 = Jugador("Carlos", 7)
        self.jugador_5 = Jugador("Jorge", 11)

    def registrar_estadisticas_jugador(self, jugador, goles, asistencias, amarillas, rojas):
        if jugador == 1:
            self.jugador_1.registrar_estadisticas(goles, asistencias, amarillas, rojas)
        elif jugador == 2:
            self.jugador_2.registrar_estadisticas(goles, asistencias, amarillas, rojas)
        elif jugador == 3:
            self.jugador_3.registrar_estadisticas(goles, asistencias, amarillas, rojas)
        elif jugador == 4:
            self.jugador_4.registrar_estadisticas(goles, asistencias, amarillas, rojas)
        elif jugador == 5:
            self.jugador_5.registrar_estadisticas(goles, asistencias, amarillas, rojas)

    def promedio_tarjetas_amarillas(self):
        jugadores = (self.jugador_1, self.jugador_2, self.jugador_3, self.jugador_4, self.jugador_5)
        suma = 0
        for jugador in jugadores:
            suma += jugador.tarjetas_amarillas

        return suma / Equipo.TOTAL_JUGADORES

    def promedio_tarjetas_rojas(self):
        jugadores = (self.jugador_1, self.jugador_2, self.jugador_3, self.jugador_4, self.jugador_5)
        suma = 0
        for jugador in jugadores:
            suma += jugador.tarjetas_rojas

        return suma / Equipo.TOTAL_JUGADORES

    def relacion_goles_asistencias(self):
        jugadores = (self.jugador_1, self.jugador_2, self.jugador_3, self.jugador_4, self.jugador_5)
        suma_goles = 0
        suma_asistencias = 0
        for jugador in jugadores:
            suma_goles += jugador.goles
            suma_asistencias += jugador.asistencias

        return suma_goles / suma_asistencias

    def estadisticas_equipo(self):
        jugadores = (self.jugador_1, self.jugador_2, self.jugador_3, self.jugador_4, self.jugador_5)
        suma_goles = 0
        suma_asistencias = 0
        suma_amarillas = 0
        suma_rojas = 0
        for jugador in jugadores:
            suma_goles += jugador.goles
            suma_asistencias += jugador.asistencias
            suma_amarillas += jugador.tarjetas_amarillas
            suma_rojas += jugador.tarjetas_rojas

        prom_amarillas = suma_amarillas / Equipo.TOTAL_JUGADORES
        prom_rojas = suma_rojas / Equipo.TOTAL_JUGADORES
        rel_goles_asist = suma_goles / suma_asistencias

        return prom_amarillas, prom_rojas, rel_goles_asist

from Silla import Silla
from Pasajero import Pasajero

class Avion :
    # Atributos
    SILLAS_EJECUTIVAS = 8
    SILLAS_ECONOMICAS = 42

    def __init__(self):
        self.sillasEjecutivas = []
        self.sillasEconomicas = []

        self.definicionSillasEconomicas()
        self.definicionSillasEjecutivas()

    # Métodos
    def definicionSillasEjecutivas(self):
        for i in range(1, self.SILLAS_EJECUTIVAS):
            if i%2 == 0:
                self.sillasEjecutivas.append(i, self.CLASE.vip, Silla.UBICACION.centro)
            else:
                self.sillasEjecutivas.append(i, self.CLASE.vip, Silla.UBICACION.pasillo)

    def definicionSillasEconomicas(self):
        for i in range(1, self.SILLAS_ECONOMICAS):
            if i%2 == 0:
                self.sillasEconomicas.append(i, self.CLASE.eco, Silla.UBICACION.centro)
            else:
                self.sillasEconomicas.append(i, self.CLASE.eco, Silla.UBICACION.pasillo)

    def contarSillasEjecutivasOcupadas(self):
        conteo = 0
        for silla in self.sillasEjecutivas:
            if silla.ocupada:
                conteo += 1
        return conteo
    
    def contarSillasEconomicasOcupadas(self):
        conteo = 0
        for silla in self.sillasEconomicas:
            if silla.ocupada:
                conteo += 1
        return conteo

    def buscarPasajeroEjecutivo(self, pCedula):
        for silla in self.sillasEjecutivas:
            if silla.pasajero.cedula == pCedula and silla.ocupada:
                return silla
        return None
    
    def buscarPasajeroEconomico(self, pCedula):
        for silla in self.sillasEconomicas:
            if silla.pasajero.cedula == pCedula and silla.ocupada:
                return silla
        return None
    
    def buscarSillaEconomicaLibre(self, pUbicacion):
        for silla in self.sillasEconomicas:
            if silla.getPasajero() is None and silla.getUbicacion() == pUbicacion:
                return silla
        return None
    
    def asignarSillaEconomica(self, pUbicacion, pPasajero):
        silla = self.buscarSillaEconomicaLibre(pUbicacion)
        if silla is not None:
            silla.asignarPasajero(pPasajero)
            return True
        return False
    
    def anularReservaEjecutivo(self, pCedula):
        silla = self.buscarPasajeroEjecutivo(pCedula)
        if silla is not None:
            silla.eliminarPasajero()
            return True
        return False
    
    def contarVentanasEconomicas(self):
        conteo = 0
        for silla in self.sillasEconomicas:
            if silla.getUbicacion() == Silla.UBICACION.ventana and silla.getPasajero() is None:
                conteo += 1
        return conteo
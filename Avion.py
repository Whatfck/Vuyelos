from Silla import Silla
from Pasajero import Pasajero

class Avion :
    SILLAS_EJECUTIVAS = 8
    SILLAS_ECONOMICAS = 42

    def __init__(self):
        self.sillasEjecutivas = []
        self.sillasEconomicas = []

        self.definicionSillasEconomicas()
        self.definicionSillasEjecutivas()

    def definicionSillasEjecutivas(self):
        for i in range(1, self.SILLAS_EJECUTIVAS):
            if i%2 == 0:
                self.sillasEjecutivas.append(i, self.CLASE.vip, Silla.UBICAION.centro)
            else:
                self.sillasEjecutivas.append(i, self.CLASE.vip, Silla.UBICAION.pasillo)

    def definicionSillasEconomicas(self):
        for i in range(1, self.SILLAS_ECONOMICAS):
            if i%2 == 0:
                self.sillasEconomicas.append(i, self.CLASE.eco, Silla.UBICAION.centro)
            else:
                self.sillasEconomicas.append(i, self.CLASE.eco, Silla.UBICAION.pasillo)

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
    

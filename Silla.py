class Silla:
    CLASE = {
        "vip": "Ejecutiva",
        "eco": "Economica"
    }

    UBICACION ={
        "ventana": "Ventana",
        "pasillo": "Pasillo",
        "centro" : "Centro"
    }

    def __init__(self, pNumero, pClase, pUbicaicon):
        self.numero = pNumero
        self.clase = (self.CLASE.vip,self.CLASE.eco)[pClase]
        if pUbicaicon == "ventana":
            self.__ubicacion = self.UBICACION.ventana
        elif pUbicaicon == "pasillo":
            self.__ubicacion = self.UBICACION.pasillo
        elif pUbicaicon == "centro":
            self.__ubicacion = self.UBICACION.centro
        else:
            self.__ubicacion = None

        self.__pasajero = None

    def asignarPasajero(self,pPasajero):
        self.__pasajero=pPasajero
    
    def designarSilla(self):
        return True if self.__numero == None else False
    
    def getNumero(self):
        return self.__numero

    def getClase(self):              
        return self.__clase

    def getUbicacion(self):
        return self.__ubicacion
    def getPasajero(self):
        return self.__pasajero


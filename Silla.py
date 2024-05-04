class Silla:
    # Enumeraciones
    CLASE = {
        "vip": "Ejecutiva",
        "eco": "Economica"
    }

    UBICACION ={
        "ventana": "Ventana",
        "pasillo": "Pasillo",
        "centro" : "Centro"
    }

    # Atributos
    def __init__(self, pNumero, pClase, pUbicacion):
        self.__numero = pNumero

        self.__clase = (self.CLASE.vip,self.CLASE.eco)[pClase]

        if pUbicacion == "ventana":
            self.__ubicacion = self.UBICACION.ventana
        elif pUbicacion == "pasillo":
            self.__ubicacion = self.UBICACION.pasillo
        elif pUbicacion == "centro":
            self.__ubicacion = self.UBICACION.centro
        else:
            self.__ubicacion = None

        self.ocupada = False
        self.__pasajero = None

    # Métodos
    def asignarPasajero(self,pPasajero):
        self.ocupada = True
        self.__pasajero = pPasajero

    def eliminarPasajero(self):
        self.ocupada = False
        self.__pasajero = None
    
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
    




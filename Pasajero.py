class Pasajero:
     # Atributos
    def __init__(self,pCedula,pNombre):
        self.Cedula = pCedula
        self.Nombre = pNombre

    # Métodos
    def getcedula(self):
        return self.Cedula
    
    def getnombre(self):
        return self.Nombre
    
    def setcedula(self,pCedula):
        self.Cedula = pCedula
    
    def setnombre(self,pNombre):
        self.Nombre = pNombre

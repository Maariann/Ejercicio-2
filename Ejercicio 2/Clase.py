class ViajeroFrecuente:
    __numViajero = str
    __dni = str
    __nombre = str
    __apellido = str
    __millasAcum = int
    
    def __init__(self, numViajero=None, dni=None, nombre=None, apellido=None, millasAcum=int):
        self.__numViajero = numViajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millasAcum = millasAcum
        
    def cantidadTotalDeMillas(self):
        return self.__millasAcum
    
    def acumularMillas(self,xmillas):
        self.__millasAcum += xmillas
        return self.__millasAcum
    
    def canjearMillas(self,millas):
        if millas <= self.__millasAcum:
            self.__millasAcum -= millas
        else:
            print('Millas Insuficientes')
    
    def getNumero(self):
        return self.__numViajero
    
from menu import Menu
from Clase import ViajeroFrecuente

if __name__ == '__main__':
    lista_viajeros = []
    
    
    
    with open("Viajeros.csv") as archivo:
        for linea in archivo:
            campos = linea.strip().split(",")
            viajero = ViajeroFrecuente(campos[0],campos[1],campos[2],campos[3],int(campos[4]))
            lista_viajeros.append(viajero)
            
    print("Lista de viajeros:")
    for viajero in lista_viajeros:
        print(viajero)
        print(vars(viajero))
    
    num_viajero = input("Ingrese el número de viajero frecuente: ")
    
    viajero_actual = None
    for viajero in lista_viajeros:
        if viajero.getNumero() == num_viajero:
            viajero_actual = viajero
            break
        
    if viajero_actual is not None:
        menu = Menu(viajero_actual)
        menu.mostrar()
    else:
        print("No se encontró el número de viajero frecuente ingresado")
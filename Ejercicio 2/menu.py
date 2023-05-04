class Menu:
    def __init__(self, viajero):
        self.viajero = viajero
        
    def mostrar(self):
        while True:
            opcion = input("\nIngrese la opción:\n"
                           "a- Consultar cantidad de millas\n"
                           "b- Acumular millas\n"
                           "c- Canjear millas\n"
                           "d- Salir\n"
                           "Opción: ")
            if opcion == "a":
                print("Cantidad de millas acumuladas:", self.viajero.cantidadTotalDeMillas())
            elif opcion == "b":
                millas = int(input("Ingrese la cantidad de millas a acumular: "))
                print("Cantidad de millas actualizada:", self.viajero.acumularMillas(millas))
            elif opcion == "c":
                millas = int(input("Ingrese la cantidad de millas a canjear: "))
                self.viajero.canjearMillas(millas)
                print("Cantidad de millas actualizada:", self.viajero.cantidadTotalDeMillas())
            elif opcion == "d":
                break
            else:
                print("Opción inválida. Intente nuevamente.")

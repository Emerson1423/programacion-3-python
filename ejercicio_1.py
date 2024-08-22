



class Veterinaria:
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.estado = self.estado()
        self.tamano = self.definir_tamaño()

    
    def definir_tamaño(self):
        if self.peso < 10:
            return "Perro Pequeño"
        else:
            return "Perro Grande"

    def estado(self):
        self.estado = "ATENDIDO"
        return self.estado
        


    def mostrar_Datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Estado: {self.estado}")
        print(f"Tamaño: {self.tamano}")
        print("---------------------------")


perros = []

Menu=0
while Menu < 3:
    print("-----------------------")
    print(" * CLÍNICA VETERINARIA * ")
    print("-----------------------")
    print()
    print("-----------------------------")
    print("1. Ingresar datos del perro")
    print("2. Mostrar datos del perro")
    print("3. Salir")
    print("-----------------------------")
    
    op = input("Ingrese la operacion que desea realizar: ")
    match op:       #! Realiza un matcheo a op, asi segun el caso ejecute cada funcion
        case "1":
           
            while True:
                nombre = input("Ingrese el nombre del perro: ")
                raza = input("Ingrese la raza del perro: ")
                while True:
                    try:
                     edad = int(input("Ingrese la edad del perro (en años): "))
                     break  # Si se ingresa un valor numérico válido, salimos del bucle
                    except ValueError:
                     print("Error: el año debe ser numerico. Por favor, intente de nuevo.")
                while True:
                   try:
                    peso = float(input("Ingrese el peso del perro (en kg): "))
                    break  # Si se ingresa un valor numérico válido, salimos del bucle
                   except ValueError:
                    print("Error: el año debe ser numerico. Por favor, intente de nuevo.")
                perro = Veterinaria(nombre, raza, edad, peso)
                perros.append(perro)
                otro = input("¿Desea ingresar otro perro? (s/n): ")
                if otro.lower() != 's':
                    break   
        case "2":
            if perros:  # Verifica si la lista tiene elementos
                print("\nInformación de todos los perros registrados:")
                for perro in perros:
                    perro.mostrar_Datos()
            else:
                print("\nNo se han registrado perros aún.")
            # Preguntar si desea continuar o salir
            continuar = input("¿Desea iniciar el programa de nuevo ? (s/n): ")
            if continuar.lower() != 's':

                print("--------------------------------")
                print("Gracias por utilizar el sistema")
                print("--------------------------------")
                break

        case "3":
            print("--------------------------------")
            print("Gracias por utilizar el sistema")
            break
        case _: #! Continua el programa hasta que se inserte  una opcion validad
            print("_____________________________")
            print("Operacion invalida, por favor intente de nuevo")
            continue

    
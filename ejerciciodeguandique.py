class Perro:
    def __init__(self, nombre, raza, edad, peso):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.tipo = "Perro Pequeño" if peso < 10 else "Perro Grande"
        self.estado = "NO ATENDIDO"

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad}")
        print(f"Peso: {self.peso}")
        print(f"Tipo: {self.tipo}")
        print(f"Estado: {self.estado}")

# Lista para almacenar objetos Perro
perros = []

def recibe_datos():
    nombre = input("Ingrese el nombre del perro: ")
    raza = input("Ingrese la raza del perro: ")
    edad = int(input("Ingrese la edad del perro en años: "))
    peso = int(input("Ingrese el peso del perro: "))
    nuevo_perro = Perro(nombre, raza, edad, peso)
    nuevo_perro.estado = "ATENDIDO"
    perros.append(nuevo_perro)

def mostrar_datos():
    for perro in perros:
        perro.mostrar_datos()
        print("-" * 20)

# ... resto del código del menú, etc.






    
#! Un menu simple que da opciones al usuario
operacion=0
while operacion < 3:
    print("\nBienvenido")
    print("_____________________________")
    print("1. Ingresar datos del perro")
    print("2. Mostrar datos del perro")
    print("3. Salir")
    print("_____________________________")
    op = input("Ingrese la operacion que desea realizar: ")
    match op:       #! Realiza un matcheo a op, asi segun el caso ejecute cada funcion
        case "1":
            print("_____________________________")
            recibe_datos()
        case "2":
            print("_____________________________")
            mostrar_datos()
        case "3":
            print("_____________________________")
            print("Gracias por utilizar el sistema")
            break #! Termina el programa
        case _: #! Continua el programa hasta que se inserte  una opcion validad
            print("_____________________________")
            print("Operacion invalida, por favor intente de nuevo")
            continue

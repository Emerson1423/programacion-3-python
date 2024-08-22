class Auto:
    precio_venta= 0 
    def __init__(self, marca, modelo, año, color, motor, transmision, combustible, pais_origen, traccion, precio_compra=0):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.motor = self.Motor(motor)
        self.transmision = self.Transmision(transmision)
        self.combustible = self.Combustible(combustible)
        self.pais_origen = pais_origen
        self.traccion = self.Traccion(traccion)
        self.tipo = tipo
        self.precio_compra = precio_compra
        self.precio_venta = self.calcular_precio_venta()

    def calcular_precio_venta(self):
        # Calcula el precio de venta como un 40% más del precio de compra
        self.precio_venta = self.precio_compra * 1.4 
        return self.precio_venta

    def Motor(self, motor):
        # Mapea el valor del motor (proporcionado como una cadena) a una descripción legible
        motores = {
            "1": "V4",
            "2": "V6",
            "3": "V8",
            "4": "Eléctrico",
            "5": "Híbrido"
        }
        return motores.get(motor, "Desconocido")

    def Transmision(self, transmision):
        # Mapea el valor de la transmisión (proporcionado como una cadena) a una descripción legible
        transmisiones = {
            "1": "Automática",
            "2": "Manual"
        }
        return transmisiones.get(transmision, "Desconocida")

    def Combustible(self, combustible):
        # Mapea el valor del combustible (proporcionado como una cadena) a una descripción legible
        combustibles = {
            "1": "Gasolina",
            "2": "Diesel",
            "3": "Eléctrico",
            "4": "Híbrido"
        }
        return combustibles.get(combustible, "Desconocido")
    
    def Traccion(self, traccion):
        # Mapea el valor de la tracción (proporcionado como una cadena) a una descripción legible
        tracciones = {
            "1": "FWD (Tracción delantera)",
            "2": "RWD (Tracción trasera)",
            "3": "AWD (Tracción en las cuatro ruedas)",
            "4": "4WD (Tracción en las cuatro ruedas con reductora)"
        }
        return tracciones.get(traccion, "Desconocida")

    def mostrar_informacion(self):
        # Muestra la información del auto
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print(f"Motor: {self.motor}")
        print(f"Transmisión: {self.transmision}")
        print(f"Tracción: {self.traccion}")
        print(f"Tipo: {self.tipo}")
        print(f"Combustible: {self.combustible}")
        print(f"País de Origen: {self.pais_origen}")
        print(f"Precio de Compra: ${self.precio_compra:.2f}")
        print(f"Precio de Venta: ${self.precio_venta:.2f}")
        print("----------------------------")

# Lista para almacenar los autos
autos = []

# Bucle para ingresar información de los autos
while True:

 
        print("Ingrese las características del auto:")

        marca = input("Marca: ")
        modelo = input("Modelo: ")
        while True:
            try:
                año = int(input("año: "))
                break  # Si se ingresa un valor numérico válido, salimos del bucle
            except ValueError:
                print("Error: el año debe ser numerico. Por favor, intente de nuevo.")
        color = input("Color: ")
        print("Opciones de Motor:")
        print("1. V4")
        print("2. V6")
        print("3. V8")
        print("4. Eléctrico")
        print("5. Híbrido")
        while True:
         motor = input("Seleccione el tipo de motor (1-5): ")
         if motor in ["1", "2", "3", "4", "5"]:
            break
         else:
            print("Selección inválida. Por favor, elija una opción del 1 al 5.")

        tipo = input("Tipo (SUV/Sedán/Camioneta/etc.): ")
    # Opciones para la transmisión
        print("Opciones de Transmisión:")
        print("1. Automática")
        print("2. Manual")
        while True:
            transmision = input("Seleccione el tipo de transmisión (1-2): ")
            if transmision in ["1", "2"]:
                break
            else:
                print("Selección inválida. Por favor, elija una opción del 1 al 2.")
    
    # Opciones para la tracción
        print("Opciones de Tracción:")
        print("1. FWD (Tracción delantera)")
        print("2. RWD (Tracción trasera)")
        print("3. AWD (Tracción en las cuatro ruedas)")
        print("4. 4WD (Tracción en las cuatro ruedas con reductora)")
    
        while True:
            traccion = input("Seleccione el tipo de tracción (1-4): ")
            if traccion in ["1", "2", "3", "4"]:
                break
            else:
                print("Selección inválida. Por favor, elija una opción del 1 al 4.")
    
        while True:
            
            try:
             precio_compra = float(input("Precio de compra: "))
             break  # Si se ingresa un valor numérico válido, salimos del bucle
            except ValueError:
             print("Error: El precio de compra debe ser un número. Por favor, intente de nuevo.")
    
        print("Opciones de Combustible:")
        print("1. Gasolina")
        print("2. Diesel")
        print("3. Eléctrico")
        print("4. Híbrido")
    
        while True:
            combustible = input("Seleccione el tipo de combustible (1-4): ")
            if combustible in ["1", "2", "3", "4"]:
               break
            else:
               print("Selección inválida. Por favor, elija una opción del 1 al 4.")
        pais_origen = input("País de origen: ")
        auto = Auto(marca, modelo, año, color, motor, transmision, combustible, pais_origen, traccion, precio_compra)
        autos.append(auto)
        
        otro = input("¿Desea ingresar otro auto? (s/n): ")
        if otro.lower() != 's': break



print("\nInformación de todos los autos registrados:")
for auto in autos:
    auto.mostrar_informacion()




class DispositivoElectronico:

    marca = "PHR"
    precio_venta = 0
    ganancia = 0

    def __init__(self, producto, modelo, almacenamiento, ram, color, sistema_operativo, precio_compra=0):
        # Asigna el valor de productos usando la función Producto
        self.producto = self.Producto(producto)
        self.modelo = modelo
        self.color = color
        self.almacenamiento = almacenamiento
        self.ram = ram
        # Asigna el valor de sistemas operativo usando la función Sistema_Operativo
        self.sistema_operativo = self.Sistema_Operativo(sistema_operativo)
        self.precio_compra = precio_compra
        self.precio_venta = self.calcular_precio_venta()
      
    def calcular_precio_venta(self):
        self.precio_venta = self.precio_compra * 1.17
        return self.precio_venta
    
    def Producto(self, producto):
        # Mapea el valor del producto (proporcionado como una cadena) a una descripción legible
        productos = {
            "1": "tablet",
            "2": "computadora",
            "3": "telefono",
        }
        return productos.get(producto, "Desconocido")
    
    def Sistema_Operativo(self, sistema_operativo_id):
        # Mapea el valor del sistema operativo (proporcionado como una cadena) a una descripción legible
        sistemas_operativos = {
            "1": "Windows",
            "2": "macOS",
            "3": "Linux",
            "4": "Android",
            "5": "iOS"
        }
        return sistemas_operativos.get(sistema_operativo_id, "Desconocido")

    def cal_ganancia(self):
        self.ganancia = self.precio_venta - self.precio_compra
        return self.ganancia  
    
    def mostrar_informacion(self):
        print(f"producto: {self.producto}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"Almacenamiento: {self.almacenamiento} GB")
        print(f"Memoria RAM: {self.ram} GB")
        print(f"Sistema operativo: {self.sistema_operativo}")
        print(f"Precio de compra: ${self.precio_compra:.2f}")
        print(f"Precio de venta: ${self.precio_venta:.2f}")
        print(f"Ganancia total: ${self.cal_ganancia():.2f}")
        print("-" * 30)

dispositivos = []

while True:
    print("Opciones de productos:")
    print("1. tablet")
    print("2. computadora")
    print("3. telefono")
    while True:
        producto = input("Seleccione el tipo de producto (1-3): ")
        if producto in ["1", "2", "3"]:
            break
        else:
            print("Selección inválida. Por favor, elija una opción del 1 al 3.")
    modelo = input("Modelo: ")
    color = input("Color: ")
    almacenamiento = input("Almacenamiento (GB): ")
    ram = input("Memoria RAM (GB): ")
    # Opciones para el sistema operativo
    print("Opciones de Sistema operativo:")
    print("1. Windows")
    print("2. macOS")
    print("3. Linux")
    print("4. Android")
    print("5. iOS")
    while True:
        sistema_operativo = input("Seleccione el tipo de Sistema operativo (1-5): ")
        if sistema_operativo in ["1", "2", "3", "4", "5"]:
            break
        else:
            print("Selección inválida. Por favor, elija una opción del 1 al 5.")
    precio_compra = float(input("Precio de compra: "))
    
    dispositivo = DispositivoElectronico(producto, modelo, almacenamiento, ram, color, sistema_operativo, precio_compra)
    dispositivos.append(dispositivo)
    
    otro = input("¿Desea ingresar otro dispositivo? (s/n): ")
    if otro.lower() != 's':
        break

print("\nInformación de los dispositivos:")
for dispositivo in dispositivos:
    dispositivo.mostrar_informacion()

    
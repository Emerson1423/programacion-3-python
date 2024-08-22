
class Articulo:


    precio_Venta= 0 


    def __init__(self, tipo, descripcion, precio_Compra =0):
        self.tipo = tipo
        self.descripcion = descripcion
        self.precio_Compra = precio_Compra
        self.precio_Venta = self.calPrecio_Venta()

        if tipo == "cuaderno":
            self.marca = "HOJITAS" 
        else:
            self.marca = "RAYAS"

    def calPrecio_Venta(self):
        self.precio_Venta = self.precio_Compra * 1.30
        return self.precio_Venta
        
    def mostrar_Datos(self):
        print(f"Tipo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Descripción: {self.descripcion}")
        print(f"Precio de Compra: ${self.precio_Compra:.2f}")
        print(f"Precio de Venta: ${self.precio_Venta:.2f}")
        print("----------------------------")


# Lista para almacenar los artículos
articulos = []

# Bucle para ingresar la información de los artículos
while True:

        tipo = input("Ingrese el tipo de artículo (cuaderno/lapiz): ").lower()
        while tipo not in ["cuaderno", "lapiz"]:
            print("Tipo de artículo no válido. Por favor, ingrese 'Cuaderno' o 'Lápiz'.")
            tipo = input("Ingrese el tipo de artículo (Cuaderno/Lápiz): ").lower()
        if tipo == "cuaderno":
            descripcion = input("Ingrese la descripción del cuaderno (50 hojas/100 hojas): ").lower()
            while descripcion not in ["50 hojas", "100 hojas"]:
                print("Descripción no válida. Por favor, ingrese '50 hojas' o '100 hojas'.")
                descripcion = input("Ingrese la descripción del cuaderno (50 hojas/100 hojas): ").lower()
            precio_Compra = float(input("Ingrese el precio de compra del cuaderno: "))
        else:
            descripcion = input("Ingrese la descripción del lápiz (grafito/colores): ").lower()
            while descripcion not in ["grafito", "colores"]:
                print("Descripción no válida. Por favor, ingrese 'grafito' o 'colores'.")
                descripcion = input("Ingrese la descripción del lápiz (grafito/colores): ").lower()
            precio_Compra = float(input("Ingrese el precio de compra del lápiz: "))

        articulo = Articulo(tipo, descripcion, precio_Compra)
        articulos.append(articulo)

        otro = input("¿Desea ingresar otro artículo? (s/n): ")
        if otro.lower() == 's':
          continue
        else:
            if len(articulos) < 2:
             print("")
             print("debe ingresar almenos 2 articulos para que se muestren en pantalla ")
             print("")
             continue
            else:
                print("\nInformación de todos los artículos registrados:")
                for articulo in articulos:
                    articulo.mostrar_Datos()
                break


#hacer un progama que calcule las notas de los alumnos con sus nota final 
# teniendo en cuenta que dos notas cuestan el 30% y una el 40%
"""
def notas(n1,n2,f):

   return (n1*0.3)+(n2*0.3)+(f*0.4)

n1 = int(input("ingrese la nota 1 "))
n2 = int(input("ingrese la nota 2 "))
f = int(input("ingrese la nota del parcial  "))
notaf = notas(n1,n2,f)




print("la nota final de alumno es:", round(notaf,2))
"""


#ejecicio 2 

"""
# calcular el iba de un producto de 19% sobre el valor total de compra 
def ivac(p):
    IVA = p*0.19
    return IVA


preciocompra = float(input("ingrese el valor de la compra  "))

IVA = ivac(preciocompra)

print("el precion del producto es: ",preciocompra)

print("el precio con iva es ",round(preciocompra+IVA,2))

"""
#ejercicio 3 
# programa que calcule la tabla del 1 al 12 de cualquier numero entero dado 
"""
def tablademultiplicar(v1,v2):
    tabla= v1 * v2
    return tabla


v1 = int(input("ingrese un numero: "))

for i in range(1,13):
    print(v1, " * ", i," = ",tablademultiplicar(v1,i))

"""

def sueldoto(sueldo):



    if sueldo >= 1200:
        total = sueldo+(sueldo*0.20)
    else:
        total = sueldo + (sueldo*0.10)
    
    return total

sueldo = int(input("ingrese su sueldo sueldo: "))
    

sueldot = sueldoto(sueldo)

print("el sueldo del empleado es: ",sueldot)






def recibe_datos():
    nombre = input("Ingrese el nombre del perro: ")
    raza = input("Ingrese la raza del perro: ")
    edad = int(input("Ingrese la edad del perro en años: "))
    peso = int(input("Ingrese el peso del perro: "))
    nuevo_perro = Perro(nombre, raza, edad, peso)
    nuevo_perro.estado = "ATENDIDO"
    perros.append(nuevo_perro)

def mostrar_datos_todos():
    for perro in perros:
        perro.mostrar_datos()
        print("-" * 20)
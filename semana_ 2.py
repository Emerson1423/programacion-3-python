

#def mifuncion():
 #print("Programaicion III")

#mifuncion()



#def par(num):
    #residuo = num%2

    #if(residuo== 0):
       # print("es par")
    #else:
       # print("es impar")


#def areat(base,altura):
    #total = (base * altura)/2
    #return total




import math

def calcular_area_circulo(radio):
  area = math.pi * radio**2
  return area

def area_rombo(mayor, menor):

  area = (mayor * menor) / 2
  return area

def d(velocidad,tiempo):

  d = velocidad*tiempo
  return d






circulo = 5
area_calculada = calcular_area_circulo(circulo)
print("El área del círculo con radio", circulo, "es:", area_calculada)

mayor = 10
menor = 8
area_calculada = area_rombo(mayor,menor)
print("El área del rombo es:", area_calculada)

velcidad = 80  
tiempo = 2
distancia = d(velcidad,tiempo)
print("la distancia recorrida es :", distancia,"M/S")

suma = lambda x:x+3
print(suma(20))

suma = lambda x,y:x+y
print(suma(2,3))
resta = lambda x,y:x-y
print(resta(4,3))
multiplicacion = lambda x,y:x*y
print(multiplicacion(2,3))
divicion = lambda x,y:x/y
print(divicion(2,3))
exponete = lambda x,y:x**y
print(exponete(2,3))

modulo = lambda x,y: x%y
print(modulo(2,2))

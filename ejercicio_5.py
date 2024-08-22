
#Propuesta de Desarrollo de un Sistema de Nómina para una empresa
#Objetivo: Desarrollar un sistema de nómina automatizado que permita calcular de manera precisa y eficiente los salarios de los empleados de 
# de google, considerando las particularidades de cada contrato y cumpliendo con la legislación laboral vigente el sistema tiene que tener 
# la credencial del empleado y el nombre a la hora de mostrar el resultado final:



class Empleado:
    def __init__(self, id_empleado, nombre, horas_trabajadas, salario_por_hora, comisiones=0):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.salario_por_hora = salario_por_hora
        self.comisiones = comisiones
        self.salario_base = 0
        self.horas_extras = 0
        self.salario_total = 0
        self.deducciones = 0
        self.salario_neto = 0

    def calcular_salario_base(self):
        # Calcula el salario base según las horas trabajadas y si hay horas extras
        if self.horas_trabajadas > 40:
            self.horas_extras = self.horas_trabajadas - 40  # Calcula horas extras si se trabajaron más de 40 horas
            self.salario_base = 40 * self.salario_por_hora   # Calcula el salario base para las primeras 40 horas
        else:
            self.horas_extras = 0                             # No hay horas extras si se trabajaron 40 horas o menos
            self.salario_base = self.horas_trabajadas * self.salario_por_hora  # Calcula el salario base para todas las horas trabajadas

    def calcsalario_total(self):
        # Calcula el salario total sumando el salario base, el pago de horas extras y las comisiones
        pago_horas_extras = self.horas_extras * (self.salario_por_hora * 1.5)  # Calcula el pago por horas extras (50% más del salario por hora)
        self.salario_total = self.salario_base + pago_horas_extras + self.comisiones  # Suma el salario base, el pago de horas extras y las comisiones

    def calcdeimpuestos(self):
        # Calcula las deducciones basadas en impuestos y seguros sociales
        impuestos = self.salario_total * 0.15   # Calcula el impuesto (15% del salario total)
        seguros_sociales = self.salario_total * 0.10  # Calcula los seguros sociales (10% del salario total)
        self.deducciones = impuestos + seguros_sociales  # Suma impuestos y seguros sociales para obtener las deducciones totales

    def calcsalarioneto(self):
        # Calcula el salario neto después de deducir los impuestos y seguros sociales
        self.salario_neto = self.salario_total - self.deducciones  # Resta las deducciones del salario total para obtener el salario neto
    

    def generar_Nomina(self):
        # Imprime un recibo de pago detallado para el empleado
        print(f"Recibo de pago para: {self.nombre}")
        print(f"ID del empleado: {self.id_empleado}")
        print(f"Horas trabajadas: {self.horas_trabajadas}")
        print(f"Horas extras: {self.horas_extras}")
        print(f"Salario base: ${self.salario_base:.2f}")
        print(f"Comisiones: ${self.comisiones:.2f}")
        print(f"Salario total: ${self.salario_total:.2f}")
        print(f"Deducciones (Impuestos + Seguros): ${self.deducciones:.2f}")
        print(f"Salario neto: ${self.salario_neto:.2f}")
        print("-" * 30) 
# Lista para almacenar los empleados
empleados = []

# Función para agregar empleados
def agregar_empleado():
    id_empleado = input("ID del empleado: ")
    nombre = input("Nombre del empleado: ")
    while True:
            try:
                horas_trabajadas = float(input("Horas trabajadas: "))
                break  # Si se ingresa un valor numérico válido, salimos del bucle
            except ValueError:
                print("Error: el valor debe ser numerico. Por favor, intente de nuevo.")
    while True:
            try:
                salario_por_hora = float(input("Salario por hora: "))
                break  # Si se ingresa un valor numérico válido, salimos del bucle
            except ValueError:
                print("Error: el valor debe ser numerico. Por favor, intente de nuevo.")
    while True:
            try:
                comisiones = float(input("Comisiones: "))
                break  # Si se ingresa un valor numérico válido, salimos del bucle
            except ValueError:
                print("Error: el valor debe ser numerico. Por favor, intente de nuevo.")                        

    empleado = Empleado(id_empleado, nombre, horas_trabajadas, salario_por_hora, comisiones)
    empleado.calcular_salario_base()
    empleado.calcsalario_total()
    empleado.calcdeimpuestos()
    empleado.calcsalarioneto()

    empleados.append(empleado)

# Ciclo para ingresar empleados
while True:
    agregar_empleado()
    otro = input("¿Desea agregar otro empleado? (s/n): ")
    if otro.lower() != 's':
        break

# Generar recibos de nómina
print("\nRecibos de Nómina:")
for empleado in empleados:
    empleado.generar_Nomina()


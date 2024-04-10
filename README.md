# advanced_programming_ud
# taller 1 advanced programing a
## Author Daniel Santiago Perez Madera 13/03/2024

class Motor:
  """esta clase representa al motor"""
  def __init__(self, tipo: str, potencia: float, peso: float):
    self.tipo = tipo
    self.potencia = potencia
    self.peso = peso

class Vehiculo:
  """clase que define los vehiculo"""

  def __init__(self, motor:Motor, chasis:str, modelo:str, año :int):
    if not chasis in ["A","B"]:
      raise ValueError("el chasis no es valido")
    
    self.motor = motor
    self.chasis = chasis
    self.modelo = modelo
    self.año = año
    self.gas_consumo = 0.0

  def _calcular_consumo(self):
    """este metodo calcula el consumo de gasolina"""
    consumo=(1.1*self.motor.potencia)+ (0.2 * self.motor.peso)-(0.3 if self.chasis == "A" else 0.5)
    self.gas_consumo= consumo

class Coche(Vehiculo):
    """Definición de la clase Coche"""

    def __init__(self, motor: Motor, chasis: str, modelo: str, año: int):
        super().__init__(motor, chasis, modelo, año)

class Moto(Vehiculo):
    """Definición de la clase Moto"""
    
    def __init__(self, motor: Motor, chasis: str, modelo: str, año: int):
        super().__init__(motor, chasis, modelo, año)

class Camion(Vehiculo):
    """Definición de la clase Camión"""

    def __init__(self, motor: Motor, chasis: str, modelo: str, año: int):
        super().__init__(motor, chasis, modelo, año)

class Yate(Vehiculo):
    """Definición de la clase Yate"""

    def __init__(self, motor: Motor, chasis: str, modelo: str, año: int):
        super().__init__(motor, chasis, modelo, año)




def crear_vehiculo(tipo_vehiculo):        
 
    tipo_motor = str(input(f"Tipo de motor: "))
    potencia_motor = float(input("Potencia del motor: "))
    peso_motor = float(input("Peso del motor: "))
    chasis = input("Chasis (A o B): ")
    modelo = input("Modelo: ")
    año = int(input("Año: "))

    motor = Motor(tipo_motor, potencia_motor, peso_motor)
    vehiculo = tipo_vehiculo(motor, chasis, modelo, año)
    return vehiculo
    

def revisar_vehiculos(catalogo):
    print("Vehículos Registrados:")
    for vehiculo in catalogo:
        vehiculo._calcular_consumo()  # Calculate gas consumption before printing
        print(f"Modelo: {vehiculo.modelo}, Chasis: {vehiculo.chasis}, Motor: Tipo: {vehiculo.motor.tipo}, Potencia: {vehiculo.motor.potencia}, Peso: {vehiculo.motor.peso}, Consumo de gasolina: {vehiculo.gas_consumo}")


def menu():
    catalogo = []

    while True:
        print("\nMenú:")
        print("1. Crear Coche")
        print("2. Crear Camión")
        print("3. Crear Moto")
        print("4. Crear Yate")
        print("5. Revisar Vehículos Registrados")
        print("6. Salir")

        opcion = input("Ingrese su elección: ")

        if opcion == '1':
            catalogo.append(crear_vehiculo(Coche))
        elif opcion == '2':
            catalogo.append(crear_vehiculo(Moto))
        elif opcion == '3':
            catalogo.append(crear_vehiculo(Camion))   
        if opcion == '4':
            catalogo.append(crear_vehiculo(Yate))     
        elif opcion == '5':
            revisar_vehiculos(catalogo)
        elif opcion == '6':
            print("Saliendo del programa.")
            break


if __name__ == "__main__":
    menu()
    

from Motor import Motor

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

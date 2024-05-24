class Motor:
  """
    This class represented all Engines can contain o created for a vehicles in a catologe 

    author: Daniel Perez - May 15/2024 <dsperezm@udistrital.edu.co>
  """
  def __init__(self, tipo: str, potencia: float, peso: float):
        """
        Constructor of the class.

        Parameters:
        - name (str): Name of the engine
        - type_motor (str): Type of the engine
        - potency (int): Value of the potency
        - weight (float): Current weight of the engine
        """
        self.tipo = tipo
        self.potencia = potencia
        self.peso = peso

  def __str__(self):
        return f"Name: {self.name}   Type: {self.type_}\
            Potency: {self.potency}   Weight: {self.weight}"
  
        

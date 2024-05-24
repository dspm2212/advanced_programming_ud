from Vehicle import Coche, Moto, Camion, Yate
from Motor import Motor


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

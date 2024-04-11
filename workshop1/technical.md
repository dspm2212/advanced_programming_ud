# Technical Concerns and Decisions for Code Architecture
Purpose of the Code:
The code represents a system for managing vehicles and their specifications, such as motor type, power, weight, chassis, model, and year. It allows users to create different types of vehicles (car, truck, motorcycle, yacht) and review registered vehicles.

## Key Technical Concerns:
### Object-Oriented Design: The code utilizes object-oriented programming principles to model different types of vehicles and their characteristics. This allows for modular and reusable code, making it easier to extend and maintain.

### Input Validation: The code validates user inputs, such as chassis type and menu options, to ensure correctness and prevent unexpected errors during runtime.

### Code Readability: The code includes meaningful variable and function names, docstrings, and comments to enhance readability and maintainability.

## Architectural Decisions:
### Class Hierarchy: The code defines a class hierarchy with a base class Vehiculo and subclasses Coche, Moto, Camion, and Yate. This hierarchy allows for representing different types of vehicles while sharing common attributes and methods.

### Encapsulation: The attributes of each class are encapsulated within the class definition, ensuring data integrity and reducing the risk of unintended modifications.

### Separation of Concerns: The code separates functionalities into different functions (e.g., crear_vehiculo, revisar_vehiculos, menu), each responsible for a specific task. This separation improves code organization and readability.

### User Interaction: The code provides a simple menu-based interface (menu function) for users to interact with the system, making it intuitive and easy to use.

### Input Handling: The code handles user inputs using conditional statements (if and elif) to perform appropriate actions based on user choices. Error handling ensures graceful handling of invalid inputs.

### Modularity: The code promotes modularity by defining classes and functions with well-defined responsibilities. This modular design facilitates code reuse and makes it easier to maintain and extend the system in the future

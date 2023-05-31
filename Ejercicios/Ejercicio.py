#Hacer una clase y método en la cual debo tener una habilidad
"""class Persona:
    def __init__(self, Nombre, edad, carrera):
        self.Nombre = Nombre
        self.edad = edad
        self.carrera = carrera
    def habilidad (self):
        return f"Yo soy {self.Nombre} y mi habilidad es ser pasiente"
    def __str__ (self):
        return self.habilidad()
    
persona1 = Persona ("Pamela",20,"TIC")
print (persona1)
print (persona1.edad)
print (persona1.habilidad())

class Padre:
    def __init__(self, nombre) -> None:
        pass
    """
#Super
"""class hijo(Padre):
    def __init__(self, nombre, profecional) -> None:
        super().__init__(nombre)
        self.profecional="""
        
"""class Madre:
    def __init__(self, apellidoMaterno) -> None:
        self.apellidoMaterno = apellidoMaterno
class Padre:
    def __init__(self, apellidoPaterno) -> None:
        self.apellidoPaterno = apellidoPaterno
        
class Hijo (Madre, Padre):
    def __init__(self, apellidoMaterno, apellidoPaterno) -> None:
        super().__init__(apellidoMaterno, apellidoPaterno)

Pedro = Hijo ("Carriel", "Mier")
print (Pedro.apellidoMaterno)"""

"""class Abuelo:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
class Padre (Abuelo):
    def __init__(self, nombre, profesion) -> None:
        super().__init__(nombre)
        self.profesion = profesion
    def habilidad(self):
        return f"Yo puedo cantar"
class Hijo (Padre):
    def __init__(self, nombre, profesion) -> None:
        super().__init__(nombre, profesion)
Juan = Hijo ("Juan", "Programador")
print(Juan.nombre)
print (Juan.habilidad())
print(Juan.profesion)"""

class Animales:
    def __init__(self, Caninos, felinos) -> None:
        self.Caninos = Caninos
        self.felinos = felinos

class Hogar (Animales):
    def __init__(self, Caninos, felinos) -> None:
        super().__init__(Caninos, felinos)

    def __str__(self):
        return f"En mi casa hay {self.Caninos} perros y hay {self.felinos} gatos"

Cantidad = Hogar (2,5)
print(Cantidad.Caninos)
print(Cantidad.felinos)
print(Cantidad)
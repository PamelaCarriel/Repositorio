#Universidad de las Fuerzas Armadas - ESPE
#Implementar una cola utilizando una lista  
#Autor: Pamela Jesabel Carriel Mier
#Fecha: 31 de mayo del 2023
class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, elemento):
        self.items.append(elemento)

    def desencolar(self):
        if self.esta_vacia():
            return None
        return self.items.pop(0)

# Ejemplo de uso
cola = Cola()
cola.encolar(5)
cola.encolar(4)
cola.encolar(3)

while not cola.esta_vacia():
    elemento = cola.desencolar()
    print(elemento)

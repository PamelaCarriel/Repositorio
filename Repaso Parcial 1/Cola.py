#Crea una Cola que permita almacenar números enteros y realiza las operaciones de encolar y desencolar
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
cola.encolar(1)
cola.encolar(2)
cola.encolar(3)

while not cola.esta_vacia():
    elemento = cola.desencolar()
    print(elemento)

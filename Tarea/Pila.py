#Universidad de las Fuerzas Armadas - ESPEc
#Implementar una pila utilizando una lista 
#Autor: Pamela Jesabel Carriel Mier
#Fecha: 31 de mayo del 2023
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if self.esta_vacia():
            return None
        return self.items.pop()

# Ejemplo de uso
pila = Pila()
pila.apilar(5)
pila.apilar(9)
pila.apilar(2)

while not pila.esta_vacia():
    elemento = pila.desapilar()
    print(elemento)

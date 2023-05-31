#Implementa una Pila utilizando una estructura de datos adecuada y realiza las operaciones de apilar y desapilar. 
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

    def obtener_tope(self):
        if self.esta_vacia():
            return None
        return self.items[-1]

# Ejemplo de uso
pila = Pila()
pila.apilar('a')
pila.apilar('b')
pila.apilar('c')

print("Tope de la pila:", pila.obtener_tope())

while not pila.esta_vacia():
    elemento = pila.desapilar()
    print("Elemento desapilado:", elemento)

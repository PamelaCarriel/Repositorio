#Universidad de las Fuerzas Armadas - ESPE
#Verificar si una lista es simétrica.
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

def es_simetrica(lista):
    pila = Pila()
    mitad = len(lista) // 2
    for i in range(mitad):
        pila.apilar(lista[i])

    if len(lista) % 2 == 1:
        inicio = mitad + 1
    else:
        inicio = mitad

    for i in range(inicio, len(lista)):
        if lista[i] != pila.desapilar():
            return False

    return True

# Ejemplo de uso
lista1 = [1, 2, 3, 3, 2, 1]
lista2 = [1, 2, 3, 4, 5, 6]

print(es_simetrica(lista1))  
print(es_simetrica(lista2))  

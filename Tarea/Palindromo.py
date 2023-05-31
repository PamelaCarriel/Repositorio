#Universidad de las Fuerzas Armadas - ESPE
#Verificar si una palabra es un palíndromo utilizando una pila 
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

def es_palindromo(palabra):
    pila = Pila()
    for letra in palabra:
        pila.apilar(letra)

    palabra_invertida = ""
    while not pila.esta_vacia():
        palabra_invertida += pila.desapilar()

    return palabra == palabra_invertida

# Ejemplo de uso
palabra1 = "radar"
palabra2 = "python"

print(es_palindromo(palabra1))  
print(es_palindromo(palabra2))  
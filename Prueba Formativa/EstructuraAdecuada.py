#Universidad de las Fuerzas Armadas - ESPE
#Una estructura de datos adecuada para implementar una Pila
#Autor: Pamela Jesabel Carriel Mier
#Fecha: 02 de junio del 2023
class Pila:
    #Constructor
    def __init__(self):
        self.pila = []
    #Verifica si la pila está vacía
    def esta_vacia(self):
        return len(self.pila) == 0
    #Agrega un elemento en la parte superior de la pila.
    def apilar(self, elemento):
        self.pila.append(elemento)
    # Elimina y devuelve el elemento en la parte superior de la pila.
    def desapilar(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.pila.pop()
    #Devuelve el elemento en la parte superior de la pila sin eliminarlo.
    def tope(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.pila[-1]
#Ponemos la pila que deseamos
mi_pila = Pila()
mi_pila.apilar(5)
mi_pila.apilar(8)
mi_pila.apilar(6)
mi_pila.apilar(3)
mi_pila.apilar(12)

print("Mi último digito de mi pila es:")
print(mi_pila.tope()) 
print ("Desapilamos el ultimo dijito de mi pila (Método LIFO):")
print(mi_pila.desapilar()) 
print("La verificación de que mi número se desapilo, mediante verificacion de mi nuevo último digito de la pila:")
print(mi_pila.tope())  

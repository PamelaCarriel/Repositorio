#Universidad de las Fuerzas Armadas - ESPE
#implementar una Cola utilizando una Lista en Python
#Autor: Pamela Jesabel Carriel Mier
#Fecha: 02 de junio del 2023
class Cola:
    def __init__(self):
        self.cola = []
    #Verifica si la cola está vacia 
    def esta_vacia(self):
        return len(self.cola) == 0
    #Agrega un elemento al final de la cola.
    def encolar(self, elemento):
        self.cola.append(elemento)
    #Elimina y devuelve el elemento del frente de la cola.
    def desencolar(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self.cola.pop(0)
    #Devuelve el elemento del frente de la cola sin eliminarlo.
    def frente(self):
        if self.esta_vacia():
            raise IndexError("La cola está vacía")
        return self.cola[0]

mi_cola = Cola()
mi_cola.encolar(4)
mi_cola.encolar(5)
mi_cola.encolar(7)
mi_cola.encolar(6)
mi_cola.encolar(9)
mi_cola.encolar(2)

print ("Mi primer digito de mi cola es:")
print(mi_cola.frente())  
print ("Desencolamos el primer digito de mi cola (Método FIFO):")
print(mi_cola.desencolar())  
print ("La verificación de que mi número se desencolo, mediante verificacion de mi nuevo primer digito de la cola:")
print(mi_cola.frente()) 

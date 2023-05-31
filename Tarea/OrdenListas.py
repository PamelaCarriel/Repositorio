#Universidad de las Fuerzas Armadas - ESPEc
#Verificar si una lista está ordenada de forma ascendente 
#Autor: Pamela Jesabel Carriel Mier
#Fecha: 31 de mayo del 2023
elementos = input("Ingrese los elementos de la lista separados por espacios: ").split()

def esta_ordenada_ascendente(elementos):
    for i in range(len(elementos) - 1):
        if elementos[i] > elementos[i + 1]:
            return False
    return True

print(esta_ordenada_ascendente(elementos))

#Universidad de las Fuerzas Armadas - ESPE
#Complejidad temporal de la operación de búsqueda en una Lista
#Autor: Pamela Jesabel Carriel Mier
#Fecha: 02 de junio del 2023
def Elemento_de_Busqueda(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

lista1 = [1, 2, 3, 4, 5]
elementoEspecifico = 7
indice = Elemento_de_Busqueda(lista1, elementoEspecifico)
if indice != -1:
    print(f"El elemento {elementoEspecifico} se encuentra en la posición {indice} de mi lista 1.")
else:
    print(f"El elemento {elementoEspecifico} no se encuentra en la lista.")

lista2 = [1, 5, 6, 8, 10]
elementoEspecifico1 = 10
indice = Elemento_de_Busqueda(lista2, elementoEspecifico1)
if indice != -1:
    print(f"El elemento {elementoEspecifico1} se encuentra en la posición {indice} de mi lista2.")
else:
    print(f"El elemento {elementoEspecifico1} no se encuentra en la lista.")
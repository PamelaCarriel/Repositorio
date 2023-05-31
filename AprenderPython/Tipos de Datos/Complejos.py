lista = []

print(type(lista))

lista = ["Ecuador","Colombia","Brasil"]
print(lista)

lista = ["Juan",45,6.5,True,["Ecuador","Colombia","Brasil"],"a"]
print(lista)

lista = ["Ecuador","Colombia","Brasil"]
lista.append("Mexico")
print(lista)

#Copia una lista
lista2 = lista.copy()
print(lista2)

#Borra la lista
lista2.clear()
print(lista2)

#Agregar elemento a la lista
lista2 = lista.copy()
print(lista2.count("Colombia"))
lista2.append("Bolivia")
lista2.append("Colombia")

#Contar cuantos elementos seleccionados hay en una lista
print(lista2.count("Colombia"))
print(lista2)

#Contar cuantos elementos totales hay en una lista
print(len(lista2))

#Posicion de un elemento en una lista
print(lista2[3])
print(lista2[1])
print(lista2[4])
lista2[5] = "Peru"
print(lista2)

#Eliminar elementos de una lista
lista2.pop()
print(lista2)

lista2.remove("Brasil")
print(lista2)

#Voltear una lista
lista2.reverse()
print(lista2)

#Ordenar una lista
lista2.sort()
print(lista2)

lista3 = ["d","B","b","c"]
lista3.sort()
print(lista3)
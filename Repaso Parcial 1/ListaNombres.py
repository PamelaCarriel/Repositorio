#Escribe un programa que permita crear una lista de nombres y luego muestre los nombres en orden alfabético.
Nombre = input("Ingrese los nombres separados por espacios: ")
listaNombre = sorted(Nombre.split())
print(listaNombre)
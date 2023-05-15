#Universidad de las Fuerzas Armadas-Espe
#Nombre del autor: Pamela Jesabel Carriel Mier
#Fecha: 14/mayo/2023
#Ejecuta la suma de la lista de numeros 
from MCD import mcd 
from MCM import mcm
from NumeroElementos import NumeroLista
from Potencia import potencia 
from SumaDeNumeros import sum_list


MaxDivisor1 = mcd(3,5)
print ("El minimo comun divisor de los numeros 3 y 5 es:")
print(MaxDivisor1)

MaxDivisor2 = mcd(7,0)
print ("\nEl minimo comun divisor de los numeros 7 y 0 es:")
print(MaxDivisor2)

MinMultiplo1 = mcm(5,6)
print("\nEl maximo comun multipo de los numero 5 y 6 es:")
print(MinMultiplo1)

MinMultiplo2 = mcm(8,3)
print("\nEl maximo comun multipo de los numero 8 y 3 es:")
print(MinMultiplo2)

NumeroLista1 = NumeroLista ([3,5,6,7,8])
print ("\nEl numero de elemento que tiene la siguiente lista [3,5,6,7,8] es:")
print (NumeroLista1)

NumeroLista2 = NumeroLista ([4,6,7,8,92,3,4,5])
print ("\nEl numero de elemento que tiene la siguiente lista [4,6,7,8,92,3,4,5] es:")
print (NumeroLista2)

Potencia1 = potencia (3,4)
print("\nLa potencia del numero 3 con exponente 4 es:")
print(Potencia1)

Potencia2 = potencia (4,0)
print("\nLa potencia del numero 4 con exponente 0 es:")
print(Potencia2)

Suma1 = sum_list([6,6,4,4])
print ("\nLa suma de la lista de numeros: 6,6,4,4 es:")
print(Suma1)

Suma2 = sum_list([2,4,5,6])
print ("\nLa suma de la lista de numeros: 2,4,5,6 es:")
print(Suma2)
#Similar a las listas
#Tipo de dato compuesto no mutable, genera inconvenientes 

tupla = ()
print(type(tupla))

tupla2 = ("Juan", "Pedro", "Maria", "Juan")
print(tupla2)

print(tupla2.count("Juan"))
#Da la posición
print(tupla2.index("Maria"))

#ctrl k ctrl c ---- Comenta 
#ctrl k ctrl u -----descomenta

print(tupla2[2])
print(tupla2[3])

#Transformar una tupla en lista ()
lista = list(tupla2)
print(type(lista))

lista.append("Mario")
print(lista)
#Transformar una lista en una tupla
tupla2 = tuple(lista)
print(type(tupla2))
print(tupla2)


#RANGE
rango = range(6)
print(rango)

#SET
set = {2, 3, 5, 6, 6}
print(set)

#metodos http
#http cats


#DICCIONARIOS
#objetos jason constuccion de elementos en una estructura

cliente001 = {
    "Nombre" : "Pamela",
    "Cedula" : 1724250798,
    "Celular" : "0980027171",
    "Correo" : "pjcarriel@espe.edu.ec"
}
print(cliente001)

#Acceder a un valor 
print(cliente001["Correo"])

print(cliente001.get("Nombre"))

#actualiza cualquier dato que quiera 
cliente001["Nombre"] = "Jesabel"
print(cliente001.get("Nombre"))
print(cliente001)
cliente001["Celular"] = "0994938938"
print(cliente001.get("Celular"))
print(cliente001)

print (len(cliente001))

cliente001["estado civil"] = "Soltero"
print (cliente001)

#Elimina el ultimo elemento
cliente001.popitem()
print (cliente001)
#Otra forma 
cliente001.pop("Celular")
print(cliente001)
#
del cliente001["Cedula"]
print(cliente001)

#COPIAS DE DICCIONARIOS 

cliente002 = dict(cliente001)
print(cliente002)


## Ejercicios ##

dato = input("Por favor ingrese algo:")
print(dato)

lista =  ["Hola", "Mundo"]
if lista.count(dato)> 0 :
    print("Esta informacion existe", dato)
else: 
    print("Esta información no existe", dato)


Primer = input("Ingrese el primer numero:")
Segundo = input("Ingrese el segundo numero:")
Numero1= int (Primer)
Nuemro2= int (Segundo)
print(Numero1+ Nuemro2)

"""personas=["Juan", "Maria", "Pedro"]
edades = [5, 27, 14]

for persona in personas:
    for edad in edades:
        print(persona, edad)"""
        
personas=["Juan", "Maria", "Pedro"]
edades = [5, 27, 14]

for i in range(len(personas)):
    print(personas[i], edades[i])

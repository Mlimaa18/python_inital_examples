"""# Listas
lista1 = [1,2,3,4,5,6,7]
print(lista1)

lista2 = ["a", "b", "c"]
print(lista2)
print(type(lista2))

lista3 = [True, False, True]
print(lista3)

lista4 = [1, "a", 2 , True, 12.4]
print(lista4)

#slice
print(lista1[0:2])
lista_nueva = lista1[0:2]
print(lista_nueva)

#Mutabilidad
lista1[0] = 0
print(lista1)

#copiar listas
lista5 = lista1[:] #Crea una copia de lista 1 pero lo guarda en otro espacio de memoria, si no se pone el corchete se modificaria para ambas tablas
lista5[1] = "torta"

print(lista1)
print(lista5)

print(len(lista1))

#Agregar elementos a las listas
lista1.append(8)
print(lista1)
lista1.insert(0, "cero")
print(lista1)

lista1.extend([9,10])
print(lista1)

#Eliminar elementos
lista1.pop()
print(lista1)

lista1.remove("cero")
print(lista1)

print(lista1.pop(0))
print(lista1)

#index y si el valor existe en la lista
#print(lista1.index(90))

print(90 in lista1)
print(9 in lista1)

lista1.append(3)
print(lista1)

#Ocurrencias de un valor dentro de una lista
print(lista1.count(30))

#Ordenamiento de los arreglos
lista7 = [2,5,7,4,1,10,20]
print(lista7)

#Invierte el valor de los indices
lista7.reverse()
print(lista7)

#Ordena elementos de menor a mayor
lista7.sort()
print(lista7)

#Invierte el orden sin usar reverse
print(lista7[::-1])

#Generar una lista automatica
lista8 = list(range(1,101))
print(lista8)


#unpacking list
a, b, c = [1,2,3]
print(a,b,c)
print(a+b+c)

d, e, f, *resto = lista8
print(d)
print(e)
print(f)
print(resto)

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matriz)

tensor = [
    [[1,2,3],[4,5,6],[7,8,9]],
    [[10,11,12],[13,14,15],[16,17,18]]
]

print(tensor)"""

#Diccionarios
dict1 = {"nombre": "carlitos"}
print(dict1)
print(dict1["nombre"])

print(dict1.get("nombre"))
print(dict1.get("edad"))
print("nombre" in dict1)
#Si no existe le asigna el valor
print(dict1.get("edad",10))
dict2 = dict(nombre= "tommy")
print(dict2)

dict3 = {
    "nombre": "pedro",
    "edad": 3,
    "genero": "masculino",
    "estatura": "80.5"
}

print(3 in dict3.values())
print("genero" in dict3.keys())
#Busca si existe la tupla completa
print(("nombre","pedro") in dict3.items()) 
dict3.pop("genero")
print(dict3)

lista9 = [
    {
        "marca": "Ford",
        "modelo": "chevy"
    },
    {
        "marca": "Nissan",
        "modelo": "tsuru"
    },
    {
        "marca": "Volkswagen",
        "modelo": "sedan"
    }
]

print(lista9)
print(len(dict3))
print(type(dict3))

#tupla
#Es una especie de arreglo al que no se le acepta hacer modificaciones
tupla = (1,2,3,4,5)
print(tupla)
print(type(tupla))

otraLista = list(tupla)
print(otraLista)
print(type(otraLista))

#Conjuntos
conjunto = {11, 11, 2, 4, 7, 3, 9, 10, 4}
print(conjunto)
conjunto1= {11, 11, 2, 4, 7, 3, 9, 10, 4, 12, 13}

conjunto2 = {"miguel angel", "donatelo", "rafael", "leonardo"}
conjunto3 = {"miguel angel", "donatelo", "rafael", "leonardo", "boticeli"}
print(conjunto3.difference(conjunto2))

conjunto3.add("velazquez")
print(conjunto3)

print(conjunto3.intersection(conjunto2))

conjunto4 = conjunto2.union(conjunto3)

print(conjunto4)
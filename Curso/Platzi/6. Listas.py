number = [1,5,10,55,6,8,90]
print(type(number))

typesList = [1, True, "Carlos", 2.5]
print(typesList)
print(type(typesList))

print(typesList[::-1])

typesList[0] = 80
print(typesList)

print("Carlos" in typesList)

# agregar un elemento al final de la lista
number.append(100)
print(number)

# agregar elementos y establecer en una posicion
number.insert(2, "nuevo elemento en la poscion 2")
print(number)

# unir listas
new_list = number + typesList
print(new_list)
# saber en que posicion esta un elemento
print(new_list.index("Carlos"))

#eliminar elemento de una lista
new_list.remove(80)
print(new_list)

# POP elemina el ultimo elemento de la lista si no se coloca nada
new_list.pop()
print(new_list)

# dar la vuelta a la lista
new_list.reverse()
print(new_list)

# ordenar una lista
number2 = [1,5,10,55,6,8,98,50]
print(number2)
number2.sort()
print(number2)

"""
Métodos de las listas

append(): Añade un ítem al final de la lista.
clear(): Vacía todos los ítems de una lista.
extend(): Une una lista a otra.
count(): Cuenta el número de veces que aparece un ítem.
index(): Devuelve el índice en el que aparece un ítem (error si no aparece).
insert(): Agrega un ítem a la lista en un índice específico.
pop(): Extrae un ítem de la lista y lo borra.
remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.
reverse(): Le da la vuelta a la lista actual.
sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor.    
"""

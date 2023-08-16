'''
Se itera de acuerdo a un numero de condiciones dadas por algún elemento

En un while no tenemos claro el número de iteraciones que vamos a realizar, mientras que en un for iteramos sobre un conjunto de datos, sea una lista, un rango, un diccionario.
'''

# Imprime los numeros del 0 al 20 (cuando no se indica el valor inicial)
for element in range(20):
    print(element)

print("*" * 20)

# Imprime los números de 1 al 20, porque el extremo final no se incluye
for element in range(1, 21):
    print(element)

print("*" * 20)

# Iterar los elementos de la lista
my_list = [23, 45, 67, 89, 43]
for element in my_list:
    print(element)

print("*" * 20)

# Iterar los elementos de una tupla
my_tuple = ("Sara", "Nico", "Freddy")
for element in my_tuple:
    print(element)

print("*" * 20)

# Iterar los elementos de un diccionario
product = {
  "name": "Camisa", 
  "price": 100, 
  "stock": 89
}

# Itera sobre las llaves
for key in product:
    print(key)

print("*" * 20)

# Itera sobre los valores
for key in product:
    print(product[key])

print("*" * 20)

for key in product:
    print(key, "=>", product[key])

print("*" * 20)

for key, value in product.items():
    print(key, "=>", value)

print("*" * 20)

# Iterar en lista de diccionarios
people = [
  {
    "name": "Nico",
    "age": 34
  },
  {
    "name": "Sara",
    "age": 30
  },
  {
    "name": "Freddy",
    "age": 38
  }
]

for person in people:
  print(person)

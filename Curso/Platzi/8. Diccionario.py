#Los diccionarios se compones de llave, valor.
# muy similares a un archivo .json
my_dict = {
    'avion': 'objeto volador',
    'name': 'Javier',
    'last_name': 'Sepulveda',
    'age': 109
}

print(my_dict)

#el tamanio del diccionario
print(len(my_dict))

#imprimiendo una llave 
print(my_dict['age'])

#La funcion get, si no existe el valor sale un mensaje none(Maneja el error)
# Se cambian los corchetes por parentesis(), ya que get es una funcion de python
print(my_dict.get('test'))

print('name' in my_dict)
print('other' in my_dict)

print(my_dict.items())

for clave, valor in my_dict.items():
    print(clave, "=>", valor )

# [ ] = Listas
# ( ) = Tuplas
# { } = Diccionarios

# https://docs.hektorprofe.net/python/metodos-de-las-colecciones/metodos-de-los-diccionarios/

person= {
  'name': 'Camilo',
  'last_name': 'Rico',
  'langs': ['python', 'javascript'],
  'age': 99
}

print(person)

person['name']='Camilo Andres'
person['age']-=50
person['langs'].append('rust')
print(person)
# una forma de eliminar
del person['last_name']
# otra forma de eliminar
person.pop('age')
print(person)


print(person.items())
print(person.keys())
print(person.values())
print(person.clear())

# Python Dictionary Methods 
abc = {'A': 1, 'B': 2, 'C':3}
abc['A'] # 1
#abc.clear() # {} empties dictionary
abc.get('C') # 3 
abc.update({'D':4}) # {'A': 1, 'B': 2, 'C':3, 'D': 4}   
print(abc)
# https://www.w3schools.com/python/python_dictionaries_methods.asp

person = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'age': 29
}
keys = []
values = []
# Escribe tu solución 👇
person.update({'twitter':"@nicobytes"})
person['name'] = "Felipe"
del person['age']


for key in person.keys():
    keys.append(key)
for value in person.values():
    values.append(value)

#print(keys)
#print(values)

k = list(person.keys())
print(k)
#print(list(person.values()))
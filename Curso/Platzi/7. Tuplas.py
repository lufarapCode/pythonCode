numbers = (1, 2, 3, 5)
strings = ('nico', 'zule', 'santi','nico')
print(numbers)
#Primer elemento
print('0 =>', numbers[0])
#Último elemtno
print('-1 =>', numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

'''
Una tupla es inmutable, es decir, 
no se puede modificar
'''

print(strings.index('zule'))
print(strings.count('nico'))

my_list = list(strings)
print(my_list)
print(type(my_list))

my_list[1] = "juli"
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)
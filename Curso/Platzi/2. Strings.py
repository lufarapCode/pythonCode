
# Manejo de Strings

nombre = "Luis"
edad = 26

print("Me llamo " + nombre + " tengo ", edad, " años de edad")
print(f"Me llamo {nombre} y tengo {edad} de edad.")

n = ("096754375")
#print(n[::2])
print(n[::3])

# find the position
print (n.find("6"))

f = "You are wrong"
print(f.upper())

#Consider the variable g, and find the first index of the sub-string snow:
g = "Mary had snow a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"

print (g.find("snow") )

# In the variable g, replace the sub-string Mary with Bob:
print (g.replace( "Mary", "Bob") )

# How do you access the last element of the following tuple: A=(0,1,2,3)? 
a = (0, 1, 2, 3)
print(a[-1])

# Consider the list: B=["a","b","c"]. What is the result of the following B[1:]?
B=["a","b","c", "d", "r", "f"]
print (B[4:])  # Si no pongo nada despues de los 2 puntos significa hasta el ultimo caracter


texto = 'Este es un texto de como programar en Python'
print("Java" in texto)

size = len(texto)
print(size)

print(texto.count('e'))
print(texto.swapcase())
print(texto.replace("Python", "Java"))
# acceder a la posicion del texto
print(texto[2])
print(texto[size-1])
print(texto[::-1])
print(texto[0:6])
print(texto[38:size])
print(texto[10:])

# Variables en Python
nombre = "Luis"
edad = 26
peso = 90.5
altura = 1.75
estado_civil = False

print("Me llamo ", nombre, " tengo ", edad, " años de edad. Mido ", altura, "m de altura y peso ", peso, "kg")
nombreB = input("¿Y tú como te llamas ? ")

print("Mucho gusto, ", nombreB, "! \n")

print("Ver el tipo de la variable")
print(type(nombre))
print(type(edad))
print(type(peso))
print(type(altura))
print(type(estado_civil))
print("El input siempre sera un String -> ", type(nombreB))

# Cast de variables
edadCast = float(edad)
nombreBCast = int(nombreB)
print(edadCast)
print(nombreBCast)
print(type(nombreBCast))


"""
In Python, the data type is set when you assign a value to a variable:

Example	Data Type	Try it
x = "Hello World"	str	
x = 20	            int	
x = 20.5	        float	
x = 1j	            complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	                    range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	        bool	
x = b"Hello"	    bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	
x = None	NoneType	

"""

"""
    --- Tipos de datos primitivos -- 
Integers: números Enteros
Floats: números de punto flotante (decimales)
Strings: cadena de caracteres (texto)
Boolean: boolenaos (Verdadero o Falso)

    -- Tipos de dato adicionales -- 
Datos en texto: str
Datos numéricos: int, float, complex
Datos en secuencia: list, tuple, range
Datos de mapeo: dict
Set Types: set, frozenset
Datos booleanos: bool
Datos binarios: bytes, bytearray, memoryview
"""
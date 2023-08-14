"""
    Hash Tables
In computing, hash tables are one of the most important data structures that resemble 
dictionaries in the Python programming language. A hash table is based on the concept of 
hashing which provides a way to store and retrieve 
data efficiently in the complexities of time and space.

The concept of hash tables is widely used in applications such as:

Database indexing
Compiler design
Caching
Password authentication
Error analysis and many more.

Hash tables are based on the concept of hash, which means using a hash function used to
map key and values. Since it is used to map key and value pairs, it is commonly known as 
a hashmap.
"""

class Hashtable:
    def __init__(self, size):
        # Inicializa la clase Hashtable con un tamaño de bucket dado
        self.bucket_size = size
        self.buckets = [[] for _ in range(self.bucket_size)]

    def assign_buckets(self, key, value):
        # Asigna una clave y su valor a un bucket en la tabla hash
        hash_value = hash(key)
        index = hash_value % self.bucket_size
        self.buckets[index].append((key, value))

    def get_value(self, key):
         # Obtiene el valor asociado a una clave en la tabla hash
        hash_value = hash(key)
        index = hash_value % self.bucket_size
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return None

# Crear una instancia de la clase Hashtable con un tamaño de bucket de 10
student_table = Hashtable(10)

# Agregar estudiantes a la tabla hash
student_table.assign_buckets("S001", {"name": "John Doe", "age": 20, "major": "Computer Science"})
student_table.assign_buckets("S002", {"name": "Jane Smith", "age": 21, "major": "Engineering"})
student_table.assign_buckets("S003", {"name": "Mike Johnson", "age": 19, "major": "Mathematics"})

# Obtener información de un estudiante específico
student_id = "S002"
student_info = student_table.get_value(student_id)
if student_info:
    print("Información del estudiante:")
    print("ID:", student_id)
    print("Nombre:", student_info["name"])
    print("Edad:", student_info["age"])
    print("Carrera:", student_info["major"])
else:
    print("No se encontró información para el estudiante con ID:", student_id)

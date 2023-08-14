
from time import process_time_ns


tuple1 = ("disco",10,1.2 )
print(tuple1)
# print(type(tuple1))

print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

# We can print out the type of each value in the tuple:     
print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))

# We can concatenate or combine tuples by using the + sign:

tuple2 = tuple1 + ("hard rock", 1,5)
print(tuple2)

#print(tuple2[3:6])
print( len(tuple2))

# We can sort the values in a tuple and save it to a new tuple:

tuplalist = (5,12,85,5,6,3,1,0,8)

listSorted = sorted(tuplalist)
print (listSorted)


# Nested Tuple
# A tuple can contain another tuple as well as other more complex data types. 
# This process is called 'nesting'. Consider the following tuple with several elements:

NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))

print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])


print("Element 2, 0 of Tuple: ",   NestedT[2][0])
print("Element 2, 1 of Tuple: ",   NestedT[2][1])
print("Element 3, 0 of Tuple: ",   NestedT[3][0])
print("Element 3, 1 of Tuple: ",   NestedT[3][1])
print("Element 4, 0 of Tuple: ",   NestedT[4][0])
print("Element 4, 1 of Tuple: ",   NestedT[4][1])

print( NestedT[2][1][3] )
print( NestedT[4][1][1] )

# 

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", "R&B", "progressive rock", "disco") 
print ( len (genres_tuple))
print ( genres_tuple[3])

print ( genres_tuple[3:6])

print ( genres_tuple[0:2])

# Find the first index of "disco":
print ( genres_tuple[7][0])

print(genres_tuple.index("disco"))

C_tuple=(-5, 1, -3)

tupleSort = sorted(C_tuple)
print (tupleSort)
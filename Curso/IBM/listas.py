
from time import process_time_ns


L = ["Michael Jackson", 10.1, 1982]

""""
print('the same element using negative and positive indexing:\n Postive:',L[0],
'\n Negative:' , L[-3]  )
print('the same element using negative and positive indexing:\n Postive:',L[1],
'\n Negative:' , L[-2]  )
print('the same element using negative and positive indexing:\n Postive:',L[2],
'\n Negative:' , L[-1]  )

"""

# # Use extend to add elements to list

L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])

print (L)

# Each time we apply a method, the list changes. If we apply extend we add two new elements to the list. The list L is then modified by adding two new elements:
# If we append the list ['a','b'] we have one new element consisting of a nested list:

# If we append the list ['a','b'] we have one new element consisting of a nested list:
L.append(["a", 5])

print (L)
#  As lists are mutable, we can change them. For example, we can change the first element as follows:
A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)

# We can also delete an element of a list using the del command:

print('Before change:', A)
del(A[0])
print('After change:', A)

# We can convert a string to a list using split. For example, the method split translates every group of 
# characters separated by a space into an element in a list:
print ('hard rock'.split())

#We can use the split function to separate strings on a specific character which we call a delimiter. 
# We pass the character we would like to split on into the argument, which in this case is a comma. The result is a list, 
# and each element corresponds to a set of characters that have been separated by a comma:
print ('A;B;C;D'.split(';'))

A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)

#print('B[0]:', B[0])
#A[0] = "banana"
#print('B[0]:', B[0])



# You can clone list A by using the following syntax:
# B = A[:], al colocar de esta manera se clona la lista y no se obtiene el resultado inesperado anterior
# ya que si cambio algo en la lista A no se vera afectado en la lista B 

 
B = A[:]
print (B)

print('B[0]:', B[0])
A[0] = "hard rocky"
print('B[0]:', B[0])
print('A[0]:', A[0])

# Create a list a_list, with the following elements 1, hello, [1,2,3] and True.

a_list = [1, "hello", [1,2,3] , True]
print (a_list[1])
print (a_list[2])
print (a_list[1:4])

# Concatenate the following lists A = [1, 'a'] and B = [2, 1, 'd']

A = [1, 'a']
B = [2, 1, 'd']

#A.append(B)
A.extend(B)
#C = A + B

print(A)
#print(C)

L.append(['a','b'])
# SORT
B = [5,2,6,8,1]
B.sort()
print (B)

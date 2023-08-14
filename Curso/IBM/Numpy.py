from turtle import shape
import numpy as np
from pandas import array
a=[1,2,3,4,5]

"""x = np.array(a)
print (type(x))

print (x.shape)
print (x.dtype)
print (x.mean())"""

print (np.array([1,-1])*np.array([1,1]))
np.array([1,-1])*np.array([1,1])

print (np.dot(np.array([1,-1]),np.array([1,1])))


a = ["0", 1, "two", "3", 4]

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

# Create a numpy array
b = [0, 1, 2, 3, 4]

a = np.array([0, 1, 2, 3, 4])
print(a)
print(b)

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

print(np.__version__)
print (type(a))
print (type(b))

print (a.dtype)

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])
print(arr[:4])
print(arr[4:])

print (arr.ndim)
print (arr.shape)
print (arr.mean())

max_A = arr.max()
print (max_A)

min_A = arr.min()
print (min_A)

# # Get the standard deviation of numpy array
standard_deviation=arr.std()
print (standard_deviation)

# Array Addition

u = np.array([1, 0])
v = np.array([0, 1])

z = np.add(u, v)
print (z)

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

arr3 = np.add(arr1, arr2)
print (arr3)


b = np.array([5, 10, 15])
a = np.array([10, 20, 30])
c = np.subtract(a, b)

print(c)

z = np.multiply(b,a)
print (z)
c = np.divide(b, a)
print (c)

#Dot Product

X = np.array([1, 2])
Y = np.array([3, 2])

W = np.dot(X, Y)

print (W)

# Adding Constant to a Numpy Array
u = np.array([1, 2, 3, -1]) 
f = u + 1

print (f)

print (np.pi)


arr1 = np.array([1, 2, 3])
print(arr1)

for x in arr1:
  print(x)


a=np.array([0,1])

b=np.array([1,0])

h = np.dot(a,b)
print (h)



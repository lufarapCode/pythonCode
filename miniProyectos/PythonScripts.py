# 1. Use of set and combinate with join ------------------------

my_string = "hola"
sett= {"hola", "hola2", "hola3"}
# converting the string to a set, set is unordered
temp_set = set("hola")
print(sett)
# stitching set into a string using join
new_string = ''.join(sett)
print(new_string)


# 2 Using rhe Title Case (First Letter Caps) -----------------------
my_string = "my name is chaitanya baweja"

# using the title() function of string class
new_string = my_string.title()

print(new_string)

# Output
# My Name Is Chaitanya Baweja


# 3. Reversing a String -------------------------------
# Reversing a string using slicing

my_string = "ABCDE"
reversed_string = my_string[::-1]

print(reversed_string)

# Output
# EDCBA

# 4. Printing a String or a List n Times-------------------------
n = 3 # number of repetitions

my_string = "abcd"
my_list = [1,2,3]

print(my_string*n)
# abcdabcdabcd

print(my_list*n)
# [1,2,3,1,2,3,1,2,3]

# 5. Combining a List of Strings Into a Single String ---------------------

list_of_strings = ['My', 'name', 'is', 'Chaitanya', 'Baweja']

# Using join with the comma separator
print(','.join(list_of_strings))
textClean = " ".join(list_of_strings)
print(textClean)
# Output
# My,name,is,Chaitanya,Baweja

# 6. Swap Values Between Two Variables ------------------
a = 1
b = 2
print (a)
print (b)
print("before of change")
a, b = b, a

print(a) # 2
print(b) # 1

# 7. Split a String Into a List of Substrings -----------------
string_1 = "My name is Chaitanya Baweja"
string_2 = "sample/ string 2"

# default separator ' '
print(string_1.split())
# ['My', 'name', 'is', 'Chaitanya', 'Baweja']

# defining separator as '/'
print(string_2.split('/'))
# ['sample', ' string 2']


# 8. List Comprehension ---------
# Multiplying each element in a list by 2

original_list = [1,2,3,4]

new_list = [2* y for y in original_list]
new_list2 = [2*original_list] # is not same

print(new_list)
print(new_list2)
# [2,4,6,8]

# 9. Check If a Given String Is a Palindrome or Not ----------
my_string = "abcba"

if my_string == my_string[::-1]:
    print("palindrome")
else:
    print("not palindrome")

# Output
# palindrome

# 10. Using Enumerate to Get Index/Value Pairs ----------
my_list = ['a', 'b', 'c', 'd', 'e']

for index, value in enumerate(my_list):
    print('{0}: {1}'.format(index, value))

# 0: a
# 1: b
# 2: c
# 3: d
# 4: e

# 11. Find Whether Two Strings are Anagrams ----------------

# An interesting application of the Counter class is to find anagrams.
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase.
# If the Counter objects of two strings are equal, then they are anagrams.

from collections import Counter

str_1, str_2, str_3 = "Nido", "odin", "abcda"
# Discriminar mayusculas y minusculas
st1 = str_1.lower()
st2 = str_2.lower()
st3 = str_3.lower()

cnt_1, cnt_2, cnt_3  = Counter(st1), Counter(st2), Counter(st3)

print (cnt_1)
print (cnt_2)
if cnt_1 == cnt_2:
    print('1 and 2 anagram')    
if cnt_1 == cnt_3:
    print('1 and 3 anagram')



# 12. Using the try-except-else Block --------------
a, b = 1,0

try:
    print(a/b)
    # exception raised when b is 0
except ZeroDivisionError:
    print("div9ision by zero")
else:
    print("no exceptions raised")
finally:
    print("Run this always")


# 13. Frequency of Elements in a List
# There are multiple ways of doing this, but my favorite is using the Python Counter class.

# Python counter keeps track of the frequency of each element in the container. Counter() returns a dictionary with elements as keys and frequency as values.

# We also use the most_common() function to get themost_frequentelement in the list.

# finding frequency of each element in a list
from collections import Counter

my_list = ['a','a','b','b','b','c','d','d','d','d','d', 'hola']
count = Counter(my_list) # defining a counter object

print(count) # Of all elements
# Counter({'d': 5, 'b': 3, 'a': 2, 'c': 1})

print(count['b']) # of individual element 
# 3

print(count.most_common(1)) # most frequent element
# [('d', 5)

# 14. Check the Memory Usage of an Object
import sys

num = 200

print(sys.getsizeof(num))

# In Python 2, 24
# In Python 3, 28

# 15. Sampling From a List
import random

my_list = ['a', 'bz', 'c', 'd', 'e']
num_samples = 4

samples = random.sample(my_list,num_samples)
print(samples)
# [ 'a', 'e'] this will have any 2 random values


# I have been recommended the secrets library for generating random samples 
# for cryptography purposes. The following snippet will work
# only on Python 3.

import secrets                              # imports secure module.
secure_random = secrets.SystemRandom()      # creates a secure random object.

my_list = ['a','b','c','d','e']
num_samples = 2

samples = secure_random.sample(my_list, num_samples)

print(samples)
# [ 'e', 'd'] this will have any 2 random values

# 16. Time Taken to Execute a Piece of Code
import time

start_time = time.time()
# Code to check follows
a, b = 1,2
c = a+ b
# Code to check ends
end_time = time.time()
time_taken_in_micro = (end_time - start_time)*(10**6)
print(" Time taken in micro_seconds: {0} ms".format(time_taken_in_micro))

# 18. Merging Two Dictionaries ---------------

dict_1 = {'apple': 9, 'banana': 16}
dict_2 = {'banana': 44, 'orange': 8}

combined_dict = {**dict_2, **dict_1}

print(combined_dict)
# Output
# {'apple': 9, 'banana': 4, 'orange': 8}
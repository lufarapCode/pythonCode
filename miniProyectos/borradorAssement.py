college_years = ['Freshman', 'Sophomore', 'Junior', 'Senior']
    
#print(list(enumerate(college_years, 2019)))
# return [(2019, 'Freshman'), (2020, 'Sophomore'), (2021, 'Junior'), (2022, 'Senior')]


# class my_secrets:
#     def __init__(self, password):
#         self.password = password
#         pass
# instance = my_secrets('1234')
# print (instance.password)

fruits = ['Apples', 'Oranges', 'Bananas']
quantities = [5, 3, 4]
prices = [1.50, 2.25, 0.89]
######
# Desired output
# [('Apples', 5, 1.50),
# ('Oranges', 3, 2.25),
# ('Bananas', 4, 0.89)]
#########
# i = 0
# output = []
# for fruit in fruits:
#     temp_qty = quantities[i]
#     temp_price = prices[i]
#     output.append((fruit, temp_qty, temp_price))
#     i += 1
# print(output)


# groceries = zip(fruits, quantities, prices)
# print( list(groceries))
###############################

def print_alpha_nums(abc_list, num_list):
    for char in abc_list:
        for num in num_list:
            print(char, num)
    return

##print(print_alpha_nums(['a', 'b', 'c'], [1, 2, 3]))
#####################

fruits = {'Apples': 5, 'Oranges': 3, 'Bananas': 4}

fruit_names = [x for x in fruits.keys()]
# print(fruit_names)

y="stuff;thing;junk;"
z = y.split(';')
#print(len(z))
#print(z)

x = {1,2,3,4,5}
print("1", x)
x.add(5)
print("2", x)
x.add(6)
print("3", x)

import numpy as np

table = np.array([
    [1,3],
    [2,4]])
print(table.max(axis=1))


print(17 % 15)

f = 5
h = 1 + (20 if f < 5 else 30)
print(h)
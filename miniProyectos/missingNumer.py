"""
Find Missing Number using Python
Finding the missing number in an array means finding the numbers missing from the array 
according to the range of values inside the array. Most of the time, the question you get based on this problem is like:

Given an array containing a range of numbers from 0 to n with a missing number, find the
 missing number in the input array.
To find the missing number in an array, we need to iterate over the input array and 
store the numbers in another array that we didn’t find in the input array while iterating 
over it. Below is how you can find the missing number in an array or a list using the Python programming language:
"""

def missignNumber(listnumer):

    numbers = set(listnumer)
    lenght = len(listnumer)
    output = []

    for i in range(1, listnumer[-1]):
        if i not in numbers:
            output.append(i)
    return output

listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 18]

print(missignNumber(listOfNumbers))

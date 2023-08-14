
"""
Group Elements of Same Indices using Python
To group elements of the same index, you will initially have
 two or more lists inside a list like [[a, b], [c, d]]. To group the elements of these 
 lists, you need to create two new lists where you will store the elements of both the 
 lists at index 0 [a, c] and index 1 [b, d]. That is the meaning of grouping the elements 
 of the same indices.

Now below is how you can group the elements of the same indices using the Python programming language:
"""

def groupElement(inputLists):
    inputLists 

    output = []
    index = 0 
    for i in range(len(inputLists[0])):
        output.append([])
        #print(output)
        for j in range(len(inputLists)):
            output[index].append(inputLists[j][index])
            #print(output)
        index = index + 1
    return output

list = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
list2 = [['A', 'B', 'C'], ['D', 'W', 'F'], ['H', 'Y', 90]]

print(groupElement(list2))
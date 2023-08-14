

def solution(inputArray):
    longiitud = len(inputArray)-1
    pos = 0
    producto = -1000

    while (pos < longiitud):   
        aux = inputArray[pos]* inputArray[pos+1]
        if aux > producto:
            producto = aux
        pos = pos + 1
    return producto

array = [3, 6, -2, -5, 7, 3]
array2 = [-23, 4, -3, 8, -12]



print(solution(array2))

def solution2(inputArray):
    return max([inputArray[i] * inputArray[i+1] for i in range(len(inputArray)-1)])


def solution3(inputArray):
    print(inputArray[:-1])
    print(inputArray[1:])
    t = zip(inputArray[:-1], inputArray[1:])
    tupla = [tupla for tupla in t]
    print(tupla)
    return max(a * b for a, b in zip(inputArray[:-1], inputArray[1:]))

print(solution3(array2))



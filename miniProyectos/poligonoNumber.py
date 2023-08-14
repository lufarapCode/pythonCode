
"""
Below we will define an n-interesting polygon. Your task is to find the area of a 
polygon for a given n.

A 1-interesting polygon is just a square with a side of length 1. An n-interesting 
polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting 
polygons to its rim, side by side. You can see the 1-, 2-, 3- and 4-interesting polygons 
in the picture below.



Example

For n = 2, the output should be
solution(n) = 5;
For n = 3, the output should be
solution(n) = 13.
    """
def solution(number):
    limite = 0
    secuecia = 4
    poligono = 1
    newPoligono =[1]

    while limite < number-1:
        poligono = poligono + secuecia
        aux = poligono
        newPoligono.append(poligono)
        secuecia = secuecia + 4
        poligono = aux
        limite += 1

    return newPoligono[-1]


# maldiciooooooooon
def solution2(n):
    return n**2 + (n-1)**2

def solution3(n):

    return 2*n*(n-1)+1


def run():
    print(solution(3))
    print(solution(2))
    print(solution(5))
    print(solution2(9999))
    print(solution(9999))





if __name__ == '__main__':
    run()
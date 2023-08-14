import math

def century(year):

    if year <= 2005 and year >=1:

        siglo = year / 100
        if siglo % 1 != 0:
            siglo = siglo + 1
            return (int(siglo))
        else: 
            return (round(siglo))
    else:
        return 0



print(century(1915))
print(century(1988))
print(century(2000))
print(century(2020))

# mira tuuuuuuuu
def solution(year):
    return (year + 99) // 100

print(solution(1915))

def solution3(year):
    # math.ceil redondea un numero al mas cercano
    print(math.ceil(3.00000001)) # 4
    print(math.ceil(3.84)) # 4
    return math.ceil(year/100)

print(solution3(1915))



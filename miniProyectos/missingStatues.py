"""
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday,
each statue having an non-negative integer size. Since he likes to make things perfect,
 he wants to arrange them from smallest to largest so that each statue will be bigger than 
 the previous one exactly by 1. He may need some additional statues to be able to accomplish 
 that. Help him figure out the minimum number of additional statues needed.

Example

For statues = [6, 2, 3, 8], the output should be
solution(statues) = 3.

Ratiorg needs statues of sizes 4, 5 and 7.

    """
def solution(lista):

    orderList = sorted(lista)
    numbers = set(orderList)
    print(orderList)
    print(orderList[-1])
    missingList = []
    for i in range(orderList[0], orderList[-1]):
        if i not in numbers:
            missingList.append(i)

    return len(missingList)

# MIRA TUUUUUUUU
def solution2(statues):
    print(max(statues))
    print(min(statues))
    return max(statues) - min(statues) - len(statues) + 1


# no lo se rick, esta solocion me dio chatGPT
def solution(statues):
    return len([x for x in range(min(statues), max(statues)) if x not in statues])

def run():
    print(solution([6, 1, 3, 8]))
    # print(solution2([0,3]))


if __name__ == '__main__':
    run()
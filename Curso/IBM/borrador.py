

def fibo(num):
    
    if (num == 0 or num == 1):
        return 1
    elif(num < 0):
        raise Exception ("Algo salio mal")

    return fibo(num - 1) + fibo(num - 2)

numero = 7
res = fibo(numero)
print(f"El bibonassi de {numero} es: {res}")


def fibo_linea(n):
    if n <=0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    
    fib_sequence = [0,1]
    for i in range(2, n): 
        print (f"pasos: {i} : {fib_sequence}")
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])

    res = f"La sesecion es: {fib_sequence}, el {n} numero de la sescion es: {fib_sequence[-1]}"
    return res

print(fibo_linea(10))
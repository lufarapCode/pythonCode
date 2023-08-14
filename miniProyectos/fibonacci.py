
def fibo(n: int):
    if (n == 0):
        return []
    elif (n == 1):
        return [0,1]
    elif(n < 0):
        raise Exception("Algo salio mal")
    
    secuencia_fibo = [0,1]
    for i in range (2, n):
        secuencia_fibo.append(secuencia_fibo[i-1]+secuencia_fibo[i-2])
    
    res = f"La sesecion es: {secuencia_fibo}, el {n} numero de la sescion es: {secuencia_fibo[-1]}"
    return res

numero = 45
print(fibo(numero))
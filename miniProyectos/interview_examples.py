import numpy as np
import time

print(
    """\n        1. Write a program to reverse an integer in Python.
        2. Write a program in Python to check whether an integer is Armstrong number or not.
        3. Write a program in Python to check given number is prime or not.
        4. Write a program in Python to print the Fibonacci series using recursive method.
        5. Write a program in Python to check whether a number is palindrome or not using iterative method.
        6. Write a program in Python to find greatest among three integers.
        7. Write a program in pytthon to count the letters of a text and count how many current appear. 
        8. Write a program in Python to check if a number is binary?
        9. Write a program in Python to find sum of digits of a number using recursion? 
        10.Write a program in Python to swap two numbers without using third variable?
        11. Write a program in Python to transform decimal to octal\n"""
)
option = input("Select the exercise: ")
match option:
    case "1":
        def reverse_int(n: int):
            """_summary_

            Args:
                n (int): number input

            Returns:
                _type_: reverse of n
            """
            print(f"El número ingresado es: {n}")
            reverse = 0
            while n!= 0:
                reverse = reverse*10 + n%10 # 12345 % 10 = 5 , 1234 % 10= 4 .... 
                n = (n//10) # 12345 // 10 = 1234,  1234 // 10 = 123 ......
            return print(f"El número al reves es: {reverse}") 

        integer = int(input("Ingrese un numero de n digitos: "))
        reverse_int(integer)

    case "2":

        print("""
        Un número de Armstrong (también llamado número de Narcisista o número de Hardy-Ramanujan) es
        un número entero positivo que se puede expresar como la suma de sus dígitos elevados a la
        n-ésima potencia, donde n es el número de dígitos del número en cuestión. Por ejemplo:

        - El número 153 es un número de Armstrong, ya que 1^3 + 5^3 + 3^3 = 153.
        - El número 9474 también es un número de Armstrong, ya que 9^4 + 4^4 + 7^4 + 4^4 = 9474.
        \n
        """)

        # Con esta linea me hubiese evitado la funcion de num_digitos(hace lo mismo) :(  -> num_dig = len(str(num))
        def num_digitos(n: int):
            contador = 0
            if (n == 0):
                contador = 1
            else:
                contador = 1
                # n > 10 ya que // recoge el numero entero, cuando es menor a 10 ya cuenta con un solo digito 
                # y detiene el bucle
                while(n >=10):
                    contador += 1
                    n = n // 10
            return contador 

        def num_armstrong(numero: int):
            # convierte un numero entero en una lista
            n_list = list(map(int, str(numero)))
            # funcion para obtener el numero de digitos
            num_dig = num_digitos(numero)

            suma = 0
            # convierte la lista en enteros para realizar la operación
            n_list2 = len(n_list)

            for i in range(n_list2):
                # eleva cada numero al numero n de digitos, y suma cada uno de ellos
                # esta funcion hace lo mismo -> suma = suma + pow(n_list[i], num_dig)
                suma = suma + n_list[i] ** num_dig

            if (suma == numero):
                print(f"{numero}: Es un número de amstrong")
            else:
                print(f"{numero}: No es un número de amstromg")

        integer = int(input("Ingrese el número: "))
        num_armstrong(integer)

    case "3":

        # Otra forma de evaluar si es primo o no (chatGPT lo dijo, no me convencio)
        def es_primo(num):
            if num <= 1:
                return False
            for i in range(2, num):
                #   print (i)
                if num % i == 0:
                    print("No es un número primos")
                    return False
            print("Es un nummero primo")
            return True
        
        def num_primo(n: int):

            cont = 0

            # itero todos los numeros desde el 1
            for i in range(1, n+1):
                if (n % i == 0):
                    # El contador evalua cuantas veces un numero tiene una división exacta
                    cont +=1

            # El concepto de numero primo dice que unicamente tiene 2 divisores distintos: el mismo numero y el 1
            # Si el contador tiene mas de 2 veces donde la división fue exacta, ya no es un numero primo
            if cont == 2:
                print("Es un número primo")
            else:
                print("No es un número primo")

        integer = int (input("Ingrese un número para validar si es primo: "))
        num_primo(integer)
    
    case "4":
        def fibonacci(n: int):
            if (n < 2):
                return n
            else:
                return fibonacci(n -1) + fibonacci (n - 2)
        
        start_time = time.time()
        print(fibonacci(25))
        end_time = time.time()

        time_taken_in_micro = (end_time - start_time)*(10**6)
        print(" Time taken in micro_seconds: {0} ms".format(time_taken_in_micro))

        def fibonacci2(n):
            a = np.array([[1, 1], [1, 0]], dtype=object)
            print(a)
            return int(np.linalg.matrix_power(a, n)[0][1])
        
        def fibo(num):
    
            if (num == 0 or num == 1):
                return 1
            elif(num < 0):
                raise Exception ("Algo salio mal")

            return fibo(num - 1) + fibo(num - 2)

        numero = 7
        #res = fibo(numero)
        #print(f"El bibonassi de {numero} es: {res}")

        # En cuanto a complejidad es lineal, la mejor que hay
        def fibo_lineal(n):
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
        res = fibo_lineal(numero)
        print(res)
        
    case "5":
        def palindromo (palabra: str):
            palabra = palabra.replace(" ", "").lower()

            if palabra[::] == palabra[::-1]:
                print(f"{palabra}: es un palindoromo.")
                return False
            else:
                print(f"{palabra}: no es un palindoromo.")
                return True

        frase = input("Ingrese la palabra o frase: ")
        palindromo(frase)

    case "6": 
        # funcion para saber el max de 2 numeros
        def num_max(n: int, n2: int):
            if(n > n2):
                return n
            else:
                return n2

        # utilizo la funcion anterior para saber el max entre 3 numeros -> esto por ley matematica
        def num_max_tres(n: int, n2: int, n3: int):
            if(num_max(n, n2) > n3):
                return num_max(n,n2)
            else:
                return n3

        numero = int(input("Ingrese los 3 nuemros: "))
        numer2 = int(input("Ingrese los 3 nuemros: "))
        numer3 = int(input("Ingrese los 3 nuemros: "))
        print("el numero mayor es: ", num_max_tres(numero, numer2, numer3))
    
    case "7":

        def lowerText(texto):
            lowerT = texto.lower()
            return lowerT

        def cleanText(texto):
            textClean = texto.replace(',', '').replace('.', '')
            
            # We can convert a string to a list using split. For example, the method split translates every group of 
            # characters separated by a space into an element in a list:
            textFinal = textClean.split(" ")
            
            return textFinal

        def countWords(texto):
            
            countCurrendWords = len(texto)
            return countCurrendWords

        def currendWord(texto):

            # un simple for tambien cuenta los caracteres, usando una variable cont
            for i, k in enumerate(texto):
                # cont +=1
                print(k,":", texto.count(k))


        def currendWordDictionari(texto):
            diccionario = {}

            for i in texto:
                if i in diccionario:
                    diccionario[i] += 1
                else:
                    diccionario[i] = 1

            sortedDictionari = dict(sorted(diccionario.items(), key=lambda item: item[0]))
            return sortedDictionari  # - > imprime el diccionario en forma de clave y valor

            # imprime de otra manera
            # for x, y in sortedDictionari.items():
            #     print(x,":",y)

                
            
        textoinput = input("Ingrese la frase: ")
        # texto = "Creo que a veces es la gente de la que nadie espera nada, la que hace cosas que nadie puede imaginar."

        textoLower = lowerText(textoinput)
        textoCleaned = cleanText(textoLower)
        contarPalabras = countWords(textoCleaned)
        contarPalabrasDiccionario = currendWordDictionari(textoCleaned)
        print("\n", contarPalabrasDiccionario)
        # print(textoCleaned)
        # permite contar el numero de palabras
        print("\n En la frase existe: ", contarPalabras, "caracteres")
    
    case "8":
        def is_binary(n: int):

            number = list(map(int, str(n)))
            for i in number:
                if (i != 0 and i != 1 ):
                    return False
            return True
        
        integer = int(input("Ingrese el número a validar: "))
        print("El número es binario: ", is_binary(integer))

    case "9":
        # forma normal 
        def suma_digitos(n):
            suma = 0
            num = list(map(int, str(n)))
            for i in num:
                suma = suma + i
            return suma

        # forma recursiva
        def suma_recursiva(n):
            if n == 0:
                return 0
            else:
                return int(n % 10) + suma_recursiva(int(n // 10))
        integer = int(input("Ingrese los números a sumar: "))  
        print(suma_recursiva(integer))

    case "10":
        def swap(a, b):
            print(f"Antes del cambio A: {a}")
            print(f"Antes del cambio B: {b}")

            a = a - b

            b = a + b
            
            a = b - a

            print(f"despues del cambio A: {a}")
            print(f"despues del cambio B: {b}")
            
            return 0
        def swap2(a,b):
            print (a)
            print (b)
            print("before of change")
            a, b = b, a

            print(a) # 2
            print(b) # 1
            return 0
        
        a = int(input("Ingrese el primer número: "))
        b = int(input("Ingrese el segundo número: "))
        swap2(a,b)

    case "11":
        def decimal_octal(n):
            res = 1
            cosiente = []

            while(res > 0):
                res = (n // 8)
                residuo = res * 8
                residuo2 = n - residuo
                cosiente.append(residuo2)
                octal = "".join(map(str, cosiente))
                n = res
            return octal

        num = int (input("Ingrese un número: "))
        print("El número octal es: ", decimal_octal(num))
    case _:
        print("Otra opcion")


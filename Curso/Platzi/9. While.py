#El bucle while evalúa una condición y luego ejecuta un bloque
#de código si la condición es verdadera.
counter = 0
while counter < 10:
    counter +=1
    if counter ==5:
        break # Rompe un flujo o ciclo de manera forzada
    print(counter)

#
counter1 = 0
while counter1 < 20:
    counter1 +=1
    if counter1 < 15:
        continue #El bucle no termina sino que continúa con la siguiente iteración.
print(counter1)

contador = 0
y = int(input("numero de la tabla: "))
x = int(input("Ingresa hasta que numero quieres multiplicar : "))
while contador < x:
    contador+= 1;
    resultado = y * contador;
    print(f"{y} X {contador} =  {resultado}")
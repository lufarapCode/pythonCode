from ast import main
import random
from tkinter.tix import MAIN

def run ():

    print("""
    El juego consiste en adivinar un número aleatorio comprendido entre 1 y 50, tines 5
    vidas para lograrlo, suerte! \n""")


    num_pc = random.randint(0,50)
    vidas = 5

    while True:
        numero = int(input("Ingresa tu número: "))
        if numero == num_pc:
            print ("Adiviniste el número, Ganaste!")
            break
        elif numero != num_pc:
            vidas -=1
            print (f"El número es incorrecto. {vidas} vidas restantes")
        if vidas == 0:
            print (f"Perdiste, el número aleatorio era: {num_pc}" )
            break

if __name__ == '__main__':
    run ()

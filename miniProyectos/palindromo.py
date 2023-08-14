from math import factorial
from sys import platlibdir
from unicodedata import name

def solution(inputString):
    inputString = inputString.replace(' ', '').lower()
    return inputString == inputString[::-1]


def es_palindromo(palabra):
    palabra = palabra.replace(' ', '').lower()
    print (palabra[::])
    print (palabra[::-1])

    if palabra[::] == palabra[::-1]:
        return True
    else:
        return False


def run ():
    palabra = input('Ingrese una palabra: ')

    if es_palindromo(palabra):
        print (palabra, 'Es un palindromo')
    else:
        print (palabra, 'No es un palindromo')


if __name__ == "__main__":
    run()


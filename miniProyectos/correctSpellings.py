
"""
Correct Spellings using Python
The SpellChecker module in Python is one of the handiest tools that can be used to correct misspelt words in a 
piece of text. If you have never used this Python module before, you can easily install it in your Python virtual 
environment by running the command mentioned below in your command prompt or terminal:

"""
from spellchecker import SpellChecker

# Crear una instancia del corrector ortográfico
spell = SpellChecker()

# Definir una lista de palabras de ejemplo
texto = "Hola, este es un texto con algunas palbras mal escritas."

# Dividir el texto en palabras individuales
palabras = texto.split()

# Verificar la ortografía de cada palabra y obtener sugerencias de corrección
for palabra in palabras:
    # Verificar si la palabra está mal escrita
    if not spell.correction(palabra) == palabra:
        # Obtener sugerencias de corrección para la palabra
        sugerencias = spell.candidates(palabra)
        print(f"La palabra '{palabra}' está mal escrita. Sugerencias: {sugerencias}")
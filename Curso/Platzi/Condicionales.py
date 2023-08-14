
# pet = input("Que mascota tienes?")

# if pet == 'perro':
#     print("Tienes buen gusto")
# elif    pet == 'gato':
#     print("cuidado con las garras")
# else:
#     print("....")

# numero = int(input("Dijita un numero: "))

# if (numero % 2 == 0):
#     print("El número es par")
# else:
#     print("El número es impar")

import random
opciones = ['piedra', 'papel', 'tijeras']
# maquina = random.randint(1,200)
vidas_user = 3
vidas_maquina = 3
game_over = True
while game_over:
        

    user = input("Escoge una opción => Piedra, papel o tijeras: ").lower()
    maquina = random.choice(opciones)
    print(f"Maquina escogio:{maquina}")



    if user == maquina:
        print("Empate")
    elif user == 'tijeras' and maquina == 'piedra':
        print("Maquina gana, user menos una vida")
        vidas_user -= 1
    elif user == 'tijeras' and maquina == 'papel':
        print("User gana, maquina menos una vida")
        vidas_maquina -= 1
    elif user == 'papel' and maquina == 'piedra':
        print('User gana, maquina menos una vida')
        vidas_maquina -= 1
    elif user == 'papel' and maquina == 'tijeras':
        print('maquina gana, user menos una vida')
        vidas_user -= 1
    elif user == 'piedra' and maquina == 'tijeras':
        print('User gana, maquina menos una vida')
        vidas_maquina -= 1
    elif user == 'piedra' and maquina == 'papel':
        print('maquina gana, user menos una vida')
        vidas_user -= 1
    if vidas_maquina == 0:
        game_over = False
        print(f"User gano! con {vidas_user} vidas restantes")
    elif vidas_user == 0:
        game_over = False
        print(f"Maquina gano! con {vidas_maquina} vidas restantes")

    print(f"Total de vidas maquina: {vidas_maquina}, Total de vidas User: {vidas_user}")
    
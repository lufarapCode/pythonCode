
list = [5,10,11,70,30,60,12,90,2,90,69,67]
print(sum(list))
# Media o tambien llamado promedio, es la suma de todos los valores divido para la cantidad
def media(lista: float):
    # obtengo la cantidad de elementos
    cantidad = len(lista)
    suma = 0
    for i in list:
        suma = suma + i

    media = suma / cantidad
    # Agrego formato de dos decimales
    media = format(media, f".{2}f")
    return media

print(f"La media es: {media(list)}")

def moda(lista):
    frecuncy = {}
    for i in lista:
        # acrtualizar el diccionario, si el valor ya existe aumenta en 1 
        frecuncy[i] = frecuncy.get(i,0) + 1
        # print(frecuncy.get(i,0))
    moda = []
    max_frecuencias = 0
    #print(frecuncy.items())
    for valor, frecuncy in frecuncy.items():
        #print(valor, frecuncy)
        if frecuncy > max_frecuencias:
            # agrego el valor con la frecuencia mas alta
            moda = [valor]
            max_frecuencias = frecuncy
        elif frecuncy == max_frecuencias:
            # en caso que se repita, agrego ese nuevo valor
            moda.append(valor)
    
    return moda

print(f"La moda es: {moda(list)}")


def mediana(list):

    list = sorted(list)
    longitud = len(list)

    if longitud%2 == 0:
        
        aux = longitud // 2
        mediana = (list[aux-1] + list[aux])/2
        return mediana
    
    else:
        aux = longitud // 2
        return list[aux]

print(f"La mediana es: {mediana(list)}")






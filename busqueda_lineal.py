"""
Busca de manera secuencial
Peor caso: ultimo elemento

Complejidad crece con el for en base al n ingresado para la lista entonce O(n)
"""

import random

#Tengo una lista, busco un objetivo
def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista:
        if elemento  == objetivo:
            match = True
            #Si no hago el break termino recorriendo toda la lista
            break
    
    return match

#Generar listas

if __name__ == "__main__":
    tamano_de_lista = int(input("De que tamano sera la lista?.."))
    objetivo = int(input("Que numero quieres encontrar...?"))

    #Vamos a crear una lista, del tamano de la lista con numero aleatorios
    lista = [random.randint(0,100) for i in range (tamano_de_lista)]
    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
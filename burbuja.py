"""
Recorre repetidamente la lista, compara los elementos adyacentes y los 
va intercambiando hasta que no se requieren mas intercambios, es decir la lista es
ordenada
"""

import random

#Retorna la lista ordenada
def ordenamiento_de_burbuja(lista):
    n = len(lista)

    for i in range(n):
        #comienza en index 0, hasta lo que va menos 1
        for j in range(0, n - i - 1): # O(n) * O(n) = O(n * n) = O(n**2)

            #Si es verdad, intercambiamos
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))

    #Imprime mi lista random
    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)

    #Imprime la lista ordenada
    lista_ordenada = ordenamiento_de_burbuja(lista)
    print(lista_ordenada)
"""
DIVIDE Y CONQUISTARAS
debe estar ordenada
se divide en 2 con cada iteracion
Cual es el peor caso

Si no esta ordenada y son pocas busquedas: Usar lineal
"""
import random

def busqueda_binaria(lista, comienzo, final, objetivo):
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    #Caso base, en dado caso no este
    if comienzo > final:
        return False

    #Divison enteros
    medio = (comienzo + final) // 2 

    if lista[medio] == objetivo:
        return True

    
    elif lista [medio] < objetivo:
        #Hago otra busqueda, ahora el comienzo es para adelante
        return busqueda_binaria(lista, medio + 1, final, objetivo)


    else:
        #Ahora me voy para la parte de abajo
        return busqueda_binaria(lista, comienzo, medio-1, objetivo)


if __name__ == "__main__":
    tamano_de_lista = int(input("De que tamano sera la lista?.."))
    objetivo = int(input("Que numero quieres encontrar...?"))

    #Vamos a crear una lista, del tamano de la lista con numero aleatorios
    #Aqui, aplique un metodo de ordenamiento
    lista = sorted([random.randint(0,100) for i in range (tamano_de_lista)])

    #Comenzamos en index 0, vamos hasta su longitud
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)


    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
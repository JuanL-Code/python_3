#Calcular el tiempo
import time

#generar dos implementaciones de factorial, iterativa y recursiva
def factorial(n):
    respuesta = 1

    while n>1:
        respuesta *= n
        n-=1


    return respuesta 


def factorial_recursivo(n):
    if n==1:
        return 1

    return n* factorial(n-1)


if __name__ == "__main__":
    n = 100000

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final-comienzo)

    comienzo = time.time()
    factorial_recursivo(n)
    final = time.time()
    print(final - comienzo)

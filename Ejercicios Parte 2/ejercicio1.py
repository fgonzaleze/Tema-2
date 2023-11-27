# Crea un proceso que cuente las vocales de un fichero de texto. Para ello crea una función que reciba una vocal y 
# devuelva cuántas veces aparece en un fichero. Lanza el proceso de forma paralela para las 5 vocales. 
# Tras lanzarse se imprimirá el resultado por pantalla.

from multiprocessing import *

fichero = "Ejercicios Parte 2/vocales.txt"

def contarVocales(letra):
    contador = 0
    with open(fichero, "r") as archivo:
        letras = archivo.read()
        contador = letras.count(letra)
    return contador

# def contarVocales2(letra, fichero):
#     contador = 0
#     with open(fichero, "r") as archivo:
#         letras = archivo.read()
#         contador = letras.count(letra)
#     return contador

if __name__ == "__main__":
    pool = Pool(processes=5)
    vocales = ["a","e","i","o","u"]
    resultados = pool.map(contarVocales, vocales)
    pool.close()
    print("Resultado: ", vocales) 
    print(resultados)

# if __name__ == "__main__":
#     pool = Pool(processes=5)
#     vocales = ["a","e","i","o","u"]
#     listaprocesos = []
#     for vocal in vocales:
#         p1 = Process(target=contarVocales2, args=(vocal, fichero))
#         p1.start()
#         listaprocesos.append(p1)
#     for proceso in listaprocesos:
#         proceso.join()
    
#     pool.close()
#     print("Resultado: ", vocales) 
#     print()

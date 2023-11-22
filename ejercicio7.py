# Realiza el ejercicio anterior pero esta vez va a haber otra función que lea los números de un fichero. 
# En el fichero habrá dos números por línea separados por un espacio. En este caso, tienes que llevar a cabo 
# una comunicación entre los dos procesos utilizando colas (Queue), de forma que la función que se encarga de leer los números los guarde en la cola, 
# y la función que realiza la suma, recibirá la cola y tomará de ahí los dos números.

from multiprocessing import Pool
import time


def contar(num1, num2):
    if num1 > num2:
        return list(range(num2, num1 + 1))
    else:
        return list(range(num1, num2 + 1))

def leerFichero(fichero):
    fichero = "numerosEj7.txt"



if __name__ == "__main__":
    inicio = time.time()

    # cantidad de procesos en el pool
    procesos = 2

    # para crear un Pool de procesos
    with Pool(procesos) as pool:
        # Starmap para lanzar la funcion cond iferentes pares de valores
        resultados = pool.starmap(contar, [(1, 12), (-2, 10), (20, 17)])

    for resultado in resultados:
        print(resultado)

    fin = time.time()
    print("Tiempo:", fin - inicio)
# Modifica el ejercicio anterior para usar un Pool para lanzar varios procesos de forma concurrente. 
# Recuerda que al tener dos argumentos debes usar el método starmap en vez de map.

from multiprocessing import Pool
import time

def contar(num1, num2):
    if num1 > num2:
        return list(range(num2, num1 + 1))
    else:
        return list(range(num1, num2 + 1))

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
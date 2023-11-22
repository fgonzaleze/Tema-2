# Modifica el ejercicio anterior para que el programa principal use un Pool para lanzar varios procesos de forma concurrente. 
# Cambia el valor del número de procesos y compara los tiempos que tarda en ejecutarse en los distintos casos.

from multiprocessing import Pool
import time
# funcion para contar numeros
def contarNum(numSumar):
    res = 0
    for num in range(1, numSumar + 1):
        res += num
    print("El resultado es:", res)

if __name__ == "__main__":
    num = int(input("Introduzca un número: "))

    # Catidad de procesos en el Pool para ver lo que tarda
    procesos = 2
    inicio = time.time()
    # Creamos un Pool de procesos
    with Pool(procesos) as pool:
        pool.map(contarNum, [num] * procesos)
    pool.close()
    fin = time.time()
    print("Todos los procesos han terminado.")
    print("Tiempo:", fin - inicio)
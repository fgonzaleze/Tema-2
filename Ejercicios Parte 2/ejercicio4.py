import multiprocessing
import time

def proceso1(ruta, anyo, queue):
    with open(ruta, 'r') as archivo:
        for linea in archivo:
            nombre, anno = linea.strip().split(';')
            if int(anno) == anyo:
                queue.put((nombre, anno))

def proceso2(cola):
    peliculas = []
    while not cola.empty():
        pelicula = cola.get()
        peliculas.append(pelicula)

    if peliculas:
        anyo = peliculas[0][1]
        with open(f'peliculas{anyo}.txt', 'w') as archivo:
            for nombre, anyo in peliculas:
                archivo.write(f'{nombre};{anyo}\n')


if __name__ == "__main__":

    inicio = time.time()
    anyo = int(input("Introduce un año: "))
    ruta = "Ejercicios Parte 2/peliculas.txt"
    cola = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=proceso1, args=(ruta, anyo, cola))
    p2 = multiprocessing.Process(target=proceso2, args=(cola,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    final = time.time()
    print(final - inicio)
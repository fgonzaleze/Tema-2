# En este ejercicio debes implementar los siguientes procesos y el Main como se explica a continuación:
#     Proceso 1: Genera 6 números aleatorios entre 1 y 10, ambos inclusive, y los guarda en un fichero. Estos números deben contener decimales. 
#     La ruta a este fichero se le indicará como parámetro de entrada. Estos 6 números representan las notas de un alumno.
#     Proceso 2: Lee un fichero pasado por parámetro que contiene las notas de un alumno, cada una en una línea distinta, y realiza la media de las notas. 
#     También recibe como parámetro el nombre del alumno. Esta media se almacenará en un fichero de nombre medias.txt. 
#     Al lado de cada media debe aparecer el nombre del alumno, separados por un espacio.
#     Proceso 3: Lee el fichero medias.txt. En cada línea del fichero aparecerá una nota, un espacio y el nombre del alumno. 
#     Este proceso debe leer el fichero y obtener la nota máxima. Imprimirá por pantalla la nota máxima junto con el nombre del alumno que la ha obtenido.
#     Main: Lanza 10 veces el primer proceso de forma concurrente. Cada una de esas veces debe guardarse el resultado en un fichero distinto. 
# Es decir, al final tiene que haber 10 ficheros distintos con las notas de cada alumno. Pon a los ficheros nombres como Alumno1.txt, Alumno2.txt, …, Alumno10.txt.
# A continuación, se debe lanzar el proceso 2 que toma los ficheros creados en el paso anterior como entrada. Por lo que el proceso 2 se lanzará 10 veces también, una por cada fichero generado por el proceso 1, y realizarlo todo de forma simultánea/concurrente. Es decir, debe haber 10 procesos ejecutándose simultáneamente.
# Por último, debe lanzarse el proceso 3. Hay que tener presente que para que este proceso pueda funcionar correctamente deben estar todas las notas ya escritas.
# Prueba a realizar el ejercicio haciendo uso de Pool y haciendo uso de bucles for.

from multiprocessing import Pool, Process
import random


def generaNota(fichero):
    with open(fichero, "w") as archivo:
        for i in range(6):
            num = round(random.uniform(0,10), 2)
            archivo.write(f"{num}\n")

def mediaNota(fichero, alumno):
    with open(fichero, "r") as archivo:
        suma = 0
        for linea in archivo.readlines():
            nota = float(linea)
            suma += nota
        media = suma/6
    with open("medias.txt", "a") as medias:
        medias.write(f"{round(media,2)} {alumno}\n")

def maximaNota():
    with open("medias.txt", "r") as archivo:
        max = 0.0
        for linea in archivo.readlines():
            array = linea.split()
            nota = float(array[0])
            if nota > max:
                max = nota
                alumno = array[1]
        print("Alumno:", alumno, "Nota:", max)

if __name__ == "__main__":
    # for i in range(10):
    #     proceso1 = Process(target=generaNota, args =(f"Alumno{i+1}.txt", ))
    #     proceso1.start()
    # for i in range(10):
    #     proceso2 = Process(target=mediaNota, args=(f"Alumno{i+1}.txt", f"Alumno{i+1}"))
    #     proceso2.start()

    # proceso3 = Process(target= mediaNota)
    # proceso3.start

    with Pool (processes = 10) as pool1:
        ficheros = []
        for i in range(10):
            ficheros.append(f"Alumno{i+1}.txt")
        pool1.map(generaNota, ficheros)

    pool1.join() # Para que pueda acabar
    
    with Pool (processes = 10) as pool2:
        ficheros = []
        for i in range(10):
            argumentos = (f"Alumno{i+1}.txt", f"Alumno{i+1}")
            ficheros.append(argumentos)
        pool2.starmap(mediaNota, ficheros)

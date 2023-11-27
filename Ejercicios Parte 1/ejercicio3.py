# Realiza el ejercicio anterior pero esta vez va a haber otra función que lea los números de un fichero. 
# En el fichero habrá un número por línea. En este caso, tienes que llevar a cabo una comunicación entre los dos procesos utilizando colas (Queue), 
# de forma que la función que se encarga de leer los números los guarde en la cola, y la función que realiza la suma, recibirá la cola y tomará de ahí los números. 
# La función que lee el fichero, una vez haya terminado de leer y de añadir elementos a la cola, 
# debe añadir un objeto None para que el receptor sepa cuándo terminar de leer de la cola.

from multiprocessing import *

def leerNumeros(archivo, cola):
    with open(archivo, 'r') as arch:
        for linea in arch:
            numero = int(linea)
            cola.put(numero)


def contarNumCola(cola):
    res = 0
    while True:
        numero = cola.get()
        res += numero
        if numero is None:
            break
        print("El resultado es:", res)

if __name__ == "__main__":
    archivo = "numerosEj3.txt"

    queue = Queue()

    # procesos pa leer y para sumar
    procesoleer = Process(target=leerNumeros, args=(archivo, queue))
    procesosumar = Process(target=contarNumCola, args=(queue,)) # <--- Coma porque es un tupla!

    # empiezan
    procesoleer.start()
    procesosumar.start()

    # pa que acaben
    procesoleer.join()
    procesosumar.join()

    print("Los procesos han terminado")

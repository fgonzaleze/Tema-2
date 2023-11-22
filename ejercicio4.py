# En este caso, vuelve a realizar la comunicación entre procesos pero usando tuberías (Pipe), de forma que la función que se encarga de leer los números 
# del fichero se los envíe (send) al proceso que se encarga de la suma. El proceso que suma los números tiene que recibir (recv) un número y realizar la suma. 
# Una vez que el proceso que lee el fichero termine de leer números en el fichero, debe enviar un None. El que recibe números dejará de realizar sumas cuando reciba un None.

from multiprocessing import *

def leerNumeros(filename, union):
    with open(filename, 'r') as file:
        for line in file:
            numero = int(line.strip())
            union.send(numero)
    # envio none para indicar que es el final de la lectura
    union.send(None)
    union.close()

def contarNumPipe(conn):
    res = 0
    numero = conn.recv()
    while numero is not None:
        res += numero
        numero = conn.recv()
    print("El resultado es:", res)

if __name__ == "__main__":

    archivo = "numeros.txt"

    # la tubería 
    leer, sumar = Pipe()

    # procesos pa leer y para sumar
    procesoleer = Process(target=leerNumeros, args=(archivo, leer))
    procesosumar = Process(target=contarNumPipe, args=(sumar,))

    # empiezan
    procesoleer.start()
    procesosumar.start()

    # pa que acaben
    procesoleer.join()
    procesosumar.join()

    print("Todos los procesos han terminado.")
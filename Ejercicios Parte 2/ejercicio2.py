# En este ejercicio vamos a lanzar varios procesos, cuyas entradas y salidas están enlazadas. Para ello tendremos tres procesos distintos:
# Proceso 1: Va a generar 10 direcciones IP de forma aleatoria y se las enviará al Proceso 2.
# Proceso 2: Va a leer las direcciones IP que recibe del Proceso 1 y va a enviar al Proceso 3 únicamente aquellas que pertenezcan a las clases A, B o C.
# Proceso 3: Va a leer las direcciones IP procedentes del Proceso 2 (no se sabe qué número llegarán) y va a imprimir por consola la dirección IP y a 
#            continuación la clase a la que pertenece.
# 	Lanza los tres procesos en orden.

# El ejercicio son dos tuberías p1 ==== p2 ===== p3 
# El primer proceso creará las IP y a medida que las vaya creando las irá enviando al p2, el cual irá filtrando y a su vez las enviará al p3, que las mostrará si corresponde.

from multiprocessing import Pipe, Process
from multiprocessing.connection import PipeConnection
import random

# def proceso1():
#     for i in range(1,11):
#         ip = ".".join(map(str, (random.randint(0, 255) 
#                                 for _ in range(4))))
#         print (ip)


def generaIP(tuberia:PipeConnection):
    for _ in range (10): # Barra baja si no usas la variable y solo quieres que el bucle se cumpla x veces
        ip =""
        for i in range(4):
            octeto = random.randint(0,255)
            ip += str(octeto)
            if(i!=3):
                ip = ip + "."
        else:
            tuberia.send(ip)
        print(ip)

def filtrar(tubleft:PipeConnection, tubright:PipeConnection):
    #Slit por el punto y filtrarlo

if __name__ == "__main__":
    p1left, p1right = Pipe()
    p2left, p2right = Pipe()
    p1 = Process(target=generaIP, args=(p1left,))
    p2 = Process(target=generaIP, args=(p1right, p2left))
    
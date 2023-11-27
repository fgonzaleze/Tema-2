# En este ejercicio vamos a lanzar varios procesos, cuyas entradas y salidas están enlazadas. Para ello tendremos tres procesos distintos:
# Proceso 1: Va a generar 10 direcciones IP de forma aleatoria y se las enviará al Proceso 2.
# Proceso 2: Va a leer las direcciones IP que recibe del Proceso 1 y va a enviar al Proceso 3 únicamente aquellas que pertenezcan a las clases A, B o C.
# Proceso 3: Va a leer las direcciones IP procedentes del Proceso 2 (no se sabe qué número llegarán) y va a imprimir por consola la dirección IP y a 
#            continuación la clase a la que pertenece.
# 	Lanza los tres procesos en orden.

# El ejercicio son dos tuberías p1 ==== p2 ===== p3 
# El primer proceso creará las IP y a medida que las vaya creando las irá enviando al p2, el cual irá filtrando y a su vez las enviará al p3, que las mostrará si corresponde.

import random

# def proceso1():
#     for i in range(1,11):
#         ip = ".".join(map(str, (random.randint(0, 255) 
#                                 for _ in range(4))))
#         print (ip)

def proceso1(conn):
    for i in range(4):
        ip = ""
        ip = ip + str(random.randint(0, 255))
        if (i!=3):
            ip = ip + "."
        print("Proceso 1 en marcha")
        conn.send(ip)
    conn.send(None)

if __name__ == "__main__":
    print()
 
    
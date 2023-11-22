# Crea una función en Python que sea capaz de sumar todos los números desde el 1 hasta un valor introducido por parámetro, 
# incluyendo ambos valores y mostrar el resultado por pantalla. 
# Desde el programa principal crea varios procesos que ejecuten la función anterior. 
# El programa principal debe imprimir un mensaje indicando que todos los procesos han terminado después de que los procesos hayan impreso el resultado.

from multiprocessing import Process

def contarNum(numSumar):
    res = 0
    for num in range(1, numSumar + 1):
        res += num
    print("El resultado es: ", res)

if __name__ == "__main__":
    num = int(input("Introduzca un número: "))
    p1 = Process(target=contarNum, args=(num,))
    p1.start()
    p1.join()
    print("todos los procesos han terminado")


from multiprocessing import *
import time

def contar(num1, num2):
    if num1 > num2:
        for num in range(num2, num1 + 1):
            print(num)
    else:
        for num in range(num1, num2 + 1):
            print(num)

if __name__ == "__main__":
    num1 = int(input("Introduce el rpimer numero: "))
    num2 = int(input("Introduce el segundo numero: "))
    inicio = time.time()
    p1 = Process(target=contar, args=(num1, num2))
    p1.start()
    p1.join()
    fin = time.time()
    print("Tiempo:", fin - inicio)
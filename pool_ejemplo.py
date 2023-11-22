from multiprocessing import *
import time
def double(num):
    return num*num

if __name__ == "__main__":
    pool = Pool(processes=3)
    numeros = [1,2,3,4,5,6,7,8,9,10]
    resultados = pool.map(double, numeros)
    pool.close()
    print("Resultados de :", numeros) 
    print(resultados)

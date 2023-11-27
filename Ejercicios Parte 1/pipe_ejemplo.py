from multiprocessing import *

def process1(extremo1):
    extremo1

def process2(extremo2):
    pass

if __name__ == "__main__":
    izq, der = Pipe()
    p1 = Process(target=process1, args=(izq,))
    p2 = Process(target=process2, args=(der,))

    p1.start()
    p2.start()
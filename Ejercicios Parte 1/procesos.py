from multiprocessing import *

def hello(name):
    print("Hola", name)

if __name__ == "__main__":
    p = Process(target=hello, args=("Javi",))
    p.start() #Para que el proceso empiece
    p.join() #Metodo para decirle que se espere, NO SE PARA, este proceso se va a esperar a que acabe el proceso p
    print("Adios Luisa")
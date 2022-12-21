#Decoradores
#Funciones en python
#Parametros
#retornados por otra función

"""def hola():
    print("Hola Mundo")

saludo = hola
del hola
# hola()

saludo()"""

#Higher order functions
#Funciones que aceptan a otras funciones como otras como parametros
#Funciones que retornan funciones
# Por ejemplo print(), int()

"""def saludo(func):
    func()

def hola():
    print("Hola")

def buenos_dias():
    print("Buenos días")

saludo(buenos_dias)"""

#Decorador
"""def decorador(func):
    print("Instruccion potenciadora 1")
    def contenedor():
        print("Instruccion potenciadora 2")
        func()
        print("Instruccion potenciadora 3")
    return contenedor

@decorador
def buenas_tardes():
    print("Buenas tardes")

buenas_tardes()"""

from time import time

def perfomance(fn):
    def contenedor(*args,**kawargs):
        t1 = time()
        result = fn(*args,**kawargs)
        t2 = time()
        print(f"Tiempo de ejecución: {t2 - t1} segundos")
        return result
    return contenedor

@perfomance
def multiplicacion():
    for i in range(10000):
        print(i*2)

multiplicacion()

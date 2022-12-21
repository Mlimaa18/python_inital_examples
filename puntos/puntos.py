#Ordenar coordenadas
#La coordenada más al norte será la primera coordenada
#Se usará la coordenada más al este
#Obtener el vecino más cercano a la última coordenada obtenida
#Indicar el orden de las coordenadas

import math

class Puntos_cartesianos:
    puntos = []
    puntos_norte = []
    puntos_este = []
    puntos_ordenados = []
    puntos_restantes = []
    def __init__(self) -> None:
        pass


    def obtener_coordenadas(self):
        numero_puntos = int(input("Cuantos puntos deseas ingresar: "))
        for i in range(numero_puntos):
            punto = {
                "id": i,
                "x": 0,
                "y": 0,
                "no": 0
            }
            print(f"Inserta las coordenadas del punto {i}")
            punto["x"] = float(input("x:"))
            punto["y"] = float(input("y:"))
            self.puntos.append(punto)

        print(self.puntos)


    def calcular_coordenadas_norte(self):
        max_y = self.puntos[0]["y"]
        print(max_y)
        for punto in self.puntos:
            if punto["y"] >= max_y:
                self.validar_puntos_norte(punto["y"],max_y,punto["id"])
                max_y = punto["y"]
        print(max_y)
        print(self.puntos_norte)


    def validar_puntos_norte(self, y, max_y, punto_id):
        if y == max_y:
            self.puntos_norte.append(punto_id)
        else:
            self.puntos_norte.clear()
            self.puntos_norte.append(punto_id)


    def calcular_coordenadas_este(self):
        max_x = self.puntos[0]["x"]
        for punto in self.puntos_norte:
            if(self.puntos[punto]["x"] >= max_x):
                self.validar_puntos_este(self.puntos[punto]["x"], max_x, self.puntos[punto]["id"])
                max_x = self.puntos[punto]["x"]
        print(self.puntos_este)



    def validar_puntos_este(self, x, max_x, punto_id):
        if x == max_x:
            self.puntos_este.append(punto_id)
        else:
            self.puntos_este.clear()
            self.puntos_este.append(punto_id)
    

    def seleccionar_primer_punto(self):
        self.puntos[self.puntos_este[0]]["no"] = 1
        self.puntos_ordenados.append(self.puntos[self.puntos_este[0]])
        self.puntos_restantes = list(filter(lambda p: p["id"] != self.puntos[self.puntos_este[0]]["id"], self.puntos))
    

    def buscar_vecino(self):
        distancias = []
        for punto in self.puntos_restantes:
            punto_distancias = {
                "distancia": math.sqrt( math.pow(self.puntos_ordenados[-1]["y"] - punto["y"],2) + math.pow(self.puntos_ordenados[-1]["x"] - punto["x"],2)) ,
                "id": punto["id"]
            }
            distancias.append(punto_distancias)
        print(distancias)

    #Buscar el más cercano
    #Agregarlo a la lista de puntos ordenados
    #Eliminarlo de puntos restantes
    #Instalar matplotlib y graficarlo con scatter

#Busqueda en anchura
#Busqueda en profundidad
#Branch and bound
#Problemas con estados

puntos = Puntos_cartesianos()
puntos.obtener_coordenadas()
puntos.calcular_coordenadas_norte()
puntos.calcular_coordenadas_este()
puntos.seleccionar_primer_punto()
puntos.buscar_vecino()
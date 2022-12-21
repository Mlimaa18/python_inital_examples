from math import log


class Busqueda_anchura:
    initialMatrix = []
    matrizSolution = [1,2,3,4,5,6,7,8,""]
    lista_abierta = []
    lista_cerrada = []
    emptyValue = 0
    padre = -1
    count = 0

    def __init__(self) -> None:
            pass

    def obtener_matriz(self):
        # for numero in range(1,10):
        #     value = ""
        #     number = 0
        #     while True:
        #         try:
        #             print(f"Inserte el valor del elemento {numero} con valores del 1 al 8 y deje en blanco para el espacio vacio: ")
        #             value = input()
        #             number = int(value)
        #             if(number in self.initialMatrix or number <= 0 or number >= 9):
        #                 raise ValueError("El número ingresado ya esta en la matriz o no esta en el rango de 1 a 8")
        #             else:
        #                 self.initialMatrix.append(number)

        #         except ValueError:
        #             if(self.emptyValue == 0 and value == ""):
        #                 self.initialMatrix.append(value)
        #                 self.emptyValue = 1
        #                 break
        #             if(int(value) and number > 0 and number < 9):
        #                 print(f"El número {value} ya ha sido ingresado")
        #             else:
        #                 print(f"Ingresa un número válido")    
        #         else: #Se ejecuta cuando se ha cumplido el try sin errores
        #             break

        # self.initialMatrix = [1, 3, 2, 4, 5, 6, 7, 8, '']
        self.initialMatrix = [ '',1, 2, 3, 4, 5, 6, 7, 8]

    def mostrar_matriz_inicial(self):
        print("La matriz inicial es: ")
        print(self.initialMatrix[0],self.initialMatrix[1],self.initialMatrix[2])
        print(self.initialMatrix[3],self.initialMatrix[4],self.initialMatrix[5])
        print(self.initialMatrix[6],self.initialMatrix[7],self.initialMatrix[8])

    def busqueda_anchura(self):
        if(self.lista_abierta == [] and self.lista_cerrada == []):
            self.lista_abierta.append({"estado": self.initialMatrix, "padre": -1})
        while self.lista_abierta[0] != self.matrizSolution or len(self.lista_abierta) > 0:
            if(self.lista_abierta[0]["estado"] == self.matrizSolution):
                print("programa terminado")
                break
            self.count = self.count + 1
            # print(f"elemento actual {self.lista_abierta[0]}")
            print(f"lista abierta longitud {len(self.lista_abierta)}      lista cerrada longitud {len(self.lista_cerrada)}     elemento actual {self.lista_abierta[0]}")
            self.lista_cerrada.append(self.lista_abierta.pop(0))
            self.buscar_nodos_hijos()
            # print("lista abierta")
            # print(self.lista_abierta)
            # print("lista cerrada")
            # print(self.lista_cerrada)

        if(self.lista_abierta[0]["estado"] == self.matrizSolution):
            print("programa terminado")
        if(len(self.lista_abierta) == 0):
            print("programa terminado")
        print(f"iteraciones {self.count}")

    def buscar_nodos_hijos(self):
        # print("funcion buscar nodos hijos")
        # print(self.lista_cerrada[-1])
        # print(self.lista_cerrada[-1]["estado"])
        estado_actual = self.lista_cerrada[-1]["estado"]
        for index, numero in enumerate(estado_actual,0):
            # print(f"index: {index}, numero: {numero}")
            if(numero == ""):
                if(index == 0):
                    hijo1 = [estado_actual[1], estado_actual[0], estado_actual[2],
                            estado_actual[3], estado_actual[4], estado_actual[5],
                            estado_actual[6], estado_actual[7], estado_actual[8]
                    ]
                    if not (any(d['estado'] == hijo1 for d in self.lista_cerrada) or any(d['estado'] == hijo1 for d in self.lista_abierta)):
                        self.lista_abierta.append({"estado": hijo1, "padre": len(self.lista_cerrada) -1 })
                    hijo2 = [estado_actual[3], estado_actual[1], estado_actual[2],
                            estado_actual[0], estado_actual[4], estado_actual[5],
                            estado_actual[6], estado_actual[7], estado_actual[8]
                    ]
                    if not (any(d['estado'] == hijo2 for d in self.lista_cerrada) or any(d['estado'] == hijo2 for d in self.lista_abierta)):
                        self.lista_abierta.append({"estado": hijo2, "padre": len(self.lista_cerrada) -1 })
                if(index == 1):
                    hijo1 = [estado_actual[1], estado_actual[0], estado_actual[2],
                            estado_actual[3], estado_actual[4], estado_actual[5],
                            estado_actual[6], estado_actual[7], estado_actual[8]
                    ]
                    
                    # print(any(d['estado'] == hijo1 for d in self.lista_cerrada))
                    # print(any(d['estado'] == hijo1 for d in self.lista_abierta))
                    # print(any(d['estado'] == hijo1 for d in self.lista_cerrada) or any(d['estado'] == hijo1 for d in self.lista_abierta))
                    # print(f"true or true {True or True}")
                    # print(f"true or false {True or False}")
                    # print(f"false or false {False or False}")
                    # print(f"Not true or true {not (True or True)}")
                    # print(f"Not true or false {not (True or False)}")
                    # print(f"Not false or false {not (False or False)}")
                    if not (any(d['estado'] == hijo1 for d in self.lista_cerrada) or any(d['estado'] == hijo1 for d in self.lista_abierta)):
                        self.lista_abierta.append({"estado": hijo1, "padre": len(self.lista_cerrada) -1 })
                    hijo2 = [estado_actual[0], estado_actual[2], estado_actual[1],
                            estado_actual[3], estado_actual[4], estado_actual[5],
                            estado_actual[6], estado_actual[7], estado_actual[8]
                    ]
                    if not (any(d['estado'] == hijo2 for d in self.lista_cerrada) or any(d['estado'] == hijo2 for d in self.lista_abierta)):
                        self.lista_abierta.append({"estado": hijo2, "padre": len(self.lista_cerrada) -1 })
                    hijo3 = [estado_actual[0], estado_actual[4], estado_actual[2],
                            estado_actual[3], estado_actual[1], estado_actual[5],
                            estado_actual[6], estado_actual[7], estado_actual[8]
                    ]
                    if not (any(d['estado'] == hijo3 for d in self.lista_cerrada) or any(d['estado'] == hijo3 for d in self.lista_abierta)):
                        self.lista_abierta.append({"estado": hijo3, "padre": len(self.lista_cerrada) -1 })
                if(index == 2):
                    hijo1 = [estado_actual[0], estado_actual[2], estado_actual[1],
                            estado_actual[3], estado_actual[4], estado_actual[5],
                            estado_actual[6], estado_actual[7], estado_actual[8]
                    ]
                    if not (any(d['estado'] == hijo1 for d in self.lista_cerrada) or any(d['estado'] == hijo1 for d in self.lista_abierta)):
                        self.lista_abierta.append({"estado": hijo1, "padre": len(self.lista_cerrada) -1 })
                    hijo2 = [estado_actual[0], estado_actual[1], estado_actual[5],
                            estado_actual[3], estado_actual[4], estado_actual[2],
                            estado_actual[6], estado_actual[7], estado_actual[8]
                    ]
                    if not (any(d['estado'] == hijo2 for d in self.lista_cerrada) or any(d['estado'] == hijo2 for d in self.lista_abierta)):
                        self.lista_abierta.append({"estado": hijo2, "padre": len(self.lista_cerrada) -1 })
                if(index == 3):
                    hijo1 = [estado_actual[3], estado_actual[1], estado_actual[2],
                            estado_actual[0], estado_actual[4], estado_actual[5],
                            estado_actual[6], estado_actual[7], estado_actual[8]
                    ]
                    if not (any(d['estado'] == hijo1 for d in self.lista_cerrada) or any(d['estado'] == hijo1 for d in self.lista_abierta)):
                        self.lista_abierta.append({"estado": hijo1, "padre": len(self.lista_cerrada) -1 })
                    hijo2 = [estado_actual[0], estado_actual[1], estado_actual[2],
                            estado_actual[4], estado_actual[3], estado_actual[5],
                            estado_actual[6], estado_actual[7], estado_actual[8]
                    ]
                    if not (any(d['estado'] == hijo2 for d in self.lista_cerrada) or any(d['estado'] == hijo2 for d in self.lista_abierta)):
                        self.lista_abierta.append({"estado": hijo2, "padre": len(self.lista_cerrada) -1 })
                    hijo3 = [estado_actual[0], estado_actual[1], estado_actual[2],
                            estado_actual[6], estado_actual[4], estado_actual[5],
                            estado_actual[3], estado_actual[7], estado_actual[8]
                    ]
                    if not (any(d['estado'] == hijo3 for d in self.lista_cerrada) or any(d['estado'] == hijo3 for d in self.lista_abierta)):
                        self.lista_abierta.append({"estado": hijo3, "padre": len(self.lista_cerrada) -1 })
                if(index == 4):
                    hijo1 = [estado_actual[0], estado_actual[4], estado_actual[2],
                            estado_actual[3], estado_actual[1], estado_actual[5],
                            estado_actual[6], estado_actual[7], estado_actual[8]
                    ]
                    if not (any(d['estado'] == hijo1 for d in self.lista_cerrada) or any(d['estado'] == hijo1 for d in self.lista_abierta)):
                        self.lista_abierta.append({"estado": hijo1, "padre": len(self.lista_cerrada) -1 })
                    hijo2 = [estado_actual[0], estado_actual[1], estado_actual[2],
                            estado_actual[4], estado_actual[3], estado_actual[5],
                            estado_actual[6], estado_actual[7], estado_actual[8]
                    ]
                    if not (any(d['estado'] == hijo2 for d in self.lista_cerrada) or any(d['estado'] == hijo2 for d in self.lista_abierta)):
                        self.lista_abierta.append({"estado": hijo2, "padre": len(self.lista_cerrada) -1 })
                    hijo3 = [estado_actual[0], estado_actual[1], estado_actual[2],
                            estado_actual[3], estado_actual[5], estado_actual[4],
                            estado_actual[6], estado_actual[7], estado_actual[8]
                    ]
                    if not (any(d['estado'] == hijo3 for d in self.lista_cerrada) or any(d['estado'] == hijo3 for d in self.lista_abierta)):
                        self.lista_abierta.append({"estado": hijo3, "padre": len(self.lista_cerrada) -1 })
                    hijo4 = [estado_actual[0], estado_actual[1], estado_actual[2],
                            estado_actual[3], estado_actual[7], estado_actual[5],
                            estado_actual[6], estado_actual[4], estado_actual[8]
                    ]
                    if not (any(d['estado'] == hijo4 for d in self.lista_cerrada) or any(d['estado'] == hijo4 for d in self.lista_abierta)):
                        self.lista_abierta.append({"estado": hijo4, "padre": len(self.lista_cerrada) -1 })
                if(index == 5):
                    hijo1 = [estado_actual[0], estado_actual[1], estado_actual[5],
                            estado_actual[3], estado_actual[4], estado_actual[2],
                            estado_actual[6], estado_actual[7], estado_actual[8]
                    ]
                    if not (any(d['estado'] == hijo1 for d in self.lista_cerrada) or any(d['estado'] == hijo1 for d in self.lista_abierta)):
                        self.lista_abierta.append({"estado": hijo1, "padre": len(self.lista_cerrada) -1 })
                    hijo2 = [estado_actual[0], estado_actual[1], estado_actual[2],
                            estado_actual[3], estado_actual[5], estado_actual[4],
                            estado_actual[6], estado_actual[7], estado_actual[8]
                    ]
                    if not (any(d['estado'] == hijo2 for d in self.lista_cerrada) or any(d['estado'] == hijo2 for d in self.lista_abierta)):
                        self.lista_abierta.append({"estado": hijo2, "padre": len(self.lista_cerrada) -1 })
                    hijo3 = [estado_actual[0], estado_actual[1], estado_actual[2],
                            estado_actual[3], estado_actual[4], estado_actual[8],
                            estado_actual[6], estado_actual[7], estado_actual[5]
                    ]
                    if not (any(d['estado'] == hijo3 for d in self.lista_cerrada) or any(d['estado'] == hijo3 for d in self.lista_abierta)):
                        self.lista_abierta.append({"estado": hijo3, "padre": len(self.lista_cerrada) -1 })
                if(index == 6):
                    hijo1 = [estado_actual[0], estado_actual[1], estado_actual[2],
                            estado_actual[6], estado_actual[4], estado_actual[5],
                            estado_actual[3], estado_actual[7], estado_actual[8]
                    ]
                    if not (any(d['estado'] == hijo1 for d in self.lista_cerrada) or any(d['estado'] == hijo1 for d in self.lista_abierta)):
                        self.lista_abierta.append({"estado": hijo1, "padre": len(self.lista_cerrada) -1 })
                    hijo2 = [estado_actual[0], estado_actual[1], estado_actual[2],
                            estado_actual[3], estado_actual[4], estado_actual[5],
                            estado_actual[7], estado_actual[6], estado_actual[8]
                    ]
                    if not (any(d['estado'] == hijo2 for d in self.lista_cerrada) or any(d['estado'] == hijo2 for d in self.lista_abierta)):
                        self.lista_abierta.append({"estado": hijo2, "padre": len(self.lista_cerrada) -1 })
                if(index == 7):
                    hijo1 = [estado_actual[0], estado_actual[1], estado_actual[2],
                            estado_actual[3], estado_actual[7], estado_actual[5],
                            estado_actual[6], estado_actual[4], estado_actual[8]
                    ]
                    if not (any(d['estado'] == hijo1 for d in self.lista_cerrada) or any(d['estado'] == hijo1 for d in self.lista_abierta)):
                        self.lista_abierta.append({"estado": hijo1, "padre": len(self.lista_cerrada) -1 })
                    hijo2 = [estado_actual[0], estado_actual[1], estado_actual[2],
                            estado_actual[3], estado_actual[4], estado_actual[5],
                            estado_actual[7], estado_actual[6], estado_actual[8]
                    ]
                    if not (any(d['estado'] == hijo2 for d in self.lista_cerrada) or any(d['estado'] == hijo2 for d in self.lista_abierta)):
                        self.lista_abierta.append({"estado": hijo2, "padre": len(self.lista_cerrada) -1 })
                    hijo3 = [estado_actual[0], estado_actual[1], estado_actual[2],
                            estado_actual[3], estado_actual[4], estado_actual[5],
                            estado_actual[6], estado_actual[8], estado_actual[7]
                    ]
                    if not (any(d['estado'] == hijo3 for d in self.lista_cerrada) or any(d['estado'] == hijo3 for d in self.lista_abierta)):
                        self.lista_abierta.append({"estado": hijo3, "padre": len(self.lista_cerrada) -1 })
                if(index == 8):
                    hijo1 = [estado_actual[0], estado_actual[1], estado_actual[2],
                            estado_actual[3], estado_actual[4], estado_actual[8],
                            estado_actual[6], estado_actual[7], estado_actual[5]
                    ]
                    if not (any(d['estado'] == hijo1 for d in self.lista_cerrada) or any(d['estado'] == hijo1 for d in self.lista_abierta)):
                        self.lista_abierta.append({"estado": hijo1, "padre": len(self.lista_cerrada) -1 })
                    hijo2 = [estado_actual[0], estado_actual[1], estado_actual[2],
                            estado_actual[3], estado_actual[4], estado_actual[5],
                            estado_actual[6], estado_actual[8], estado_actual[7]
                    ]
                    if not (any(d['estado'] == hijo2 for d in self.lista_cerrada) or any(d['estado'] == hijo2 for d in self.lista_abierta)):
                        self.lista_abierta.append({"estado": hijo2, "padre": len(self.lista_cerrada) -1 })
                    





matriz = Busqueda_anchura()
matriz.obtener_matriz()
matriz.mostrar_matriz_inicial()
matriz.busqueda_anchura()

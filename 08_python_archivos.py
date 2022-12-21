#archivos
archivo = open("puntos/requirements.txt", "r")
"""print(archivo)
print(archivo.read())
print(archivo.seek(0))
print(archivo.read())
archivo.seek(0)"""

"""print(archivo.readLine())
print(archivo.readLine())
archivo.seek(0)
print(archivo.readLine())"""

"""lineas = archivo.readlines()
print(lineas)
for linea in lineas:
    print(linea)

archivo.close()"""


with open("nombres.txt", "a") as archivo:
    text = archivo.write("3 Contenido del archivo escrito desde python \n")
    print(text)


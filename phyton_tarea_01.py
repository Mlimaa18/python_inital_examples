numeros = []
numeros = [3, 15, 23, 42, 30, 10, 10, 12]
numeroDatos = 7
if len(numeros) > 0:
    numeroDatos = len(numeros)

print(f"Función que devuelve la moda, media, mediana de un conjunto de {numeroDatos} datos")
if len(numeros) == 0:
    for x in range(numeroDatos):
        print(f"Ingrese el número: {x+1}")
        numeros.append(int(input()))

print(f"El arreglo de numeros inicial es: {numeros}")

def maxNumber(data):
    data.sort(reverse=True)
    return data[0]

def minNumber(data):
    data.sort()
    return data[0]

def sortNumbers(data,isReversed = False):
    data.sort(reverse=isReversed)
    return data

def media (data):
    result = 0
    for numero in data:
        result += numero
    return result/len(data)

def mediana(data):
    data.sort()
    centerIndex = len(data)//2
    mediana = 0
    if(len(data)%2 == 0):
        mediana = (data[centerIndex - 1] + data[centerIndex])/2
    else:
        mediana = data[centerIndex]
    return mediana

def moda(data):
    modaNumbers = {}
    modaNumber = [0]
    for index, numero in enumerate(data):
        # print({numero: data.count(numero)})
        # print(numero in modaNumbers)
        if numero in modaNumbers:
            modaNumbers[numero] = modaNumbers[numero] + 1
        else:
            modaNumbers[numero] = 1
        if index == 0:
            modaNumber = [data[0]]
        else:
            if modaNumbers[numero] >= modaNumbers[modaNumber[0]]:
                if numero not in modaNumber:
                    if modaNumbers[numero] == modaNumbers[modaNumber[0]]:
                        modaNumber.append(numero)
                    else:
                        modaNumber = []
                        modaNumber.append(numero)
                else:
                    modaNumber = []
                    modaNumber.append(numero)
                    
    # return string  
    return (', '.join(map(str, modaNumber)))

def textAnalysis():
    text = "El Lorem Ipsum fue concebido como un texto de relleno, formateado de una cierta manera para permitir la presentación de elementos gráficos en documentos, sin necesidad de una copia formal. El uso de Lorem Ipsum permite a los diseñadores reunir los diseños y la forma del contenido antes de que el contenido se haya creado, dando al diseño y al proceso de producción más libertad."
    splitText = text.split()
    wordsInText = {}
    for index, word in enumerate(splitText):
        if word in wordsInText:
            wordsInText[word] = wordsInText[word] + 1
        else:
            wordsInText[word] = 1
    print(f"\nEl texto tiene {len(splitText)} palabras y {len(wordsInText)} son diferentes")
    print(wordsInText)
    # for key in sorted(wordsInText):
    #     print(key, wordsInText[key])
    sorted_dict = {k: wordsInText[k] for k in sorted(wordsInText)}
    print(sorted_dict)

print(f"El arreglo ordenado de forma ascendete es {sortNumbers(numeros,)}")
print(f"El arreglo ordenado de forma descendete es {sortNumbers(numeros,True)}")
print(f"El número más pequeño es: {minNumber(numeros)}")
print(f"El número más grande es: {maxNumber(numeros)}")
print(f"La media o promedio es: {media(numeros)}")
print(f"La mediana es: {mediana(numeros)}")
print(f"La moda del conjunto de datos es: {moda(numeros)}")
textAnalysis()
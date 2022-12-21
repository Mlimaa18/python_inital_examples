#errores
while True:
    try:
        edad = int(input("Edad:"))
        print(edad)

        nacimiento = 2021 - edad
        print(nacimiento)
        resultado = nacimiento/edad
        print(resultado)

    except ValueError as err: #as crea un alias para ValueError
        print(f"Ingresa un número válido: {err}")
    except ZeroDivisionError:
        print("El 0 no es un número válido")
    else: #Se ejecuta cuando se ha cumplido el try sin errores
        print("Gracias :)")
        break
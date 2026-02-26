estudiante = []

while True:
    try:
        cantidades = int(input("cuantas opciones desea realizar: "))
        if cantidades < 0:
            print("Error solo ponga numeros positivos")
        else:
            print("siguiente paso...")
            break

    except ValueError:
        print("Error solo ponga numeros y que sean enteros")

for i in range(cantidades):
    nombre = input("ingrese el nombre del estudiante: ")
    edad = int(input("ingrese la edad del estudiante: "))
    estudiante.append(nombre)
    estudiante.append(edad)

for data in estudiante:
    print(data)
while True:
    print("1. saludar")
    print("2. la hora")
    print("3. salir")
    try:
        opcion = int(input(" que opcion desea realizar: "))
        if opcion == 1:
            print("holaaa!")
        elif opcion == 2:
            import datetime
            hora_actual = datetime.datetime.now()
            print("La hora actual es:", hora_actual.strftime("%H:%M:%S"))
        elif opcion == 3:
            break
        else:
            print("opcion invalida")
    except ValueError:
        print("opcion invalida, ingrese solamente numeros")
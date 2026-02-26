saldo = 1000
while True:
    try:
        opciones = int(input("cuantas opciones desea realizar: "))
        if opciones > 0:
            break
        else:
            print("opcion invalida ponga numeros positivos")

    except ValueError:
        print("opcion invalida, ponga numeros enteros")
    
for i in range(opciones):
    print("operacion", i + 1)
    print("menu: ")
    print("1. consultar saldo")
    print("2. retirar dinero")
    print("3. depositar dinero")
    while True:
        try:
            decision = int(input("que opcion desea utilizar (1/2/3): "))

            if decision == 1:
                print(f"su saldo actual es: {saldo}")
                break
            elif decision == 2:
                while True:
                    try:
                        monto = float(input("cuanto desea retirar: "))
                        if monto < 0:
                            print("Error ponga solamente numeros positivos")

                        elif monto > saldo:
                            print("saldo insuficiente")

                        else:
                            saldo -= monto 
                            print(f"su saldo actual es: {saldo}")
                            break
                    except ValueError:
                        print("Error opcion invalida, solo ponga numeros")
                break
            elif decision == 3:
                while True:
                    try:
                        monto = float(input("cuanto dinero desea depositar: "))
                        if monto < 0:
                            print("Error ponga solamente numeros positivos")
                        else:
                            saldo += monto
                            print(f"su saldo actual es: {saldo}")
                            break
                    except ValueError:
                        print("Error opcion invalida, solo ponga numeros")

                break     
            else:
                print("opcion invalida escoga entre las opciones que se le mostro")   
        
        except ValueError:
            print("opcion invalida, solo ponga numeros y enteros")

print("gracias por usar nuestros cajero")
saldo = 1000
contraseña = 1234
Intentos_max = 3
historial = []

def logica_retiro(saldo, historial):
    while True:
        try:
            monto = float(input("ingrese cuanto desea retirar: "))
            if monto < 0:
                 print("Error solo ingrese numeros positivos.")
            elif monto > saldo:
                print("saldo insuficiente.")
            else:
                saldo -= monto
                print(f"proceso exitoso su saldo actual es {saldo}.")
                historial.append(f"retiro de {monto} | Saldo actual: {saldo}")
                break
        except ValueError:
            print("Error")
    return saldo

def logica_deposito(saldo, historial):
    while True:
        try:
            monto = float(input("cuanto desea depositar: "))
            if monto > 0:
                saldo += monto
                print(f"proceso finalizado, tu saldo actual es {saldo}.")
                historial.append(f"Deposito de {monto} | Saldo actual: {saldo}")
                break    
            else:
                print("opcion invalida.")
        except ValueError:
            print("Error.")
    return saldo
    

def gestion_saldo(saldo, historial):
    print(f"su saldo actual: {saldo}")
    historial.append(f"saldo actual es: {saldo}")
    return saldo

def gestion_historial(historial):
    if len(historial) == 0:
        print("No hay movimientos registrados.")
    else:
        print("HISTORIAL")
        for movimiento in historial:
            print(movimiento)

def menu(saldo):
    while True:
        try:
            opciones = int(input("cuantas ocpiones desea realizar: "))
            if opciones > 0:
                break
            else:
                print("opcion invalida")
        except ValueError:
            print("Error")
    for i in range(opciones):
        print("operacion", i + 1)
        print("menu: ")
        print("1. consultar saldo")
        print("2. retirar")
        print("3. depositar")
        print("4. mostrar historial")
        while True:
            try:
                opcion = int(input("que opcion desea realizar (1/2/3): "))
                if opcion == 1:
                    saldo = gestion_saldo(saldo, historial)
                    break
                elif opcion == 2:
                    saldo = logica_retiro(saldo, historial)
                    break
                elif opcion == 3:
                    saldo = logica_deposito(saldo, historial)
                    break
                elif opcion == 4:
                    gestion_historial(historial)
                    break
                else:
                    print("opcion invalida")
            except ValueError:
                print("opcion invalida.")

def auntenticar():
    intentos = 0
    while intentos < Intentos_max:
        pin = int(input("ingresar contraseña: "))
        if pin == contraseña :
            print("autenticacion completa.")
            menu(saldo)
            return True
        else:
            intentos += 1
            print(f"contraseña incorrecta {intentos}/{Intentos_max}")
    print("intentos maximos.")
    return False

print("bienvenido a tu cajero automatico :)")

auntenticar()
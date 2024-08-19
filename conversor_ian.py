import os

def conversion(opcion,dinero):
    CambioHoy=18.41
    if opcion==1:
        print("Tus",dinero,"MXN son",round(dinero/CambioHoy,2),"USD\n")
    elif opcion==2:
        print("Tus",dinero,"USD son",round(dinero*CambioHoy,2),"MXN\n")

while 1:
    menu1=int(input("Hola mi amor uwu\nSelecciona:\n1. Acceder a la selección\n2. Salir del sistema\n"))
    if menu1==1:
        os.system("clear")
        while 1:
            menu2=int(input("Selecciona el tipo de cambio que quieres\n1. MXN a USD\n2. USD a MXN\n3. Regresar\n"))
            if menu2==1 or menu2==2:
                cantidad_dinero=float(input("Ingrese la cantidad de dinero que desea convertir:\n"))
                conversion(menu2,cantidad_dinero)
                break
            else:
                os.system("clear")
                break

    elif menu1==2:
        os.system("clear")
        print("Se cerró el sistema")
        break
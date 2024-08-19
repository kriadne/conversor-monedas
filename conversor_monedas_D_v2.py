# fx conversiones
def convert(condition, currency, usd_value):
    # de USD a X moneda
    if condition == 2:
        money = float(input('Ingresar valor en USD a convertir a ' +currency+ ': '))
        res = str(round((money*usd_value),2))
        print('Al día 24 de julio de 2024, son $' +res+ ' ' +currency+ '.')
    # de X moneda a USD
    elif condition == 1:
        money = float(input("Ingresar valor en " +currency+ " a convertir a USD:"))
        usd = str(round((money / usd_value),2))
        print("Al día 24 de julio de 2024, son: $" +usd+ " dólares estadounidenses (USD).")


while 1:
    # menu 1: inicio
    menu = int(input('Conversor de Monedas\n[1] Iniciar\n[2] Salir\nSelecciona una opción e ingresa el número correspondiente:\n'))
    # opcion iniciar
    if menu == 1:
        # menu 2: conversiones
        opcion_conversor = int(input('Desea convertir:\n[1] Moneda en específico a USD\n[2] USD a una moneda en específico\nSelecciona una opción e ingresa el número correspondiente:\n'))
        
        # menu 3.1: de X moneda a USD
        if opcion_conversor == 1:
            opcion_currency1 = int(input('Moneda que desea convertir a USD:\n[1] MXN\n[2] ARS\n[3] COP\n[4] CLP\n[5] EUR\nSelecciona una opción e ingresa el número correspondiente:\n'))
            if opcion_currency1 == 1:
                convert(1, 'MXN', 18.37)
            elif opcion_currency1 == 2:
                convert(1, 'ARS', 927.76)
            elif opcion_currency1 == 3:
                convert(1, 'COP', 4046.28)
            elif opcion_currency1 == 4:
                convert(1, 'CLP', 947.23)
            elif opcion_currency1 == 5:
                convert(1, 'EUR', 1.08)
            else:
                print("Opción no válida")

        # menu 3.2: de USD a X moneda
        elif opcion_conversor == 2:
            opcion_currency2 = int(input('Moneda a la que se desean convertir los USD:\n[1] MXN\n[2] ARS\n[3] COP\n[4] CLP\n[5] EUR\nSelecciona una opción e ingresa el número correspondiente:\n'))
            if opcion_currency2 == 1:
                convert(2, 'MXN', 18.37)
            elif opcion_currency2 == 2:
                convert(2, 'ARS', 927.76)
            elif opcion_currency2 == 3:
                convert(2, 'COP', 4046.28)
            elif opcion_currency2 == 4:
                convert(2, 'CLP', 947.23)
            elif opcion_currency2 == 5:
                convert(2, 'EUR', 1.08)
            else:
                print("Opción no válida")

        # opcion no prevista en menu 2
        else:
            print("Opción no válida")

    # opcion salir
    elif menu == 2: break

    # opcion distinta a 1 o 2
    else:
        print('Elige una opción válida')
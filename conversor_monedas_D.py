import os

# fx conversiones
def convert(condition, currency, usd_value):
    os.system("clear")
    # de USD a X moneda
    if condition == 2:
        money = float(input('Ingresar valor en USD a convertir a ' +currency+ ': '))
        res = str(round((money*usd_value),2))
        print('***\nAl día 24 de julio de 2024, $' +str(money)+ ' '+usd+' equivalen a: \n$' +res+ ' ' +currency+ '.\n***')
    # de X moneda a USD
    elif condition == 1:
        money = float(input("Ingresar valor en " +currency+ " a convertir a "+usd+":"))
        res = str(round((money / usd_value),2))
        print("***\nAl día 24 de julio de 2024, $" +str(money)+ " " +currency+ " equivalen a: \n$" +res+ " " +usd+".\n***")

# fx opcion no valida
def error():
    os.system("clear")
    print('Error: elige una opción válida')

# variables currency
mxn = 'peso(s) mexicano(s) (MXN)'
ars = 'peso(s) argentino(s) (ARS)'
cop = 'peso(s) colombiano(s) (COP)'
clp = 'peso(s) chileno(s) (CLP)'
eur = 'euro(s) (EUR)'
usd = 'dólar(es) estadounidense(s) (USD)'
# lista currencies + texto selecciona
lista = '[1]'+mxn+'\n[2]'+ars+'\n[3]'+cop+'\n[4]'+clp+'\n[5]'+eur
select_text = 'Selecciona una opción e ingresa el número correspondiente:\n'

while 1:
    # menu 1: inicio
    menu = int(input('Conversor de Monedas\n[1] Iniciar\n[2] Salir\n'+select_text))
    # opcion iniciar
    if menu == 1:
        os.system("clear")
        # menu 2: conversiones
        opcion_conversor = int(input('Desea convertir:\n[1] Moneda en específico a '+usd+'\n[2] '+usd+' a una moneda en específico\n'+select_text))
        # menu 3.1: de X moneda a USD
        if opcion_conversor == 1:
            os.system("clear")
            opcion_currency1 = int(input('Moneda que desea convertir a '+usd+':\n'+lista+'\n'+select_text))
            if opcion_currency1 == 1: convert(1, mxn, 18.37)
            elif opcion_currency1 == 2: convert(1, ars, 927.76)
            elif opcion_currency1 == 3: convert(1, cop, 4046.28)
            elif opcion_currency1 == 4: convert(1, clp, 947.23)
            elif opcion_currency1 == 5: convert(1, eur, 1.08)
            else: error()
        # menu 3.2: de USD a X moneda
        elif opcion_conversor == 2:
            os.system("clear")
            opcion_currency2 = int(input('Moneda a la que se desean convertir los '+usd+':\n'+lista+'\n'+select_text))
            if opcion_currency2 == 1: convert(2, mxn, 18.37)
            elif opcion_currency2 == 2: convert(2, ars, 927.76)
            elif opcion_currency2 == 3: convert(2, cop, 4046.28)
            elif opcion_currency2 == 4: convert(2, clp, 947.23)
            elif opcion_currency2 == 5: convert(2, eur, 1.08)
            else: error()
        # opcion no prevista en menu 2
        else: error()
    # opcion salir
    elif menu == 2: 
        os.system("clear")
        break
    # opcion distinta a 1 o 2
    else: error()
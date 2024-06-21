from funcion import *
import os, time 

while True:
    os.system ('cls')
    print('\tMENÚ BUS')
    print('\nopc.1 = mostrar asientos disponibles.')
    print('opc.2 = comprar asiento.')
    print('opc.3 = mostrar ventas realizadas.')
    print('opc.4 = generar archivo csv.')
    print('opc.5 = salir.')

    opc = int(input('ingrese opción: '))

    if opc==1:
        opc_1()
        time.sleep(4)
    elif opc==2:
        opc_2()
    elif opc==3:
        opc_3()
        time.sleep(4)
    elif opc==4:
        opc_4()
    else:
        print("adios..")
        break

personas =[]
import csv
valor= 10000
import time
bus =[["o" for x in range(4)] for y in range(4)]
for fila_indice, fila in enumerate(bus):
    print(f"fila {fila_indice + 1}:",",".join(fila))
def opc_1():
    print('\t\nMOSTRAR ASIENTOS')
    for fila_indice, fila in enumerate(bus):
        print(f"fila {fila_indice + 1}:",",".join(fila))
    

def opc_2():
    persona ={}
    print("\tCOMPRAR  ASIENTO")
    while True:
        nombre =  input('\ningresa nombre del comprador: ')
        if len(nombre)>=3 and nombre.isalpha:
            print('valido.')
            time.sleep(2)
            break
        else:
            print("carácteres, más de 3 letras.")
    while True:
        try:
            edad =  int(input('ingresa la edad del comprador: '))
            if edad==0 or edad<0:
                print('valor positivo, porfavor (a menos que el comprador no exista..)')
            else:
                break
        except:
            print('digitos enteros.')
    if edad<18:
        valor_asiento = 0.7*valor
    elif edad>18:
        valor_asiento= valor
    elif edad<65:
        valor_asiento= valor
    else:
        valor_asiento = 0.75*valor

    while True:
        try:
            telefono =  int(input('ingresa telefono del comprador: '))
            if len(str(telefono))==9 and str(telefono)[0]=="9":
                print('valido.')
                break
            else:
                print('debe existir el 9 como inicial y 8 numeros más. ej: 912345678)')
        except:
            print('digitos enteros.')
    
    opc_1()
    while True:
        try:
            fila =  int(input('\ningrese la fila del asiento: '))
            if fila>=0:
                break
            else:
                    print('no números negativos.')
        except:
            print('numeros.')
        while True:
            try:
                asiento = int(input('ingrese el asiento del asiento: '))
                if fila>=0:
                    break
                else:
                    print('no números negativos.')
            except:
                print('numeros.')
    fila1= fila-1
    asiento1 = asiento-1
    if bus[fila1][asiento1]=="o":
        bus[fila1][asiento1]="x"
    else:
        print('está ocupado.')
    print('se compró el asiento con éxito.')
    persona ={"nombre":nombre,
              "edad":edad,
              "fono":telefono,
              "pago":valor_asiento,
              "asiento":bus[fila1][asiento1]}
    personas.append(persona)
    opc_1()
    time.sleep(3)

def opc_3 ():
        if personas ==0:
            print('no hay nada..')
        else:
            for  z in personas:
                print(f"NOMBRE : {z["nombre"]}")
                print(f"EDAD: {z["edad"]}")
                print(f"TELÉFONO: {z["fono"]}")
                print(f'PAGO BUS: {z["pago"]}')
                print(f"ASIENTO: {z["asiento"]}")

def opc_4():
    if personas ==0:
            print('no hay nada..')
    else:
        with open ("archivoBus.csv","w") as csvfile:
            escritor = csv.writer(csvfile)
            for clave, valor in personas:
                escritor.writerow("\n")
                escritor.writerow(clave)
                escritor.writerow(valor)
            



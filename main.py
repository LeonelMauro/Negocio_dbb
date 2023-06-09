from funciones import *

while True:
    menu()
    try:
        opcion = int(input("Eliga la opcion: "))
    except:
        print("Opcion incorrecta.")
    if opcion ==1:
        agregar_cliente()
    elif opcion==2: 
        agregar_productos()
    elif opcion==3:
        list_productos()
    elif opcion==4:
        list_clientes()
    elif opcion==5:
        borra_cliente()    
    elif opcion==6:
        update_produc()
    else:
        print("Opcion incorrecta.")


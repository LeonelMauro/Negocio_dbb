import psycopg2

conn = psycopg2.connect(
    user= "postgres", password= "1234", port="5432", host= "localhost", database= "polleria"

)

cursor= conn.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS clientes (id SERIAL PRIMARY KEY,name VARCHAR (255), age INTEGER, email VARCHAR (255))"
)

cursor.execute(
    "CREATE TABLE IF NOT EXISTS productos (id SERIAL PRIMARY KEY, name VARCHAR(255), precio INTEGER, area VARCHAR(255))"
)
conn.commit()


def agregar_cliente():
    name= input("ingrese el nombre del cliente: ").title()
    age = input("ingrese la edad : ")
    email= input("ingrese el email: ").title()
    cursor= conn.cursor()
    cursor.execute(
    "INSERT INTO clientes (name, age, email) VALUES (%s, %s, %s)",
    (name, age, email),
    )
    conn.commit()

def agregar_productos():
    name= input("ingrese el nombre del producto: ").title()
    precio = input("ingrese el precio:$ ")
    area= input("ingrese el area: ").title()
    cursor = conn.cursor()
    cursor.execute(
    "INSERT INTO productos (name, precio, area) VALUES (%s, %s, %s)",
    (name, precio, area)
    )
    conn.commit()

def list_productos():
    cursor =conn.cursor()
    cursor.execute(
        "SELECT * FROM productos ")
    lista_prod= cursor.fetchall()
    for row in lista_prod:
        print(row)


def list_clientes():
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM clientes") 
    lista =cursor.fetchall()
    for row in lista:
        print("id",row[0],"Nombre: ",row[1]," Edad: ",row[2], "Area: ",row[3])

def borra_cliente():
    nombre=input("Ingre el nombre del cliente: ").title()
    cursor.execute("DELETE FROM clientes WHERE name= %s RETURNING *",(nombre,))
    borrado= cursor.fetchone()
    print(borrado)
    conn.commit()
    

def update_produc():
    list_productos()
    ingr_id = input('ingrese id del producto: ')
    name= input("ingrese el nombre del producto: ").title()
    precio = input("ingrese el precio:$ ")
    area= input("ingrese el area: ").title()
    cursor.execute("UPDATE productos SET name= %s, precio= %s, area=%s WHERE id= %s",
                   (name, precio, area,ingr_id,)
    )
    conn.commit()
    

def menu():
    print('''
            MENU
    1. Ingresar cliente
    2. Ingresar producto
    3. Lista de producto  
    4. Lista de clientes
    5. Borrar cliente
    6. Actualizar producto
    ''')

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


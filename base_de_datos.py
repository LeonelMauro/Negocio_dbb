import base_de_datos

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

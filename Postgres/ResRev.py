import psycopg2
import pandas as pd
import streamlit as st

def obtener_contraseña(filepath, name):
    with open(filepath, 'r') as archivo:
        for linea in archivo:
            if linea.startswith(name + ":"):
                return linea.split(":", 1)[1].strip()
    return None

# Uso del método
filepath = "passwords.txt"; name = "postgres"
keys = [obtener_contraseña(filepath, name)]

conexion = psycopg2.connect(database="TriadData", user="postgres", password=keys[0])
cursor = conexion.cursor()

query = """ SELECT * FROM "Restaurant_Revenue" """

#Ejecutamos la seleccion para hallar los datos 
cursor.execute(query)

# Obtener los resultados
resultados = cursor.fetchall()

# Convertir los resultados a un DataFrame de Pandas
values = ["# of Customers","Menu Price","Mrkg Spend","Cuisinem Type","Avg Customer Spending","Promotions","Reviews","Monthly Revenue"]
df = pd.DataFrame(resultados, columns=values)

# ---------------------------------------
# *           STREAMLIT PAGE            *
# ---------------------------------------

st.title("Restaurant Revenue")
st.write(df.head())
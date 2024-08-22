import psycopg2
import pandas as pd
import streamlit as st


# Path to your CSV file
csv_file_path = 'Database\Restaurant_revenue.csv'

# Read the CSV file, assuming the first row contains the column names
df = pd.read_csv(csv_file_path)

# ---------------------------------------
# *           STREAMLIT PAGE            *
# ---------------------------------------

st.title("Restaurant Revenue")
st.write(df.head())
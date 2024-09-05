import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression

# Path to your CSV file
csv_file_path = 'Database\\Restaurant_revenue.csv'

# Read the CSV file, assuming the first row contains the column names
df = pd.read_csv(csv_file_path)

# Leer y aplicar el archivo CSS externo
with open('styles.css') as f:
    css = f.read()
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# ---------------------------------------
# *           STREAMLIT PAGE            *
# ---------------------------------------

st.title("Restaurant Revenue")
# Crear layout de columnas con proporciones personalizadas
col1, col2 = st.columns([0.4, 0.6])  # Ajustar proporciones si es necesario

# Configurar opciones interactivas para el gráfico circular en la columna 1
with col1:    
    # Crear el gráfico circular con Plotly
    fig_pie = px.pie(df, names='Cuisine_Type', values='Number_of_Customers', title="Popularidad de Tipos de Cocina",
                        width=1000, height=400)

    # Personalizar el gráfico circular
    fig_pie.update_traces(textposition='inside', textinfo='percent+label')

    # Mostrar el gráfico circular en Streamlit
    st.plotly_chart(fig_pie, use_container_width=True)

# Configurar opciones interactivas para el gráfico de dispersión en la columna 2
with col2:
    # Ajustar la línea de tendencia
    X = df[['Number_of_Customers']].values
    y = df['Monthly_Revenue'].values

    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    # Calcular la distancia de los puntos a la línea de tendencia
    distances = np.abs(y - y_pred)
    max_distance = np.max(distances)
    min_distance = np.min(distances)

    # Normalizar las distancias para los colores
    normalized_distances = (distances - min_distance) / (max_distance - min_distance)

    # Crear el gráfico de dispersión con la línea de tendencia
    fig_scatter = go.Figure()

    # Añadir puntos de dispersión
    fig_scatter.add_trace(go.Scatter(
        x=df['Number_of_Customers'],
        y=df['Monthly_Revenue'],
        mode='markers',
        marker=dict(
            size=10,
            color=normalized_distances
        ),
        name='Datos'
    ))

    # Añadir línea de tendencia
    fig_scatter.add_trace(go.Scatter(
        x=df['Number_of_Customers'],
        y=y_pred,
        mode='lines',
        line=dict(color='green', width=2),
        name='Línea de Tendencia'
    ))

    # Actualizar el layout para mover la leyenda a la parte superior
    fig_scatter.update_layout(
        title="Relación entre Número de Clientes e Ingresos Mensuales",
        width=1000,
        height=400,
        xaxis_title='Número de Clientes',
        yaxis_title='Ingresos Mensuales',
        legend=dict(
            orientation="h",  # Orientación horizontal de la leyenda
            yanchor="bottom",  # Ancla vertical de la leyenda en la parte inferior
            y=1.001,             # Posición vertical de la leyenda (por encima del gráfico)
            xanchor="center",  # Ancla horizontal de la leyenda en el centro
            x=0.5              # Posición horizontal de la leyenda (centrado)
        )
    )

    # Mostrar el gráfico de dispersión en Streamlit
    st.plotly_chart(fig_scatter, use_container_width=True)
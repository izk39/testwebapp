import streamlit as st
import pandas as pd
import plotly.express as px

vehicles = pd.read_csv('./vehicles_us.csv')

st.header('Vehículos de segunda mano en EEUU')
st.write("""Esta webapp contiene información sobre vehículos de segunda mano en EEUU.
         Puedes elegir entre las diferentes opciones de gráfios para visualizar los datos.""")


# Crear gráfico de dispersión: Días Listados vs. Odómetro
fig1 = px.scatter(vehicles, x="days_listed", y="odometer", 
                      title="Gráfico de dispersión de Días Listados vs. Odómetro",
                      labels={"days_listed": "Días Listados", "odometer": "Odómetro (millas)"})
    
# Crear gráfico de dispersión: Días Listados vs. Precio
fig2 = px.scatter(vehicles, x="days_listed", y="price", 
                      title="Gráfico de dispersión de Días Listados vs. Precio",
                      labels={"days_listed": "Días Listados", "price": "Precio ($)"})
    
# Crear histograma: Distribución de Precios
fig3 = px.histogram(vehicles, x="price", 
                         title="Distribución de Precios de Vehículos", 
                         labels={"price": "Precio (en $)"}, nbins=250)

# Botón para el primer gráfico (Días Listados vs. Odómetro)
if st.button('Mostrar Gráfico de Dispersión: Días Listados vs. Odómetro'):
        st.subheader('Gráfico de Dispersión de Días Listados vs. Odómetro')
        st.write('Este gráfico muestra la correlación entre el número de días que un vehículo ha sido listado y su lectura del odómetro.')
        st.plotly_chart(fig1)

# Botón para el segundo gráfico (Días Listados vs. Precio)
if st.button('Mostrar Gráfico de Dispersión: Días Listados vs. Precio'):
        st.subheader('Gráfico de Dispersión de Días Listados vs. Precio')
        st.write('Este gráfico muestra la correlación entre el número de días que un vehículo ha sido listado y su precio.')
        st.plotly_chart(fig2)

# Botón para el tercer gráfico (Distribución de Precios)
if st.button('Mostrar Histograma de Distribución de Precios'):
        st.subheader('Distribución de Precios de Vehículos')
        st.write('Este histograma muestra la distribución de precios de los vehículos en el conjunto de datos.')
        st.plotly_chart(fig3)
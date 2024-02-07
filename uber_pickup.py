import streamlit as st
import pandas as pd 
import numpy as np

st.title('Uber pickups im NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


@st.cache_data

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Se crea una etiqueta de cargando info
data_load_state = st.text('Loading data...')

#Aqui se cargan solo 1000 registros de todo el archivo

data = load_data(10000)

#Se crea una etiqueta en donde indique que la carga del archivo fue correcta

data_load_state.text("Done! (using st.cache_data)")

# Se carga la informacion del dt y solo se muestasn las 10 primerfas filas
st.subheader("Raw data")
st.write(data.head(10))

#se agrega subtitulo

st.subheader("Number of pickups by hour")
 
 #Agregar un histograma

hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range= (0,24)) [0]

st.bar_chart(hist_values)

import streamlit as st
import pandas as pd
import pickle

st.write("""
# Flight Status Prediction

This app predicts the **Flight status** 
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    CarrierCode = st.sidebar.selectbox('CarrierCode', [0, 1, 2, 3])
    FlightNumber = st.sidebar.number_input('FlightNumber',value=0)
    DepartureStation = st.sidebar.number_input('DepartureStation', value=0)
    Arrivalstation = st.sidebar.number_input('Arrivalstation', value=0)
    PAX = st.sidebar.number_input('PAX', value=1)
    AOCHolder = st.sidebar.number_input('AOCHolder', value=0)
    DelayCode = st.sidebar.number_input('DelayCode', value=0)
    DelayTime = st.sidebar.number_input('DelayTime', value=0)
    data = {'CarrierCode': CarrierCode,
            'FlightNumber': FlightNumber,
            'DepartureStation': DepartureStation,
            'Arrivalstation': Arrivalstation,
            'PAX': PAX,
            'AOCHolder': AOCHolder,
            'DelayCode': DelayCode,
            'DelayTime': DelayTime}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

loaded_model = pickle.load(open("flightdatac.h5", "rb"))

prediction = loaded_model.predict(df)

st.subheader('Prediction')
st.write(prediction)

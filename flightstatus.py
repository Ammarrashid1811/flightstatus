import streamlit as st
import pandas as pd
import pickle

st.write("""
# Flight Status Prediction

This app predicts the **Flight status** 
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    CarrierCode = st.sidebar.number_input('CarrierCode', 0.0, 5.0, 2.0)
    DepartureStation = st.sidebar.number_input('DepartureStation', 0.0, 109.0, 55.0)
    Arrivalstation = st.sidebar.number_input('Newspaper', 0.0, 125.0, 70.0)
    AOCHolder = st.sidebar.number_input('AOCHolder', 0.0, 7.0, 3.0)
    data = {'CarrierCode': CarrierCode,
            'DepartureStation': DepartureStation,
            'Arrivalstation': Arrivalstation,
            'AOCHolder': AOCHolder}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

loaded_model = pickle.load(open("flightdatac.h5", "rb"))

prediction = loaded_model.predict(df)

st.subheader('Prediction')
st.write(prediction)

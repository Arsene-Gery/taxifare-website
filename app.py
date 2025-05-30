import streamlit as st
import pandas as pd
import numpy as np
import requests

'''
# TaxiFare Price Simulator
'''

date = st.text_input('choose a date and time')
longitude = st.text_input('choose a longitude')
latitude = st.text_input('choose a latitude')
drop_longitude = st.text_input('choose drop_longitude')
drop_latitude = st.text_input('choose drop_latitude')
passenger_count = st.text_input('choose a passenger_count')

url = 'https://taxifare.lewagon.ai/predict'

X_pred = {
    'pickup_datetime' : date,
    'pickup_longitude' : longitude,
    'pickup_latitude' : latitude,
    'dropoff_longitude' : drop_longitude,
    'dropoff_latitude' : drop_latitude,
    'passenger_count' : passenger_count
}

response = requests.get(url, params=X_pred)
data = response.json()

def get_map(longitude, latitude, drop_longitude, drop_latitude):

    df = pd.DataFrame({
        'latitude': [float(latitude), float(drop_latitude)],
        'longitude': [float(longitude), float(drop_longitude)]
    })

    return df

if st.button('DISPLAY MAP'):
    st.map(get_map(longitude, latitude, drop_longitude, drop_latitude))

if st.button('PREDICT FARE'):
    if '' in X_pred.values():
        st.write('Please be sure to submit all fields before predicting fare')
    else:
        st.write(f"Your fare is expected to cost ${round(data['fare'], 2)}")

import pickle 
import numpy as np
import streamlit as st

# load save model
model = pickle.load(open('penyakit_LungCancer.sav', 'rb'))

# judul web
st.title('Prediksi Penyakit Kanker Paru-paru')

GENDER = st.number_input('Jenis Kelamin')

AGE = st.number_input('AGE')

SMOKING = st.number_input('SMOKING')

YELLOW_FINGERS = st.number_input('YELLOW FINGERS')

ANXIETY = st.number_input('ANXIETY')

PEER_PRESSURE = st.number_input('PEER PRESSURE')

CHRONIC_DISEASE = st.number_input('CHRONIC DISEASE')

FATIGUE = st.number_input('FATIGUE')

ALLERGY = st.number_input('ALLERGY')

WHEEZING = st.number_input('WHEEZING')

ALCOHOL_CONSUMING = st.number_input('ALCOHOL CONSUMING')

COUGHING = st.number_input('COUGHING')

SHORTNESS_OF_BREATH = st.number_input('SHORTNESS OF BREATH')

SWALLOWING_DIFFCULTY = st.number_input('SWALLOWING DIFFCULTY')

CHEST_PAIN = st.number_input('CHEST PAIN')

# code for prediction
LungCancer_diagnosis = ''

if st.button ('Prediksi Penyakit Kanker Paru-paru') :
    LungCancer_prediction = model.predict([[GENDER,AGE,SMOKING,YELLOW_FINGERS,ANXIETY,PEER_PRESSURE,CHRONIC_DISEASE,FATIGUE,ALLERGY,WHEEZING,ALCOHOL_CONSUMING,COUGHING,SHORTNESS_OF_BREATH,SWALLOWING_DIFFCULTY,CHEST_PAIN]])
    
    if (LungCancer_prediction[0]==1):
        LungCancer_diagnosis = ' Mengidap'
    else:
        LungCancer_diagnosis = 'tidak mengidap'
        
st.success(LungCancer_diagnosis)
st.text('Putri Natahsya Sugianto - 201351110 - Malam A')
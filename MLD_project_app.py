from textwrap import fill
import pickle
import requests
import json
import streamlit as st
import pandas as pd


html_temp = """
<div style="background-color:green;padding:10px">
<h2 style="color:white;text-align:center;">Car Price Prediction</h2>
</div>"""
st.markdown(html_temp,unsafe_allow_html=True)
st.write("\n")

st.sidebar.write("Please, enter your car information:")

age=st.sidebar.selectbox("What is the age of the car:",(0,1,2,3))
gears=st.sidebar.selectbox("How many gears in the car?",(5,6,7,8))
hp=st.sidebar.slider("What is the hp_kw of the car?", 40, 294, step=5)
km=st.sidebar.slider("What is the km of the car", 0,317000, step=1000)
car_model=st.sidebar.selectbox("Select model of the car", ('Audi A1', 'Audi A2', 'Audi A3', 'Opel Astra', 'Opel Corsa', 'Opel Insignia', 'Renault Clio', 'Renault Duster', 'Renault Espace'))

my_dict = {
    "age": age,
    "hp_kW": hp,
    "km": km,
    'Gears':gears,
    "make_model": car_model
    
}

df = pd.DataFrame.from_dict([my_dict])

st.write("The configuration of your car is below")

#st.header("The configuration of your car is below")
st.table(df)

# To load machine learning model
import pickle
filename = "MLDproject_Final_model"
model = pickle.load(open(filename, "rb"))


# Prediction with user inputs
predict = st.button("Predict")
result = model.predict(df)
if predict :
    st.success("The estimated price of your car is {} ".format(int(result[0])))

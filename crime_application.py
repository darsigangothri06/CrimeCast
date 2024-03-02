import streamlit as st
import joblib
import pandas as pd
import sklearn

# to display plotly graphs
import json
import plotly

def get_crime_type(crime):
    if crime == 0: return 'THEFT'
    elif crime == 1: return 'BATTERY'
    elif crime == 2: return 'CRIMINAL DAMAGE'
    elif crime == 3: return 'ASSAULT'
    else: return 'No Major Crime Happened'

def prediction(x_cor, y_cor, loaded_data):
    example_data = pd.DataFrame({
        'Location Description': [1],
        'Arrest': [1],
        'Domestic': [0],
        'Beat': [1],
        'Ward': [15],
        'X Coordinate': [100.815117282],
        'Y Coordinate': [-0.669999562],
        'Year': [2024]
    })

    # x_cor = float(input('Enter Lattitude: '))
    # y_cor = float(input('Enter Longitude: '))

    example_data['X Coordinate'] = x_cor
    example_data['Y Coordinate'] = y_cor

    predictions = loaded_data.predict(example_data[['Location Description','Arrest','Domestic','Beat','Ward','X Coordinate', 'Y Coordinate','Year']])

    return (get_crime_type(predictions.tolist()[0]))

# main

loaded_data = joblib.load('crimecast_location_based_model.pkl')
st.title('Crime Prediction By Location Using Machine Learning')
x_cor = st.number_input('Enter Latittude: ', step=0.1)
y_cor = st.number_input('Enter Longitude: ', step=0.1)

if st.button('Predict crime type'):
    crime_type = prediction(x_cor, y_cor, loaded_data)
    if crime_type == 'No Major Crime Happened':
        st.success(crime_type)
    else:
        st.error(crime_type)

with open('1_number_of_crimes_by_year.json', 'r') as file:
    graph1 = json.load(file)

with open('2_count_of_crimes_by_crime_type.json', 'r') as file:
    graph2 = json.load(file)

with open('3_top_four_crime_types.json', 'r') as file:
    graph3 = json.load(file)

with open('4_count_of_top_four_crimes_by_location.json', 'r') as file:
    graph4 = json.load(file)

with open('5_count_of_all_crimes_by_location.json', 'r') as file:
    graph5 = json.load(file)

with open('6_number_of_crimes_by_month.json', 'r') as file:
    graph6 = json.load(file)

with open('7_count_of_crimes_by_year_and_arrest_status.json', 'r') as file:
    graph7 = json.load(file)

with open('8_correlation_between_attributes.json', 'r') as file:
    graph8 = json.load(file)

st.plotly_chart(graph1)
st.plotly_chart(graph2)
st.plotly_chart(graph3)
st.plotly_chart(graph4)
st.plotly_chart(graph5)
st.plotly_chart(graph6)
st.plotly_chart(graph7)
st.markdown("<span style='font-family: Arial; font-size: 15px;'><b>Correlation between dataset attributes</b></span>", unsafe_allow_html=True)
st.plotly_chart(graph8)
import joblib
import pandas as pd
import sklearn

def get_crime_type(crime):
    if crime == 0: return 'THEFT'
    elif crime == 1: return 'BATTERY'
    elif crime == 2: return 'CRIMINAL DAMAGE'
    elif crime == 3: return 'ASSAULT'
    else: return 'Other type'

loaded_data = joblib.load('crimecast_location_based_model.pkl')

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

x_cor = float(input('Enter Lattitude: '))
y_cor = float(input('Enter Longitude: '))

example_data['X Coordinate'] = x_cor
example_data['Y Coordinate'] = y_cor

predictions = loaded_data.predict(example_data[['Location Description','Arrest','Domestic','Beat','Ward','X Coordinate', 'Y Coordinate','Year']])

print(get_crime_type(predictions.tolist()[0]))
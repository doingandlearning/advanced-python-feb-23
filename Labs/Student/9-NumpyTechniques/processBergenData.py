import numpy as np
import pandas as pd

# Read a csv file, get a Pandas DataFrame back, and assign the 'Prediction' column to a NumPy array.
dataframe = pd.read_csv('BergenWeather2019.csv')
precipitation_mm = np.array(dataframe['Precipitation'])
print('\nPrecipitation mm\n', precipitation_mm)

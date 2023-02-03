# Import the Pandas module.
import pandas as pd

# Create a Series for each column.
bornSeries = pd.Series(
    {'Kevin': 1983, 'Kath': 1978, 'Ethan': 2012, 'Caleb': 2014})
heightSeries = pd.Series(
    {'Kevin':  180, 'Kath':  170, 'Ethan':  165, 'Caleb':  177})
weightSeries = pd.Series(
    {'Kevin': 83.5, 'Kath': 65.0, 'Ethan': 58.0, 'Caleb': 70.0})


df = pd.DataFrame({
	'Born': bornSeries,
	"Height": heightSeries,
	"Weight": weightSeries
})
# Use [] notation to get 1 column, as a Series.
# print('\nBorn\n',            df['Born'])
# # Use [] notation to get multiple columns, as a DataFrame.
# print('\nHeight, Weight\n',  df[['Height', 'Weight']])
# # Use property notation to get 1 column.
# print('\nBorn\n',            df.Born)

# # Create a new column.
# df['BMI'] = df['Weight'] / ((df['Height']/100.0) ** 2)
# print('\nBMI calculation\n', df['BMI'])

# print('\nKevin and Kath\n',   df['Kevin': 'Kath'])
# print('\nEthan onwards\n',       df['Ethan':])
# print('\nup to Ethan\n',         df[:'Ethan'])
# print('\nup to Ethan, step 2\n', df[:'Ethan':2])
# print('\nall, step 2\n',      df[::2])

# Use .loc to treat like 2D array, specifying [row-indexer-by-name, col-indexer-by-name].
print('\nEthan onwards, all columns\n',
      df.loc['Ethan':])                               # Slice
print('\nKevin and Kath, height and weight\n',
      df.loc['Kevin':'Kath', 'Height':'Weight'])   # Slice
print('\nKevin and Caleb, born and height\n',     df.loc[[
      'Kevin', 'Caleb'], ['Born', 'Height']])  # Fancy indexing
print('\n170cm or taller, height\n',
      df.loc[df['Height'] >= 170, [ 'Weight']] )      # Mask

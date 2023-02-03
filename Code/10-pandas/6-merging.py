import pandas as pd

df1 = pd.DataFrame({
		  'height': [180, 170, 165, 177],
    'name':   ['Kevin', 'Kath', 'Ethan', 'Caleb'],
    'born':   [1983, 1978, 2012, 2014],
})
print('\ndf1\n', df1)

df2 = pd.DataFrame({
    'height': [180, 170, 165, 20],
		    'name':   ['Kevin', 'Kath', 'Ethan', 'John'],
    'weight': [84.5, 65.0, 58.0, 70.0]
})
print('\ndf2\n', df2)

df3 = pd.merge(df1, df2, on="name")
print(df3)
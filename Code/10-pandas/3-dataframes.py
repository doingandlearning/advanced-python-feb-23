import pandas as pd
import numpy as np

names = ['Kevin', 'Kath', "Ethan", "Caleb"]
birth = [1983, 1978, 2012, 2014]

stats = list(zip(names,birth))

df = pd.DataFrame(stats, columns=["Name", "Born"])

print(2023 - df['Born'] ) 

stats = [
    {'name': 'Kevin',  'born': 1983, 'height': 180, 'weight': 83.5},
    {'name': 'Kath', 'born': 1978, 'height': 170, 'weight': 65.0},
    {'name': 'Ethan',    'born': 2012, 'height': 165, 'weight': 58.0},
    {'name': 'Caleb',   'born': 2014, 'height': 177, 'weight': 70.0}
]

df = pd.DataFrame(stats, index=[item['name'] for item in stats])
print(df)
print(df['born']['Kath'])
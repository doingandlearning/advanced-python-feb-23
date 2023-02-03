import pandas as pd

# Create a Series where the index is non-numeric.
data = pd.Series(['John', 'Mary', 'Ethan', 'Alex', 'Jeff'],
                 index=[100, 101, 257, 118, 123])

# print(data["E101"])
# print(data["E101": "E123"])
# print(data[1: 5])

print(data[101])
print(data[1:3])

print(data.loc[101])
print(data.loc[101:118])

print(data.iloc[1])
print(data.iloc[1:3])
import pandas as pd

# load the dataset
df = pd.read_csv("dataset.csv")
print(df)
# check for missing values
print(df.isna())

# fill missing values with a specific value
filled = df.copy()
filled.fillna(0, inplace=True)
print(filled)

# fill missing values with a calculation
cal_filled = df.copy()
cal_filled['Age'].fillna(df['Age'].mean(), inplace=True)
cal_filled['Name'].fillna("Unknown", inplace=True)
print("Filled with calculations: ", cal_filled)

# drop rows with missing values
dropped = df.copy()
dropped.dropna(inplace=True)
print(dropped)

print(df)

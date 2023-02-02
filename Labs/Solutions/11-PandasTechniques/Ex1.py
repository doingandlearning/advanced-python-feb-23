import pandas as pd

df = pd.read_csv("ex1.csv")
print(df)

df['B'] *= 2

df['C'] = df['A'] + df['B']
print(df)

# Without changing the original data
df = pd.read_csv("ex1.csv")
new_df = df.copy()
new_df['B'] = df['B'] * 2
new_df['C'] = df['A'] + new_df['B']

print("original df", df)
print("new df: ", new_df)

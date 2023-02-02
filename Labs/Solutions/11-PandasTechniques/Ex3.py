import pandas as pd

# load the datasets
transactions = pd.read_csv("transactions.csv")
stores = pd.read_csv("stores.csv")


merged = pd.merge(transactions, stores)
print(merged)

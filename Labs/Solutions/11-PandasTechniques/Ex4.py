import pandas as pd

# load the datasets
customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")

merged = pd.merge(customers, products,
                  left_on="Customer_ID", right_on="Cust_ID")
print(merged)

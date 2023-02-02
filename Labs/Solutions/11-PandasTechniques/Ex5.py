import pandas as pd

# load the datasets
customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")

merged_outer = pd.merge(customers, products,
                        left_on="Customer_ID", right_on="Cust_ID", how="outer")
print(merged_outer)

merged_left = pd.merge(customers, products,
                       left_on="Customer_ID", right_on="Cust_ID", how="left")
print(merged_left)

merged_right = pd.merge(customers, products,
                        left_on="Customer_ID", right_on="Cust_ID", how="right")
print(merged_right)

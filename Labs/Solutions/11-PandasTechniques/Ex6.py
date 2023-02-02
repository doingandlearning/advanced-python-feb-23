import pandas as pd

# load the datasets
left_dataset = pd.read_csv("left_dataset.csv")
middle_dataset = pd.read_csv("middle_dataset.csv")
right_dataset = pd.read_csv("right_dataset.csv")

# merge the left_dataset and middle_dataset on the ID column
merged_df1 = pd.merge(left_dataset, middle_dataset, on='ID')

# merge the resulting dataset from step 2 with the right_dataset on the ID column
merged_df = pd.merge(merged_df1, right_dataset, on='ID')

# show the resulting merged dataset
print(merged_df)

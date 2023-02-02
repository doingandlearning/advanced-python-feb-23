# Pandas Techniques
 
## Overview
In this lab you’ll create a simple Pandas DataFrame containing information about FIFA World Cup winners since the tournament started in 1930. You’ll use various techniques to manipulate the rows and columns in the DataFrame.

Source folders
Student folder​: Labs\Student\PandasTechniques
Solution folder: Labs\Solutions\PandasTechniques


## 1. Universal functions with Pandas: 

We're going to convert some data to a data frame and then apply universal functions to them.

Here's the CSV data:

```csv
A,B
1,4
2,5
3,6
```

- Create a CSV file with this data, import and form it as a data frame

```python
csv_df = pd.read_csv(csv_location)
```

- Multiply all of the B values by 2.
- Create a new column which is the sum of the first two and call it C
- Can you do this without modifying the underlying data?
- What else could you do here?

# 2. One-to-one merge:
Here is a dataset of employee information and another dataset of their corresponding department information:

```csv
employees.csv
ID,Name,Dept_ID
1,John,1
2,Sara,2
3,Mike,1

employees_start.csv
ID,Start
1,2012
2,2020
3,2022
```
Use Pandas to merge the two datasets on the employee ID column and print the results.
When might this be useful?

## 3. Many-to-one merge: 
Here's a dataset of sales transactions and another dataset of the corresponding store information. 

```csv
transactions.csv
Store_ID,Transaction_ID,Amount
1,1,100
2,2,200
3,3,300
1,4,50
2,5,250

stores.csv
Store_ID,Name,City
1,Store1,New York
2,Store2,Chicago
3,Store3,Los Angeles
```

Use Pandas to merge the two datasets on the store ID column.

## 4. Merging on explicit column names: 

Here's a dataset of product information and another dataset of customer information. 

```csv
products.csv
Product_ID,Name,Price,Cust_ID
1,Product1,10,2
2,Product2,20,1
3,Product3,30,2

customers.csv
Customer_ID,Name,Address
1,John,NY
2,Sara,Chicago
3,Mike,LA
```

Use Pandas to merge the two datasets on the customer ID column. Notice it has different names in the two datasets.

# 5. All the joins: 
Using the data from the last exercise, practice using an inner join to merge them. What is inclued/left out?

Do the same with the other join - same questions:

- Outer Join
- Left Join
- Right Join



## 6. Using the merge function multiple times (if time permits) 

```csv
left_dataset.csv
ID,Name,Value
1,John,10
2,Sara,20
3,Mike,30

middle_dataset.csv
ID,Age
1,25
2,30
3,35

right_dataset.csv
ID,Address
1,NY
2,Chicago
3,LA
```

- Start by loading the three datasets 'left_dataset', 'middle_dataset' and 'right_dataset' using the pd.read_csv() function and store them in variables.
- Use the pd.merge() function to merge the 'left_dataset' and 'middle_dataset' on the ID column. Store the resulting merged dataset in a new variable.
- Use the pd.merge() function to merge the resulting dataset from step 2 with the 'right_dataset' on the ID column. Store the final merged dataset in a new variable.
- Print the final merged dataset to see the result.

In this example, the three datasets left_dataset, middle_dataset and right_dataset are loaded into memory by using the pd.read_csv() function. Then, the pd.merge() function is used to merge the 'left_dataset' and 'middle_dataset' on the ID column and store the resulting merged dataset in a new variable merged_df1. The final step of the code merges merged_df1 with the right_dataset on ID column and store the final merged dataset in a new variable merged_df. The resulting merged dataset is printed to the console using the print() function.

You can also use other join types such as 'left', 'right' or 'outer' by adding the 'how' parameter on the pd.merge() function

```python
merged_df = pd.merge(merged_df1, right_dataset, on='ID', how = 'left')
```
This will do a left join on the merge function.

If time permits, experiment with different joins.

## 7. Handling missing data (if time permits): 

This final dataset has some missing values:

```csv
dataset.csv
ID,Name,Age,Address
1,John,25,NY
2,,30,Chicago
3,Mike,,LA
```

- Start by loading the dataset 'dataset' using the pd.read_csv() function and store it in a variable.
- Check for missing values in the dataset using the pd.isna() function.
- Use the pd.fillna() function to fill the missing values with a specific value or a value from a different column.
- Use the pd.dropna() function to drop the rows with missing values.
- Print the resulting dataset to see the result.

The dataset is loaded into memory by using the pd.read_csv() function and stored in the variable df. Then, the pd.isna() function is used to check for missing values in the dataset. The pd.fillna() function is then used to fill the missing values with a specific value (0 in this case) by setting the inplace parameter to True. To drop the rows with missing values, pd.dropna() is used with inplace = True . Finally, the resulting dataset is printed to the console using the print() function to see the result.

You can also use a value from another column to fill the missing values.

```python
df['Age'].fillna(df['Age'].mean(), inplace=True)
```

This would fill the missing values in the 'Age' column with the mean of the column.

It's worth mentioning that you should be careful while dropping rows with missing values, as it can have a huge impact on the final result, especially if the missing values are not missing at random.
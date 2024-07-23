import pandas as pd
data = pd.read_csv('D:\VS CODE\Mainflow\\01.Data Cleaning and Preprocessing.csv')

# Filter rows where a specific column value is greater than 15
filtered_data = data[data["ChipRate"] > 15]
print(filtered_data)

# Filter rows where two conditions are met (logical AND)
filtered_data2 = data[(data["BlowFlow"] > 10) & (data["UCZAA"] >= 0.89)]
print(filtered_data2)

# query method to filter data based on a string expression.
filtered_data3 = data.query('ChipRate > 13 and BlowFlow == 0')
print(filtered_data3)

# Check for missing values in a specific column
missing_values = data['BlowFlow'].isna().sum()
print("missing values =",missing_values)

# Check for any missing values in the entire DataFrame
missing_values2 = data.isna().sum().sum()
print("missing values 2 =",missing_values2)

# Drop rows with any missing values
data.dropna(inplace=True)

# Drop columns with more than 50% missing values (threshold can be adjusted)
data.dropna(thresh=0.5, axis=1, inplace=True)

# Fill missing values in a column with the mean value
data['ChipRate'].fillna(data['ChipRate'].mean(), inplace=True)

# Fill missing values with a specific value (e.g., 0)
data['BlowFlow'].fillna(0, inplace=True)

# Get descriptive statistics for numerical columns
summary = data.describe()

# Get mean, standard deviation etc. for a specific column
mean_value = data['BlowFlow'].mean()
std_dev = data['BlowFlow'].std()
print(mean_value)
print(std_dev)

# Calculate mean value grouped by a categorical column
grouped_data = data.groupby('Observation')['BlowFlow'].mean()
print(grouped_data)






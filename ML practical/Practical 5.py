import pandas as pd
import numpy as np

# Creating a sample DataFrame
data = {
    'Name': ['anuj','rohan','krish','rohit'],
    'Age': [25, np.nan, 30, 28],
    'Salary': [50000, 48000, np.nan, 52000]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Fill Age column with mean
df['Age'] = df['Age'].fillna(df['Age'].mean())
print("\nFilled with Mean:\n", df)

# Fill Salary column with median
df['Salary'] = df['Salary'].fillna(df['Salary'].median())

print("\nFilled with Median:\n", df)

df['Salary'] = df['Salary'].fillna(df['Salary'].mode())

print("\nFilled with Mode:\n", df)


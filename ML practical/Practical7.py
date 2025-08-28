import pandas as pd

# Sample Data
data = pd.DataFrame({
    'Employee': ['A', 'B', 'C', 'D'],
    'Department': ['HR', 'IT', 'Finance', 'HR']
})

print("Original DataFrame:\n", data)

# One-Hot Encoding using pandas
encoded_df = pd.get_dummies(data, columns=['Department'])

print("\nOne-Hot Encoded DataFrame (using pandas):\n", encoded_df)

# One-Hot Encoding using sklearn

from sklearn.preprocessing import OneHotEncoder

# Extract categorical column
dept = data[['Department']]

# Create OneHotEncoder
encoder = OneHotEncoder(sparse_output=False)  # sparse=False returns NumPy array

encoded = encoder.fit_transform(dept)

# Create DataFrame with column names
encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(['Department']))

# Combine with original data
final_df = pd.concat([data['Employee'], encoded_df], axis=1)

print("\nOne-Hot Encoded DataFrame (using sklearn):\n", final_df)

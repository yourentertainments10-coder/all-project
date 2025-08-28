# Import required libraries
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import csv
from io import StringIO  # Used to simulate a CSV file in memory

# 1️⃣ Load Iris dataset from sklearn
iris = load_iris()

# Convert to pandas DataFrame
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

print("Iris Dataset Loaded using sklearn:\n")
print(df.head())

# -----------------------------------------------
#  Simulate saving this DataFrame as a CSV in memory
csv_buffer = StringIO()
df.to_csv(csv_buffer, index=False)  # Write to in-memory buffer as CSV format
csv_buffer.seek(0)  # Move to the beginning of the buffer

# -----------------------------------------------
#  Load the CSV using csv.reader
print("Loaded using csv.reader:\n")
csv_buffer.seek(0)  # Reset buffer before reading
reader = csv.reader(csv_buffer)
for row in reader:
    print(row)

# -----------------------------------------------
#  Load CSV using NumPy
print("\n✅ Loaded using NumPy (as strings):\n")
csv_buffer.seek(0)  # Reset again before NumPy reads
np_data = np.genfromtxt(csv_buffer, delimiter=",", dtype=str, skip_header=1)
print(np_data)

# -----------------------------------------------
#  Load CSV using Pandas
print("\n✅ Loaded using Pandas:\n")
csv_buffer.seek(0)  # Reset again for pandas
df_loaded = pd.read_csv(csv_buffer)
print(df_loaded.head())

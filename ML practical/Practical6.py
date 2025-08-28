import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data with outliers
data = [10, 12, 14, 15, 13, 12, 300, 14, 13, 12, 15, 11, 12, 400]

df = pd.DataFrame(data, columns=["value"])

# Method 1: Using IQR (Interquartile Range)

Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers_iqr = df[(df['value'] < lower_bound) | (df['value'] > upper_bound)]

print("Outliers detected using IQR method:\n", outliers_iqr)


# Method 2: Z-Score Method 
# ----------------------------------
from scipy import stats

z_scores = np.abs(stats.zscore(df['value']))
df['z_score'] = z_scores

outliers_z = df[df['z_score'] > 3]  # z-score > 3 is considered outlier

print("\nOutliers detected using Z-score method:\n", outliers_z[['value']])

# ----------------------------------
# Method 3: Visualizing with Boxplot
# ----------------------------------

plt.figure(figsize=(8, 4))
sns.boxplot(x=df["value"])
plt.title("Box Plot to Visualize Outliers")
plt.show()

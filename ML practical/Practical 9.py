#Absolute Max Scaled
import numpy as np

value = 18
age = np.array([15, 18, 21, 30])
max_val = np.max(np.abs(age))
x_scaled = (value - max_val) / max_val

print("1. Absolute Max Scaled:", x_scaled)

#Min-Max Scaled:
value = 18
age = np.array([15, 18, 21, 30])
x_min = np.min(age)
x_max = np.max(age)
x_scaled = (value - x_min) / (x_max - x_min)

print("2. Min-Max Scaled:", x_scaled)

#Normalized 
features = np.array([18, 30])  # Example vector (can include more)
norm = np.sqrt(np.sum(features ** 2))
x_scaled = features / norm

print("3. Normalized :", x_scaled)


#Standardized (Z-score)
value = 18
age = np.array([15, 18, 21, 30])
mean = np.mean(age)
std = np.std(age)
x_scaled = (value - mean) / std

print("4. Standardized (Z-score):", x_scaled)

#Robust Scaled:
value = 18
age = np.array([15, 18, 21, 30])
median = np.median(age)
q1 = np.percentile(age, 25)
q3 = np.percentile(age, 75)
iqr = q3 - q1
x_scaled = (value - median) / iqr

print("5. Robust Scaled:", x_scaled)


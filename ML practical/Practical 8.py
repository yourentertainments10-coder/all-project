from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd

# 1. Load Iris dataset
iris = load_iris()

# Features (X) and Labels (y)
X = iris.data              # shape = (150, 4)
y = iris.target            # shape = (150,)

# 2. Split into training (80%) and testing (20%) data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42  # random_state ensures reproducibility
)

# 3. Print shapes to verify
print("Training data shape (X_train):", X_train.shape)
print("Testing data shape (X_test):", X_test.shape)
print("Training labels shape (y_train):", y_train.shape)
print("Testing labels shape (y_test):", y_test.shape)

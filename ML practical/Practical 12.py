import pandas as pd
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy as np

data = {
    'HoursStudied': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Pass': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]   # 0 = Fail, 1 = Pass
}
df = pd.DataFrame(data)
X = df[['HoursStudied']]   
y = df['Pass']             

# Step 2: Train Logistic Regression Model
model = LogisticRegression()
model.fit(X, y)

# Step 3: Predictions
print("Prediction for 3 hours studied:", model.predict(pd.DataFrame([[3]], columns=["HoursStudied"]))[0])
print("Prediction for 7 hours studied:", model.predict(pd.DataFrame([[7]], columns=["HoursStudied"]))[0])

plt.scatter(X, y, color='blue', label='Training Data')
X_test = np.linspace(0, 10, 100).reshape(-1, 1)
X_test_df = pd.DataFrame(X_test, columns=["HoursStudied"])
y_prob = model.predict_proba(X_test_df)[:, 1]   # probability of passing

plt.plot(X_test, y_prob, color='red', label='Logistic Curve')
plt.xlabel("Hours Studied")
plt.ylabel("Probability of Passing")
plt.legend()
plt.show()

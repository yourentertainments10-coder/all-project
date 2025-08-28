import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = {
    'YearsExperience': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Salary': [30000, 35000, 40000, 45000, 50000, 60000, 65000, 70000, 75000, 80000]
}
df = pd.DataFrame(data)

X = df[['YearsExperience']]   
y = df['Salary']              

# Step 2: Train Linear Regression Model
model = LinearRegression()
model.fit(X, y)

# Step 3: Check Results
print("Intercept (b):", model.intercept_)
print("Coefficient (m):", model.coef_)

predicted_salary = model.predict(pd.DataFrame([[6.5]], columns=["YearsExperience"]))
print("Predicted Salary for 6.5 years experience:", predicted_salary[0])

# Step 4: Visualization
plt.scatter(X, y, color='blue', label='Training Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend()
plt.show()

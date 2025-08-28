from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

iris = load_iris()
X = iris.data   # Features
y = iris.target # Labels

# 2. Split dataset into training and testing sets (70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 3. Create Naive Bayes model
model = GaussianNB()

# 4. Train the model
model.fit(X_train, y_train)

# 5. Predict test data
y_pred = model.predict(X_test)

# 6. Evaluate performance
print("Predicted Labels:", y_pred)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

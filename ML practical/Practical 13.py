import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)  # Features
y = pd.Series(iris.target)                               # Target (0,1,2)

print("Dataset shape:", X.shape)
print("Target classes:", iris.target_names)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print("Training set size:", X_train.shape)
print("Testing set size:", X_test.shape)

knn = KNeighborsClassifier(n_neighbors=3)  # K = 3
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

print("\nPredicted Labels:", y_pred)
print("Actual Labels:   ", list(y_test.values))


print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=iris.target_names))

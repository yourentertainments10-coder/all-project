import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle

# Load dataset
df = pd.read_csv('student_data.csv')

# Features and target
X = df[['age', 'study_time', 'failures', 'absences', 'G1', 'G2', 'G3']]
y = df['passed']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
y_pred = clf.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f'Accuracy: {acc:.2f}')
print(classification_report(y_test, y_pred))

# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(clf, f)

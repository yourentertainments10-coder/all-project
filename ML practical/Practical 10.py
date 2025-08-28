
import pandas as pd
from sklearn.feature_selection import SelectKBest, chi2, RFE
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("sample_dataset.csv")
print("Columns in dataset:", list(data.columns))

X = data.iloc[:, :-1]  
for col in X.columns:
	if X[col].dtype == 'object':
		le = LabelEncoder()
		X[col] = le.fit_transform(X[col])
y = data.iloc[:, -1]    

print("\nShape of X:", X.shape)
print("Shape of y:", y.shape)

# 1. Filter Method - Chi-Square
print("\n=== Filter Method (Chi-Square Test) ===")

chi2_selector = SelectKBest(score_func=chi2, k=2)  # Select top 2 features
X_chi2 = chi2_selector.fit_transform(X, y)
selected_features_chi2 = X.columns[chi2_selector.get_support()]
print("Selected Features by Chi-Square:", list(selected_features_chi2))

# 2. Wrapper Method - RFE
print("\n=== Wrapper Method (Recursive Feature Elimination - RFE) ===")

model = LogisticRegression(max_iter=1000)
rfe_selector = RFE(model, n_features_to_select=2)
X_rfe = rfe_selector.fit_transform(X, y)

selected_features_rfe = X.columns[rfe_selector.support_]
print("Selected Features by RFE:", list(selected_features_rfe))

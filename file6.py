import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


iris = load_iris()


X = iris.data
y = iris.target


df = pd.DataFrame(data=X, columns=iris.feature_names)


print(df.head())


print("Missing values:", df.isnull().sum())


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


print("Training set dimensions:", X_train.shape, y_train.shape)
print("Testing set dimensions:", X_test.shape, y_test.shape)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)


X_test_scaled = scaler.transform(X_test)


df_train_scaled = pd.DataFrame(data=X_train_scaled, columns=iris.feature_names)
print(df_train_scaled.head())

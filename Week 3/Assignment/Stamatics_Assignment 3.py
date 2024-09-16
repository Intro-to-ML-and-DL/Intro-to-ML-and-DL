# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.preprocessing import LabelEncoder as le
from sklearn.preprocessing import StandardScaler

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session
data = pd.read_csv('/kaggle/input/who-is-the-real-winner/train.csv')
testing_data=pd.read_csv('/kaggle/input/who-is-the-real-winner/test.csv')
submit=pd.read_csv('/kaggle/input/who-is-the-real-winner/sample_submission.csv')

columns=['Party','Criminal Case','state']
X=data[columns]
X_test=testing_data[columns]
X.head(10)

y=data['Education']
print(y.head())
label_encoder=le()
X_encoded = X.copy()
X_test_encoded = X_test.copy()
for col in X.columns:
    X_encoded[col] = label_encoder.fit_transform(X[col])
    X_test_encoded[col] = label_encoder.fit_transform(X_test[col])
y_encoded=label_encoder.fit_transform(y)
print(X_encoded.head())

scaler = StandardScaler()
X_encoded_scaled = X_encoded.copy()
X_test_encoded_scaled = X_test_encoded.copy()
X_encoded_scaled['Criminal Case'] = scaler.fit_transform(X_encoded[['Criminal Case']])
X_test_encoded_scaled['Criminal Case'] = scaler.transform(X_test_encoded[['Criminal Case']])
model=rfc(random_state=15)
model.fit(X_encoded_scaled,y_encoded)
y_pred=model.predict(X_test_encoded_scaled)
y_pred_original = label_encoder.inverse_transform(y_pred)
print(y_pred_original[0:20])
cols=['ID','Education']
submission=pd.DataFrame(columns=['ID','Education'])
submission['ID']=testing_data['ID']
submission['Education']=y_pred_original

file_path=r'/kaggle/working/submission.csv'
submission.to_csv(file_path, index=False)

################ Plots ###############
import matplotlib.pyplot as plt

# Plotting the distribution of target variable 'Education'
plt.figure(figsize=(10, 10))

plt.subplot(2, 2, 1)
data['Education'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Distribution of Education')
plt.xlabel('Education Level')
plt.ylabel('Count')
plt.xticks(rotation=45)

# Plotting feature importances
plt.subplot(2, 2, 2)

feature_importances = model.feature_importances_

# Get the names of the features
feature_names = X.columns

# Sort the feature importances and corresponding feature names
sorted_indices = feature_importances.argsort()[::-1]
sorted_feature_importances = feature_importances[sorted_indices]
sorted_feature_names = feature_names[sorted_indices]
plt.barh(range(len(sorted_feature_names)), sorted_feature_importances, align='center', color='lightgreen')
plt.yticks(range(len(sorted_feature_names)), sorted_feature_names)
plt.xlabel('Feature Importance')
plt.ylabel('Feature')
plt.title('Feature Importance Plot')
plt.gca().invert_yaxis()  # Invert y-axis to have the most important feature at the top

# Sorting candidates according to total assets
sorted_candidates = data.sort_values(by='Criminal Case', ascending=False)
top_500_candidates = sorted_candidates.head(500)

# Distribution of top 500 candidates among parties
plt.subplot(2, 2, 3)
party_distribution = top_500_candidates['Party'].value_counts()
top_10_parties_distribution = party_distribution.head(10)
plt.pie(top_10_parties_distribution, labels=top_10_parties_distribution.index, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Percentage Distribution of Top 500 Candidates Among Top 10 Parties')

# Convert asset values and plot distribution
plt.subplot(2, 2, 4)
def convert_to_numeric(asset_value):
    if 'Crore+' in asset_value:
        return float(asset_value.split()[0]) * 10000000
    elif 'Lac+' in asset_value:
        return float(asset_value.split()[0]) * 100000
    elif 'Thou+' in asset_value:
        return float(asset_value.split()[0]) * 1000
    else:
        return float(asset_value)

data['Total Assets Numeric'] = data['Total Assets'].apply(convert_to_numeric)
sorted_candidates_assets = data.sort_values(by='Total Assets Numeric', ascending=False)
top_1800_candidates = sorted_candidates_assets.head(1800)
party_distribution_assets = top_1800_candidates['Party'].value_counts()
top_10_parties_distribution_assets = party_distribution_assets.head(10)
percentage_distribution_assets = (top_10_parties_distribution_assets / top_1800_candidates.shape[0]) * 100

plt.bar(percentage_distribution_assets.index, percentage_distribution_assets.values, color='skyblue')
plt.xlabel('Party')
plt.ylabel('Percentage of Candidates')
plt.xticks(rotation=45)
plt.title('Percentage Distribution of Top 1800 Candidates Among Top 10 Parties (Based on Assets)')

plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()
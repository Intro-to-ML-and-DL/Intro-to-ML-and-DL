import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.utils import shuffle
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from collections import Counter


np.random.seed(42)


num_samples = 1000
num_features = 2
num_classes = 2
num_clusters = 1
imbalance_ratio = 0.05

X, y = make_classification(n_samples=num_samples, n_features=num_features,
                           n_informative=num_features, n_redundant=0,
                           n_classes=num_classes, n_clusters_per_class=num_clusters,
                           weights=[imbalance_ratio, 1 - imbalance_ratio])


class_counts = Counter(y)
print("Class Distribution (Before Resampling):", class_counts)


plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Imbalanced Classification Dataset')
plt.grid(True)
plt.colorbar()
plt.show()


oversampler = SMOTE(random_state=42)
X_oversampled, y_oversampled = oversampler.fit_resample(X, y)


oversampled_class_counts = Counter(y_oversampled)
print("Class Distribution (After Oversampling):", oversampled_class_counts)


plt.figure(figsize=(8, 6))
plt.scatter(X_oversampled[:, 0], X_oversampled[:, 1], c=y_oversampled, cmap='viridis')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Oversampled Classification Dataset')
plt.grid(True)
plt.colorbar()
plt.show()


undersampler = RandomUnderSampler(sampling_strategy=0.05, random_state=42)
X_undersampled, y_undersampled = undersampler.fit_resample(X, y)


undersampled_class_counts = Counter(y_undersampled)
print("Class Distribution (After Undersampling):", undersampled_class_counts)

plt.figure(figsize=(8, 6))
plt.scatter(X_undersampled[:, 0], X_undersampled[:, 1], c=y_undersampled, cmap='viridis')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Undersampled Classification Dataset')
plt.grid(True)
plt.colorbar()
plt.show()

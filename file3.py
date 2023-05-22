import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs


np.random.seed(42)


num_samples = 1000
num_features = 2
num_clusters = 4

X, y = make_blobs(n_samples=num_samples, n_features=num_features,
                  centers=num_clusters, random_state=42)


plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Clustering Dataset')
plt.grid(True)
plt.colorbar()
plt.show()

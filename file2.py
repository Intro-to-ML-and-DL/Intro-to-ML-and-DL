import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification


np.random.seed(42)


num_samples = 1000
num_features = 2
num_classes = 2
num_clusters = 2

X, y = make_classification(n_samples=num_samples, n_features=num_features,
                           n_informative=num_features, n_redundant=0,
                           n_classes=num_classes, n_clusters_per_class=num_clusters)


plt.figure(figsize=(8, 6))
for class_label in range(num_classes):
   
    class_samples = X[y == class_label]
    plt.scatter(class_samples[:, 0], class_samples[:, 1], label='Class {}'.format(class_label))

plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.title('Classification Dataset')
plt.grid(True)
plt.show()

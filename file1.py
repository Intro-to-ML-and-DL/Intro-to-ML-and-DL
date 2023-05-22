import numpy as np
import matplotlib.pyplot as plt


np.random.seed(42)


num_samples = 1000
num_features = 5


X = np.random.rand(num_samples, num_features)


true_coefficients = np.array([2, -1, 0.5, 3, -2]) 
noise = np.random.normal(0, 1, size=num_samples)  
y = np.dot(X, true_coefficients) + noise

fig, axes = plt.subplots(1, num_features, figsize=(15, 3), sharey=True)

for i in range(num_features):
    ax = axes[i]
    ax.scatter(X[:, i], y, s=10, label="Data")
    ax.set_xlabel(f"Feature {i+1}")
    ax.set_ylabel("Target")
    
   
    coefficients = np.polyfit(X[:, i], y, deg=1)
    best_fit_line = np.poly1d(coefficients)
    ax.plot(X[:, i], best_fit_line(X[:, i]), color='red', label="Best Fit Line")
    
    ax.legend()

plt.tight_layout()
plt.show()


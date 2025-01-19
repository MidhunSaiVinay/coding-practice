import numpy as np

#k-means clustering
def kmeans(data, k, max_iters=100):
    # Initialize k random centroids
    n_samples, n_features = data.shape
    centroids = data[np.random.choice(n_samples, k, replace=False)]
    
    for _ in range(max_iters):
        # Compute distances between points and centroids
        distances = np.sqrt(((data[:, np.newaxis] - centroids) ** 2).sum(axis=2))
        
        # Assign points to nearest centroid
        labels = np.argmin(distances, axis=1)
        
        # Update centroids
        new_centroids = np.array([data[labels == i].mean(axis=0) for i in range(k)])
        
        # Check for convergence
        if np.all(centroids == new_centroids):
            break
            
        centroids = new_centroids
    
    return labels, centroids

# Create sample data
np.random.seed(42)  # For reproducibility
data = np.random.randn(100, 2)  # 100 points in 2D

# Apply k-means clustering
k = 3  # Number of clusters
labels, centroids = kmeans(data, k,56)

# Print results
print("Cluster centers:")
print(centroids)
print("\nCluster assignments:")
print(labels)


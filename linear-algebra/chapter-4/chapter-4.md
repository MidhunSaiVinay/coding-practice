# Vector Applications

## Correlation and Cosine Similarity

- **Correlation Coefficient:**
    - Quantifies linear relationship between variables
    - Range: -1 to +1
    - -1: Perfect negative relationship
    - +1: Perfect positive relationship
    - 0: No linear relationship

- **Correlation Formula Components:**
    1. Mean center each variable (subtract average)
    2. Divide dot product by product of vector norms
    
    Pearson correlation coefficient (ρ):
    ```
    ρ = (x̄ᵀȳ) / (||x̄|| ||ȳ||)
    ```

- **Cosine Similarity:**
    - Similar to correlation but without mean centering
    - Formula: cos θx,y = α / (||x|| ||y||)
    - α is dot product between x and y

- **Key Differences:**
    - Correlation considers relative changes
    - Cosine similarity considers absolute values
    - Example: [0,1,2,3] and [100,101,102,103]
        - Correlation: 1.0
        - Cosine similarity: 0.808

## Time Series Filtering

- **Purpose:** Feature detection in signals
- **Components:**
    - Kernel: Template for pattern matching
    - Signal: Time series data
    
- **Process:**
    1. Compute dot product between kernel and signal segment
    2. Move kernel one step
    3. Repeat for entire signal length

- **Applications:**
    - Music processing
    - Radio communications
    - Telecommunications
    - Satellite signals
    
The dot product serves as fundamental operation in both correlation analysis and signal processing.

# k means clustering
## K-Means Clustering

- **Purpose:** Partition data into k distinct clusters based on feature similarity

- **Algorithm Steps:**
    1. **Initialization:**
        - Choose k initial centroids randomly from the dataset
    2. **Assignment:**
        - Assign each data point to the nearest centroid based on Euclidean distance
    3. **Update:**
        - Recalculate the centroids as the mean of all data points assigned to each centroid
    4. **Repeat:**
        - Repeat the assignment and update steps until centroids no longer change or a maximum number of iterations is reached

- **Example:**
    - Given data points: (1,1), (2,1), (4,3), (5,4)
        - Choose k = 2
        - Initial centroids: c₁=(1,1) and c₂=(5,4)
        - **Assignment step (using Euclidean distance):**
            - d((1,1), c₁) = √((1-1)² + (1-1)²) = 0
            - d((1,1), c₂) = √((1-5)² + (1-4)²) = 5
            - (1,1) → Cluster 1
            
            - d((2,1), c₁) = √((2-1)² + (1-1)²) = 1
            - d((2,1), c₂) = √((2-5)² + (1-4)²) = 4.24
            - (2,1) → Cluster 1
            
            - d((4,3), c₁) = √((4-1)² + (3-1)²) = 3.61
            - d((4,3), c₂) = √((4-5)² + (3-4)²) = 1.41
            - (4,3) → Cluster 2
            
            - d((5,4), c₁) = √((5-1)² + (4-1)²) = 5
            - d((5,4), c₂) = √((5-5)² + (4-4)²) = 0
            - (5,4) → Cluster 2
            
        - **Update step:**
            - Cluster 1 centroid: ((1+2)/2, (1+1)/2) = (1.5, 1)
            - Cluster 2 centroid: ((4+5)/2, (3+4)/2) = (4.5, 3.5)
        - Process continues until convergence


    - **Applications:**
    - Market segmentation
    - Image compression
    - Anomaly detection
    - Document clustering

K-means clustering is a simple yet powerful algorithm for grouping data points into meaningful clusters based on their features.
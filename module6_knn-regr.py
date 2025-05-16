import numpy as np

def read_training_data(N):
    X = []
    y = []
    print(f"Enter {N} (x, y) points:")
    for i in range(N):
        x_val = float(input(f"  Point {i+1} - x: "))
        y_val = float(input(f"  Point {i+1} - y: "))
        X.append(x_val)
        y.append(y_val)
    return np.array(X), np.array(y)

def knn_regression(X_train, y_train, x_query, k):
    distances = np.abs(X_train - x_query)  # L2 distance for 1D is abs difference
    nearest_indices = np.argsort(distances)[:k]
    return np.mean(y_train[nearest_indices])

def main():
    try:
        N = int(input("Enter the number of training points (N): "))
        if N <= 0:
            raise ValueError("N must be a positive integer.")

        k = int(input("Enter the number of neighbors (k): "))
        if k <= 0:
            raise ValueError("k must be a positive integer.")
        if k > N:
            print("Error: k must be less than or equal to N.")
            return

        X_train, y_train = read_training_data(N)
        x_query = float(input("Enter the query x value: "))
        y_pred = knn_regression(X_train, y_train, x_query, k)

        print(f"Predicted y value using {k}-NN Regression: {y_pred:.4f}")

    except ValueError as e:
        print(f"Input error: {e}")

if __name__ == "__main__":
    main()

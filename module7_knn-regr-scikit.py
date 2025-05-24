import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def read_training_data(N):
    X = np.empty(N, dtype=float)
    y = np.empty(N, dtype=float)
    print(f"Enter {N} (x, y) points:")
    for i in range(N):
        X[i] = float(input(f"  Point {i+1} - x: "))
        y[i] = float(input(f"  Point {i+1} - y: "))
    return X, y

def knn_regression_sklearn(X_train, y_train, x_query, k):
    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(X_train.reshape(-1, 1), y_train)
    return model.predict(np.array([[x_query]]))[0]

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

        # Print variance of training labels
        label_variance = np.var(y_train)
        print(f"Variance of training labels: {label_variance:.4f}")

        x_query = float(input("Enter the query x value: "))

        # Use scikit-learn for k-NN regression
        y_pred = knn_regression_sklearn(X_train, y_train, x_query, k)

        print(f"Predicted y value using {k}-NN Regression: {y_pred:.4f}")

    except ValueError as e:
        print(f"Input error: {e}")

if __name__ == "__main__":
    main()

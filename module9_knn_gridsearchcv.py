import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def read_dataset(num_points, name=""):
    X = np.empty((num_points, 1), dtype=float)
    y = np.empty(num_points, dtype=int)
    print(f"\nEnter {num_points} (x, y) pairs for the {name} set:")
    for i in range(num_points):
        while True:
            try:
                x = float(input(f"  Point {i+1} - x (real number): "))
                y_val = int(input(f"  Point {i+1} - y (non-negative integer): "))
                if y_val < 0:
                    raise ValueError("y must be a non-negative integer.")
                X[i] = x
                y[i] = y_val
                break
            except ValueError as e:
                print(f"Invalid input: {e}")
    return X, y

def main():
    try:
        N = int(input("Enter number of training samples (N): "))
        if N <= 0:
            raise ValueError("N must be a positive integer.")
        train_X, train_y = read_dataset(N, "Training")

        M = int(input("\nEnter number of test samples (M): "))
        if M <= 0:
            raise ValueError("M must be a positive integer.")
        test_X, test_y = read_dataset(M, "Test")

        best_k = 1
        best_accuracy = 0.0

        print("\nEvaluating accuracy for k from 1 to 10:")
        for k in range(1, 11):
            clf = KNeighborsClassifier(n_neighbors=k)
            clf.fit(train_X, train_y)
            predictions = clf.predict(test_X)
            acc = accuracy_score(test_y, predictions)
            print(f"  k = {k}, accuracy = {acc:.4f}")
            if acc > best_accuracy:
                best_accuracy = acc
                best_k = k

        print(f"\nBest k: {best_k}")
        print(f"Test accuracy with best k: {best_accuracy:.4f}")

    except ValueError as e:
        print(f"Input error: {e}")

if __name__ == "__main__":
    main()

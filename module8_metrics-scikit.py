import numpy as np
from sklearn.metrics import precision_score, recall_score

def read_binary_classification_data(N):
    true_labels = np.empty(N, dtype=int)
    predicted_labels = np.empty(N, dtype=int)
    print(f"Enter {N} (x, y) classification points (x = true label, y = predicted label):")
    for i in range(N):
        while True:
            try:
                x = int(input(f"  Point {i+1} - x (true label, 0 or 1): "))
                y = int(input(f"  Point {i+1} - y (predicted label, 0 or 1): "))
                if x not in (0, 1) or y not in (0, 1):
                    raise ValueError("Only 0 or 1 allowed.")
                true_labels[i] = x
                predicted_labels[i] = y
                break
            except ValueError as e:
                print(f"Invalid input: {e}")
    return true_labels, predicted_labels

def main():
    try:
        N = int(input("Enter the number of classification points (N): "))
        if N <= 0:
            raise ValueError("N must be a positive integer.")

        y_true, y_pred = read_binary_classification_data(N)

        precision = precision_score(y_true, y_pred, zero_division=0)
        recall = recall_score(y_true, y_pred, zero_division=0)

        print(f"\nPrecision: {precision:.4f}")
        print(f"Recall:    {recall:.4f}")

    except ValueError as e:
        print(f"Input error: {e}")

if __name__ == "__main__":
    main()

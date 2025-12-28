import argparse
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report


def main():
    parser = argparse.ArgumentParser(description="KNN Classification on Iris dataset")
    parser.add_argument("--k", type=int, default=5, help="Number of neighbors (K)")
    parser.add_argument(
        "--weights", type=str, default="uniform", choices=["uniform", "distance"],
        help="Weight function used in prediction"
    )
    parser.add_argument(
        "--metric", type=str, default="minkowski",
        help="Distance metric (default minkowski)"
    )
    parser.add_argument("--p", type=int, default=2, help="Power parameter for Minkowski metric (p=2 → Euclidean)")
    parser.add_argument("--test-size", type=float, default=0.2, help="Test set size fraction")
    args = parser.parse_args()

    data = load_iris()
    X, y = data.data, data.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=args.test_size, random_state=42, stratify=y
    )

    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("knn", KNeighborsClassifier(n_neighbors=args.k, weights=args.weights, metric=args.metric, p=args.p)),
    ])

    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {acc:.4f}")
    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred, target_names=data.target_names))


if __name__ == "__main__":
    main()



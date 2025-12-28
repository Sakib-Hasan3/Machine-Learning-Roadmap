import argparse
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import math


def main():
    parser = argparse.ArgumentParser(description="KNN Regression on Diabetes dataset")
    parser.add_argument("--k", type=int, default=7, help="Number of neighbors (K)")
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

    data = load_diabetes()
    X, y = data.data, data.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=args.test_size, random_state=42
    )

    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("knn", KNeighborsRegressor(n_neighbors=args.k, weights=args.weights, metric=args.metric, p=args.p)),
    ])

    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    rmse = math.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    print(f"MAE: {mae:.4f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"R^2: {r2:.4f}")


if __name__ == "__main__":
    main()

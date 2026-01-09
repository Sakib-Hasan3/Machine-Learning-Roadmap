from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score, classification_report


def main() -> None:
    # 1) Create synthetic classification data
    X, y = make_classification(
        n_samples=1000,
        n_features=10,
        n_informative=5,
        n_redundant=0,
        random_state=42,
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    # 2) Weak learner = Decision Stump
    stump = DecisionTreeClassifier(max_depth=1, random_state=42)

    # 3) AdaBoost classifier
    clf = AdaBoostClassifier(
        estimator=stump,  # sklearn >= 1.2
        n_estimators=50,
        learning_rate=1.0,
        random_state=42,
    )

    # 4) Train
    clf.fit(X_train, y_train)

    # 5) Evaluate
    y_pred = clf.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {acc:.4f}")
    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred, digits=4))

    if hasattr(clf, "feature_importances_"):
        print("\nFeature importances:")
        print(clf.feature_importances_)


if __name__ == "__main__":
    main()

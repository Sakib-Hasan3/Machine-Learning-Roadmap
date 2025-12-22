import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.svm import SVC


def make_separable_data(n_samples=200, random_state=42, std=0.6):
    X, y = make_blobs(
        n_samples=n_samples,
        centers=[(-2, -2), (2, 2)],
        cluster_std=std,
        random_state=random_state,
    )
    # Convert labels from {0,1} to {-1, +1}
    y = np.where(y == 0, -1, 1)
    return X, y


def plot_svm(ax, X, y, model, title="SVM"):
    ax.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm, s=30, edgecolors="k")

    # Support vectors
    ax.scatter(
        model.support_vectors_[:, 0],
        model.support_vectors_[:, 1],
        s=120,
        facecolors="none",
        edgecolors="k",
        linewidths=1.5,
        label="support vectors",
    )

    # Decision function grid
    xlim = (X[:, 0].min() - 1, X[:, 0].max() + 1)
    ylim = (X[:, 1].min() - 1, X[:, 1].max() + 1)
    xx = np.linspace(*xlim, 200)
    yy = np.linspace(*ylim, 200)
    YY, XX = np.meshgrid(yy, xx)
    grid = np.c_[XX.ravel(), YY.ravel()]
    Z = model.decision_function(grid).reshape(XX.shape)

    # Plot decision boundary and margins
    cs = ax.contour(
        XX,
        YY,
        Z,
        levels=[-1, 0, 1],
        linestyles=["--", "-", "--"],
        colors=["tab:orange", "k", "tab:orange"],
        linewidths=1.2,
    )
    ax.clabel(cs, inline=True, fontsize=8)

    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_title(title)
    ax.set_xlabel("x1")
    ax.set_ylabel("x2")


def main():
    X, y = make_separable_data()

    # Hard margin approximation: very large C
    svc_hard = SVC(kernel="linear", C=1_000_000)
    svc_hard.fit(X, y)

    # Soft margin: moderate C
    svc_soft = SVC(kernel="linear", C=1.0)
    svc_soft.fit(X, y)

    fig, axes = plt.subplots(1, 2, figsize=(10, 4), constrained_layout=True)
    plot_svm(axes[0], X, y, svc_hard, title="Hard-ish Margin (C=1e6)")
    plot_svm(axes[1], X, y, svc_soft, title="Soft Margin (C=1)")

    # Overall title and save
    fig.suptitle("Linear SVM: Hard vs Soft Margin", fontsize=12)
    out = "hard_margin_vs_soft.png"
    plt.savefig(out, dpi=150)
    print(f"Saved plot to {out}")


if __name__ == "__main__":
    main()

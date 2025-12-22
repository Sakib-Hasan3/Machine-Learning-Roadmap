import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.svm import SVC

X, y = make_blobs(n_samples=120, centers=[(-2, -2), (2, 2)], cluster_std=1.5, random_state=7)


def plot_svm(C_value, ax):
    clf = SVC(kernel='linear', C=C_value)
    clf.fit(X, y)

    w = clf.coef_[0]
    b = clf.intercept_[0]

    x0_min, x0_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    xx = np.linspace(x0_min, x0_max, 200)
    yy = -(w[0]/w[1]) * xx - b/w[1]
    yy_plus = -(w[0]/w[1]) * xx - (b + 1)/w[1]
    yy_minus = -(w[0]/w[1]) * xx - (b - 1)/w[1]

    ax.scatter(X[y == 0, 0], X[y == 0, 1], c='steelblue', edgecolor='k', label='ক্লাস 0')
    ax.scatter(X[y == 1, 0], X[y == 1, 1], c='tomato', edgecolor='k', label='ক্লাস 1')
    ax.plot(xx, yy, 'k-', lw=2, label='সিদ্ধান্ত সীমারেখা')
    ax.plot(xx, yy_plus, 'k--', lw=1, label='মার্জিন +1')
    ax.plot(xx, yy_minus, 'k--', lw=1, label='মার্জিন -1')

    sv = clf.support_vectors_
    ax.scatter(sv[:, 0], sv[:, 1], s=120, facecolors='none', edgecolors='k', label='Support Vectors')
    ax.set_title(f'Linear SVM (C={C_value})')
    ax.legend(loc='upper left')


if __name__ == "__main__":
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    plot_svm(C_value=0.1, ax=axes[0])
    plot_svm(C_value=10.0, ax=axes[1])
    plt.tight_layout()
    plt.show()

---

## ✅ Cell 1 — Imports

```python
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

np.set_printoptions(precision=4, suppress=True)
print("✅ Imports done: numpy, pandas, sklearn KMeans, matplotlib")
```

**Output**

* ✅ Imports done: numpy, pandas, sklearn KMeans, matplotlib

---

## ✅ Cell 2 — Small Dataset (12 points, 2D)

```python
df = pd.DataFrame({
    "x": [1.0, 1.2, 0.8, 1.4,   5.0, 5.2, 4.8, 5.4,   9.0, 9.2, 8.8, 9.4],
    "y": [1.0, 0.9, 1.1, 1.2,   5.0, 4.9, 5.1, 5.2,   9.0, 8.9, 9.1, 9.2],
}, index=[f"P{i}" for i in range(1, 13)])

print("✅ Dataset (12 points, 2 features):")
display(df)
```

**Output**

* 12টা point-এর (x,y) টেবিল দেখাবে (P1…P12)

---

## ✅ Cell 3 — KMeans run (K=3)

```python
X = df.values
k = 3

km3 = KMeans(n_clusters=k, init="k-means++", n_init=10, random_state=42)
labels3 = km3.fit_predict(X)

print("✅ KMeans fitted (K=3)")
print("Centroids (x,y):\n", np.round(km3.cluster_centers_, 4))
print("Inertia (WCSS):", round(float(km3.inertia_), 6))
print("Iterations:", km3.n_iter_)

df_k3 = df.copy()
df_k3["cluster"] = labels3
print("\nCluster assignment table:")
display(df_k3)
```

**Output (আপনার রান অনুযায়ী)**

* ✅ KMeans fitted (K=3)
* Centroids (x,y):
  `[[5.1  5.05], [9.1  9.05], [1.1  1.05]]`
* Inertia (WCSS): `0.75`
* Iterations: `2`
* Cluster assignment টেবিল (প্রতিটা point কোন cluster-এ গেছে)

---

## ✅ Cell 4 — Distance to each centroid (Nearest-centroid rule)

```python
centroids = km3.cluster_centers_
dists = np.linalg.norm(X[:, None, :] - centroids[None, :, :], axis=2)

dist_cols = [f"dist_to_C{i}" for i in range(k)]
dist_df = pd.DataFrame(dists, index=df.index, columns=dist_cols)

print("✅ Distances to each centroid (K=3):")
display(dist_df.round(3))

print("\nNearest centroid for each point:")
print(dist_df.idxmin(axis=1).to_string())
```

**Output (key)**

* Distances টেবিল দেখাবে
* Nearest centroid list (example):

  * P1–P4 → `dist_to_C2`
  * P5–P8 → `dist_to_C0`
  * P9–P12 → `dist_to_C1`

---

## ✅ Cell 5 — Elbow Table (K বাড়ালে inertia কমে)

```python
inertias = []
Ks = list(range(1, 8))
for kk in Ks:
    km = KMeans(n_clusters=kk, init="k-means++", n_init=10, random_state=42)
    km.fit(X)
    inertias.append(float(km.inertia_))

elbow_table = pd.DataFrame({"K": Ks, "Inertia(WCSS)": inertias})
print("✅ Elbow table (K vs Inertia):")
display(elbow_table)
```

**Output**

* K=1..7 এর জন্য inertia টেবিল (K বাড়লে inertia **always** কমবে)

---

## ✅ Cell 6 — Elbow Plot

```python
plt.figure()
plt.plot(Ks, inertias, marker='o')
plt.xlabel("K (number of clusters)")
plt.ylabel("Inertia (WCSS)")
plt.title("Elbow Method: Inertia vs K")
plt.show()
```

**Output**

* Elbow graph (Inertia vs K)

---


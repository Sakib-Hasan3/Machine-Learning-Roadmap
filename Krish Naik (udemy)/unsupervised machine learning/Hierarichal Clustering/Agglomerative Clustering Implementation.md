---

## ✅ Cell 1 — Imports (লাইব্রেরি আনা)

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import AgglomerativeClustering

np.set_printoptions(precision=4, suppress=True)
print("✅ Imports done: numpy, pandas, matplotlib, sklearn AgglomerativeClustering")
```

### এই cell কী করছে?

* `numpy` → সংখ্যার কাজ (array, distance, matrix)
* `pandas` → টেবিল/ডেটাফ্রেম বানানো
* `matplotlib.pyplot` → গ্রাফ/প্লট আঁকা
* `AgglomerativeClustering` → hierarchical clustering algorithm (bottom-up)

### `np.set_printoptions(...)` কেন?

* array প্রিন্ট করলে যেন:

  * দশমিক 4 ঘর পর্যন্ত দেখায় (`precision=4`)
  * বৈজ্ঞানিক notation (1e-05) না দেখিয়ে normal number দেখায় (`suppress=True`)

---

## ✅ Cell 2 — Dataset তৈরি (১২টা পয়েন্ট, ২টা feature)

```python
df = pd.DataFrame({
    "x": [1.0, 1.2, 0.8, 1.4,   5.0, 5.2, 4.8, 5.4,   9.0, 9.2, 8.8, 9.4],
    "y": [1.0, 0.9, 1.1, 1.2,   5.0, 4.9, 5.1, 5.2,   9.0, 8.9, 9.1, 9.2],
}, index=[f"P{i}" for i in range(1, 13)])

print("✅ Dataset (12 points, 2 features):")
display(df)
```

### এই cell কী করছে?

* 2D dataset বানাচ্ছে (x,y)
* intentionally ৩টা group রাখা হয়েছে:

  * (1,1) এর পাশে 4টা point
  * (5,5) এর পাশে 4টা point
  * (9,9) এর পাশে 4টা point
* index নাম দিয়েছে `P1...P12` যাতে dendrogram/plot এ পয়েন্ট চিনতে সহজ হয়

---

## ✅ Cell 3 — Raw points plot (ডেটা আগে দেখে নেওয়া)

```python
plt.figure()
plt.scatter(df["x"], df["y"])
for name, row in df.iterrows():
    plt.text(row["x"] + 0.03, row["y"] + 0.03, name, fontsize=8)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Raw data points")
plt.show()
```

### এই cell কী করছে?

* `scatter` দিয়ে 2D পয়েন্টগুলো প্লট করছে
* `for name, row in df.iterrows()` → প্রতিটা point ঘুরে দেখে
* `plt.text(...)` → point-এর পাশে label লিখে দেয় (P1, P2…)
* এটা করলে আপনি visually বুঝতে পারবেন **কতগুলো natural cluster আছে**

---

## ✅ Cell 4 — Agglomerative Clustering (K=3, Ward linkage)

```python
X = df.values
k = 3

agg = AgglomerativeClustering(n_clusters=k, linkage="ward")
labels = agg.fit_predict(X)

print("✅ AgglomerativeClustering fitted (Ward linkage)")
print("Labels (cluster id for each point):")
labels_series = pd.Series(labels, index=df.index, name="cluster")
print(labels_series.to_string())

df_out = df.copy()
df_out["cluster"] = labels
print("\n✅ Dataset with assigned clusters:")
display(df_out)
```

### এই cell কী করছে?

1. `X = df.values`

   * DataFrame → numpy array বানাচ্ছে (sklearn এ input হিসেবে লাগে)

2. `k = 3`

   * আমরা চাই ৩টা cluster

3. `AgglomerativeClustering(n_clusters=k, linkage="ward")`

   * **Ward linkage** মানে:

     * এমন merge করবে যাতে cluster-এর ভেতরের variance (spread) কম থাকে
     * সাধারণত compact, ভালো cluster দেয়

4. `fit_predict(X)`

   * model fit করে + প্রতিটা point-এর cluster label দেয়

5. `df_out["cluster"]=labels`

   * output টেবিলে cluster column যোগ করে

📌 Output-এ দেখা যায়:

* P1–P4 এক cluster
* P5–P8 এক cluster
* P9–P12 এক cluster

---

## ✅ Cell 5 — Cluster plot (ফলাফল দেখতে)

```python
plt.figure()
plt.scatter(df_out["x"], df_out["y"], c=df_out["cluster"])
for name, row in df_out.iterrows():
    plt.text(row["x"] + 0.03, row["y"] + 0.03, name, fontsize=8)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Agglomerative Clustering result (K=3, Ward)")
plt.show()
```

### এই cell কী করছে?

* আগের plot-এর মতো, কিন্তু এবার:

  * `c=df_out["cluster"]` → cluster অনুযায়ী রঙ আলাদা
* ফলে আপনি visually confirm করতে পারবেন clustering ঠিক হয়েছে কিনা

---

## ✅ Cell 6 — Dendrogram (Hierarchy দেখা)

```python
from scipy.cluster.hierarchy import linkage, dendrogram

Z = linkage(X, method="ward")

print("✅ Linkage matrix shape:", Z.shape)
print("First 5 merge steps (rows: [cluster1, cluster2, distance, sample_count]):")
print(np.round(Z[:5], 4))

plt.figure()
dendrogram(Z, labels=df.index.tolist())
plt.title("Dendrogram (Ward linkage)")
plt.xlabel("Points")
plt.ylabel("Merge distance")
plt.show()
```

### এই cell কেন দরকার?

`sklearn` এর AgglomerativeClustering dendrogram বানিয়ে দেয় না, তাই আমরা `scipy` ব্যবহার করি।

### এই cell কী করছে?

1. `linkage(X, method="ward")`

   * Hierarchical merging steps হিসাব করে
   * Output: `Z` নামের linkage matrix

2. `Z` এর প্রতিটা row মানে:

   * কোন দুই cluster merge হলো
   * merge distance কত
   * নতুন cluster-এ কয়টা sample হলো

3. `dendrogram(Z, labels=...)`

   * tree diagram আঁকে
   * এখান থেকে আপনি **K না দিয়েও** cut করে K বের করতে পারেন

---

## ✅ Cell 7 — distance_threshold দিয়ে cluster (K না ধরে)

```python
agg_thr = AgglomerativeClustering(n_clusters=None, distance_threshold=3.0, linkage="ward")
labels_thr = agg_thr.fit_predict(X)

print("✅ AgglomerativeClustering with distance_threshold=3.0 (Ward)")
print("Number of clusters found:", len(np.unique(labels_thr)))

df_thr = df.copy()
df_thr["cluster"] = labels_thr
display(df_thr)
```

### এই cell কী করছে?

এখানে আমরা বলছি:

* “K আমি দেব না”
* “তুমি dendrogram-এর distance অনুযায়ী cut করো”

1. `n_clusters=None`

   * K নির্দিষ্ট করা হয়নি

2. `distance_threshold=3.0`

   * merge distance 3.0 এর বেশি হলে merge করবে না
   * মানে: ঐ distance-এ dendrogram cut

3. `len(np.unique(labels_thr))`

   * কয়টা cluster হলো সেটা গণনা

---

# ✅ এক লাইনে পুরো workflow

**Data → (optional plot) → Agglomerative fit → labels → visualize → dendrogram → threshold-based clustering**

---


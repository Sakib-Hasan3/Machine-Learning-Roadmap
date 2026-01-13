নিচে **PCA implementation (Python)** দিলাম **cell-by-cell**—এবং প্রতিটা cell-এর **output**-ও দেখানো হয়েছে (উপরে টেবিল/প্রিন্ট আকারে দেখা যাচ্ছে)।
আমি এখানে **২ভাবে PCA করেছি**:

1. **Manual PCA (Covariance → Eigen Decomposition)**
2. **sklearn PCA**

---

## ✅ Cell 1 — Libraries import

```python
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

np.set_printoptions(precision=4, suppress=True)
print("✅ Libraries imported. numpy, pandas, sklearn(StandardScaler, PCA)")
```

**Output**

* ✅ Libraries imported. numpy, pandas, sklearn(StandardScaler, PCA)

---

## ✅ Cell 2 — Example dataset (Students × Subjects)

```python
df = pd.DataFrame({
    "Math":      [85, 78, 92, 60, 73, 88, 66, 95],
    "Physics":   [88, 80, 94, 62, 75, 90, 68, 96],
    "Chemistry": [90, 82, 96, 65, 77, 91, 70, 97],
    "English":   [60, 55, 62, 85, 72, 58, 80, 61],
    "Biology":   [65, 58, 67, 88, 74, 60, 83, 66],
}, index=[f"Student_{c}" for c in list("ABCDEFGH")])

print("✅ Example dataset (first rows):")
display(df.head())
```

**Output**

* Dataset table (head) দেখায়

---

## ✅ Cell 2b — Full dataset দেখানো

```python
print("Full dataset:")
display(df)
```

**Output**

* Full dataset table দেখায়

---

## ✅ Cell 3 — Standardize (mean=0, std=1)

```python
scaler = StandardScaler()
X = df.values
X_std = scaler.fit_transform(X)

df_std = pd.DataFrame(X_std, columns=df.columns, index=df.index)

print("✅ Standardized data (mean≈0, std≈1):")
display(df_std.round(3))

print("\nColumn means (should be ~0):")
print(df_std.mean().round(6).to_string())

print("\nColumn std devs (should be ~1):")
print(df_std.std(ddof=0).round(6).to_string())
```

**Output (key)**

* Column means ≈ 0
* Column std devs ≈ 1
* Standardized table দেখায়

---

## ✅ Cell 4 — Covariance matrix (standardized data)

```python
cov = np.cov(X_std, rowvar=False)
cov_df = pd.DataFrame(cov, index=df.columns, columns=df.columns)

print("✅ Covariance matrix (on standardized data):")
display(cov_df.round(3))
```

**Output**

* Covariance matrix table দেখায়

---

## ✅ Cell 5 — Eigen Decomposition (Eigenvalues + Eigenvectors/Loadings)

```python
eigvals, eigvecs = np.linalg.eigh(cov)

idx = np.argsort(eigvals)[::-1]
eigvals_sorted = eigvals[idx]
eigvecs_sorted = eigvecs[:, idx]

print("✅ Eigenvalues (sorted, largest→smallest):")
print(np.round(eigvals_sorted, 6))

explained_ratio = eigvals_sorted / eigvals_sorted.sum()
print("\n✅ Explained variance ratio (%):")
print(np.round(explained_ratio * 100, 3))

loadings = pd.DataFrame(eigvecs_sorted, index=df.columns,
                        columns=[f"PC{i+1}" for i in range(eigvecs_sorted.shape[1])])

print("\n✅ Eigenvectors / Loadings (each PC column):")
display(loadings.round(3))
```

**Output (key)**

* Eigenvalues: **[5.2139, 0.4934, 0.0054, 0.0014, 0.0002]**
* Explained variance (%): **[91.243, 8.634, 0.095, 0.025, 0.003]**
* Loadings table দেখায়

---

## ✅ Cell 6 — Manual PCA Projection (k=2)

```python
k = 2
W = eigvecs_sorted[:, :k]
Z_manual = X_std @ W

Z_df = pd.DataFrame(Z_manual, index=df.index, columns=[f"PC{i+1}" for i in range(k)])

print(f"✅ Projected data into {k} dimensions (manual PCA via eigenvectors):")
display(Z_df.round(3))

print("\nVariance captured by these PCs (%):", round(explained_ratio[:k].sum()*100, 3))
```

**Output (key)**

* PC1/PC2 scores table দেখায়
* Variance captured ≈ **99.877%**

---

## ✅ Cell 7 — sklearn PCA (compare)

```python
pca = PCA(n_components=k)
Z_sklearn = pca.fit_transform(X_std)

print("✅ sklearn PCA explained variance ratio (%):")
print(np.round(pca.explained_variance_ratio_ * 100, 3))

print("\n✅ sklearn PCA components_ (loadings; rows=PCs, cols=features):")
components_df = pd.DataFrame(pca.components_, columns=df.columns,
                             index=[f"PC{i+1}" for i in range(k)])
display(components_df.round(3))

Z_sklearn_df = pd.DataFrame(Z_sklearn, index=df.index, columns=[f"PC{i+1}" for i in range(k)])
print("\n✅ sklearn PCA projected scores:")
display(Z_sklearn_df.round(3))
```

**Output (key)**

* Explained variance (%): **[91.243, 8.634]**
* Components/loadings + projected scores table দেখায়

> (PC-এর sign উল্টা হতে পারে—এটা normal)

---

## ✅ Cell 8 — Reconstruction + Error (k=2)

```python
X_std_recon = Z_manual @ W.T
recon_df = pd.DataFrame(X_std_recon, columns=df.columns, index=df.index)

print(f"✅ Reconstructed standardized data using {k} PCs (approx):")
display(recon_df.round(3))

mse = np.mean((X_std - X_std_recon) ** 2)
print("\n✅ Reconstruction MSE (lower is better):", round(float(mse), 6))
```

**Output (key)**

* Reconstructed standardized table দেখায়
* Reconstruction MSE ≈ **0.001226**

---

## ✅ Cell 9 — PC interpretation (Top contributing features)

```python
abs_loadings_pc1 = loadings["PC1"].abs().sort_values(ascending=False)
abs_loadings_pc2 = loadings["PC2"].abs().sort_values(ascending=False)

print("✅ Top feature contributions for PC1 (by |loading|):")
print(abs_loadings_pc1.head(5).round(3).to_string())

print("\n✅ Top feature contributions for PC2 (by |loading|):")
print(abs_loadings_pc2.head(5).round(3).to_string())
```

**Output (key)**

* PC1 top |loadings|: Physics 0.456, Chemistry 0.455, Math 0.454, English 0.442, Biology 0.428
* PC2 top |loadings|: Biology 0.611, English 0.501, Math 0.364, Chemistry 0.352, Physics 0.345

---



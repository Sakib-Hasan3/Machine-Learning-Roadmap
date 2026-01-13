![Image](https://miro.medium.com/1%2AqG4PEnoSWQRLoEL_P1ruhw.jpeg)

![Image](https://www.visiondummy.com/wp-content/uploads/2014/04/eigenvectors_covariance.png)

![Image](https://georgemdallas.wordpress.com/wp-content/uploads/2013/10/pca13.jpg)

![Image](https://miro.medium.com/v2/resize%3Afit%3A1400/0%2AfSfgExsETK72Si3-)

## 🔷 **Eigen Decomposition on Covariance Matrix** — সহজ কিন্তু গভীর ব্যাখ্যা (PCA-এর হৃদয়)

এটা বুঝলে PCA পুরো পরিষ্কার হয়ে যায়। নিচে **কি → কেন → কিভাবে → উদাহরণ**—সব ধাপে ধাপে।

---

## 🧠 এক লাইনের সারকথা

> **Covariance matrix বলে দেয় ডেটা কোন দিকগুলোতে একসাথে ছড়ায়;
> Eigen decomposition সেই দিকগুলো (eigenvectors) ও তাদের শক্তি (eigenvalues) বের করে।**

---

# 1️⃣ Covariance Matrix কেন দরকার?

ধরা যাক আপনার ডেটা (X) (mean-centered করা হয়েছে)।

Covariance matrix:
[
\Sigma = \frac{1}{n-1} X^T X
]

এটা বলে:

* কোন feature জোড়া **একসাথে বাড়ে/কমে** (covariance)
* কোন দিক বরাবর **variance বেশি**

📌 PCA-র প্রশ্ন:

> “ডেটা কোন **direction**-এ সবচেয়ে বেশি ছড়ানো?”

---

# 2️⃣ Eigen Decomposition কী?

Covariance matrix (\Sigma) কে ভাঙা হয়:

[
\Sigma = Q \Lambda Q^T
]

যেখানে—

* **(Q)** = eigenvectors (columns) → **দিক (axes)**
* **(\Lambda)** = diagonal eigenvalues → **ঐ দিকের variance**

👉 এই ভাঙাটাই **Eigen Decomposition**।

---

# 3️⃣ Eigenvector & Eigenvalue-এর অর্থ (Intuition)

### 🔹 Eigenvector (দিক)

* নতুন axis (PC direction)
* যেদিকে ডেটা সবচেয়ে সুন্দরভাবে line up করে

### 🔹 Eigenvalue (শক্তি)

* ঐ axis বরাবর ডেটা **কতটা ছড়ানো (variance)**

📌 Largest eigenvalue ↔ **PC1**
📌 2nd largest ↔ **PC2** (PC1-এর সাথে 90°)

---

# 4️⃣ কেন Covariance matrix-এই decomposition?

কারণ PCA solve করে:
[
\max_{|w|=1} ; w^T \Sigma w
]

এই optimization-এর solution হলো:
[
\Sigma w = \lambda w
]

👉 এটিই **Eigenvalue Equation**
👉 তাই covariance matrix-এর eigenvectors-ই PCA-এর principal directions।

---

# 5️⃣ ছোট 2D Numeric Example (হাতে-কলমে intuition)

ধরা যাক mean-centered ডেটা থেকে covariance matrix:

[
\Sigma =
\begin{bmatrix}
4 & 3 \
3 & 4
\end{bmatrix}
]

### Eigenvalues:

[
\lambda_1 = 7,\quad \lambda_2 = 1
]

### Eigenvectors (normalized):

* (w_1 = \frac{1}{\sqrt{2}}(1,1))
* (w_2 = \frac{1}{\sqrt{2}}(1,-1))

🧠 ব্যাখ্যা:

* (w_1) দিক বরাবর variance = **7** (সবচেয়ে বেশি) → **PC1**
* (w_2) দিক বরাবর variance = **1** → **PC2**

👉 ডেটা diagonal ((1,1)) দিকেই সবচেয়ে বেশি ছড়ানো।

---

# 6️⃣ PCA-তে কীভাবে ব্যবহার হয়? (Step-by-step)

1. **Standardize** ডেটা
2. **Covariance matrix** বানাও
3. **Eigen decomposition** করো
4. **Eigenvalues** বড় থেকে ছোট সাজাও
5. Corresponding **Eigenvectors** নাও
6. Top-(k) eigenvectors দিয়ে data **project** করো

Projection:
[
Z = X W_k
]

* (W_k) = top-(k) eigenvectors

---

# 7️⃣ Orthogonality কেন আসে?

Covariance matrix symmetric ⇒

* Eigenvectors **orthogonal** (90°)

📌 মানে:

* PCs একে অপরের তথ্য পুনরাবৃত্তি করে না
* প্রত্যেকটা PC নতুন variance যোগ করে

---

# 8️⃣ Variance Explained (কেন eigenvalues দরকার)

Total variance:
[
\sum_i \lambda_i
]

Explained variance ratio:
[
\frac{\lambda_k}{\sum_i \lambda_i}
]

👉 Top PCs রাখি যতক্ষণ না 90–95% variance ধরা পড়ে।

---

# 9️⃣ Geometry-র সাথে মিল

* **Eigenvectors** = নতুন ঘোরানো axes
* **Eigenvalues** = axes-এর লম্বা/ছোট হওয়া
* PCA = axes এমনভাবে ঘোরানো যাতে লম্বা দিকগুলো আগে ধরা পড়ে

---

## 🔑 Golden Answer (Exam/Viva)

> **Eigen decomposition of the covariance matrix yields eigenvectors that define the principal component directions and eigenvalues that quantify the variance captured along those directions.**

---



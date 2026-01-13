![Image](https://miro.medium.com/v2/resize%3Afit%3A1168/1%2A_zzCYEUm1KSjBMgEDJCS0A.png)

![Image](https://miro.medium.com/1%2AqG4PEnoSWQRLoEL_P1ruhw.jpeg)

![Image](https://miro.medium.com/1%2AAGm7H5hp32qTH4hoOhamcw.jpeg)

![Image](https://i.sstatic.net/XFngC.png)

## 🔢 PCA — **Maths Intuition** (একদম সহজভাবে, step-by-step)

এখানে আমরা PCA-র **গাণিতিক ধারণা** বুঝব
👉 কিন্তু ভারী ম্যাথ না
👉 শুধু *কেন এই ফর্মুলা আসে* সেটা বোঝার জন্য

---

## 🧠 এক লাইনের Maths Idea

> **PCA এমন একটি direction খোঁজে, যেদিকে ডেটা project করলে variance সর্বোচ্চ হয়।**

এই এক লাইনের ভেতরেই PCA-র পুরো ম্যাথ লুকানো।

---

# 1️⃣ PCA আসলে কোন problem solve করে?

ধরা যাক:

* আপনার কাছে data matrix আছে:

[
X \in \mathbb{R}^{n \times d}
]

* (n) = number of samples
* (d) = number of features

👉 আমরা চাই:

* নতুন একটি direction (w)
* যেদিকে data project করলে **variance সবচেয়ে বেশি**

---

# 2️⃣ Projection (গাণিতিকভাবে)

একটা data point (x_i) কে direction (w)-এর উপর project করলে পাই:

[
z_i = w^T x_i
]

এটাই **PC score**

---

# 3️⃣ Variance of projection

আমরা চাই এই projected values-এর variance সর্বোচ্চ হোক:

[
\text{Var}(z) = \text{Var}(w^T X)
]

Math বলে:

[
\text{Var}(w^T X) = w^T \Sigma w
]

যেখানে
(\Sigma) = **Covariance Matrix**

---

# 4️⃣ PCA-র মূল Optimization Problem

👉 PCA solve করে এই problem:

[
\max_w \quad w^T \Sigma w
]

শর্ত (constraint):

[
|w| = 1
]

📌 কেন constraint?

* না দিলে (w) অসীম বড় করে variance বাড়ানো যেত (cheating 😄)

---

# 5️⃣ এই optimization solve করলে কী হয়?

এই problem-এর solution হলো:

[
\Sigma w = \lambda w
]

👉 এটা হলো **Eigenvalue Equation**

এখান থেকেই আসে:

* **Eigenvector** (w)
* **Eigenvalue** (\lambda)

---

# 6️⃣ Eigenvalue & Eigenvector এর Maths Meaning

### 🔹 Eigenvector

* Direction (axis)
* যেদিকে data সবচেয়ে ভালোভাবে ছড়ানো

### 🔹 Eigenvalue

* ঐ direction-এ variance কত

📌 তাই:

* Largest eigenvalue → **PC1**
* 2nd largest → **PC2**

---

# 7️⃣ ছোট Numeric Intuition (2D example)

ধরা যাক covariance matrix:

[
\Sigma =
\begin{bmatrix}
4 & 3 \
3 & 4
\end{bmatrix}
]

Eigenvalues:
[
\lambda_1 = 7,\quad \lambda_2 = 1
]

👉 মানে:

* এক দিক দিয়ে variance = 7 (বড়)
* আরেক দিক দিয়ে variance = 1 (ছোট)

📌 PCA বলে:

> “৭ যেদিকে, সেটাই PC1”

---

# 8️⃣ Why PCs are Orthogonal? (৯০° কেন?)

Math constraint থেকে আসে:

[
w_1^T w_2 = 0
]

👉 মানে:

* PC1 ⟂ PC2

📌 কারণ:

* একই variance দুবার গণনা করা যাবে না
* নতুন PC-কে **নতুন information** আনতে হবে

---

# 9️⃣ Dimensionality Reduction (Math view)

ধরা যাক:

* Total variance = (\lambda_1 + \lambda_2 + \dots + \lambda_d)

আমরা প্রথম (k)টা PC রাখি যদি:

[
\frac{\sum_{i=1}^k \lambda_i}{\sum_{i=1}^d \lambda_i} \ge 0.9
]

👉 মানে: **90% information retained**

---

# 🔄 PCA Transformation Formula

নতুন data:

[
Z = X W
]

যেখানে:

* (W = [w_1, w_2, \dots, w_k])
* (Z) = reduced dataset

---

# 🧠 Maths Intuition এক লাইনে আবার

* **Covariance** → কোন direction-এ data ছড়ায়
* **Eigenvector** → সেই direction
* **Eigenvalue** → ছড়ানোর পরিমাণ

👉 PCA = **Variance maximization under unit-length constraint**

---

## 🔑 Exam / Viva Golden Answer

> **Mathematically, PCA finds the eigenvectors of the covariance matrix corresponding to the largest eigenvalues, which maximize the variance of the projected data.**

---


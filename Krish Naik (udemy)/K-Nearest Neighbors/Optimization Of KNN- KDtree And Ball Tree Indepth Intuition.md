# KNN Optimization — KD-Tree ও Ball Tree: In-Depth বাংলা Intuition

---

## 🔴 সমস্যা: কেন KNN slow?

Normal (Brute Force) KNN এ:

- নতুন point এলে
- সব training point–এর সাথে distance হিসাব করতে হয়

⏱️ Time Complexity:

$$
\mathcal{O}(n \times d)
$$

🧠 Intuition:

> “একজন মানুষকে খুঁজতে পুরো গ্রাম ঘুরে দেখা”

➡️ Solution: **Smart data structure দিয়ে search fast করা**

---

## 🟢 KD-Tree (K-Dimensional Tree)

### 1️⃣ KD-Tree কী?

**KD-Tree হলো space-partitioning data structure** — feature space কে বারবার **axis অনুযায়ী ভাগ করে** একটা **binary tree** বানায়।

### 2️⃣ Core Intuition (সবচেয়ে গুরুত্বপূর্ণ)

> “পুরো জায়গাটা আগে ভাগ করে ফেলি, তারপর দরকারি জায়গায় খুঁজি”

### 3️⃣ 2D Example দিয়ে Intuition

ধরি data point গুলো \((x, y)\) plane-এ আছে।

**Step 1️⃣: Root node (x-axis দিয়ে split)**

- \(x\) এর median নিই
- বাম পাশে → \(x\) ছোট
- ডান পাশে → \(x\) বড়

✂️ Vertical cut

**Step 2️⃣: Next level (y-axis দিয়ে split)**

- এবার \(y\) এর median
- উপর–নিচ ভাগ

✂️ Horizontal cut

**Step 3️⃣: Alternate split**

- \(x \to y \to x \to y \dots\)

🧠 Intuition:

> “একবার লম্বা কেটে, একবার আড়াআড়ি কেটে জমি ভাগ করা”

### 4️⃣ Search করার Intuition (KNN)

ধরি query point \(Q\) এসেছে।

**Step 1️⃣: Tree অনুযায়ী নিচে নামি** — কোন side-এ পড়ছে → সেই branch এ যাই।

**Step 2️⃣: Leaf এ পৌঁছে nearest candidate নিই**

**Step 3️⃣: Backtracking (গুরুত্বপূর্ণ!)**

- অন্য branch-এ closer point থাকতে পারে কি না check
- যদি **splitting plane distance < current best distance** → তাহলে সেই branch-এও যাই

🧠 Intuition:

> “পাশের রাস্তায় একটু ঘুরে দেখলে হয়তো কাছের দোকান পাওয়া যাবে”

### 5️⃣ KD-Tree কবে ভালো কাজ করে?

✅ Dimension কম (\(d \le 10\)–20)

✅ Data evenly distributed

❌ High dimension হলে performance খারাপ

### 6️⃣ KD-Tree Complexity

- Build: \(\mathcal{O}(n \log n)\)
- Query (avg): \(\mathcal{O}(\log n)\)
- Worst: \(\mathcal{O}(n)\) (high dimension)

---

## 🔵 Ball Tree

### 1️⃣ Ball Tree কী?

**Ball Tree data কে sphere (ball) আকারে ভাগ করে** — axis দিয়ে নয়, **distance** দিয়ে।

### 2️⃣ Core Intuition

> “চারকোণা ভাগ না করে গোল বল বানাই”

### 3️⃣ Ball Tree কিভাবে বানানো হয়?

**Step 1️⃣: সব data নিয়ে একটা বড় ball** — Center = mean, Radius = farthest point।

**Step 2️⃣: Data কে দুই ভাগে split** — দুইটা সবচেয়ে দূরের point ধরি; বাকি পয়েন্টগুলো যেটার বেশি কাছে → সেই group।

**Step 3️⃣: Recursively smaller balls** — বড় ball এর ভিতর ছোট ছোট ball।

🧠 Intuition:

> “একটা বড় বেলুন → ছোট ছোট বেলুনে ভাগ”

### 4️⃣ Search Intuition (সবচেয়ে গুরুত্বপূর্ণ)

Query point \(Q\) এর জন্য:

**Step 1️⃣: Ball distance check**

$$
	ext{lowerBound}(Q, \text{ball}) = \operatorname{dist}(Q, \text{center}) - \text{radius}
$$

- যদি এই মান \(>\) current best distance → পুরো ball বাদ।

**Step 2️⃣: Closer ball আগে search** — যেটা কাছে → আগে; দূরেরটা পরে / skip।

🧠 Intuition:

> “এই গোল জায়গার ভেতরে আমার কাছের কেউ নেই, ঢুকবো না”

### 5️⃣ Ball Tree কবে ভালো?

✅ High dimensional data

✅ Distance metric complex (cosine, haversine)

❌ Low dimension হলে KD-Tree faster

### 6️⃣ Ball Tree Complexity

- Build: \(\mathcal{O}(n \log n)\)
- Query: pruning-এর উপর নির্ভর করে
- High-D তে KD-Tree এর চেয়ে ভালো হওয়ার সম্ভাবনা বেশি

---

## 🔥 KD-Tree vs Ball Tree (Deep Comparison)

| বিষয়         | KD-Tree          | Ball Tree       |
| ------------ | ---------------- | --------------- |
| Partition    | Axis-aligned     | Distance-based  |
| Shape        | Rectangle        | Sphere          |
| Split        | x, y, z          | Center + radius |
| Best for     | Low dimension    | High dimension  |
| Metric       | Mostly Euclidean | Any metric      |
| Curse of Dim | Yes              | Less impact     |

---

## 🎯 Brute Force vs Tree (Intuition)

| Method      | Intuition            |
| ----------- | -------------------- |
| Brute Force | পুরো শহর খোঁজা       |
| KD-Tree     | রাস্তা ভাগ করে খোঁজা |
| Ball Tree   | এলাকা বাদ দিয়ে খোঁজা |

---

## 🧠 One-line Intuition

- **KD-Tree** → “দিক ধরে জায়গা ভাগ”
- **Ball Tree** → “দূরত্ব ধরে এলাকা বাদ”

---

## 📌 বাস্তবে (scikit-learn)

```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(
	n_neighbors=5,
	algorithm="kd_tree"  # বা "ball_tree" / "brute" / "auto"
)
knn.fit(X_train, y_train)
pred = knn.predict(X_test)
```

### 🔎 `algorithm="auto"` হলে কী হয়?

- sklearn **metric** (যেমন Euclidean/Minkowski) ও **dimension/distribution** দেখে অভ্যন্তরীণভাবে `kd_tree`, `ball_tree` বা `brute` বেছে নেয়।
- Unsupported metric বা খুব high-D হলে **brute** fallback দেখা যায়।
- ছোট dataset-এ brute অনেক সময় যথেষ্ট দ্রুত।

### 📎 NearestNeighbors দিয়ে pure search

```python
from sklearn.neighbors import NearestNeighbors

nn = NearestNeighbors(n_neighbors=5, algorithm="ball_tree", metric="euclidean")
nn.fit(X)
dist, idx = nn.kneighbors(Q)  # Q: query points
```

---

## 🧪 Bonus: KD vs Ball vs Brute — ছোট বেঞ্চমার্ক

একই data-তে তিনটি algorithm চালিয়ে **fit/query time** তুলনা করলে ধারণা স্পষ্ট হয়।

- কম dimension → KD-Tree সুবিধা
- বেশি dimension/complex metric → Ball Tree বা brute ভালো হতে পারে

বেঞ্চমার্ক রান করার স্ক্রিপ্ট: দেখো [code/knn_tree_benchmark.py](code/knn_tree_benchmark.py)

Quick run (Windows PowerShell):

```powershell
python -m pip install -r requirements.txt
python code/knn_tree_benchmark.py --dims 5 20 50 --samples 3000 --queries 100 --k 5 --metric euclidean
```


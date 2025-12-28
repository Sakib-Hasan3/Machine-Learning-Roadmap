# KNN (K-Nearest Neighbors) — Classification ও Regression: In-Depth বাংলা Intuition

## 1️⃣ KNN কী? (Core Idea)

**KNN একটি instance-based / lazy learning algorithm**।

- ট্রেনিংয়ের সময় কোনো **model বানায় না**
- পুরো training data **মেমোরিতে রেখে দেয়**
- নতুন data এলে “সবচেয়ে কাছের” কিছু data দেখে সিদ্ধান্ত নেয়

🧠 মানুষের intuition:

> “আমার আশেপাশের মানুষগুলো যদি ডাক্তার হয়, আমি সম্ভবত ডাক্তার হবো।”

---

## 2️⃣ “Nearest” মানে কী?

Nearest মানে **distance সবচেয়ে কম**। সবচেয়ে বেশি ব্যবহৃত distance:

- **Euclidean Distance** (সোজা লাইনের দূরত্ব)

$$
d(\mathbf{x},\mathbf{z}) = \sqrt{\sum_{j=1}^{d} (x_j - z_j)^2}
$$

👉 Multi-feature হলে সব feature যোগ হয়ে উপরের মতোই কাজ করে।

---

## 3️⃣ K কী?

**K = কয়জন nearest neighbor দেখবো**

- K = 1 → শুধু সবচেয়ে কাছের ১টা
- K = 5 → কাছের ৫টা
- K = 7 → কাছের ৭টা

⚠️ K খুব গুরুত্বপূর্ণ hyperparameter — খুব ছোট হলে overfitting, খুব বড় হলে underfitting।

---

# 🔷 KNN Classification (গভীর intuition)

## Step-by-step চিন্তা

ধরি:

- তুমি একটি নতুন data point দিলে
- তার class জানা নেই

### Step 1️⃣: Distance হিসাব
নতুন point থেকে **সব training point**–এর distance বের করা হয়।

### Step 2️⃣: K জন closest neighbour নেওয়া
ধরি K = 5 → সবচেয়ে কাছের ৫টা data নেওয়া হলো।

### Step 3️⃣: Majority Voting
৫ জনের মধ্যে:

- ৩ জন যদি Class A
- ২ জন যদি Class B

👉 নতুন point → **Class A** (majority vote)

🧠 Real-life intuition:
> “আমার ৫ জন কাছের বন্ধুদের মধ্যে ৩ জন CSE হলে আমিও সম্ভবত CSE।”

---

## Example (Classification)

| Neighbor | Class |
| -------- | ----- |
| N1       | Red   |
| N2       | Red   |
| N3       | Blue  |
| N4       | Red   |
| N5       | Blue  |

👉 Red = 3, Blue = 2 → **Prediction = Red**

---

## K ছোট হলে কী হয়?

### K = 1
- Noise-এর প্রভাব বেশি
- Overfitting হয়

🧠 intuition: “একজন মানুষ দেখে সিদ্ধান্ত নেওয়া” (ঝুঁকি বেশি)।

## K বড় হলে কী হয়?
- Decision smooth হয়
- Underfitting হতে পারে

🧠 intuition: “খুব বেশি মানুষ দেখে গড় সিদ্ধান্ত” (ডিটেইল হারাতে পারে)।

---

# 🔶 KNN Regression (গভীর intuition)

Classification → discrete label; Regression → **continuous value**।

## Step-by-step চিন্তা

### Step 1️⃣: Distance হিসাব
একইভাবে distance বের করা হয়।

### Step 2️⃣: K nearest neighbour নেওয়া
সবচেয়ে কাছের K টি প্রতিবেশী নাও।

### Step 3️⃣: Average (বা weighted average)
কাছের K জনের **value-এর গড়** নিয়ে prediction করা হয়।

---

## Example (Regression)

ধরি K = 3

| Neighbor | House Price |
| -------- | ----------- |
| N1       | 20 lakh     |
| N2       | 22 lakh     |
| N3       | 24 lakh     |

$$
	ext{Prediction} = \frac{20 + 22 + 24}{3} = 22\,\text{lakh}
$$

🧠 Real-life intuition:
> “এই এলাকায় কাছের ৩টা বাসার দাম গড়ে যা, আমার বাসার দামও প্রায় তাই।”

---

## Weighted KNN (Advanced intuition)

কাছের neighbour বেশি গুরুত্বপূর্ণ — দূরত্ব যত কম, ওজন তত বেশি।

$$
\hat{y} = \frac{\sum_{i=1}^{K} w_i\,y_i}{\sum_{i=1}^{K} w_i},\quad w_i = \frac{1}{d_i + \epsilon}
$$

👉 ছোট distance → বড় weight। ছোট \(\epsilon\) দিলে division-by-zero এড়ানো যায়।

---

# 📌 Classification vs Regression (Intuition Table)

| বিষয়     | Classification  | Regression       |
| -------- | --------------- | ---------------- |
| Output   | Class/Label     | Continuous value |
| Decision | Majority vote   | Average / Weighted average |
| Example  | Spam / Not spam | House price      |

---

# ⚠️ গুরুত্বপূর্ণ সমস্যা ও Intuition

## 1️⃣ Scaling না করলে সমস্যা

যদি Features:

- Age (0–100)
- Income (0–10,00,000)

👉 Income distance dominate করবে।

✔️ Solution: **Normalization / Standardization** (যেমন `StandardScaler`)।

## 2️⃣ Curse of Dimensionality

Feature বেশি হলে:

- Distance প্রায় একই হয়ে যায়
- “Nearest” অর্থ হারায়

🧠 intuition: অনেক dimension-এ সবাই দূরে থাকে, তাই nearest নির্বাচন কঠিন হয়ে যায়।

## 3️⃣ Time Complexity বেশি

Prediction time:

$$
\mathcal{O}(n \times d)
$$

👉 বড় dataset হলে slow — indexing (KD-Tree, Ball-Tree) সাহায্য করতে পারে কিন্তু high-dimension এ লাভ কম।

---

# 🧭 Graph Intuition (2D)

- 2D plane-এ লাল (Class A) ও নীল (Class B) পয়েন্ট ছড়ানো আছে ভাবো।
- নতুন একটি পয়েন্ট এলে তার **কাছের** K পয়েন্ট দেখো:
	- যদি বেশি লাল → লাল predict
	- যদি বেশি নীল → নীল predict
- Regression হলে কাছের মানগুলোর গড়/weighted গড় নেওয়া হয় — পয়েন্টটি যে এলাকায় পড়ে সেই এলাকার trend অনুসরণ করে।

---

# ✅ কখন KNN ভালো?

✔️ Dataset ছোট
✔️ Boundary complex
✔️ Non-linear data

❌ Dataset খুব বড়
❌ Real-time prediction দরকার

---

# 📝 Exam-ready Short Notes

- KNN: lazy learner; training-এ কোনো parametric model নেই।
- Distance: Euclidean (common), Manhattan ইত্যাদি।
- Classification: majority vote; Regression: average/weighted average।
- Hyperparameter: `K`, `distance metric`, `weights`।
- Preprocessing: **scaling আবশ্যক**; high-dim-এ performance কমে।
- Complexity: prediction heavy — \(\mathcal{O}(n\times d)\)।

---

# 🧪 Numerical Examples (Hand-crafted)

## Classification (binary)

Train points (feature = height in cm), labels:

| Height | Label |
| ------ | ----- |
| 160    | A     |
| 162    | A     |
| 170    | B     |
| 172    | B     |
| 168    | B     |

New point: 165, K=3 → Nearest heights: 162(A), 168(B), 160(A) → **A (2 vs 1)**

## Regression (1D)

Train points (x → y): (1→2), (2→2.5), (3→3.5), (4→4.2)

New x=2.2, K=3 → Nearest y: 2, 2.5, 3.5 → \(\frac{2+2.5+3.5}{3}=2.67\) → **Prediction ≈ 2.67**

---

# 🧑🏽‍💻 Python (scikit-learn) — Ready to Run

নিচের স্ক্রিপ্টগুলো ব্যবহার করে দ্রুত রান করতে পারবে:

1. Classification: `code/knn_classification.py`
2. Regression: `code/knn_regression.py`

উভয় স্ক্রিপ্টেই scaling করা আছে এবং `K`, `weights` CLI argument হিসেবে দেওয়া যায়।

Quick start কমান্ডগুলো নিচে দেওয়া হলো (Windows PowerShell):

```powershell
python -m pip install -r requirements.txt
python code/knn_classification.py --k 5 --weights distance
python code/knn_regression.py --k 7 --weights uniform
```

আউটপুটে accuracy (classification) এবং MAE/RMSE (regression) দেখা যাবে।

---

# 🎯 এক লাইনের Intuition

- **KNN Classification** → “আমার কাছের মানুষদের মত আমি হবো”
- **KNN Regression** → “আমার আশেপাশের মানগুলোর গড়ই আমার মান”

---




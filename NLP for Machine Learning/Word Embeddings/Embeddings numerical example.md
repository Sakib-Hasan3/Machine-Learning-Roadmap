---

# 🔢 Word Embeddings — Numerical Example (Exam Style)

## 📘 Given (ধরা যাক)

আমাদের কাছে খুব ছোট একটি embedding space আছে (2-D শুধু বোঝার জন্য)।

ধরা যাক নিচের **pre-trained embeddings** দেওয়া আছে:

| Word  | Embedding Vector |
| ----- | ---------------- |
| king  | (2.0, 3.0)       |
| queen | (2.2, 3.1)       |
| man   | (1.0, 1.0)       |
| woman | (1.2, 1.1)       |

📌 বাস্তবে dimension 100–300 হয়, কিন্তু **exam বোঝানোর জন্য 2-D** ধরা হয়।

---

## 🔷 Example 1: Similarity বোঝা (Cosine Similarity)

### ❓ Question

**king** এবং **queen** কি অর্থে কাছাকাছি?

---

### Step 1️⃣: Cosine Similarity Formula

[
\cos(\theta) = \frac{\vec{A}\cdot\vec{B}}{|\vec{A}||\vec{B}|}
]

---

### Step 2️⃣: Dot Product

[
king \cdot queen = (2.0×2.2) + (3.0×3.1)
]

[
= 4.4 + 9.3 = 13.7
]

---

### Step 3️⃣: Magnitude

[
|king| = \sqrt{2^2 + 3^2} = \sqrt{13} \approx 3.61
]

[
|queen| = \sqrt{2.2^2 + 3.1^2} = \sqrt{14.45} \approx 3.80
]

---

### Step 4️⃣: Cosine Similarity

[
\cos(\theta) = \frac{13.7}{3.61 × 3.80} \approx 0.998
]

✔ **খুব কাছাকাছি (≈1)**
➡ অর্থে খুব similar

---

## 🔷 Example 2: Famous Embedding Arithmetic (Exam Gold ⭐)

### ❓ Question

প্রমাণ করো:
[
king − man + woman ≈ queen
]

---

### Step 1️⃣: Vector Subtraction

```
king − man
= (2.0, 3.0) − (1.0, 1.0)
= (1.0, 2.0)
```

---

### Step 2️⃣: Add woman

```
(1.0, 2.0) + (1.2, 1.1)
= (2.2, 3.1)
```

---

### Step 3️⃣: Compare

```
queen = (2.2, 3.1)
```

✔ Exact match 🎯

➡ **Embedding semantic relationship ধরে**

---

## 🔷 Example 3: Sentence Embedding (Simple Average)

ধরা যাক embeddings:

| Word | Vector     |
| ---- | ---------- |
| I    | (0.1, 0.2) |
| love | (0.8, 0.9) |
| NLP  | (1.0, 1.1) |

Sentence:

```
"I love NLP"
```

---

### Step 1️⃣: Average Embedding

[
\frac{(0.1,0.2) + (0.8,0.9) + (1.0,1.1)}{3}
]

[
= \frac{(1.9, 2.2)}{3}
= (0.63, 0.73)
]

✔ এটিই **sentence embedding**

---

## 🔷 Compare with BoW (Numerical Contrast)

### BoW Vector (Vocabulary = [I, love, NLP])

```
[1, 1, 1]
```

❌ কোনো অর্থ নেই
❌ similarity weak

### Embedding Vector

```
[0.63, 0.73]
```

✔ অর্থবহ
✔ similarity গণনা meaningful

---

## ✍️ Exam-Ready Short Answer

> Word embedding numerical example-এ প্রতিটি শব্দ একটি dense vector দ্বারা প্রকাশিত হয় এবং cosine similarity বা vector arithmetic ব্যবহার করে শব্দের semantic সম্পর্ক নির্ণয় করা যায়।

---

## 🧠 মনে রাখার ট্রিক

> **“BoW গোনে,
> Embedding হিসাব করে সম্পর্ক”**

---

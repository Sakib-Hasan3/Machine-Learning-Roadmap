---

# 🧠 Word Embeddings — সহজ কিন্তু গভীর ব্যাখ্যা

## 🔷 Word Embeddings কী?

**Word Embedding** হলো এমন একটি পদ্ধতি যেখানে
👉 প্রতিটি শব্দকে **সংখ্যার একটি dense vector** (ভেক্টর) দিয়ে প্রকাশ করা হয়
👉 যাতে শব্দের **অর্থ (meaning)**, **সম্পর্ক (relationship)** ও **context** ধরা থাকে

📌 সাধারণত vector-এর dimension হয় **50–300**

---

## ❓ কেন Word Embeddings দরকার হলো?

কারণ আগের পদ্ধতি **Bag of Words (BoW)**–

* শব্দের অর্থ বোঝে না
* word order ও context বোঝে না
* sparse matrix তৈরি করে

➡ এই সব limitation কাটানোর জন্যই **Word Embeddings**

---

## 🧠 Intuition 1: শব্দকে map-এ বসানো 🗺️

ভাবুন একটা 2D/3D জায়গা আছে:

* কাছাকাছি শব্দ → কাছাকাছি অবস্থান
* দূরের শব্দ → অর্থে দূরে

```
king —— queen
man  —— woman
```

👉 মডেল শিখে নেয়:

> কোন শব্দ কোন শব্দের সাথে বেশি related

---

## 🔢 Dense Vector কেমন হয়?

```
king  → [0.21, -0.43, 0.78, 0.12, ...]
queen → [0.22, -0.41, 0.76, 0.14, ...]
```

✔ বেশিরভাগ মান non-zero
✔ তাই একে বলে **Dense**

---

## 🔥 Famous Embedding Example (Exam Gold ⭐)

```
king − man + woman ≈ queen
```

❌ BoW দিয়ে অসম্ভব
✅ Embedding দিয়ে সম্ভব

👉 কারণ embedding **semantic relationship ধরে**

---

## 🔷 Word Embeddings কীভাবে শেখে?

👉 ধারণা খুব simple:

> **যে শব্দগুলো একসাথে আসে, তাদের অর্থ কাছাকাছি**

📌 একে বলে:
**Distributional Hypothesis**

> *“You shall know a word by the company it keeps.”*

---

## 🔷 Types of Word Embeddings

### 1️⃣ Static Word Embeddings

(এক শব্দ = এক vector, context বদলালেও vector একই)

#### 🔹 Word2Vec

* CBOW
* Skip-gram

#### 🔹 GloVe

* Global co-occurrence based

#### 🔹 FastText

* Subword (character-level) information

📌 Example:

```
bank (river) = bank (money)  ❌
```

---

### 2️⃣ Contextual Word Embeddings (Modern NLP) 🚀

👉 **একই শব্দ, ভিন্ন context → ভিন্ন vector**

#### 🔹 BERT

#### 🔹 GPT

#### 🔹 RoBERTa

📌 Example:

```
river bank ≠ bank account
```

➡ embeddings আলাদা হবে ✔

---

## 🆚 BoW vs Word Embeddings (Exam Table)

| Feature     | BoW       | Word Embeddings |
| ----------- | --------- | --------------- |
| Vector type | Sparse    | Dense           |
| Meaning     | ❌         | ✅               |
| Context     | ❌         | ✅               |
| Dimension   | Very high | Low             |
| Similarity  | Weak      | Strong          |
| Modern NLP  | ❌         | ✅               |

---

## 🔷 NLP Tasks যেখানে Embeddings জরুরি

* Sentiment Analysis
* Semantic Search
* Question Answering
* Chatbots
* Machine Translation
* Text Similarity

---

## ✍️ Exam-Ready Definition

> **Word Embedding** হলো এমন একটি representation যেখানে শব্দকে dense numerical vector আকারে প্রকাশ করা হয়, যাতে শব্দের অর্থ ও পারস্পরিক সম্পর্ক সংরক্ষিত থাকে।

---

## 🧠 মনে রাখার ট্রিক

> **“BoW শব্দ গোনে,
> Embedding শব্দ বোঝে”**

---

## 🎯 কখন কোনটা ব্যবহার করবো?

* **Basic ML / Exam / Small data** → BoW / TF-IDF
* **Meaning-based NLP** → Word Embeddings
* **State-of-the-art NLP** → Contextual Embeddings (BERT)

---

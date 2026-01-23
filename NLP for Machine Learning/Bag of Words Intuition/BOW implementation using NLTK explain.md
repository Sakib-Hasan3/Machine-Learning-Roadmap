চলুন এখন আগের **NLTK দিয়ে BoW implementation**–এর **প্রতিটি cell একে একে ব্যাখ্যা করি**
একদম **exam + practical intuition** ধরে 👇

---

# 🧠 Bag of Words (BoW) using NLTK — **Cell-by-Cell Explanation**

---

## ✅ **Cell 1 — NLTK downloads + Imports**

```python
import nltk
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

import re
import pandas as pd
```

### 🔍 এই cell কী করছে?

🔹 `nltk.download(...)`

* **punkt** → tokenization (sentence/word ভাঙতে)
* **stopwords** → is, the, and টাইপ শব্দ বাদ দিতে
* **wordnet + omw** → lemmatization এর জন্য

🔹 Imports:

* `word_tokenize` → বাক্য → শব্দ
* `stopwords` → common শব্দ বাদ
* `WordNetLemmatizer` → শব্দকে base form এ আনা
* `re` → text cleaning (regex)
* `pandas` → table আকারে output দেখাতে

📌 **এই cell ছাড়া NLP preprocessing হবে না**

---

## ✅ **Cell 2 — Corpus (Raw Text Dataset)**

```python
corpus = [
    "I love machine learning. Machine learning is fun!",
    "I love NLP and I love deep learning.",
    "NLP is about text processing and understanding language."
]
corpus
```

### 🔍 এই cell কী করছে?

🔹 `corpus` = **documents-এর list**

* প্রতিটা element = একেকটা document / sentence

📌 NLP-তে:

* Corpus = সম্পূর্ণ text collection
* Document = corpus-এর একটি element

---

## ✅ **Cell 3 — Preprocessing Function**

```python
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()
```

🔹 এখানে:

* English stopwords load করা হচ্ছে
* Lemmatizer object তৈরি

---

### 🔹 Preprocessing Function

```python
def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stop_words]
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return tokens
```

### 🧠 ধাপে ধাপে কী হচ্ছে?

1️⃣ `lower()`
→ সব শব্দ ছোট হাতের

```
Machine → machine
```

2️⃣ Regex cleaning
→ punctuation, number বাদ

```
learning. → learning
```

3️⃣ `word_tokenize()`
→ sentence → শব্দের list

```
"I love NLP" → ["i","love","nlp"]
```

4️⃣ Stopword removal
→ is, the, and বাদ

5️⃣ Lemmatization

```
learning → learn
```

📌 Output = **clean tokens**

---

### 🔹 Apply preprocessing

```python
processed = [preprocess(doc) for doc in corpus]
processed
```

➡ প্রতিটা document এখন **clean word list**

---

## ✅ **Cell 4 — Vocabulary তৈরি**

```python
vocab = sorted(set(word for doc in processed for word in doc))
vocab
```

### 🔍 এই cell কী করছে?

🔹 সব document থেকে:

* unique শব্দ বের করা
* duplicate বাদ
* alphabetically sort

📌 Vocabulary = **BoW-এর backbone**

Example:

```
["about", "deep", "fun", "language", "learn", ...]
```

---

## ✅ **Cell 5 — Word → Index Mapping**

```python
word2idx = {word: i for i, word in enumerate(vocab)}
word2idx
```

### 🔍 কেন দরকার?

BoW vector বানাতে:

* প্রতিটা শব্দের একটা **fixed position** দরকার

Example:

```
"learn" → index 4
```

📌 এখন vector-এর 4 নম্বর position মানে “learn”

---

## ✅ **Cell 6 — BoW Vector তৈরি (Count-based)**

```python
def bow_vector(tokens, word2idx):
    vec = [0] * len(word2idx)
    for w in tokens:
        vec[word2idx[w]] += 1
    return vec
```

### 🧠 এই function কী করছে?

* শুরুতে vector = `[0,0,0,0,...]`
* token আসলে → সেই index এ count বাড়ে

Example:

```
tokens = ["love","nlp","love"]
vector → love index = 2
→ [0,0,2,0,...]
```

---

### 🔹 Apply to all documents

```python
bow_vectors = [bow_vector(doc_tokens, word2idx) for doc_tokens in processed]
bow_vectors
```

➡ এখন প্রতিটা document = **numerical vector**

---

## ✅ **Cell 7 — BoW Matrix (Readable Table)**

```python
bow_df = pd.DataFrame(bow_vectors, columns=vocab)
bow_df.index = [f"D{i+1}" for i in range(len(corpus))]
bow_df
```

### 🔍 এই cell কী করছে?

* BoW vectors → DataFrame
* Columns = Vocabulary
* Rows = Documents (D1, D2, D3)

📌 এটাকেই বলে:

> **Document–Term Matrix**

---

## ✅ **Cell 8 — Tokens + BoW একসাথে দেখা**

```python
for i, (tokens, vec) in enumerate(zip(processed, bow_vectors), start=1):
    print(f"Document D{i}:")
    print("Tokens:", tokens)
    print("BoW:", vec)
    print("-" * 60)
```

### 🔍 এই cell কেন?

* Learning purpose
* বোঝার জন্য:

```
এই tokens → এই vector
```

📌 Exam-এ বোঝানোর জন্য খুব useful

---

# 🧠 Final Intuition (সব মিলিয়ে)

```
Raw Text
 ↓
Cleaning
 ↓
Tokenization
 ↓
Stopword Removal
 ↓
Lemmatization
 ↓
Vocabulary
 ↓
Count words
 ↓
BoW Vector
 ↓
BoW Matrix
```

---

## ✍️ Exam-Ready One-Liner

> NLTK ব্যবহার করে Bag of Words implementation-এ প্রথমে text preprocessing করা হয়, তারপর vocabulary তৈরি করে প্রতিটি document-কে শব্দের frequency ভেক্টর হিসেবে প্রকাশ করা হয়।

---

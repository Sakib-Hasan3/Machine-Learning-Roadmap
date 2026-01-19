## 🔹 05. Text Preprocessing: **Stemming (NLTK ব্যবহার করে)** — *বাংলায় সহজ ব্যাখ্যা*

![Image](https://www.researchgate.net/publication/385694230/figure/fig4/AS%3A11431281289486592%401731231458366/Stemming-and-lemmatization.png)

![Image](https://miro.medium.com/v2/resize%3Afit%3A1400/0%2ABgalYghgF7tejjzW.png)

![Image](https://vijinimallawaarachchi.com/wp-content/uploads/2017/05/porterstemmer.png?w=772)

### 🔸 Stemming কী?

**Stemming** হলো **Text Preprocessing**-এর একটি গুরুত্বপূর্ণ ধাপ, যেখানে
একটি শব্দকে তার **মূল রুট (root/base form)**-এ নামিয়ে আনা হয়।

📌 লক্ষ্য:

> একই অর্থের শব্দগুলোকে একটি ফর্মে আনা, যাতে মডেল সহজে প্যাটার্ন ধরতে পারে।

#### উদাহরণ:

| Original Word | Stemmed Word |
| ------------- | ------------ |
| playing       | play         |
| played        | play         |
| plays         | play         |
| studies       | studi        |
| studying      | studi        |

👉 এখানে লক্ষ্য করলে দেখবেন, **grammar ঠিক থাকতেই হবে এমন না**, শুধু **root** পেলেই যথেষ্ট।

---

### 🔸 NLP-তে Stemming কেন দরকার?

✔ শব্দের ভ্যারিয়েশন কমায়
✔ Vocabulary size ছোট করে
✔ Text classification / sentiment analysis-এ সাহায্য করে
✔ Computational cost কমায়

---

### 🔸 Stemming vs Lemmatization (সংক্ষেপে)

| Stemming        | Lemmatization    |
| --------------- | ---------------- |
| দ্রুত           | তুলনামূলক ধীর    |
| grammar মানে না | grammar মানে     |
| rule-based      | dictionary-based |
| play, studi     | play, study      |

---

## 🔸 NLTK দিয়ে Stemming

আমরা এখানে Python লাইব্রেরি **NLTK (Natural Language Toolkit)** ব্যবহার করব।

### 🔹 Step 1: NLTK ইনস্টল

```python
pip install nltk
```

---

### 🔹 Step 2: Porter Stemmer ব্যবহার

```python
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["playing", "played", "plays", "studies", "studying"]

for word in words:
    print(word, "→", stemmer.stem(word))
```

#### 🔸 Output:

```
playing → play
played → play
plays → play
studies → studi
studying → studi
```

📌 **PorterStemmer** সবচেয়ে বেশি ব্যবহৃত এবং দ্রুত।

---

## 🔸 NLTK-এর বিভিন্ন Stemmer

| Stemmer          | বৈশিষ্ট্য              |
| ---------------- | ---------------------- |
| PorterStemmer    | সবচেয়ে জনপ্রিয়       |
| SnowballStemmer  | Porter-এর উন্নত ভার্সন |
| LancasterStemmer | বেশি aggressive (কঠোর) |

### 🔹 Snowball Stemmer উদাহরণ

```python
from nltk.stem import SnowballStemmer

stemmer = SnowballStemmer("english")
stemmer.stem("running")
```

---

## 🔸 কখন Stemming ব্যবহার করবেন?

✅ Text Classification
✅ Spam Detection
✅ Sentiment Analysis
❌ Grammar-sensitive কাজ (যেমন: Chatbot response generation)

---

## 🔚 সংক্ষেপে মনে রাখুন

* **Stemming = শব্দ ভেঙে root বানানো**
* grammar ঠিক থাকা বাধ্যতামূলক নয়
* দ্রুত ও lightweight preprocessing
* ML model-এর জন্য খুব উপকারী

---



## 🔹 **NLTK** ও **spaCy** কী? — *বাংলায় সহজ ব্যাখ্যা*

![Image](https://media.licdn.com/dms/image/v2/D5612AQH-AcQSsJT7Wg/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1722023278165?e=2147483647\&t=W9khkDqas5ZQKLvmpUEDf4hA8PB61BDpvfN1ahfcI-M\&v=beta)

![Image](https://miro.medium.com/v2/resize%3Afit%3A1128/1%2AHLQgkMt5-g5WO5VpNuTl_g.jpeg)

![Image](https://www.shaip.com/wp-content/uploads/2022/02/Blog_Named-Entity-Recognition-%E2%80%93-The-Concept-Types-Applications.jpg)

---

## 🔸 NLTK কী?

**NLTK (Natural Language Toolkit)** হলো Python-এর একটি জনপ্রিয় **NLP শেখার ও গবেষণাভিত্তিক লাইব্রেরি**।

### 🧠 NLTK কী কাজে লাগে?

* Tokenization (শব্দ/বাক্য ভাঙা)
* Stemming (Porter, Snowball)
* Lemmatization
* Stopword removal
* POS tagging (noun, verb ইত্যাদি)
* Text classification (basic)

### ✅ বৈশিষ্ট্য

* শেখার জন্য দারুণ
* প্রচুর example ও dataset
* ধাপে ধাপে বোঝা সহজ
* তুলনামূলক ধীর (production-এ কম ব্যবহৃত)

### 🔹 উদাহরণ

```python
from nltk.tokenize import word_tokenize
word_tokenize("I love Natural Language Processing")
```

---

## 🔸 spaCy কী?

**spaCy** হলো একটি **Modern, Fast ও Production-Ready NLP লাইব্রেরি**।

### 🧠 spaCy কী কাজে লাগে?

* Fast tokenization
* Accurate lemmatization
* Named Entity Recognition (NER)
* Dependency parsing
* POS tagging
* Industrial-grade NLP pipelines

### ✅ বৈশিষ্ট্য

* খুব দ্রুত
* উচ্চ accuracy
* Real-world application-এর জন্য তৈরি
* Deep learning-based models

### 🔹 উদাহরণ

```python
import spacy
nlp = spacy.load("en_core_web_sm")

doc = nlp("Apple is looking at buying a startup in London")
for ent in doc.ents:
    print(ent.text, ent.label_)
```

---

## 🔸 NLTK vs spaCy — পার্থক্য টেবিল

| বিষয়          | NLTK          | spaCy                 |
| ------------- | ------------- | --------------------- |
| লক্ষ্য        | শেখা / গবেষণা | Production / Industry |
| Speed         | ধীর           | খুব দ্রুত             |
| Accuracy      | মাঝারি        | বেশি                  |
| ML Models     | Basic         | Advanced              |
| Easy to Learn | ✅             | মাঝারি                |
| Real Project  | ❌             | ✅                     |

---

## 🔸 কখন কোনটা ব্যবহার করবেন?

### ✅ NLTK ব্যবহার করুন যখন:

* NLP শেখা শুরু করছেন
* Stemming / Tokenization বোঝা দরকার
* Academic / Exam purpose

### ✅ spaCy ব্যবহার করুন যখন:

* Real-world NLP project
* Chatbot, Resume parser, NER
* Fast & accurate output দরকার

---

## 🔚 এক লাইনে মনে রাখুন

* **NLTK = NLP শেখার বই**
* **spaCy = NLP কাজের মেশিন**

---



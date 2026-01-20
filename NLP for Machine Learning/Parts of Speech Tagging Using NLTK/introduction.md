## 📌 **Parts of Speech (POS) Tagging Using NLTK — বিস্তারিত ব্যাখ্যা (Concept Only)**

![Image](https://cdn-media-1.freecodecamp.org/images/1%2Af6e0uf5PX17pTceYU4rbCA.jpeg)

![Image](https://byteiota.com/wp-content/uploads/2021/01/POS-Tagging-800x400.jpg)

![Image](https://miro.medium.com/1%2AqZELwIpKeEQ-j3EnRF-CrQ.jpeg)

---

## 🔹 POS Tagging কী?

**POS (Part of Speech) Tagging** হলো এমন একটি প্রক্রিয়া যেখানে
👉 একটি বাক্যের **প্রতিটি শব্দকে তার ব্যাকরণগত ভূমিকা অনুযায়ী চিহ্নিত (tag)** করা হয়।

অর্থাৎ, কোন শব্দটি—

* Noun (বিশেষ্য)
* Verb (ক্রিয়া)
* Adjective (বিশেষণ)
* Adverb (ক্রিয়া বিশেষণ)
* Preposition, Determiner ইত্যাদি

👉 তা নির্ধারণ করাই POS Tagging।

---

## 🔹 POS Tagging কেন গুরুত্বপূর্ণ?

POS Tagging NLP-এর একটি **fundamental (মৌলিক) ধাপ**। কারণ—

### 🧠 1️⃣ শব্দের সঠিক অর্থ বোঝার জন্য

একই শব্দ ভিন্ন POS হলে অর্থ বদলে যায়।

🔹 উদাহরণ:

* **book (noun)** → একটি বই
* **book (verb)** → বুক করা

👉 POS না জানলে কম্পিউটার ভুল অর্থ ধরতে পারে।

---

### 🔹 2️⃣ Lemmatization সঠিক করার জন্য

Lemmatization করতে গেলে **শব্দটি verb না noun—এটা জানা খুব জরুরি**।

উদাহরণ:

* running (verb) → run
* running (noun) → running

👉 POS ছাড়া Lemmatization করলে ভুল হতে পারে।

---

### 🔹 3️⃣ Sentence Structure বোঝার জন্য

POS Tagging দিয়ে বোঝা যায়—

* Subject কে?
* Verb কোনটা?
* Object কোনটা?

👉 Parsing, Grammar analysis, Chatbot-এর জন্য দরকার।

---

### 🔹 4️⃣ NLP Applications-এ ব্যবহার

POS Tagging ব্যবহার হয়—

* 🗣️ Chatbot
* 📊 Sentiment Analysis
* 🧾 Information Extraction
* 🧠 Question Answering System
* 🧬 Machine Translation

---

## 🔹 POS Tagging কীভাবে কাজ করে? (High Level Idea)

POS Tagging সাধারণত কাজ করে—

* **Machine Learning model**
* **Statistical patterns**
* **Context (আগে-পরে কোন শব্দ আছে)**

👉 **NLTK**-এ ব্যবহৃত tagger-এর নাম:
**Averaged Perceptron Tagger**

এটি—

* আগের শব্দ
* পরের শব্দ
* বাক্যের গঠন
  সবকিছু দেখে সিদ্ধান্ত নেয়।

---

## 🔹 POS Tag কী?

**POS Tag** হলো ছোট ছোট কোড, যা শব্দের ধরন বোঝায়।

### 🔸 কিছু গুরুত্বপূর্ণ POS Tag

| Tag | অর্থ          | উদাহরণ  |
| --- | ------------- | ------- |
| NN  | Noun (একবচন)  | boy     |
| NNS | Noun (বহুবচন) | boys    |
| NNP | Proper Noun   | London  |
| VB  | Verb (base)   | run     |
| VBG | Verb (-ing)   | running |
| VBD | Verb (past)   | ran     |
| JJ  | Adjective     | good    |
| RB  | Adverb        | quickly |
| DT  | Determiner    | the, a  |
| IN  | Preposition   | in, on  |

📌 এগুলোকে বলা হয় **Penn Treebank POS Tags**।

---

## 🔹 POS Tagging-এর Input ও Output

### 🔸 Input

```
The children are running fast
```

### 🔸 Output (Conceptually)

```
The → DT
children → NNS
are → VBP
running → VBG
fast → RB
```

👉 প্রতিটি শব্দের সাথে একটি POS tag যুক্ত হয়।

---

## 🔹 POS Tagging কোথায় বসে NLP Pipeline-এ?

```
Raw Text
  ↓
Tokenization
  ↓
POS Tagging   ← (এই ধাপ)
  ↓
Lemmatization
  ↓
Feature Extraction
```

👉 POS Tagging সাধারণত **Tokenization-এর পরে** করা হয়।

---

## 🔹 POS Tagging-এর সুবিধা ও সীমাবদ্ধতা

### ✅ সুবিধা

* Text বোঝা সহজ করে
* Lemmatization accurate করে
* Grammar-aware NLP সম্ভব করে

### ❌ সীমাবদ্ধতা

* Ambiguous word হলে ভুল হতে পারে
  (যেমন: “book”, “lead”)
* Context না পেলে accuracy কমে

---

## 🧠 Exam-ready সংক্ষেপে

> POS Tagging is the process of assigning grammatical categories (noun, verb, adjective, etc.) to each word in a sentence.

---


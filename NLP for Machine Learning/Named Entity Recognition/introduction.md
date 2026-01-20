## 🔹 *বাংলায় বিস্তারিত ব্যাখ্যা (Code + Output সহ)*

![Image](https://www.shaip.com/wp-content/uploads/2022/02/Blog_Named-Entity-Recognition-%E2%80%93-The-Concept-Types-Applications.jpg)

![Image](https://miro.medium.com/1%2A5O7w5I7vf2TbFp0XoC1NSQ.jpeg)

![Image](https://www.researchgate.net/publication/365181273/figure/fig2/AS%3A11431281095232066%401667791028710/The-end-to-end-pipeline-of-an-updated-NER-model-in-spaCy-Under-a-black-box-setting-the.png)

---

## 🔸 Named Entity Recognition (NER) কী?

**Named Entity Recognition (NER)** হলো NLP-এর একটি গুরুত্বপূর্ণ কাজ, যেখানে
👉 একটি টেক্সট থেকে **নির্দিষ্ট নামযুক্ত সত্তা (Entity)** শনাক্ত করা হয়।

এই Entity গুলো হতে পারে—

* 👤 **Person** (ব্যক্তির নাম)
* 🏢 **Organization** (কোম্পানি/প্রতিষ্ঠান)
* 🌍 **Location / GPE** (দেশ, শহর)
* 📅 **Date / Time**
* 💰 **Money**
* 📦 **Product**

---

## 🔸 NER কেন দরকার?

NER ব্যবহার করা হয়—

* 📄 Resume Parsing
* 📰 News Analysis
* 🤖 Chatbot
* 🔍 Information Extraction
* 📊 Knowledge Graph তৈরিতে

👉 সহজভাবে: **টেক্সট থেকে দরকারি তথ্য আলাদা করে বের করা**

---

## 🔹 NLP Pipeline-এ NER-এর অবস্থান

```
Raw Text
  ↓
Tokenization
  ↓
POS Tagging
  ↓
NER   ← (এই ধাপ)
```

NER সাধারণত **POS Tagging-এর পরে** কাজ করে।

---

## 🔹 NER-এর সাধারণ Entity টাইপ

| Entity Label | অর্থ          | উদাহরণ             |
| ------------ | ------------- | ------------------ |
| PERSON       | ব্যক্তির নাম  | Elon Musk          |
| ORG          | প্রতিষ্ঠান    | Google             |
| GPE          | দেশ/শহর       | London, Bangladesh |
| LOC          | ভৌগোলিক স্থান | Himalaya           |
| DATE         | তারিখ         | 2024               |
| TIME         | সময়          | 5 PM               |
| MONEY        | টাকা          | $500               |
| PRODUCT      | পণ্য          | iPhone             |

---

# 🟢 NER using **spaCy** (Recommended)

**spaCy** NER-এর জন্য সবচেয়ে জনপ্রিয় ও accurate।

---

## ✅ Step 1: Install & Model Download

```bash
pip install spacy
python -m spacy download en_core_web_sm
```

---

## ✅ Step 2: spaCy NER Code

```python
import spacy

nlp = spacy.load("en_core_web_sm")

text = "Apple is looking to buy a startup in London for $1 billion in 2024."

doc = nlp(text)

print("Named Entities:")
for ent in doc.ents:
    print(ent.text, "→", ent.label_)
```

---

## 📤 Output

```
Named Entities:
Apple → ORG
London → GPE
$1 billion → MONEY
2024 → DATE
```

📌 spaCy নিজে নিজে entity চিনে ফেলেছে।

---

# 🔵 NER using **NLTK**

**NLTK** দিয়েও NER করা যায়, কিন্তু তুলনামূলকভাবে কম accurate।

---

## ✅ Step 1: Required Downloads

```python
import nltk
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("maxent_ne_chunker")
nltk.download("words")
```

---

## ✅ Step 2: NLTK NER Code

```python
from nltk import word_tokenize, pos_tag, ne_chunk

sentence = "Apple is looking to buy a startup in London."

tokens = word_tokenize(sentence)
pos_tags = pos_tag(tokens)
ner_tree = ne_chunk(pos_tags)

print(ner_tree)
```

---

## 📤 Output (Tree Format)

```
(S
  (ORGANIZATION Apple/NNP)
  is/VBZ
  looking/VBG
  to/TO
  buy/VB
  a/DT
  startup/NN
  in/IN
  (GPE London/NNP)
  ./.)
```

📌 এখানে entity গুলো **tree আকারে** এসেছে।

---

## 🔸 spaCy vs NLTK — NER তুলনা

| বিষয়           | NLTK        | spaCy         |
| -------------- | ----------- | ------------- |
| Accuracy       | মাঝারি      | বেশি          |
| Speed          | ধীর         | দ্রুত         |
| Output         | Tree format | Simple labels |
| Production use | ❌           | ✅             |
| Ease           | মাঝারি      | সহজ           |

---

## 🔚 সংক্ষেপে মনে রাখুন

* **NER = Name-based information extraction**
* spaCy → fast & production-ready
* NLTK → শেখার জন্য ভালো

---

### 🧠 Exam-ready One-liner

> Named Entity Recognition is the process of identifying and classifying named entities such as person, organization, and location from text.

---


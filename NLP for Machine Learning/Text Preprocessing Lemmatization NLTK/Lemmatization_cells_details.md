নিশ্চিতভাবে—নিচে **Lemmatization.ipynb**-এর **প্রতিটি Cell-এর কোড লাইন–বাই–লাইন বাংলায় ব্যাখ্যা** দেওয়া হলো।
(কোন Cell কী কাজ করছে, কেন দরকার—সব পরিষ্কারভাবে)

---

## 🧩 **Cell 1 — POS Tagger ডাউনলোড**

```python
import nltk
nltk.download('averaged_perceptron_tagger_eng')
```

### 🔍 ব্যাখ্যা

* `import nltk`
  👉 NLTK লাইব্রেরি Python-এ ইমপোর্ট করা হচ্ছে।

* `nltk.download('averaged_perceptron_tagger_eng')`
  👉 **POS Tagger model** ডাউনলোড করা হচ্ছে।
  👉 এটি শব্দের **Part of Speech (Noun, Verb, Adjective ইত্যাদি)** শনাক্ত করতে ব্যবহৃত হয়।

📌 **কেন দরকার?**
Lemmatization-এ সঠিক ফল পেতে হলে POS জানা জরুরি।

---

## 🧩 **Cell 2 — প্রয়োজনীয় NLTK Resources ডাউনলোড**

```python
import nltk
# প্রথমবার চালালে
nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
```

### 🔍 ব্যাখ্যা

* `wordnet`
  👉 English dictionary database
  👉 Lemmatization-এর মূল ভিত্তি

* `omw-1.4`
  👉 WordNet-এর supporting multilingual data
  👉 Lemma accuracy বাড়ায়

* `punkt`
  👉 **Tokenization** (sentence → words) করার জন্য

* `averaged_perceptron_tagger`
  👉 POS tagging-এর জন্য ব্যবহৃত model

📌 **নোট:**
এই Cell সাধারণত **একবারই** চালাতে হয় (first-time setup)।

---

## 🧩 **Cell 3 — Basic Lemmatization (POS ছাড়া)**

```python
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
words = ["running", "studies", "better", "mice", "cars"]

for w in words:
    print(w, "→", lemmatizer.lemmatize(w))
```

### 🔍 ব্যাখ্যা (লাইন ধরে)

* `from nltk.stem import WordNetLemmatizer`
  👉 Lemmatizer ক্লাস ইমপোর্ট করা হচ্ছে।

* `lemmatizer = WordNetLemmatizer()`
  👉 Lemmatizer-এর একটি object তৈরি করা হলো।

* `words = [...]`
  👉 যেসব শব্দে Lemmatization করব, সেগুলোর লিস্ট।

* `lemmatizer.lemmatize(w)`
  👉 প্রতিটি শব্দকে **lemma (base form)**-এ রূপান্তর করে।

### 📤 Output ব্যাখ্যা

```
running → running
studies → study
better → better
mice → mouse
cars → car
```

📌 এখানে `running` বদলায়নি কারণ
👉 **default হিসেবে noun ধরে নেওয়া হয়**
👉 verb হলে POS দিতে হয়

---

## 🧩 **Cell 4 — POS Mapping Function**

```python
from nltk.corpus import wordnet
from nltk import word_tokenize, pos_tag

def get_wordnet_pos(tag):
    if tag.startswith("J"):
        return wordnet.ADJ
    elif tag.startswith("V"):
        return wordnet.VERB
    elif tag.startswith("N"):
        return wordnet.NOUN
    elif tag.startswith("R"):
        return wordnet.ADV
    else:
        return wordnet.NOUN
```

### 🔍 ব্যাখ্যা

* `word_tokenize`
  👉 বাক্যকে শব্দে ভাঙে

* `pos_tag`
  👉 প্রতিটি শব্দের POS tag দেয় (NN, VB, JJ ইত্যাদি)

* `get_wordnet_pos(tag)`
  👉 NLTK POS tag → **WordNet POS format**-এ রূপান্তর করে

### 🔁 Mapping Logic

| NLTK Tag শুরু | অর্থ      | WordNet Tag    |
| ------------- | --------- | -------------- |
| J             | Adjective | `wordnet.ADJ`  |
| V             | Verb      | `wordnet.VERB` |
| N             | Noun      | `wordnet.NOUN` |
| R             | Adverb    | `wordnet.ADV`  |

📌 **কেন দরকার?**
WordNetLemmatizer **WordNet POS** চায়,
NLTK দেয় **short POS code**—তাই mapping লাগে।

---

## 🧩 **Cell 5 — POS সহ Lemmatization (Main Cell)**

```python
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
sentence = "The children were running better cars in London"

tokens = word_tokenize(sentence)
pos_tags = pos_tag(tokens)

lemmas = [lemmatizer.lemmatize(w, get_wordnet_pos(t)) for w, t in pos_tags]
print(lemmas)
```

### 🔍 ব্যাখ্যা (ধাপে ধাপে)

1️⃣ `sentence = ...`
👉 যেই বাক্যটা preprocess করব

2️⃣ `tokens = word_tokenize(sentence)`
👉 বাক্য → শব্দ

```
['The','children','were','running','better','cars','in','London']
```

3️⃣ `pos_tags = pos_tag(tokens)`
👉 প্রতিটি শব্দের POS

```
('children','NNS'), ('running','VBG'), ('better','JJR') ...
```

4️⃣ List comprehension:

```python
lemmatizer.lemmatize(w, get_wordnet_pos(t))
```

👉

* শব্দ (`w`)
* তার POS (`t`)
* POS mapping → WordNet POS
* তারপর **সঠিক lemma বের করা**

### 📤 Final Output

```
['The', 'child', 'be', 'run', 'good', 'car', 'in', 'London']
```

📌 এখানে:

* children → child
* were → be
* running → run
* better → good

👉 **এটাই Accurate Lemmatization**

---

## 🧩 **Cell 6 — Empty Cell**

```python
```

### 🔍 ব্যাখ্যা

* এই Cell এখনো খালি
* সাধারণত এখানে রাখা হয়:

  * Extra experiment
  * Notes
  * Future code (Stopwords, Pipeline ইত্যাদি)

---

## ✅ **পুরো Notebook-এর Flow (এক লাইনে)**

```
Download resources
→ Tokenize sentence
→ POS tagging
→ POS mapping
→ Lemmatization
```

---

## 🧠 Exam-friendly Summary

> Lemmatization converts words into their base dictionary form using POS information, and NLTK’s WordNetLemmatizer gives accurate results when POS tagging is applied.

---



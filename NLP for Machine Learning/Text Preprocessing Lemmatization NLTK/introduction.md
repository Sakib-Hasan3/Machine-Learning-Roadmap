## 🔹 **Text Preprocessing: Lemmatization (NLTK ব্যবহার করে)** — *বাংলায় সহজ ব্যাখ্যা*

![Image](https://www.mygreatlearning.com/blog/wp-content/uploads/2025/03/lemmanization-example.png)

![Image](https://www.researchgate.net/publication/385694230/figure/fig4/AS%3A11431281289486592%401731231458366/Stemming-and-lemmatization.png)

![Image](https://images.prismic.io/turing/659d76b9531ac2845a27428f_Word_Net_lemmatizer_without_the_POS_tag_15_11zon_3d7e19466a.webp?auto=format%2Ccompress)

---

## 🔸 Lemmatization কী?

**Lemmatization** হলো Text Preprocessing-এর একটি ধাপ যেখানে
শব্দকে তার **সঠিক dictionary form (lemma)**-এ রূপান্তর করা হয়।

📌 এখানে **grammar ও শব্দের অর্থ (POS – noun, verb ইত্যাদি)** বিবেচনা করা হয়।

### 🔹 উদাহরণ

| Word    | Lemma |
| ------- | ----- |
| running | run   |
| better  | good  |
| studies | study |
| mice    | mouse |
| was     | be    |

👉 লক্ষ্য করুন: Lemma সবসময় **বাস্তব অর্থপূর্ণ শব্দ**।

---

## 🔸 Stemming vs Lemmatization (দ্রুত তুলনা)

| বিষয়          | Stemming        | Lemmatization   |
| ------------- | --------------- | --------------- |
| Grammar দেখে? | ❌ না            | ✅ হ্যাঁ         |
| Output        | root (ভাঙা)     | সঠিক শব্দ       |
| Speed         | দ্রুত           | তুলনামূলক ধীর   |
| Example       | studies → studi | studies → study |

---

## 🔸 NLP-তে Lemmatization কেন দরকার?

✅ Meaning preserve করে
✅ Chatbot, QA system-এ দরকার
✅ NER, POS-based কাজের জন্য উপকারী
❌ একটু slow

---

## 🔸 NLTK দিয়ে Lemmatization

আমরা ব্যবহার করব **NLTK**-এর
**WordNetLemmatizer**

---

## 🔹 Step 1: Required Packages

```python
import nltk

# প্রথমবার চালালে দরকার হবে
nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download("averaged_perceptron_tagger")
nltk.download("punkt")
```

---

## 🔹 Step 2: Basic Lemmatization (Without POS)

```python
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

words = ["running", "studies", "better", "mice", "cars"]

for word in words:
    print(word, "→", lemmatizer.lemmatize(word))
```

### 📤 Output

```
running → running
studies → study
better → better
mice → mouse
cars → car
```

📌 এখানে দেখুন:
`running` verb হলেও default হিসেবে noun ধরে নেওয়ায় বদলায়নি।

---

## 🔹 Step 3: Lemmatization with POS (Recommended)

### 🔸 POS mapping function

```python
from nltk.corpus import wordnet
from nltk import pos_tag, word_tokenize

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

### 🔸 Full Lemmatization Code

```python
sentence = "The children are running and studies were better than expected"

tokens = word_tokenize(sentence)
pos_tags = pos_tag(tokens)

lemmatized_words = []

for word, tag in pos_tags:
    wn_tag = get_wordnet_pos(tag)
    lemmatized_words.append(lemmatizer.lemmatize(word, wn_tag))

print("Original Tokens:")
print(tokens)

print("\nLemmatized Tokens:")
print(lemmatized_words)
```

### 📤 Output

```
Original Tokens:
['The', 'children', 'are', 'running', 'and', 'studies', 'were', 'better', 'than', 'expected']

Lemmatized Tokens:
['The', 'child', 'be', 'run', 'and', 'study', 'be', 'good', 'than', 'expect']
```

📌 এখানে দেখুন:

* children → child
* running → run
* better → good
* were → be

👉 এটাই **True Lemmatization**

---

## 🔚 সংক্ষেপে মনে রাখুন

* **Lemmatization = dictionary + grammar**
* Output সবসময় অর্থপূর্ণ শব্দ
* NLP production system-এ গুরুত্বপূর্ণ
* NLTK-তে POS দিলে best result

---

### 🧠 Exam-friendly One Liner

> Lemmatization is the process of converting words into their base dictionary form using grammatical analysis.

---


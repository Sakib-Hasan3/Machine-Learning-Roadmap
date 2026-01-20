## 🔹 **07. Text Preprocessing: Stopwords** — *বাংলায় সহজ, পরীক্ষামুখী ব্যাখ্যা (Code + Output সহ)*

![Image](https://media.geeksforgeeks.org/wp-content/cdn-uploads/Stop-word-removal-using-NLTK.png)

![Image](https://media.licdn.com/dms/image/v2/D5612AQGeJ5FET7M8lQ/article-cover_image-shrink_720_1280/B56ZebNFxzG0AI-/0/1750655621243?e=2147483647\&t=q_F45m3wtJbYY9-ARt9VZd8eZ7tsc32-JG-CqdOj9Ew\&v=beta)

![Image](https://www.researchgate.net/publication/228670007/figure/tbl2/AS%3A671525258657813%401537115506709/Sample-of-stop-words.png)

---

## 🔸 Stopwords কী?

**Stopwords** হলো এমন শব্দ, যেগুলো **বাক্যের অর্থ বোঝাতে খুব কম ভূমিকা রাখে**, কিন্তু প্রায় সব বাক্যেই ঘনঘন ব্যবহৃত হয়।

📌 যেমন:
**the, is, are, in, on, at, and, a, an, to**

👉 এগুলো সাধারণত **Text Preprocessing-এর সময় বাদ দেওয়া হয়**।

---

## 🔸 Stopwords কেন remove করা হয়?

* ✅ Noise কমায়
* ✅ Vocabulary size ছোট করে
* ✅ Model fast করে
* ✅ Text classification / sentiment analysis-এ সাহায্য করে

❌ কিন্তু সব ক্ষেত্রে নয় (Chatbot / QA system-এ দরকার হতে পারে)

---

## 🔹 NLTK দিয়ে Stopwords Removal

আমরা ব্যবহার করব **NLTK**-এর stopwords corpus।

---

### 🔹 Step 1: Stopwords ডাউনলোড

```python
import nltk
# প্রথমবার চালালে
nltk.download("stopwords")
nltk.download("punkt")
```

---

### 🔹 Step 2: Basic Stopwords Removal

```python
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

sentence = "The children were running fast in the park"

stop_words = set(stopwords.words("english"))

tokens = word_tokenize(sentence)
filtered_words = [w for w in tokens if w.lower() not in stop_words]

print("Original Tokens:", tokens)
print("After Stopwords Removal:", filtered_words)
```

### 📤 Output

```
Original Tokens: ['The', 'children', 'were', 'running', 'fast', 'in', 'the', 'park']
After Stopwords Removal: ['children', 'running', 'fast', 'park']
```

📌 দেখুন:

* **the, were, in** → বাদ গেছে
* meaningful শব্দগুলো রয়ে গেছে

---

## 🔸 Stopwords Removal + Cleaning (Recommended)

```python
filtered_words = [
    w.lower() for w in tokens
    if w.isalpha() and w.lower() not in stop_words
]

print(filtered_words)
```

### 📤 Output

```
['children', 'running', 'fast', 'park']
```

📌 এখানে:

* lowercase করা হয়েছে
* punctuation বাদ গেছে

---

## 🔸 Custom Stopwords (নিজের মতো করে)

```python
custom_stopwords = stop_words.union({"fast", "park"})

filtered_words = [
    w.lower() for w in tokens
    if w.lower() not in custom_stopwords
]

print(filtered_words)
```

### 📤 Output

```
['children', 'running']
```

📌 নিজের problem অনুযায়ী stopwords বাড়ানো যায়।

---

## 🔸 Stopwords + Lemmatization (Mini Pipeline)

```python
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

filtered_lemmas = [
    lemmatizer.lemmatize(w)
    for w in filtered_words
]

print(filtered_lemmas)
```

### 📤 Output

```
['child', 'running']
```

---

## 🔚 সংক্ষেপে মনে রাখুন

* **Stopwords = low-meaning frequent words**
* সব NLP task-এ remove করা উচিত নয়
* NLTK-তে built-in list আছে
* Custom stopwords যোগ করা যায়

---

### 🧠 Exam-ready One-liner

> Stopwords are commonly used words that are removed during text preprocessing to reduce noise and improve model performance.

---

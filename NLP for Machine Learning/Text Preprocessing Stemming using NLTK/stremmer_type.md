## 🔹 **PorterStemmer** ও **SnowballStemmer** — *বাংলায় সহজ ও তুলনামূলক ব্যাখ্যা*

![Image](https://vijinimallawaarachchi.com/wp-content/uploads/2017/05/porterstemmer.png?w=772)

![Image](https://media.geeksforgeeks.org/wp-content/uploads/20250717111850680663/popular_stemming_algorithms.webp)

![Image](https://dezyre.gumlet.io/images/blog/stemming-in-nlp/Types_of_Stemming.png?dpr=2.6\&w=376)

এই দুইটিই **NLTK**-এর জনপ্রিয় **Stemming Algorithm**।

---

## 🔸 1️⃣ PorterStemmer কী?

**PorterStemmer** হলো NLP-তে ব্যবহৃত **সবচেয়ে পুরোনো ও জনপ্রিয় stemmer**।

### 🔹 বৈশিষ্ট্য

* Rule-based
* দ্রুত কাজ করে
* Grammar নিয়ে খুব একটা মাথা ঘামায় না
* কখনো কখনো শব্দ কেটে অদ্ভুত root বানায়

### 🔹 উদাহরণ

```python
from nltk.stem import PorterStemmer

ps = PorterStemmer()
print(ps.stem("studies"))
print(ps.stem("studying"))
print(ps.stem("running"))
```

#### 🔸 Output

```
studi
studi
run
```

📌 এখানে **study → studi** হয়েছে, যা বাস্তব শব্দ না — কিন্তু ML মডেলের জন্য সমস্যা না।

---

## 🔸 2️⃣ SnowballStemmer কী?

**SnowballStemmer** হলো **PorterStemmer-এর উন্নত (improved) version**।

### 🔹 বৈশিষ্ট্য

* বেশি accurate
* একাধিক ভাষা সাপোর্ট করে (English, French, German ইত্যাদি)
* কম aggressive
* Production-level NLP-তে বেশি ব্যবহৃত

### 🔹 উদাহরণ

```python
from nltk.stem import SnowballStemmer

ss = SnowballStemmer("english")
print(ss.stem("studies"))
print(ss.stem("studying"))
print(ss.stem("running"))
```

#### 🔸 Output

```
studi
studi
run
```

📌 অনেক ক্ষেত্রে output Porter-এর মতোই,
কিন্তু complex শব্দে Snowball বেশি stable।

---

## 🔸 Porter vs Snowball — পার্থক্য টেবিল

| বিষয়             | PorterStemmer | SnowballStemmer        |
| ---------------- | ------------- | ---------------------- |
| Accuracy         | মাঝারি        | বেশি                   |
| Speed            | দ্রুত         | সামান্য ধীর            |
| Language Support | শুধু English  | বহু ভাষা               |
| Aggressiveness   | মাঝারি        | Balanced               |
| Recommendation   | শেখার জন্য    | বাস্তব প্রজেক্টের জন্য |

---

## 🔸 একই শব্দে তুলনা

```python
words = ["generously", "generation", "running"]

for w in words:
    print(w,
          PorterStemmer().stem(w),
          SnowballStemmer("english").stem(w))
```

📌 Snowball অনেক সময় **অপ্রয়োজনীয় কাটছাঁট কম করে**।

---

## 🔸 কখন কোনটা ব্যবহার করবেন?

### ✅ PorterStemmer ব্যবহার করুন যখন:

* NLP শেখা শুরু করছেন
* ছোট প্রজেক্ট
* দ্রুত preprocessing দরকার

### ✅ SnowballStemmer ব্যবহার করুন যখন:

* Real-world ML / NLP প্রজেক্ট
* Multilingual text
* তুলনামূলক ভালো accuracy দরকার

---

## 🔚 এক লাইনে মনে রাখুন

* **PorterStemmer = Classic + Fast**
* **SnowballStemmer = Improved + Professional**

---


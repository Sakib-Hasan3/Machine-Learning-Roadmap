---

# 🔹 03. Tokenisation and Basic Terminologies (NLP)

![Image](https://miro.medium.com/1%2AUhfwmhMN9sdfcWIbO5_tGg.jpeg)

![Image](https://miro.medium.com/1%2AN1YsdSJihlzJrvYBUDI-_A.jpeg)

![Image](https://miro.medium.com/1%2AVzhvZVKGVGynlsU0AZZQww.jpeg)

---

## 🧠 Tokenisation কী?

**Tokenisation** হলো
👉 **একটি বড় Text-কে ছোট ছোট অংশে ভেঙে ফেলা**,
যেগুলোকে বলা হয় **Token**।

সহজ কথায়—

> **Sentence → Word এ ভাগ করা = Tokenisation**

---

## ✂️ উদাহরণ দিয়ে বোঝি

### 🔹 Sentence:

```
"I love Natural Language Processing"
```

### 🔹 Tokenisation করার পর:

```
["I", "love", "Natural", "Language", "Processing"]
```

এখানে প্রতিটা শব্দই একটি **Token**।

---

## 🧩 Token কী?

👉 **Token = Text-এর সবচেয়ে ছোট meaningful unit**

Token হতে পারে:

* একটি word
* একটি number
* একটি punctuation
* এমনকি একটি emoji 😄

---

## 🧪 Tokenisation-এর প্রকারভেদ

### 1️⃣ Word Tokenisation

Sentence কে word-এ ভাঙা।

**উদাহরণ**

```
"Data Science is fun"
→ ["Data", "Science", "is", "fun"]
```

---

### 2️⃣ Sentence Tokenisation

Paragraph কে sentence-এ ভাঙা।

**উদাহরণ**

```
"I love NLP. It is very useful."
→ ["I love NLP.", "It is very useful."]
```

---

### 3️⃣ Character Tokenisation

Text কে character এ ভাঙা।

**উদাহরণ**

```
"NLP"
→ ["N", "L", "P"]
```

📌 সাধারণত Deep Learning-এ ব্যবহার হয়।

---

## 🔤 NLP-এর Basic Terminologies (Must Know)

---

### 🔹 1. Corpus

👉 **Corpus = অনেকগুলো Text document-এর collection**

**উদাহরণ**

* সব movie reviews একসাথে
* সব news article একসাথে

---

### 🔹 2. Document

👉 **Document = Corpus-এর একটি single text**

**উদাহরণ**

* একটি news article
* একটি review

---

### 🔹 3. Vocabulary

👉 **Vocabulary = Corpus-এর সব unique word**

**উদাহরণ**

```
Corpus = ["I love NLP", "I love ML"]
Vocabulary = ["I", "love", "NLP", "ML"]
```

---

### 🔹 4. Stop Words

👉 **Stop words = খুব common শব্দ যেগুলো meaning কম দেয়**

**উদাহরণ**

* is
* am
* are
* the
* a
* an

📌 NLP-তে এগুলো অনেক সময় remove করা হয়।

---

### 🔹 5. Stemming

👉 **Word-এর root বের করা (ভাঙা-ভাঙা root)**

**উদাহরণ**

```
playing → play
played → play
```

📌 Root সবসময় correct word নাও হতে পারে।

---

### 🔹 6. Lemmatization

👉 **Grammatically correct root word বের করা**

**উদাহরণ**

```
better → good
running → run
```

📌 Stemming-এর চেয়ে better কিন্তু slow।

---

### 🔹 7. Punctuation

👉 Comma, dot, ?, ! ইত্যাদি

NLP-তে অনেক সময় remove করা হয়:

```
Hello!!! → Hello
```

---

### 🔹 8. Lowercasing

👉 সব text ছোট হাতের করা

```
"NLP Is FUN"
→ "nlp is fun"
```

---

### 🔹 9. Noise

👉 Text-এর unnecessary অংশ

**উদাহরণ**

* URLs
* Emojis
* Special characters

---

## 🔁 NLP Preprocessing Pipeline (সহজ Flow)

![Image](https://media.licdn.com/dms/image/v2/D5612AQH-AcQSsJT7Wg/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1722023278165?e=2147483647\&t=W9khkDqas5ZQKLvmpUEDf4hA8PB61BDpvfN1ahfcI-M\&v=beta)

![Image](https://miro.medium.com/1%2AVzhvZVKGVGynlsU0AZZQww.jpeg)

```
Raw Text
↓
Lowercase
↓
Tokenisation
↓
Remove Stopwords
↓
Stemming / Lemmatization
↓
Clean Text
```

---

## 🎯 কেন Tokenisation এত গুরুত্বপূর্ণ?

কারণ—

* Computer text বুঝে না
* Token ছাড়া ML কাজ করে না
* NLP-এর সব algorithm token-এর উপর কাজ করে

📌 **Tokenisation = NLP-এর দরজা**

---

## 🧠 One-Line Summary

> **Tokenisation হলো NLP-এর প্রথম ও সবচেয়ে গুরুত্বপূর্ণ ধাপ, যেখানে text-কে meaningful ছোট অংশে ভাঙা হয়।**

---


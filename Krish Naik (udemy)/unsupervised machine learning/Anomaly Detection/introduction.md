![Image](https://www.researchgate.net/profile/Ilias-Gerostathopoulos/publication/336874543/figure/fig1/AS%3A883856525783044%401587739225926/Overview-of-anomaly-detection-process.ppm)

![Image](https://www.researchgate.net/publication/384471832/figure/fig2/AS%3A11431281281193716%401727752864613/Three-time-series-anomaly-types-Types-of-Anomalies-Point-Contextual-Collective-Figure.jpg)

![Image](https://www.researchgate.net/publication/371321853/figure/tbl1/AS%3A11431281165771930%401686065720295/Comparison-of-different-anomaly-detection-methods.png)

![Image](https://www.researchgate.net/publication/326734364/figure/tbl2/AS%3A667871277486084%401536244329145/Comparison-of-anomaly-detection-training-methods.png)

## 🔎 **Anomaly Detection — সহজ ও সম্পূর্ণ পরিচিতি**

**Anomaly Detection** হলো এমন একটি পদ্ধতি যেখানে ডেটার ভেতর থেকে **স্বাভাবিক প্যাটার্নের বাইরে থাকা অস্বাভাবিক (rare) ঘটনা/পয়েন্ট** খুঁজে বের করা হয়।

---

## 🧠 এক লাইনের ধারণা

> **যা বেশিরভাগ ডেটার মতো না—সেটাই Anomaly।**

---

## 1️⃣ Anomaly-এর ধরন (খুব গুরুত্বপূর্ণ)

### 🔹 **Point Anomaly**

* একক পয়েন্ট অস্বাভাবিক
* উদাহরণ: হঠাৎ খুব বড় ব্যাংক ট্রান্স্যাকশন

### 🔹 **Contextual Anomaly**

* নির্দিষ্ট প্রেক্ষাপটে অস্বাভাবিক
* উদাহরণ: শীতে 40°C তাপমাত্রা

### 🔹 **Collective Anomaly**

* এককভাবে স্বাভাবিক, কিন্তু **একসাথে অস্বাভাবিক**
* উদাহরণ: সার্ভারে একসাথে অস্বাভাবিক ট্রাফিক স্পাইক

---

## 2️⃣ কেন Anomaly Detection দরকার?

* 💳 Fraud detection
* 🖥️ System / Network intrusion
* 🏭 Sensor fault detection
* 🏥 Medical abnormality
* 📈 Market manipulation

---

## 3️⃣ Anomaly Detection করার প্রধান পদ্ধতি

### 🔸 **Statistical Methods**

* Mean–Std, Z-score, IQR
* ছোট ও সহজ ডেটার জন্য

### 🔸 **Distance-based**

* kNN distance, LOF
* “বাকি ডেটা থেকে কত দূরে?”

### 🔸 **Density-based**

* DBSCAN
* ঘন জায়গা = normal, sparse = anomaly

### 🔸 **Isolation-based**

* **Isolation Forest** ⭐
* “আলাদা করতে কতটা সহজ?”

### 🔸 **Model-based**

* One-Class SVM
* Autoencoder (DL)

---

## 4️⃣ জনপ্রিয় অ্যালগরিদম তুলনা (Intuition)

| Algorithm        | কী দেখে              | কখন ভালো             |
| ---------------- | -------------------- | -------------------- |
| Z-score          | Mean থেকে দূরত্ব     | Simple numeric       |
| DBSCAN           | Density              | Noise-heavy data     |
| LOF              | Local density        | Local anomalies      |
| Isolation Forest | Isolation speed      | High-dim, large data |
| Autoencoder      | Reconstruction error | Complex patterns     |

---

## 5️⃣ Isolation Forest কেন জনপ্রিয়?

* K লাগে না
* Distance লাগে না
* High-dimensional data-তে ভালো
* দ্রুত ও scalable

---

## 6️⃣ Output কীভাবে আসে?

* **Label**: Normal / Anomaly
* বা **Score**: যত বেশি → তত বেশি anomaly

---

## 7️⃣ সাধারণ ভুল ❌

* Feature scaling না করা
* Context ignore করা
* Threshold ভুল ধরা
* Imbalanced nature ভুলে যাওয়া

---

## 🧠 সহজ Analogy

ভিড়ের মধ্যে **অন্যরকম পোশাক পরা মানুষ**—চোখে পড়বে।
👉 Anomaly Detection ঠিক সেটাই করে।

---

## 🔑 Exam / Interview One-liner

> **Anomaly detection identifies rare and unusual patterns that significantly deviate from the majority of the data.**

---


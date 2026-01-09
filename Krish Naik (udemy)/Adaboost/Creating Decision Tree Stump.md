## 🌳 Creating a **Decision Tree Stump**

*(AdaBoost-এর সবচেয়ে গুরুত্বপূর্ণ building block — বাংলায় সম্পূর্ণ ব্যাখ্যা)*

---

## 1️⃣ Decision Tree Stump কী?

**Decision Tree Stump** হলো একটি **খুবই ছোট Decision Tree** যেখানে:

* ✅ মাত্র **১টি feature**
* ✅ মাত্র **১টি split**
* ✅ মাত্র **১টি decision rule**
* ❌ কোনো child split নেই (depth = 1)

📌 একে বলা হয় **Weak Learner**, কারণ একা একা এটা খুব শক্তিশালী না
কিন্তু **AdaBoost-এর জন্য এটিই perfect**।

---

## 2️⃣ Decision Stump কেন AdaBoost-এ ব্যবহার হয়?

AdaBoost-এর মূল ধারণা:

> “অনেক দুর্বল মডেল + সঠিক weight = শক্তিশালী মডেল”

Decision stump:

* খুব সহজ
* দ্রুত train হয়
* bias বেশি, variance কম
* sequential boosting-এর জন্য আদর্শ

👉 তাই AdaBoost প্রায় সবসময় **decision stump ব্যবহার করে**

---

## 3️⃣ Decision Tree vs Decision Stump

| বিষয়         | Decision Tree | Decision Stump |
| ------------ | ------------- | -------------- |
| Depth        | যেকোনো        | মাত্র 1        |
| Split সংখ্যা | অনেক          | 1              |
| Complexity   | বেশি          | খুব কম         |
| Overfitting  | হতে পারে      | প্রায় না       |
| AdaBoost     | ❌             | ✅              |

---

## 4️⃣ Decision Stump কিভাবে তৈরি হয়? (Concept)

ধরা যাক আমাদের dataset:

| Age | Income | Buy (Label) |
| --- | ------ | ----------- |
| 22  | Low    | No          |
| 35  | High   | Yes         |
| 40  | Medium | Yes         |
| 28  | Low    | No          |

### Step 1️⃣ একটি feature বেছে নেওয়া

ধরা যাক → **Age**

---

### Step 2️⃣ একটি threshold ঠিক করা

উদাহরণ:

```
Age ≤ 30 ?
```

---

### Step 3️⃣ দুইটা leaf তৈরি

* Left leaf → Yes / No
* Right leaf → Yes / No

📌 যে label বেশি থাকে, সেটাই prediction

---

## 5️⃣ Decision Stump কীভাবে “best” হয়?

Stump নির্বাচন করা হয় **Error কমানোর ভিত্তিতে**
AdaBoost-এ এটি হয় **weighted error** দিয়ে।

### 🔹 Weighted Error Formula:

```
Error = Σ (weight_i × wrong_prediction_i)
```

👉 যেই stump-এর error সবচেয়ে কম, সেটাই নির্বাচিত হয়

---

## 6️⃣ AdaBoost-এ Decision Stump তৈরি করার ধাপ

### 🔹 Step 1: সব data weight দিয়ে শুরু

```
w1 = w2 = ... = wn = 1/n
```

---

### 🔹 Step 2: প্রতিটি feature নিয়ে চেষ্টা

* Feature 1 → threshold test
* Feature 2 → threshold test
* …

---

### 🔹 Step 3: প্রতিটি stump-এর error বের করা

---

### 🔹 Step 4: যেটার error সবচেয়ে কম → সেটাই stump

---

## 7️⃣ Decision Stump-এর Mathematical Form

একটি stump মূলত এই form-এর:

```
h(x) = 
  +1  if x_j ≤ θ
  -1  otherwise
```

যেখানে:

* `x_j` = chosen feature
* `θ` = threshold

---

## 8️⃣ Decision Stump + AdaBoost (Connection)

AdaBoost-এ:
1️⃣ Stump train হয়
2️⃣ Error বের হয়
3️⃣ Alpha হিসাব হয়
4️⃣ Data weight update হয়

📌 প্রতিটি round-এ **একটি নতুন stump**

---

## 9️⃣ Python দিয়ে Decision Stump তৈরি (Sklearn)

```python
from sklearn.tree import DecisionTreeClassifier

stump = DecisionTreeClassifier(
    max_depth=1,
    criterion='gini'
)

stump.fit(X_train, y_train)
```

👉 `max_depth=1` মানেই Decision Stump

---

## 🔟 Interview / Viva প্রশ্নোত্তর (Bangla)

**Q1:** Decision stump কেন weak learner?
👉 কারণ এতে মাত্র একটি split থাকে

**Q2:** AdaBoost কি deep tree ব্যবহার করে?
👉 না, সাধারণত stump ব্যবহার করে

**Q3:** Decision stump কিভাবে select হয়?
👉 Minimum weighted error-এর ভিত্তিতে

**Q4:** Stump overfitting করে?
👉 না, কারণ model খুব simple

---

## 🧠 মনে রাখার shortcut

> **Decision Stump = One feature + One split + One rule**

---



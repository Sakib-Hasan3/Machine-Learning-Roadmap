
---

# 🎯 Logistic Regression — **OVR (One-Vs-Rest / One-Vs-All)** কী?

যখন Logistic Regression দিয়ে **multi-class classification** করতে হয়, তখন সবচেয়ে সহজ এবং জনপ্রিয় পদ্ধতি হলো **OVR**।

এটি ব্যবহার হয় যখন ক্লাস সংখ্যা ≥ 3 এবং আমরা Binary Logistic Regression-এর শক্তিকে ব্যবহার করে multi-class করতে চাই।

### উদাহরণ:

ক্লাস = **A, B, C**

OVR আলাদা করে ৩টি Logistic Regression model তৈরি করবে:

* Model 1 → A vs (B, C)
* Model 2 → B vs (A, C)
* Model 3 → C vs (A, B)

শেষে যেই ক্লাসের probability সবচেয়ে বেশি → সেটাই prediction।

---

![Image](https://media.geeksforgeeks.org/wp-content/uploads/20230330170812/Screenshot-2023-03-30-170740.png?utm_source=chatgpt.com)

![Image](https://miro.medium.com/v2/resize%3Afit%3A788/1%2Au9Kj9xXuGXiu8RJqwCGtig.png?utm_source=chatgpt.com)

---

# 🧠 কেন OVR প্রয়োজন?

Binary Logistic Regression শুধু **দুই ক্লাস** করতে পারে।

OVR সেই Binary মডেলগুলোর শক্তিকে ব্যবহার করে multi-class classification তৈরি করে:

[
K \text{ classes } \Rightarrow K \text{ binary classifiers}
]

---

# 🔥 OVR কীভাবে কাজ করে? (Step-by-Step)

ধরুন ক্লাস = 3 → {A, B, C}

---

## **1️⃣ Step — প্রতিটি ক্লাসের জন্য Binary Model তৈরি করা**

### Model 1: A vs Not-A

* A → 1
* B, C → 0

### Model 2: B vs Not-B

* B → 1
* A, C → 0

### Model 3: C vs Not-C

* C → 1
* A, B → 0

Thus → 3 logistic regression models।

---

## **2️⃣ Step — প্রতিটি মডেল একটি probability দেয়**

Example prediction for a sample:

| Model     | Probability |
| --------- | ----------- |
| A vs rest | 0.10        |
| B vs rest | 0.62        |
| C vs rest | 0.28        |

---

## **3️⃣ Step — Highest Probability = Predicted Class**

Prediction = **B**

---

# 📌 Mathematical View (OVR)

For a test sample (x):

[
P(y=k|x) = \sigma(w_k^T x + b_k)
]

Prediction:

[
\hat{y} = \arg\max_k P(y=k|x)
]

এখানে (K) = total number of classes।

---

# 🔍 OVR vs Softmax (Multinomial Logistic Regression)

| বিষয়                 | OVR                                 | Multinomial (Softmax) |
| -------------------- | ----------------------------------- | --------------------- |
| Number of Models     | K binary models                     | One model             |
| Complexity           | Simple                              | More complex          |
| Output probabilities | Independent probabilities           | Sum to 1              |
| Best use case        | High-dimensional sparse data (text) | Small/medium datasets |
| Training time        | Faster                              | Slower                |
| Accuracy             | Lower (some cases)                  | Higher                |

Softmax model mathematically superior, কিন্তু OVR computation-wise সহজ এবং scalable।

---

# 📚 বাস্তব উদাহরণ (Bangla)

ধরুন আমরা ফল classify করছি:

ক্লাস = {Apple, Banana, Mango}

তাহলে OVR তৈরি করে:

### Model 1: Apple vs Others

### Model 2: Banana vs Others

### Model 3: Mango vs Others

Prediction এর output:

* Apple → 0.25
* Banana → 0.15
* Mango → 0.60

তবে ক্লাস = **Mango**

---

# 🧪 Python Example (sklearn) — OVR Mode

Sklearn-এ Logistic Regression default ভাবে OVR করে।

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

model = LogisticRegression(multi_class='ovr', solver='liblinear')
model.fit(X, y)

print(model.predict([[5.2, 3.4, 1.5, 0.2]]))
```

যদি multi_class='ovr' না দিই → কিছু solver automatically OVR নেয়।

---

# ⭐ OVR-এর সুবিধা ও অসুবিধা

## ✔ সুবিধা

* Simple to implement
* Training fast
* Binary Logistic Regression reuse করা যায়
* High-dimensional sparse data (like text classification)-এ খুব কার্যকর
* Debugging সহজ (কোন ক্লাসে সমস্যা হচ্ছে বোঝা যায়)

## ❌ অসুবিধা

* Probabilities sum to 1 হয় না (softmax-এর মতো proper probability distribution না)
* কিছু সময় overlapping decision boundary তৈরি হতে পারে
* Multinomial logistic regression তুলনায় accuracy কিছু কম হয়

---

# 🧠 Summary (Short Notes)

* OVR = Multi-class classification-এর জন্য K binary logistic regressions
* প্রতিটি model predict করে P(class=k | x)
* Final prediction = highest probability
* Simple, fast, interpretable
* কিন্তু softmax-এর মতো mathematically elegant নয়

---



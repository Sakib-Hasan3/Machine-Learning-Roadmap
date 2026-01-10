![Image](https://miro.medium.com/1%2AREUu0LJytEt6kIOFQeB0Tw.png)

![Image](https://media.geeksforgeeks.org/wp-content/uploads/20250903173429506712/des.webp)

![Image](https://www.researchgate.net/publication/351542039/figure/fig1/AS%3A11431281172877200%401688685833363/Flow-diagram-of-gradient-boosting-machine-learning-method-The-ensemble-classifiers.png)

![Image](https://www.analytixlabs.co.in/wp-content/uploads/2022/10/Artboard-1-copy-11-100.jpg)

## 🔰 Gradient Boosting Classifier – Training Process (বাংলায় বিস্তারিত)

### 🔹 Gradient Boosting Classifier কী?

**Gradient Boosting Classifier** হলো একটি **Ensemble Classification algorithm**, যেখানে অনেকগুলো **দুর্বল classifier (weak learners)** ধাপে ধাপে (sequentially) ট্রেন করে একটি **শক্তিশালী classifier** তৈরি করা হয়।

📌 এখানে প্রতিটি নতুন মডেল আগের মডেলের **ভুল (error / residual)** কমানোর চেষ্টা করে।

---

## 🧠 Gradient Boosting Classifier Training – Step by Step

### 🧩 Step 1: Initial Model (শুরুর মডেল)

Classification–এ শুরুতে একটি **constant prediction** নেওয়া হয়।

* Binary classification হলে:

  * সাধারণত **log-odds (logit)** দিয়ে শুরু হয়
* সহজভাবে ভাবলে:

  * শুরুতে সবার জন্য একই prediction

👉 উদাহরণ:
ধরি ক্লাস = {0, 1}
শুরুতে model বলে: “সবাই 0 হওয়ার সম্ভাবনা 50%”

---

### 🧩 Step 2: Loss Function নির্ধারণ

Classification–এ সবচেয়ে বেশি ব্যবহৃত loss:

* **Log Loss (Binary Cross Entropy)**

[
Loss = -[y\log(p) + (1-y)\log(1-p)]
]

📌 Gradient Boosting এখানে **loss function minimize** করতে শেখে।

---

### 🧩 Step 3: Pseudo-Residual (Gradient) গণনা

এটাই Gradient Boosting–এর মূল ধাপ 🔥

[
\text{Residual} = y - p
]

👉 এখানে:

* (y) = আসল label
* (p) = model-এর predicted probability

📌 এই residual আসলে loss function-এর **negative gradient**।

---

### 🧩 Step 4: Weak Learner ট্রেন করা

একটি **Decision Tree Classifier (shallow tree)** ট্রেন করা হয় এই residual-এর ওপর।

* Tree শেখে:
  👉 “কোন feature দেখে error বেশি হচ্ছে?”

---

### 🧩 Step 5: Prediction Update (Model Update)

Model আপডেট হয় এভাবে:

[
F_{new}(x) = F_{old}(x) + \eta \times h(x)
]

যেখানে:

* (h(x)) = নতুন tree-এর output
* (\eta) = **Learning Rate**

---

### 🧩 Step 6: Probability Update

Updated score থেকে আবার probability বের করা হয়:

[
p = \frac{1}{1 + e^{-F(x)}}
]

---

### 🧩 Step 7: Iteration (Repeat)

এই ধাপগুলো বারবার চলে:

* Residual হিসাব
* Tree train
* Model update

👉 যতবার `n_estimators`, ততবার

---

### 🧩 Step 8: Final Prediction

শেষে:

* Probability ≥ threshold → Class 1
* Probability < threshold → Class 0

---

## 🔹 Training–এর Intuition (সহজ ভাষায়)

> ❝ প্রতিবার আমি শুধু সেই জায়গায় শিখব, যেখানে আমি ভুল করেছি ❞

Gradient Boosting Classifier:

* আগের ভুল sample–গুলোতে বেশি ফোকাস করে
* ধীরে ধীরে decision boundary ঠিক করে

---

## 🔹 কেন Gradient Boosting Classifier এত শক্তিশালী?

✔ Non-linear boundary শিখতে পারে
✔ Complex feature interaction ধরতে পারে
✔ Bias কমায়
✔ Probability output দেয়

---

## 🔹 Important Hyperparameters (Training Control)

| Parameter       | কাজ            |
| --------------- | -------------- |
| `n_estimators`  | কয়টা tree      |
| `learning_rate` | শেখার গতি      |
| `max_depth`     | tree-এর গভীরতা |
| `subsample`     | data sampling  |
| `loss`          | `log_loss`     |

---

## 🔹 Overfitting কিভাবে কমাবেন?

* Learning rate ছোট রাখুন
* Tree depth কমান
* `subsample < 1.0` ব্যবহার করুন
* Early stopping ব্যবহার করুন

---

## 🔹 এক লাইনে সারাংশ

**Gradient Boosting Classifier Training = Initial guess → Gradient (error) শেখা → Tree যোগ → Probability refine**

---

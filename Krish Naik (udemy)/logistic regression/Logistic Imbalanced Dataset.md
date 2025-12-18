

---

# 📌 Logistic Regression ও Imbalanced Dataset (সম্পূর্ণ গাইড – বাংলা)

## 1️⃣ Logistic Regression কী?

**Logistic Regression** হলো একটি **Supervised Classification Algorithm**
যেটা সাধারণত **Binary Classification** সমস্যা সমাধানে ব্যবহৃত হয়।

### উদাহরণ:

* Email → Spam / Not Spam
* Loan → Default / Non-default
* Disease → Yes / No

### Logistic Regression কীভাবে কাজ করে?

* এটি **Sigmoid Function** ব্যবহার করে
* আউটপুট দেয় **0 থেকে 1** এর মধ্যে Probability

#### Sigmoid Formula:

[
\sigma(z) = \frac{1}{1 + e^{-z}}
]

---

## 2️⃣ Imbalanced Dataset কী?

যখন কোনো Dataset-এ **একটি Class অন্য Class-এর তুলনায় অনেক বেশি বা কম হয়**, তখন তাকে **Imbalanced Dataset** বলে।

### উদাহরণ:

| Class        | Count |
| ------------ | ----- |
| 0 (Negative) | 9,500 |
| 1 (Positive) | 500   |

➡️ এখানে **Positive class মাত্র 5%** → Dataset Imbalanced

---

## 3️⃣ কেন Imbalanced Dataset সমস্যা তৈরি করে?

### ❌ Accuracy Trap

ধরা যাক:

* 95% Data = Class 0
* Model সবকিছু Class 0 বলল

👉 Accuracy = **95%**
👉 কিন্তু Model একটাও Class 1 ধরতে পারলো না!

➡️ তাই **Accuracy এখানে Misleading**

---

## 4️⃣ Logistic Regression এ Imbalance হলে কী সমস্যা হয়?

* Model **Majority Class** শেখে
* **Minority Class Ignore** করে
* Decision Boundary সরে যায়
* False Negative বেড়ে যায় (বিশেষ করে Medical / Fraud Case-এ ভয়ংকর)

---

## 5️⃣ Imbalanced Dataset চিহ্নিত করার উপায়

### 🔍 Class Distribution দেখুন

```python
y.value_counts()
```

### 📊 Visualization

* Bar Plot
* Pie Chart

---

## 6️⃣ Accuracy কেন ব্যবহার করা যাবে না?

### ❌ ভুল Metric:

* Accuracy

### ✅ সঠিক Metric:

* Precision
* Recall
* F1-score
* ROC-AUC
* Confusion Matrix

---

## 7️⃣ Confusion Matrix (খুব গুরুত্বপূর্ণ)

|          | Predicted 0 | Predicted 1 |
| -------- | ----------- | ----------- |
| Actual 0 | TN          | FP          |
| Actual 1 | FN          | TP          |

### গুরুত্বপূর্ণ টার্ম:

* **Recall = TP / (TP + FN)**
* **Precision = TP / (TP + FP)**

➡️ Imbalanced Dataset-এ **Recall বেশি গুরুত্বপূর্ণ**

---

## 8️⃣ Logistic Regression এ Imbalance Handle করার উপায়

---

### 🔹 1. Class Weight ব্যবহার করা (সবচেয়ে জনপ্রিয়)

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(class_weight='balanced')
```

🔸 এটি Minority Class-কে বেশি গুরুত্ব দেয়

---

### 🔹 2. Manual Class Weight

```python
model = LogisticRegression(class_weight={0:1, 1:5})
```

➡️ Class 1 কে 5 গুণ গুরুত্ব

---

### 🔹 3. Oversampling (Minority বাড়ানো)

#### SMOTE:

```python
from imblearn.over_sampling import SMOTE

smote = SMOTE()
X_res, y_res = smote.fit_resample(X, y)
```

✔️ Minority Class Artificial Data তৈরি করে

---

### 🔹 4. Undersampling (Majority কমানো)

```python
from imblearn.under_sampling import RandomUnderSampler
```

❌ Data Loss হতে পারে

---

### 🔹 5. Threshold Tuning

ডিফল্ট Threshold = 0.5
Imbalanced Dataset-এ Threshold কমানো হয়

```python
y_pred = (model.predict_proba(X)[:,1] > 0.3).astype(int)
```

---

## 9️⃣ ROC Curve & AUC

* **ROC Curve** → TPR vs FPR
* **AUC** → Model কতটা ভালো

➡️ Imbalanced Dataset-এ **ROC-AUC খুব গুরুত্বপূর্ণ Metric**

---

## 🔟 Precision vs Recall – কোনটা বেশি দরকার?

| Case             | Priority  |
| ---------------- | --------- |
| Cancer Detection | Recall    |
| Fraud Detection  | Recall    |
| Spam Filter      | Precision |
| Recommendation   | Precision |

---

## 1️⃣1️⃣ Logistic Regression Cost Function (Imbalanced Impact)

Logistic Regression ব্যবহার করে:
**Log Loss (Cross Entropy)**

Imbalanced Dataset-এ:

* Majority Class Loss Dominant হয়
* Minority Class Ignore হয়

➡️ Class Weight Loss সমাধান করে

---

## 1️⃣2️⃣ বাস্তব জীবনের উদাহরণ

### 🏥 Medical Diagnosis

* 1% মানুষ রোগী
* Disease Miss করলে বিপদ
	➡️ Recall বেশি দরকার

### 💳 Fraud Detection

* 0.1% Fraud
	➡️ Imbalanced Dataset অত্যন্ত গুরুতর

---

## 1️⃣3️⃣ Best Practice Checklist ✅

✔️ Accuracy Ignore করুন
✔️ Confusion Matrix দেখুন
✔️ Class Weight ব্যবহার করুন
✔️ SMOTE Try করুন
✔️ Threshold Tune করুন
✔️ ROC-AUC দেখুন

---

## 1️⃣4️⃣ Interview Important Points ⭐

* Logistic Regression Imbalance handle করতে পারে না by default
* Class Weight সবচেয়ে সহজ সমাধান
* Accuracy misleading
* Recall/Precision গুরুত্বপূর্ণ
* Threshold tuning খুব কার্যকর

---

## 1️⃣5️⃣ Short Summary (Exam Friendly)

> Imbalanced Dataset হলো এমন Dataset যেখানে Class Distribution অসম। Logistic Regression এতে Majority Class-এ Bias তৈরি করে। এই সমস্যা সমাধানে Class Weight, SMOTE, Undersampling, Threshold Tuning এবং সঠিক Evaluation Metric ব্যবহার করতে হয়।

---



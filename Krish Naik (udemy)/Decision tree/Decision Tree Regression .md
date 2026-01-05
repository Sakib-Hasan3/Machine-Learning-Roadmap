# Decision Tree Regression

![Image](https://towardsdatascience.com/wp-content/uploads/2021/11/16RMrFGwU-qH4nHW89xc0Xw.jpeg)

![Image](https://cdn-proxy.slickplan.com/wp-content/uploads/2025/08/types-of-decision-trees-classification-vs-regression.jpg)

![Image](https://scikit-learn.org/1.5/_images/sphx_glr_plot_tree_regression_001.png)

---

# 🌳 Decision Tree Regression

## 📌 Decision Tree Regression কী?

**Decision Tree Regression** হলো এমন একটি মডেল যা **continuous (সংখ্যাগত) মান predict** করতে ব্যবহৃত হয়।

📊 উদাহরণ:

- বাড়ির দাম (House Price)
- তাপমাত্রা
- বেতন
- স্টক প্রাইস (approx.)

---

## 🧠 Decision Tree Regression কীভাবে কাজ করে?

Decision Tree Regression ডেটাকে **বারবার ভাগ (split)** করে এমনভাবে, যাতে প্রতিটি ভাগে থাকা target value গুলো **যতটা সম্ভব কাছাকাছি হয়**।

👉 প্রতিটি **leaf node** একটি **সংখ্যাগত মান** দেয় (সাধারণত mean)।

---

## 🔁 Working Process (Step-by-Step)

1️⃣ সম্পূর্ণ dataset নেওয়া হয়

2️⃣ এমন feature ও split point বেছে নেওয়া হয়, যাতে error সবচেয়ে কম হয়

3️⃣ Dataset দুই ভাগে ভাগ হয়

4️⃣ একই প্রক্রিয়া recursively চলে

5️⃣ Leaf node এ গিয়ে prediction দেওয়া হয়

---

## 🎯 Split করার Criterion (Regression এ)

### ❌ Entropy / Gini ব্যবহার হয় না

Regression এ ব্যবহৃত হয় ⬇️

### ✅ Mean Squared Error (MSE)

```
MSE = (Actual − Predicted)² এর গড়

```

### ✅ Mean Absolute Error (MAE)

```
MAE = |Actual − Predicted| এর গড়

```

### ✅ Variance Reduction (সবচেয়ে বেশি ব্যবহৃত)

Split এমনভাবে করা হয় যাতে:

> Variance সবচেয়ে বেশি কমে
> 

---

## 🧩 Leaf Node এ কী থাকে?

Leaf node এ থাকে:

- ঐ node-এর সব target value-এর **mean (average)**

📌 Prediction = Leaf node-এর mean value

---

## 🖼️ Simple Example

ধরা যাক:

- Feature: House Size (sqft)
- Target: House Price

Tree এমনভাবে split করবে:

```
Size < 1000 → Avg Price = 40 lakh
Size ≥ 1000 → Avg Price = 80 lakh

```

---

## 🆚 Decision Tree Regression vs Classification

| বিষয় | Regression | Classification |
| --- | --- | --- |
| Output | Continuous value | Class / Label |
| Split Metric | MSE / Variance | Gini / Entropy |
| Leaf Output | Mean value | Class |
| Example | Price, Salary | Spam / Not Spam |

---

## ⚠️ Overfitting Problem

Decision Tree Regression খুব সহজেই **overfitting** করে।

কারণ:

- Tree খুব গভীর হয়ে যায়
- Training data মুখস্থ করে ফেলে

---

## ✂️ Overfitting কমানোর উপায়

### 🔹 Pre-Pruning

- `max_depth`
- `min_samples_split`
- `min_samples_leaf`

### 🔹 Post-Pruning

- Cost Complexity Pruning (α-pruning)

---

## ✅ Advantages (সুবিধা)

- সহজে বোঝা যায়
- Feature scaling দরকার হয় না
- Non-linear relationship ধরতে পারে
- Visualization সম্ভব

---

## ❌ Disadvantages (অসুবিধা)

- Overfitting প্রবণ
- ছোট পরিবর্তনে বড় প্রভাব পড়ে
- Ensemble ছাড়া performance কম

---

## 🚀 কখন ব্যবহার করবেন?

- Dataset ছোট বা মাঝারি হলে
- Relationship non-linear হলে
- Interpretability দরকার হলে

---

## 🔁 Ensemble Alternatives

Decision Tree Regression-এর উন্নত রূপ:

- Random Forest Regression
- Gradient Boosting
- XGBoost

---

##
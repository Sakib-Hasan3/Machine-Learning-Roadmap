# 📊 Multiple Linear Regression — বাংলায় সহজ ব্যাখ্যা

---

## 📘 Multiple Linear Regression কী?

**Multiple Linear Regression** হলো একটি পরিসংখ্যানিক পদ্ধতি, যেখানে একাধিক স্বাধীন ভেরিয়েবল (independent variables) ব্যবহার করে একটি নির্ভরশীল ভেরিয়েবল (dependent variable) এর মান পূর্বাভাস করা হয়।

### **সমীকরণ:**

$$
Y = \beta_0 + \beta_1X_1 + \beta_2X_2 + ... + \beta_nX_n + \epsilon
$$

**যেখানে:**
- $Y$ = নির্ভরশীল ভেরিয়েবল (Dependent Variable)
- $X_1, X_2, ..., X_n$ = স্বাধীন ভেরিয়েবল (Independent Variables)
- $\beta_0$ = Intercept (যেখানে রেখা Y-অক্ষকে ছেদ করে)
- $\beta_1, \beta_2, ..., \beta_n$ = Coefficients (প্রতিটি স্বাধীন ভেরিয়েবলের প্রভাব)
- $\epsilon$ = ত্রুটি (Error Term)

---

## 🛠️ Multiple Linear Regression কীভাবে কাজ করে?

1. **ডেটা সংগ্রহ:**
   - নির্ভরশীল এবং স্বাধীন ভেরিয়েবল চিহ্নিত করা।

2. **সমীকরণ তৈরি:**
   - ডেটার উপর ভিত্তি করে $\beta$ (coefficients) নির্ধারণ করা।

3. **Cost Function:**
   - **Mean Squared Error (MSE)** ব্যবহার করে ভুলের পরিমাণ মাপা।

4. **Optimization:**
   - Gradient Descent বা অন্য অপ্টিমাইজেশন পদ্ধতি ব্যবহার করে $\beta$-এর মান আপডেট করা।

5. **Prediction:**
   - নতুন ডেটার জন্য $Y$ এর মান পূর্বাভাস করা।

---

## 🧮 উদাহরণ:

ধরা যাক, আমরা একটি বাড়ির দাম পূর্বাভাস করতে চাই।

| আয়তন (Sq Ft) | বেডরুম সংখ্যা | দাম (লক্ষ টাকা) |
|----------------|---------------|-----------------|
| 1000          | 2             | 50              |
| 1500          | 3             | 75              |
| 2000          | 4             | 100             |

### **সমীকরণ:**

$$
দাম = \beta_0 + \beta_1(আয়তন) + \beta_2(বেডরুম সংখ্যা)
$$

### **কোয়াফিসিয়েন্ট বের করা:**
- $\beta_0 = 10$
- $\beta_1 = 0.03$
- $\beta_2 = 5$

### **প্রেডিকশন:**

যদি একটি বাড়ির আয়তন 1800 Sq Ft এবং বেডরুম সংখ্যা 3 হয়, তাহলে:

$$
দাম = 10 + 0.03(1800) + 5(3) = 10 + 54 + 15 = 79 লক্ষ টাকা
$$

---

## 🔹 Assumptions of Multiple Linear Regression

1. **লিনিয়ার সম্পর্ক:**
   - স্বাধীন এবং নির্ভরশীল ভেরিয়েবলের মধ্যে সম্পর্ক লিনিয়ার হতে হবে।

2. **মাল্টিকলিনিয়ারিটি নেই:**
   - স্বাধীন ভেরিয়েবলগুলোর মধ্যে খুব বেশি সম্পর্ক থাকা যাবে না।

3. **ত্রুটির স্বাভাবিক বন্টন:**
   - ত্রুটি (Residuals) স্বাভাবিকভাবে বিতরণ হতে হবে।

4. **হোমোসেডাস্টিসিটি:**
   - ত্রুটির ভ্যারিয়েন্স ধ্রুবক হতে হবে।

5. **স্বাধীন ত্রুটি:**
   - ত্রুটিগুলো একে অপরের উপর নির্ভরশীল হবে না।

---

## 📈 মডেল মূল্যায়ন (Model Evaluation)

1. **R-squared (R²):**
   - মডেল কতটা ভালো ডেটার সাথে ফিট হয়েছে তা মাপে।

2. **Adjusted R-squared:**
   - R² এর উন্নত সংস্করণ, যা স্বাধীন ভেরিয়েবলের সংখ্যা বিবেচনা করে।

3. **Mean Squared Error (MSE):**
   - প্রেডিকশন এবং আসল মানের মধ্যে গড় বর্গ ত্রুটি।

4. **Root Mean Squared Error (RMSE):**
   - MSE এর বর্গমূল।

---

## 🛠️ Python কোড উদাহরণ:

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# ডেটা তৈরি
X = np.array([[1000, 2], [1500, 3], [2000, 4]])  # স্বাধীন ভেরিয়েবল
Y = np.array([50, 75, 100])  # নির্ভরশীল ভেরিয়েবল

# মডেল তৈরি
model = LinearRegression()
model.fit(X, Y)

# কোয়াফিসিয়েন্ট
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

# প্রেডিকশন
new_data = np.array([[1800, 3]])
prediction = model.predict(new_data)
print("Prediction:", prediction)

# MSE
predictions = model.predict(X)
mse = mean_squared_error(Y, predictions)
print("Mean Squared Error:", mse)
```

---

## ✅ উপসংহার

- Multiple Linear Regression একটি শক্তিশালী টুল যা একাধিক ফিচার ব্যবহার করে পূর্বাভাস করতে সাহায্য করে।
- এটি সহজ এবং কার্যকর, তবে Assumptions মেনে চলা গুরুত্বপূর্ণ।
- Python এর মতো টুল ব্যবহার করে সহজেই এটি প্রয়োগ করা যায়।

---

*© 2025 - Multiple Linear Regression বাংলা টিউটোরিয়াল*

# K-Fold Cross Validation

K-Fold Cross Validation হলো একটি জনপ্রিয় টেকনিক যেখানে পুরো ডেটাসেটকে সমান আকারের K টি ফোল্ডে ভাগ করা হয়।

প্রতিবার ১টি fold টেস্ট সেট হিসেবে এবং বাকি K-1 fold ট্রেনিং সেট হিসেবে ব্যবহৃত হয়।

এই প্রক্রিয়া K বার হয় এবং প্রতিটি ফোল্ড একবার করে test সেট হয়।

সব শেষে গড় পারফরম্যান্স নেওয়া হয়।

---

## 🎯 কেন ব্যবহার করা হয়?

- **Hold-Out এর মতো শুধু একবার ভাগ না করে**, একাধিক ভাগে টেস্ট করা যায়।
- **ছোট ডেটাসেটে** মডেলের generalization ক্ষমতা যাচাই করতে কাজে লাগে।
- **Random train-test split এর কারণে** performance variation কমে।

---

## 📝 উদাহরণ (K = 5 ধরে নিই)

যদি ডেটাসেটে **100টি ডেটা** থাকে এবং আমরা **5-Fold** ব্যবহার করি:

- প্রতিটি fold = **20 ডেটা**।

### Iteration-wise বিভাজন:

| Iteration | Test Set | Training Set |
|-----------|----------|--------------|
| **Iteration 1** | 20 test | 80 train |
| **Iteration 2** | অন্য 20 test | 80 train |
| **Iteration 3** | অন্য 20 test | 80 train |
| **Iteration 4** | অন্য 20 test | 80 train |
| **Iteration 5** | শেষ 20 test | 80 train |

👉 **সবশেষে ৫টি টেস্ট রেজাল্ট গড় করে মডেলের Accuracy বের হয়।**

---

## 🧑‍💻 Python কোড (K-Fold Cross Validation)

### বেসিক Implementation:

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LogisticRegression

# ডেটা লোড করা
data = load_iris()
X = data.data
y = data.target

# Logistic Regression মডেল
model = LogisticRegression(max_iter=200)

# 5-Fold Cross Validation
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

# প্রতিটি ফোল্ডের স্কোর বের করা
scores = cross_val_score(model, X, y, cv=kfold)

print("প্রতিটি ফোল্ডের স্কোর:", scores)
print("গড় Accuracy:", scores.mean())
print("Standard Deviation:", scores.std())
```

### ✅ আউটপুট (উদাহরণস্বরূপ):
```
প্রতিটি ফোল্ডের স্কোর: [0.9666 1.     0.9666 0.9333 1.    ]
গড় Accuracy: 0.9733
Standard Deviation: 0.0230
```

---

## 🔍 বিস্তারিত Manual Implementation:

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# ডেটা লোড
data = load_iris()
X = data.data
y = data.target

# K-Fold setup
k = 5
kfold = KFold(n_splits=k, shuffle=True, random_state=42)
model = LogisticRegression(max_iter=200)

# Manual implementation
fold_scores = []
fold_number = 1

for train_index, test_index in kfold.split(X):
    # ট্রেইন ও টেস্ট ডেটা ভাগ করা
    X_train_fold, X_test_fold = X[train_index], X[test_index]
    y_train_fold, y_test_fold = y[train_index], y[test_index]
    
    # মডেল ট্রেইন করা
    model.fit(X_train_fold, y_train_fold)
    
    # প্রেডিকশন
    y_pred = model.predict(X_test_fold)
    
    # Accuracy হিসাব
    accuracy = accuracy_score(y_test_fold, y_pred)
    fold_scores.append(accuracy)
    
    print(f"Fold {fold_number}: Accuracy = {accuracy:.4f}")
    print(f"  Training samples: {len(X_train_fold)}")
    print(f"  Test samples: {len(X_test_fold)}")
    print("-" * 40)
    
    fold_number += 1

# ফাইনাল রেজাল্ট
print(f"\nসব ফোল্ডের স্কোর: {fold_scores}")
print(f"গড় Accuracy: {np.mean(fold_scores):.4f}")
print(f"Standard Deviation: {np.std(fold_scores):.4f}")
```

---

## 📊 কখন ব্যবহার করবেন?

### ✅ উপযুক্ত পরিস্থিতি:

1. **যখন ডেটাসেট ছোট** → একবার train-test split করলে bias হতে পারে।
2. **যখন মডেলের performance এর উপর ভরসা করতে চান।**
3. **যখন মডেলের generalization ability যাচাই করতে চান।**
4. **Model selection এর জন্য** (বিভিন্ন algorithm তুলনা)
5. **Hyperparameter tuning এর জন্য**

### ❌ এড়িয়ে চলুন যখন:

1. **খুব বড় ডেটাসেট** (computational cost বেশি)
2. **Time series data** (temporal order নষ্ট হয়)
3. **অত্যন্ত imbalanced dataset** (Stratified K-Fold ব্যবহার করুন)

---

## 🛠️ বিভিন্ন K মানের প্রভাব:

```python
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier

# ডেটা লোড
data = load_breast_cancer()
X, y = data.data, data.target
model = RandomForestClassifier(random_state=42)

# বিভিন্ন K মান টেস্ট করা
k_values = [3, 5, 7, 10, 15]

for k in k_values:
    kfold = KFold(n_splits=k, shuffle=True, random_state=42)
    scores = cross_val_score(model, X, y, cv=kfold)
    
    print(f"K = {k:2d}: Mean = {scores.mean():.4f}, Std = {scores.std():.4f}")
```

### আউটপুট:
```
K =  3: Mean = 0.9455, Std = 0.0123
K =  5: Mean = 0.9490, Std = 0.0187
K =  7: Mean = 0.9507, Std = 0.0211
K = 10: Mean = 0.9472, Std = 0.0234
K = 15: Mean = 0.9455, Std = 0.0298
```

---

## 📈 K নির্বাচনের গাইডলাইন:

### **K = 5 (সবচেয়ে জনপ্রিয়)**
- **সুবিধা:** দ্রুত, reasonable bias-variance tradeoff
- **ব্যবহার:** সাধারণ উদ্দেশ্যে

### **K = 10 (Research standard)**
- **সুবিধা:** কম bias, গবেষণায় standard
- **অসুবিধা:** একটু বেশি সময় লাগে

### **K = 3 (দ্রুত টেস্ট)**
- **সুবিধা:** খুব দ্রুত
- **অসুবিধা:** বেশি bias

### **K = n (LOOCV)**
- **সুবিধা:** সর্বনিম্ন bias
- **অসুবিধা:** অত্যন্ত ধীর, high variance

---

## 🎯 Ridge Regression এর সাথে K-Fold:

```python
from sklearn.linear_model import Ridge
from sklearn.model_selection import KFold, cross_val_score
from sklearn.datasets import load_boston
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# বোস্টন হাউজিং ডেটা (regression example)
# Note: load_boston deprecated, using alternative
from sklearn.datasets import fetch_california_housing

data = fetch_california_housing()
X, y = data.data, data.target

# Ridge regression with different alpha values
alphas = [0.1, 1.0, 10.0, 100.0]
k = 5

for alpha in alphas:
    # Pipeline তৈরি (scaling + ridge)
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('ridge', Ridge(alpha=alpha))
    ])
    
    # K-Fold CV
    kfold = KFold(n_splits=k, shuffle=True, random_state=42)
    scores = cross_val_score(pipeline, X, y, cv=kfold, 
                           scoring='neg_mean_squared_error')
    
    rmse_scores = np.sqrt(-scores)  # RMSE এ convert
    
    print(f"Alpha = {alpha:5.1f}: RMSE = {rmse_scores.mean():.4f} ± {rmse_scores.std():.4f}")
```

---

## 📋 Best Practices:

### 1. **Always Shuffle:**
```python
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
```

### 2. **Set Random State:**
```python
# Reproducible results এর জন্য
random_state=42
```

### 3. **Use Pipeline:**
```python
# Data leakage এড়াতে
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', Ridge())
])
```

### 4. **Multiple Metrics:**
```python
from sklearn.model_selection import cross_validate

scoring = ['accuracy', 'precision', 'recall', 'f1']
results = cross_validate(model, X, y, cv=kfold, scoring=scoring)

for metric in scoring:
    scores = results[f'test_{metric}']
    print(f"{metric.capitalize()}: {scores.mean():.4f} ± {scores.std():.4f}")
```

---

## 🔍 সুবিধা ও অসুবিধা:

### ✅ সুবিধা:
1. **আরো নির্ভরযোগ্য performance estimate**
2. **সব ডেটা training ও testing উভয়ে ব্যবহৃত হয়**
3. **Performance variance measure করা যায়**
4. **Model selection এ কার্যকর**
5. **Overfitting detection সহজ**

### ❌ অসুবিধা:
1. **Computational cost বেশি** (K বার training)
2. **Time series data এ suitable নয়**
3. **Memory requirements বেশি**
4. **K নির্বাচন subjective**

---

## 📊 K-Fold vs Hold-Out তুলনা:

| বৈশিষ্ট্য | K-Fold | Hold-Out |
|----------|--------|----------|
| **Reliability** | উচ্চ | মাঝারি |
| **Computational Cost** | বেশি | কম |
| **Data Utilization** | সম্পূর্ণ | আংশিক |
| **Variance** | কম | বেশি |
| **Implementation** | জটিল | সহজ |
| **Small Dataset** | উপযুক্ত | অনুপযুক্ত |

---

## 💡 মনে রাখার বিষয়:

1. **K-Fold হলো gold standard** for model evaluation
2. **K=5 বা K=10** সবচেয়ে common choices
3. **ছোট ডেটাসেটে অপরিহার্য**
4. **Pipeline ব্যবহার করে data leakage এড়ান**
5. **Standard deviation দেখে consistency বুঝুন**

---


**সংক্ষেপে:** K-Fold Cross Validation আপনাকে মডেলের **সত্যিকারের performance** বুঝতে সাহায্য করে, যা একক train-test split দিয়ে সম্ভব নয়।




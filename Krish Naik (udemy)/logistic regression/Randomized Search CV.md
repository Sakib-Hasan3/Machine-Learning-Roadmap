---

# 🎯 **Randomized Search CV কী?**

**Randomized Search CV** হলো Hyperparameter tuning-এর একটি পদ্ধতি, যেখানে সব প্যারামিটারের সব সম্ভাব্য combination পরীক্ষা না করে, বরং **র‍্যান্ডমলি কিছু combination** বেছে নিয়ে model train করা হয়।

➡ Grid Search = Exhaustive (সব কম্বিনেশন)
➡ Random Search = Random sampling (কিছু গুরুত্বপূর্ণ কম্বিনেশন)

এটি দ্রুত, কার্যকরী, এবং বড় parameter space-এর জন্য অনেক উপযোগী।

---

![Image](https://360digitmg.com/assets/admin/ckfinder/userfiles/images/blog/4-08-2023/image3.png?utm_source=chatgpt.com)

![Image](https://miro.medium.com/max/1280/1%2Ao2rMCJKUcpqRBFfHZ3Jkfg.png?utm_source=chatgpt.com)

---

# 🧠 **কেন Randomized Search দরকার?**

Grid Search সব সম্ভাব্য combination পরীক্ষা করে, যা বড় search space-এ খুব ধীর।

### উদাহরণ:

| Parameter | Values     | Count |
| --------- | ---------- | ----- |
| C         | 100 values | 100   |
| gamma     | 100 values | 100   |
| kernel    | 3 values   | 3     |

Grid Search → **100 × 100 × 3 = 30,000** models train করতে হবে 😵

Randomized Search → মাত্র **৫০ বা ১০০** sample → বিশাল সময় বাঁচাবে।

---

# 🟦 **Randomized Search কীভাবে কাজ করে? (Intuition)**

### Step 1

Hyperparameter space define করা হয়
(যেমন range: 0.001–100)

### Step 2

কতটি random combination পরীক্ষা করা হবে সেটি নির্ধারণ
(n_iter parameter)

### Step 3

প্রতিটি sampled combination-এর জন্য model train
cross-validation সহ

### Step 4

Best parameters + best score return করে

---

# ⭐ Randomized Search কে Grid Search থেকে বিশেষ করে তোলে?

| Feature    | Grid Search              | Randomized Search   |
| ---------- | ------------------------ | ------------------- |
| Search     | Exhaustive               | Random              |
| Speed      | Slow                     | Faster              |
| Best for   | ছোট grid                 | বড়/continuous space |
| Sampling   | সব কম্বিনেশন             | নির্দিষ্ট n_iter    |
| Efficiency | Low for high-dimensional | High                |

Randomized Search often **finds as good parameters as Grid Search in much less time**.

---

# 🔍 RandomizedSearchCV গুরুত্বপূর্ণ প্যারামিটার

| Parameter               | কাজ                                         |
| ----------------------- | ------------------------------------------- |
| **param_distributions** | যেসব hyperparameter randomly sample করা হবে |
| **n_iter**              | কয়টা random combination টেস্ট করবে          |
| **cv**                  | cross validation folds                      |
| **scoring**             | metric: accuracy/F1/AUC/RMSE                |
| **n_jobs=-1**           | parallel processing                         |
| **random_state**        | reproducibility                             |

---

# 🧪 Python Example — RandomizedSearchCV (Logistic Regression)

```python
import numpy as np
from sklearn.model_selection import RandomizedSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

model = LogisticRegression(max_iter=300)

param_dist = {
    'C': np.logspace(-3, 3, 50),
    'penalty': ['l1', 'l2'],
    'solver': ['liblinear']
}

rand_search = RandomizedSearchCV(
    estimator=model,
    param_distributions=param_dist,
    n_iter=20,          # শুধু 20 টি র‍্যান্ডম কম্বিনেশন পরীক্ষা করবে
    cv=5,
    scoring='accuracy',
    random_state=42
)

rand_search.fit(X, y)

print("Best Parameters:", rand_search.best_params_)
print("Best Score:", rand_search.best_score_)
```

---

# 🧪 Randomized Search with Random Forest

```python
from sklearn.ensemble import RandomForestClassifier

param_dist = {
    'n_estimators': np.arange(50, 500, 50),
    'max_depth': np.arange(3, 20),
    'min_samples_split': np.arange(2, 10),
    'min_samples_leaf': np.arange(1, 5),
}

rand_search = RandomizedSearchCV(
    estimator=RandomForestClassifier(),
    param_distributions=param_dist,
    n_iter=30,
    cv=3,
    random_state=0
)

rand_search.fit(X, y)

print(rand_search.best_params_)
```

---

# 🔥 কখন Randomized Search ব্যবহার করবেন?

| পরিস্থিতি                  | সুপারিশ             |
| -------------------------- | ------------------- |
| Parameter space বড়         | ✔ Randomized Search |
| Training cost বেশি         | ✔ Randomized Search |
| Quickly good model দরকার   | ✔ Randomized Search |
| Parameter range continuous | ✔ Randomized Search |
| ছোট parameter grid         | Grid Search হয় ভালো |

---

# 🟢 Randomized Search এর সুবিধা

✔ দ্রুত
✔ বড় parameter space explore করতে পারে
✔ কম resource লাগে
✔ continuous রেঞ্জ search করতে সুবিধা
✔ প্রায় grid search-এর মতোই ভালো ফলাফল দেয়

---

# 🔴 অসুবিধা

❌ সব combination দেখা হয় না
❌ ‘best’ combination মিস করতে পারে
❌ Repeat না হলে reproducibility কম

---

# 🧠 Summary (Short Notes)

* Randomized Search randomly কিছু parameters পরীক্ষা করে
* Fast, efficient, ideal for large search space
* `n_iter` নির্ধারণ করে trained models কত হবে
* Best hyperparameters return করে + cross-validation করে

---


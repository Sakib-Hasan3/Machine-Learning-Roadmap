# Random Forest Regression Problem

## 🌳 Random Forest Regression — Diagram (Intuition)

![Image](https://cdn.prod.website-files.com/5e6f9b297ef3941db2593ba1/5f6315207ab68b113cf57b1c_Screenshot%202020-09-17%20at%2009.49.20.png)

![Image](https://www.researchgate.net/publication/303835073/figure/fig3/AS%3A377949833449472%401467121670301/The-flowchart-of-random-forest-RF-for-regression-adapted-from-Rodriguez-Galiano-et.png)

[Image](https://miro.medium.com/v2/resize%3Afit%3A1400/0%2AYEwFetXQGPB8aDFV)

---

# 1️⃣ Random Forest Regression — Python / Sklearn Code

### 🔹 উদাহরণ সমস্যা

👉 **House Price Prediction** (continuous value → regression)

---

## 📌 Step-1: Libraries Import

```python
import numpy as np
import pandas as pd

from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

```

---

## 📌 Step-2: Dataset তৈরি

```python
# Synthetic regression dataset
X, y = make_regression(
    n_samples=1000,
    n_features=6,
    noise=20,
    random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

X_train.shape, X_test.shape

```

**Output**

```
((750, 6), (250, 6))

```

---

## 📌 Step-3: Random Forest Regression (Default)

```python
rf = RandomForestRegressor(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)

rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)

print("MAE:", mean_absolute_error(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R2 Score:", r2_score(y_test, y_pred))

```

**Example Output**

```
MAE: 14.8
RMSE: 18.9
R2 Score: 0.92

```

---

# 2️⃣ Hyperparameter Tuning (Bangla Explanation + Code)

## 🔧 Hyperparameter Tuning কী?

👉 Model train করার **আগে** যেসব সেটিং ঠিক করা হয়

👉 সেগুলোর **best combination** বের করার প্রক্রিয়াই **Hyperparameter Tuning**

---

## 🎛️ Random Forest Regression-এর গুরুত্বপূর্ণ Hyperparameters

| Hyperparameter | কাজ |
| --- | --- |
| `n_estimators` | কয়টা tree হবে |
| `max_depth` | tree কত গভীর |
| `min_samples_split` | split করার minimum data |
| `min_samples_leaf` | leaf-এ minimum data |
| `max_features` | প্রতি split-এ feature সংখ্যা |

---

## 📌 GridSearchCV দিয়ে Tuning

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    "n_estimators": [100, 200],
    "max_depth": [None, 10, 20],
    "min_samples_leaf": [1, 3]
}

grid = GridSearchCV(
    estimator=RandomForestRegressor(random_state=42),
    param_grid=param_grid,
    cv=3,
    scoring="r2",
    n_jobs=-1
)

grid.fit(X_train, y_train)

grid.best_params_, grid.best_score_

```

**Example Output**

```
({'max_depth': 20, 'min_samples_leaf': 1, 'n_estimators': 200}, 0.94)

```

---

## 📌 Tuned Model দিয়ে Test

```python
best_rf = grid.best_estimator_

y_pred_tuned = best_rf.predict(X_test)

print("R2 Score (Tuned):", r2_score(y_test, y_pred_tuned))

```

**Output**

```
R2 Score (Tuned): 0.94

```

📌 **Tuning করার পর performance বেড়েছে ✅**

---

# 3️⃣ Numerical Example (খুব সহজ)

ধরা যাক **একটা বাড়ির দাম** predict করতে 5টা tree নিচের মান দিলো:

| Tree | Prediction |
| --- | --- |
| Tree-1 | 52,000 |
| Tree-2 | 54,000 |
| Tree-3 | 51,000 |
| Tree-4 | 53,000 |
| Tree-5 | 55,000 |

### 👉 Final Prediction

[

\frac{52000 + 54000 + 51000 + 53000 + 55000}{5} = 53,000

]

📌 এটাই **Random Forest Regression**

---

```
Random Forest Regression
------------------------
• Ensemble learning technique
• Uses multiple regression trees
• Final prediction = average of all tree predictions
• Based on Bagging (Bootstrap Aggregating)

Why use?
• Reduces overfitting
• Handles non-linear data
• Robust to noise & outliers
• No feature scaling required

Key Hyperparameters
• n_estimators
• max_depth
• min_samples_split
• min_samples_leaf
• max_features

Evaluation Metrics
• MAE
• RMSE
• R² Score

Use Cases
• House price prediction
• Salary prediction
• Sales forecasting
• Medical cost estimation

```

---

# 🎤 Viva / Interview One-Liners

- **Random Forest Regression কী?**
    
    👉 Multiple regression tree এর average দিয়ে prediction
    
- **Bagging না Boosting?**
    
    👉 Bagging
    
- **Overfitting কম কেন?**
    
    👉 Bootstrap sampling + feature randomness
    
- **Scaling দরকার?**
    
    👉 না
    

---
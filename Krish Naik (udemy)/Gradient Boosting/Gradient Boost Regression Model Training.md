---

## ✅ Cell 1 — Imports + Reproducibility

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

print("Libraries imported.")
```

**Output:**

```
Libraries imported.
```

---

## ✅ Cell 2 — Synthetic Regression Dataset তৈরি

```python
rng = np.random.default_rng(42)
n = 800

# Features
x1 = rng.uniform(-3, 3, n)
x2 = rng.uniform(0, 6, n)
x3 = rng.normal(0, 1, n)

# Non-linear target with noise
noise = rng.normal(0, 1.2, n)
y = 3*np.sin(x1) + 0.5*(x2**2) - 2*x3 + 0.8*x1*x2 + noise

X = pd.DataFrame({"x1": x1, "x2": x2, "x3": x3})
y = pd.Series(y, name="target")

print("X shape:", X.shape)
print("y shape:", y.shape)

X.head(), y.head()
```

**Output (main):**

```
X shape: (800, 3)
y shape: (800,)
```

এবং `X.head()` ও `y.head()` টেবিল আকারে দেখাবে।

---

## ✅ Cell 3 — Train/Test Split

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Train shapes:", X_train.shape, y_train.shape)
print("Test shapes :", X_test.shape, y_test.shape)
```

**Output:**

```
Train shapes: (640, 3) (640,)
Test shapes : (160, 3) (160,)
```

---

## ✅ Cell 4 — GradientBoostingRegressor Train

```python
gbr = GradientBoostingRegressor(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=3,
    subsample=0.9,
    random_state=42
)

gbr.fit(X_train, y_train)

print("Model trained.")
print(gbr)
```

**Output (example):**

```
Model trained.
GradientBoostingRegressor(learning_rate=0.05, n_estimators=300, random_state=42,
                          subsample=0.9)
```

---

## ✅ Cell 5 — Prediction + Metrics + Sample Output Table

```python
y_pred = gbr.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"MAE : {mae:.4f}")
print(f"MSE : {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"R^2 : {r2:.4f}")

comparison = pd.DataFrame({
    "y_true": y_test.values[:10],
    "y_pred": y_pred[:10],
    "error": (y_test.values[:10] - y_pred[:10])
})
comparison
```

**Output (আমার রান অনুযায়ী):**

```
MAE : 1.1358
MSE : 2.3406
RMSE: 1.5299
R^2 : 0.9682
```

এবং `comparison` টেবিলে প্রথম ১০টা prediction দেখাবে।

---

## ✅ Cell 6 — True vs Predicted Plot

```python
plt.figure(figsize=(6, 5))
plt.scatter(y_test, y_pred, alpha=0.6)

min_v = min(y_test.min(), y_pred.min())
max_v = max(y_test.max(), y_pred.max())
plt.plot([min_v, max_v], [min_v, max_v])

plt.xlabel("True y")
plt.ylabel("Predicted y")
plt.title("Gradient Boosting Regression: True vs Predicted")
plt.show()
```

**Output:** একটি scatter plot (perfect fit হলে পয়েন্টগুলো diagonal লাইনের কাছে থাকবে)।

---

## ✅ Cell 7 — Boosting Stage অনুযায়ী Test MSE (Training Progress)

```python
stage_mse = []
for y_stage_pred in gbr.staged_predict(X_test):
    stage_mse.append(mean_squared_error(y_test, y_stage_pred))

stage_mse = np.array(stage_mse)

print("Number of stages:", len(stage_mse))
print("MSE at first stage :", f"{stage_mse[0]:.4f}")
print("MSE at last stage  :", f"{stage_mse[-1]:.4f}")

plt.figure(figsize=(7, 4))
plt.plot(np.arange(1, len(stage_mse) + 1), stage_mse)
plt.xlabel("Boosting stage (n_estimators)")
plt.ylabel("Test MSE")
plt.title("Test MSE vs Boosting Stage")
plt.show()
```

**Output (আমার রান অনুযায়ী):**

```
Number of stages: 300
MSE at first stage : 67.5579
MSE at last stage  : 2.3406
```

এবং একটি line plot দেখাবে (stage বাড়ার সাথে MSE কমতে থাকবে)।

---


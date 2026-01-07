# problem Statement

### **Trips & Travel.com** wants to establish a viable business model to expand its customer base. One of the strategies to grow the customer base is by introducing new travel packages. Currently, the company offers five types of packages: **Basic, Standard, Deluxe, Super Deluxe, and King**.

### Analysis of last year’s data shows that **only 18% of customers purchased these packages**, while the **marketing cost remained high** because customers were contacted **randomly without utilizing available customer information**.

### The company is now planning to launch a new product called the **Wellness Tourism Package**, which focuses on travel experiences that promote a healthy lifestyle and enhance overall well-being.

### This time, the company wants to **leverage data from existing and potential customers** to make marketing efforts more efficient and cost-effective.

---

## ✅ Notebook Code (Cell by Cell + Output)

---

### ✅ Cell 1 — Imports

```python
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.cluster import KMeans
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.ensemble import RandomForestClassifier

```

**Output (Cell 1):**

```
(no output)

```

---

### ✅ Cell 2 — Demo Dataset তৈরি (আপনার আসল CSV থাকলে নিচের cell-টা বদলাবেন)

```python
np.random.seed(42)
n = 2000

df = pd.DataFrame({
    "age": np.random.randint(18, 65, n),
    "income": np.random.normal(60000, 20000, n).clip(12000, 160000).astype(int),
    "location": np.random.choice(["Dhaka","Chattogram","Sylhet","Khulna","Rajshahi"], n),
    "gender": np.random.choice(["Male","Female"], n),
    "prev_package": np.random.choice(["Basic","Standard","Deluxe","Super Deluxe","King"], n,
                                     p=[0.34,0.28,0.2,0.12,0.06]),
    "trips_last_year": np.random.poisson(2.2, n).clip(0, 12),
    "days_since_last_trip": np.random.gamma(2.0, 55, n).clip(3, 365).astype(int),
    "avg_trip_spend": np.random.normal(450, 200, n).clip(80, 1600).round(1),
    "wellness_interest": np.random.beta(2.2, 2.0, n).round(3),
    "marketing_channel": np.random.choice(["Email","SMS","Call","Social","Agent"], n)
})

# (hidden) purchase probability তৈরি করে label বানানো
pkg = df["prev_package"].map({"Basic":0.0,"Standard":0.2,"Deluxe":0.5,"Super Deluxe":0.7,"King":0.9})
logit = (-4.0
         + 3.2*df["wellness_interest"]
         + 0.000025*df["income"]
         + 0.18*df["trips_last_year"]
         + 0.0012*df["avg_trip_spend"]
         - 0.006*df["days_since_last_trip"]
         + 0.9*pkg)

p = 1/(1+np.exp(-logit))
df["purchase_wellness"] = (np.random.rand(n) < p).astype(int)

df.head()

```

**Example Output (Cell 2):**

```
   age  income location gender prev_package  ... wellness_interest marketing_channel purchase_wellness
0   56   73150  Sylhet  Female      Basic    ... 0.318            Social            1
1   46   62841  Khulna   Male       Standard ... 0.679            SMS               1
...

```

---

### ✅ Cell 3 — Basic EDA (Conversion rate)

```python
print("Shape:", df.shape)
print("Purchase rate:", df["purchase_wellness"].mean().round(4))
df["purchase_wellness"].value_counts()

```

**Example Output (Cell 3):**

```
Shape: (2000, 11)
Purchase rate: 0.46

purchase_wellness
1    920
0   1080
Name: count, dtype: int64

```

---

# ✅ Part A: Customer Segmentation (Unsupervised)

### ✅ Cell 4 — Segmentation Features + KMeans

```python
seg_features = ["age","income","trips_last_year","days_since_last_trip","avg_trip_spend","wellness_interest"]

X_seg = StandardScaler().fit_transform(df[seg_features])

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
df["cluster"] = kmeans.fit_predict(X_seg)

df["cluster"].value_counts().sort_index()

```

**Example Output (Cell 4):**

```
cluster
0    520
1    480
2    510
3    490
Name: count, dtype: int64

```

---

### ✅ Cell 5 — Cluster Profile (কোন ক্লাস্টার কেমন)

```python
cluster_profile = df.groupby("cluster")[seg_features + ["purchase_wellness"]].mean().round(2)
cluster_profile

```

**Example Output (Cell 5):**

```
         age   income  trips_last_year  days_since_last_trip  avg_trip_spend  wellness_interest  purchase_wellness
cluster
0        28.1  52000   2.9             60.2                 520.4           0.72              0.62
1        43.5  61000   1.4            150.7                 360.9           0.35              0.31
2        35.2  78000   2.1             45.3                 680.5           0.61              0.55
3        52.8  59000   1.8            200.1                 410.2           0.40              0.34

```

📌 এখানে দেখবেন কোন cluster-এ **purchase_wellness বেশি** → সেই cluster টার্গেট করবেন।

---

# ✅ Part B: Purchase Prediction (Classification)

### ✅ Cell 6 — Train/Test Split + Preprocessing

```python
X = df.drop(columns=["purchase_wellness"])
y = df["purchase_wellness"]

categorical_cols = ["location", "gender", "prev_package", "marketing_channel"]
numeric_cols = [c for c in X.columns if c not in categorical_cols and c != "cluster"]

preprocess = ColumnTransformer([
    ("num", StandardScaler(), numeric_cols),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols)
])

X_train, X_test, y_train, y_test = train_test_split(
    X.drop(columns=["cluster"]), y, test_size=0.25, random_state=42, stratify=y
)

print(X_train.shape, X_test.shape)

```

**Example Output (Cell 6):**

```
(1500, 10) (500, 10)

```

---

### ✅ Cell 7 — Random Forest Classifier (Baseline)

```python
rf = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    n_jobs=-1,
    min_samples_leaf=2
)

rf_model = Pipeline([
    ("prep", preprocess),
    ("model", rf)
])

rf_model.fit(X_train, y_train)

proba = rf_model.predict_proba(X_test)[:, 1]
pred  = (proba >= 0.5).astype(int)

print("ROC-AUC:", roc_auc_score(y_test, proba).round(4))
print(classification_report(y_test, pred, digits=4))
print("Confusion Matrix:\n", confusion_matrix(y_test, pred))

```

**Example Output (Cell 7):**

```
ROC-AUC: 0.71

              precision    recall  f1-score   support
0             0.66        0.72     0.69      270
1             0.64        0.57     0.60      230
accuracy                          0.65

Confusion Matrix:
[[195  75]
 [ 99 131]]

```

---

## ✅ XGBoost Version (Best Accuracy Usually)

### ✅ Cell 8 — Install XGBoost (Colab/Jupyter এ লাগবে)

```python
# If you are in Google Colab / Jupyter:
# !pip -q install xgboost

```

**Output (Cell 8):**

```
(installs package)

```

---

### ✅ Cell 9 — XGBoost Classifier

```python
from xgboost import XGBClassifier

xgb = XGBClassifier(
    n_estimators=600,
    learning_rate=0.05,
    max_depth=4,
    subsample=0.9,
    colsample_bytree=0.9,
    reg_lambda=1.0,
    random_state=42,
    eval_metric="logloss",
    n_jobs=-1
)

xgb_model = Pipeline([
    ("prep", preprocess),
    ("model", xgb)
])

xgb_model.fit(X_train, y_train)

xgb_proba = xgb_model.predict_proba(X_test)[:, 1]
xgb_pred  = (xgb_proba >= 0.5).astype(int)

print("ROC-AUC:", roc_auc_score(y_test, xgb_proba).round(4))
print(classification_report(y_test, xgb_pred, digits=4))
print("Confusion Matrix:\n", confusion_matrix(y_test, xgb_pred))

```

**Example Output (Cell 9):**

```
ROC-AUC: 0.76

accuracy: 0.69
Confusion Matrix:
[[205  65]
 [ 90 140]]

```

---

# ✅ Part C: Marketing List (Top Customers)

### ✅ Cell 10 — Top Customers to Target (Probability অনুযায়ী)

```python
df_scored = df.copy()
df_scored["p_buy_rf"] = rf_model.predict_proba(df.drop(columns=["purchase_wellness","cluster"]))[:, 1]

top_customers = df_scored.sort_values("p_buy_rf", ascending=False).head(15)
top_customers[["age","income","location","prev_package","wellness_interest","marketing_channel","p_buy_rf"]]

```

**Example Output (Cell 10):**

```
      age  income  location  prev_package  wellness_interest marketing_channel  p_buy_rf
121    31  120000  Dhaka     King         0.94              Social            0.96
884    29  110500  Dhaka     Super Deluxe 0.91              Email             0.94
...

```

✅ এই list-টাই আপনার **targeted marketing list**.

---

#
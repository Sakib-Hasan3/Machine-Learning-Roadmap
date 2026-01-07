# HyperParameter Tuning

---

## ✅ Cell 1 — Raw Data (Sample)

```python
import pandas as pd
import numpy as np

np.random.seed(7)

# Cell 1: tiny demo dataset (replace with your real df)
df = pd.DataFrame({
    "customer_id": range(1, 11),
    "age": np.random.randint(18, 65, 10),
    "income": np.random.randint(20000, 150000, 10),
    "prev_package": np.random.choice(["Basic","Standard","Deluxe","Super Deluxe","King"], 10),
    "trips_last_year": np.random.poisson(2.0, 10),
    "days_since_last_trip": np.random.randint(1, 365, 10),
    "avg_trip_spend": np.random.randint(100, 1500, 10),
    "wellness_interest": np.random.rand(10).round(3),
    "marketing_channel": np.random.choice(["Email","SMS","Call","Social","Agent"], 10),
    # target label
    "purchase_wellness": np.random.choice([0,1], 10, p=[0.7,0.3])
})

print("Cell 1 ✅ Raw data (sample):")
df

```

**Output (Cell 1):**

```
Cell 1 ✅ Raw data (sample):
   customer_id  age  income  prev_package  trips_last_year  days_since_last_trip  avg_trip_spend  wellness_interest marketing_channel  purchase_wellness
0            1   22   73593          King                2                   131             207              0.649             Agent                 1
1            2   43  147342         Basic                2                    84             493              0.557            Social                 1
...

```

---

# ✅ Feature Engineering (এইটাই মূল অংশ)

## ✅ Cell 2 — Feature Engineering (RFM + Business + Interactions)

```python
df_fe = df.copy()

# 1) Recency features
df_fe["recency_days"] = df_fe["days_since_last_trip"]
df_fe["recency_bucket"] = pd.cut(
    df_fe["recency_days"], bins=[0, 30, 90, 180, 365],
    labels=["0-30", "31-90", "91-180", "181-365"], include_lowest=True
)

# 2) Frequency features
df_fe["freq_trips"] = df_fe["trips_last_year"]
df_fe["is_frequent_traveler"] = (df_fe["freq_trips"] >= 3).astype(int)

# 3) Monetary features
df_fe["monetary_total_spend_est"] = (df_fe["avg_trip_spend"] * df_fe["freq_trips"]).astype(int)
df_fe["log_income"] = np.log1p(df_fe["income"])  # income skew reduce

# 4) Package-based features (premium mapping)
pkg_rank = {"Basic":1, "Standard":2, "Deluxe":3, "Super Deluxe":4, "King":5}
df_fe["prev_pkg_rank"] = df_fe["prev_package"].map(pkg_rank).astype(int)
df_fe["is_premium_pkg"] = (df_fe["prev_pkg_rank"] >= 4).astype(int)  # Super Deluxe/King

# 5) Channel grouping (business simplification)
df_fe["channel_type"] = df_fe["marketing_channel"].replace({
    "Email": "Digital", "Social": "Digital",
    "SMS": "Direct", "Call": "Direct",
    "Agent": "Partner"
})

# 6) Interaction features
df_fe["wellness_x_income"] = (df_fe["wellness_interest"] * df_fe["income"]).round(2)
df_fe["wellness_x_recency"] = (df_fe["wellness_interest"] / (1 + df_fe["recency_days"])).round(5)

# 7) Age bucket
df_fe["age_bucket"] = pd.cut(
    df_fe["age"], bins=[17, 25, 35, 50, 65],
    labels=["18-25", "26-35", "36-50", "51-65"]
)

engineered_cols = [
    "recency_days","recency_bucket","freq_trips","is_frequent_traveler",
    "monetary_total_spend_est","log_income","prev_pkg_rank","is_premium_pkg",
    "channel_type","wellness_x_income","wellness_x_recency","age_bucket"
]

print("Cell 2 ✅ Feature engineering done.")
print("New engineered columns:", engineered_cols)
df_fe[["customer_id"] + engineered_cols + ["purchase_wellness"]].head(8)

```

**Output (Cell 2):**

```
Cell 2 ✅ Feature engineering done.
New engineered columns: ['recency_days', 'recency_bucket', 'freq_trips', 'is_frequent_traveler', 'monetary_total_spend_est', 'log_income', 'prev_pkg_rank', 'is_premium_pkg', 'channel_type', 'wellness_x_income', 'wellness_x_recency', 'age_bucket']

   customer_id  recency_days recency_bucket  freq_trips  is_frequent_traveler  monetary_total_spend_est  log_income  prev_pkg_rank  is_premium_pkg channel_type  wellness_x_income  wellness_x_recency age_bucket  purchase_wellness
0            1           131         91-180           2                     0                       414   11.206319              5               1     Partner        47779.26            0.00492     18-25                 1
1            2            84          31-90           2                     0                       986   11.900518              1               0     Digital        82073.69            0.00655     36-50                 1
...

```

---

## ✅ Cell 3 — ML-ready Feature Matrix (Encoding + Scaling)

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

target = "purchase_wellness"
drop_cols = ["customer_id", target, "days_since_last_trip", "trips_last_year"]  # replaced by engineered versions

X = df_fe.drop(columns=drop_cols)
y = df_fe[target]

cat_cols = ["prev_package", "marketing_channel", "recency_bucket", "channel_type", "age_bucket"]
num_cols = [c for c in X.columns if c not in cat_cols]

preprocess = ColumnTransformer( transformers=[
    ("num", StandardScaler(), num_cols),
    ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)
])

X_trans = preprocess.fit_transform(X)

print("Cell 3 ✅ ML-ready feature matrix created.")
print("Raw X shape:", X.shape)
print("Transformed feature matrix shape:", X_trans.shape)
print("Numeric cols:", num_cols)
print("Categorical cols:", cat_cols)

```

**Output (Cell 3):**

```
Cell 3 ✅ ML-ready feature matrix created.
Raw X shape: (10, 18)
Transformed feature matrix shape: (10, 33)
Numeric cols: ['age', 'income', 'avg_trip_spend', 'wellness_interest', 'recency_days', 'freq_trips', 'is_frequent_traveler', 'monetary_total_spend_est', 'log_income', 'prev_pkg_rank', 'is_premium_pkg', 'wellness_x_income', 'wellness_x_recency']
Categorical cols: ['prev_package', 'marketing_channel', 'recency_bucket', 'channel_type', 'age_bucket']

```

---

# 🔥 এই Feature Engineering কেন এই সমস্যার জন্য Perfect?

- **RFM** (Recency/Frequency/Monetary) → কে কিনবে বোঝাতে শক্তিশালী
- **Package rank & premium flag** → luxury vs budget behavior ধরতে
- **Channel type** → কোন channel-এ response বেশি আসে সেটা ধরতে
- **Interaction features** → wellness interest + income/recency এর combined effect ধরতে
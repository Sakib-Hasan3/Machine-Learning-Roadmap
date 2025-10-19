# ডেটাসেট ক্লিনিং গাইড (clean_dataset.md)

এই ডকুমেন্টে রিজ রিগ্রেশনসহ যেকোনো মডেলিংয়ের আগে ডেটাসেট কীভাবে পরিষ্কার (clean) ও প্রস্তুত (preprocess) করবেন, তার ধাপে ধাপে বাংলা নির্দেশনা ও উদাহরণ কোড দেওয়া হলো।

---

## 🎯 লক্ষ্য (Objectives)
- Missing values হ্যান্ডেল করা
- Outliers শনাক্ত/হ্যান্ডেল করা
- ডুপ্লিকেট সারি সরানো
- টাইপ কনভার্সন ও পার্সিং (তারিখ/ক্যাটেগরি)
- Feature scaling/encoding
- Data leakage এড়িয়ে train/test split সহ প্রিপ্রসেসিং পাইপলাইন তৈরি

---

## ১) ডেটা লোড ও প্রাথমিক চেক

```python
import pandas as pd

# CSV লোড
df = pd.read_csv('data.csv')

# শীর্ষ সারি
print(df.head())

# গঠন/সারাংশ
print(df.info())
print(df.describe(include='all'))

# Missing overview
print(df.isna().sum())

# ডুপ্লিকেট
print('Duplicates:', df.duplicated().sum())
```

টিপস:
- `info()` দিয়ে dtype, nulls বোঝা যায়
- `describe()` দিয়ে সংখ্যাসূচক/বর্ণনামূলক পরিসংখ্যান দেখা যায়

---

## ২) ডুপ্লিকেট সরানো

```python
# সম্পূর্ণ ডুপ্লিকেট সারি বাদ
df = df.drop_duplicates().reset_index(drop=True)
```

---

## ৩) টাইপ কনভার্সন

```python
# তারিখ কলাম পার্স
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# ক্যাটেগরিক্যাল কলাম
cat_cols = ['gender', 'city']
for c in cat_cols:
	df[c] = df[c].astype('category')

# সংখ্যাসূচক হওয়া দরকার এমন কলাম
num_cols = ['age', 'income']
for c in num_cols:
	df[c] = pd.to_numeric(df[c], errors='coerce')
```

---

## ৪) Missing Values হ্যান্ডেলিং

পদ্ধতি বেছে নিন: drop, fill (mean/median/mode), বা model-based imputation।

```python
# অনেক null থাকলে কলাম ড্রপ (উদাহরণ)
null_ratio = df.isna().mean()
to_drop_cols = null_ratio[null_ratio > 0.6].index
df = df.drop(columns=to_drop_cols)

# সংখ্যাসূচক -> median, ক্যাটেগরি -> mode দিয়ে ইম্পিউট
num_cols = df.select_dtypes(include='number').columns
cat_cols = df.select_dtypes(include=['object','category']).columns

for c in num_cols:
	df[c] = df[c].fillna(df[c].median())

for c in cat_cols:
	df[c] = df[c].fillna(df[c].mode().iloc[0])
```

নোট: Modeling পাইপলাইনে imputation স্কেলিংয়ের সাথে করা উত্তম (নিচে দেখুন)।

---

## ৫) Outliers শনাক্ত ও হ্যান্ডেল

IQR ভিত্তিক রুল (Q1, Q3):

```python
import numpy as np

def cap_outliers_iqr(s, k=1.5):
	q1, q3 = s.quantile(0.25), s.quantile(0.75)
	iqr = q3 - q1
	lower, upper = q1 - k*iqr, q3 + k*iqr
	return s.clip(lower, upper)

for c in df.select_dtypes(include='number').columns:
	df[c] = cap_outliers_iqr(df[c])
```

বিকল্প: লগ ট্রান্সফর্ম, Winsorization, বা মডেল-রোবাস্ট পদ্ধতি।

---

## ৬) ফিচার ইঞ্জিনিয়ারিং (ঐচ্ছিক)

```python
# উদাহরণ: তারিখ থেকে বছর/মাস
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month

# ইন্টারঅ্যাকশন/রেশিও
df['income_per_age'] = df['income'] / (df['age'] + 1)
```

---

## ৭) Train/Test Split এবং Pipeline (Data Leakage এড়াতে)

স্কেলার/এনকোডার/ইম্পিউটার সবই পাইপলাইনে রাখুন, যাতে train-এর ওপর fit হয় এবং test-এ কেবল transform হয়।

```python
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge

# Feature/Target আলাদা করুন
X = df.drop(columns=['target'])
y = df['target']

num_features = X.select_dtypes(include='number').columns
cat_features = X.select_dtypes(include=['object','category']).columns

numeric_transformer = Pipeline(steps=[
	('imputer', SimpleImputer(strategy='median')),
	('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
	('imputer', SimpleImputer(strategy='most_frequent')),
	('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocess = ColumnTransformer(
	transformers=[
		('num', numeric_transformer, num_features),
		('cat', categorical_transformer, cat_features)
	]
)

model = Ridge(alpha=1.0)

pipe = Pipeline(steps=[('preprocess', preprocess),
					  ('model', model)])

X_train, X_test, y_train, y_test = train_test_split(
	X, y, test_size=0.2, random_state=42
)

pipe.fit(X_train, y_train)
y_pred = pipe.predict(X_test)

from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print({'MSE': mse, 'R2': r2})
```

---

## ৮) স্কেলিং ও এনকোডিং নোটস

- Ridge/Lasso/Linear মডেলের জন্য scaling গুরুত্বপূর্ণ
- Tree-based মডেলের (RandomForest, XGBoost) জন্য scaling দরকার নেই
- High-cardinality ক্যাটেগরির জন্য Target/Leave-one-out encoding বিবেচ্য

---

## ৯) Cross-Validation সহ পাইপলাইন

```python
from sklearn.model_selection import KFold, cross_val_score
import numpy as np

kfold = KFold(n_splits=5, shuffle=True, random_state=42)
cv_scores = cross_val_score(pipe, X, y, cv=kfold, scoring='neg_mean_squared_error')
rmse = np.sqrt(-cv_scores)
print(f'CV RMSE: {rmse.mean():.4f} ± {rmse.std():.4f}')
```

ইমব্যালান্সড ক্লাসিফিকেশনের জন্য `StratifiedKFold` ব্যবহার করুন।

---

## ১০) সেভ/লোড (Reproducibility)

```python
import joblib

# পাইপলাইন সেভ
joblib.dump(pipe, 'ridge_pipeline.joblib')

# লোড
loaded = joblib.load('ridge_pipeline.joblib')
pred = loaded.predict(X_test)
```

---

## ✅ Best Practices চেকলিস্ট

- [ ] Train/Test split এর আগে target leakage নেই
- [ ] Imputation/Scaling/Encoding পাইপলাইনে
- [ ] Outlier handling যুক্তিযুক্তভাবে প্রয়োগ
- [ ] Missing ratio > 60% হলে কলাম রিভিউ/ড্রপ
- [ ] Cross-validation চালিয়ে স্থিতিশীলতা যাচাই
- [ ] Random state সেট করে reproducibility নিশ্চিত
- [ ] Artifacts (pipeline, encoder) সেভ

---

## 🔗 সংশ্লিষ্ট ফাইল

- `ridge_regression_bangla.md` – রিজ রিগ্রেশন ধারণা
- `multicollinearity.md` – মাল্টিকলিনিয়ারিটি
- `cross validation/Cross_Validation.md` – ক্রস ভ্যালিডেশন ওভারভিউ
- `cross validation/K_Fold_Cross.md` – K-Fold ডিটেইল
- `cross validation/hold_out.md` – Hold-Out পদ্ধতি


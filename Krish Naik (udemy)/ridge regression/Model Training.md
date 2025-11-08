# Model Training (মডেল ট্রেইনিং) — বাংলা গাইড

এই ডকুমেন্টে মেশিন লার্নিং মডেল ট্রেইনিং-এর প্রধান ধাপগুলো সংক্ষেপে বাংলা ভাষায় ব্যাখ্যা করে প্রয়োজনীয় কোড উদাহরণ, ভাল প্র্যাকটিস এবং চেকলিস্ট দেয়া হয়েছে।

---

## ১. ট্রেইন/টেস্ট/ভ্যালিডেশন স্প্লিট

১) Hold-Out (সরল):

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
	X, y, test_size=0.2, random_state=42, stratify=y if is_classification else None
)
```

২) Train/Validation/Test: গবেষণার ক্ষেত্রে ভ্যালিডেশন সেট আলাদা রাখা ভালো hyperparameter tuning-এর জন্য।

৩) Cross-Validation: K-Fold বা StratifiedKFold ব্যবহার করে মডেলটি স্থিতিশীলভাবে যাচাই করা হয়।

---

## ২. স্কেলিং ও পাইপলাইন

প্রিপ্রসেসিং (imputation, scaling, encoding) সবসময় পাইপলাইনে রাখুন যাতে data leakage না হয়।

```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge

num_features = ['age','income']
cat_features = ['city','gender']

numeric_transformer = Pipeline([
	('imputer', SimpleImputer(strategy='median')),
	('scaler', StandardScaler())
])

categorical_transformer = Pipeline([
	('imputer', SimpleImputer(strategy='most_frequent')),
	('ohe', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer([
	('num', numeric_transformer, num_features),
	('cat', categorical_transformer, cat_features)
])

pipe = Pipeline([
	('pre', preprocessor),
	('model', Ridge(alpha=1.0))
])

pipe.fit(X_train, y_train)
```

---

## ৩. হাইপারপ্যারামিটার টিউনিং

১) GridSearchCV (গ্রিড সার্চ): সব কম্বিনেশন পরীক্ষা করে — নির্ভুল কিন্তু ধীর।

```python
from sklearn.model_selection import GridSearchCV

param_grid = {'model__alpha':[0.01, 0.1, 1.0, 10.0]}
grid = GridSearchCV(pipe, param_grid, cv=5, scoring='neg_mean_squared_error')
grid.fit(X_train, y_train)
print(grid.best_params_, grid.best_score_)
```

২) RandomizedSearchCV: বড় স্পেসে দ্রুত পরীক্ষার জন্য উপযোগী।

৩) Bayesian optimization (Optuna, scikit-optimize) — আরো কৌশলগত সার্চ।

Nested CV: যখন feature selection বা tuning করলে inner CV করে তারপর outer CV-এ পরীক্ষা করুন (prevent leakage).

---

## ৪. মেট্রিকস ও মূল্যায়ন

- Regression: MSE, RMSE, MAE, R²
- Classification: Accuracy, Precision, Recall, F1-score, ROC-AUC, PR-AUC

```python
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, classification_report

# Regression
pred = pipe.predict(X_test)
print('RMSE:', mean_squared_error(y_test, pred, squared=False))
print('R2:', r2_score(y_test, pred))

# Classification
pred = pipe.predict(X_test)
print(classification_report(y_test, pred))
```

Confusion matrix এবং ROC curve ভিজ্যুয়ালাইজ করে ভুল ধরুন এবং Threshold tuning করুন যদি প্রয়োজন।

---

## ৫. Class imbalance এর হ্যান্ডলিং

- Resampling: oversampling (SMOTE) বা undersampling
- Class-weight: model arguments (e.g., LogisticRegression(class_weight='balanced'))

```python
from imblearn.over_sampling import SMOTE
sm = SMOTE(random_state=42)
X_res, y_res = sm.fit_resample(X_train, y_train)
```

---

## ৬. Early stopping ও ম্যাট্রিক মনিটরিং

Gradient boosting বা neural networks-এ early stopping ব্যবহার করে overfitting রোধ করা যায়।

```python
from sklearn.ensemble import GradientBoostingRegressor
model = GradientBoostingRegressor(n_estimators=1000)
model.fit(X_train, y_train, 
		  eval_set=[(X_val, y_val)], 
		  early_stopping_rounds=50, 
		  verbose=10)
```

---

## ৭. Model persistence (save/load)

```python
import joblib
joblib.dump(pipe, 'ridge_pipeline.joblib')
loaded = joblib.load('ridge_pipeline.joblib')
```

---

## ৮. Reproducibility

- সব জায়গায় `random_state` বা seed সেট করুন (NumPy, sklearn, libraries)
- versions, environment এবং requirement তালিকা (`requirements.txt`) রাখুন

```python
import numpy as np
np.random.seed(42)
```

---

## ৯. Model monitoring ও Deployment টিপস

- Production-এ মডেল ডিপ্লয় করার আগে: input validation, feature pipeline consistent, logging
- Monitor drift: feature distribution ও prediction distribution পরিবর্তন চেক করুন
- Periodic retraining strategy নির্ধারণ করুন

---

## ১০. Practical Checklist

- [ ] Data split reproducible (random_state)
- [ ] Preprocessing pipeline (impute/scale/encode) তৈরি করা হয়েছে
- [ ] Cross-validation দিয়ে মডেল যাচাই করা হয়েছে
- [ ] Hyperparameter tuning চালানো হয়েছে (Grid/Random/Optuna)
- [ ] Final model পরীক্ষা করা হয়েছে hold-out set এ
- [ ] Model সেভ করা হয়েছে ও reproducible inference নিশ্চিত
- [ ] Monitoring ও retraining পরিকল্পনা আছে

---

## ১১. Quick end-to-end example (Ridge Regression)

```python
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

X, y = make_regression(n_samples=1000, n_features=10, noise=10, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = Ridge(alpha=1.0)
model.fit(X_train, y_train)
pred = model.predict(X_test)
print('RMSE:', mean_squared_error(y_test, pred, squared=False))
```

---

আপনি চাইলে আমি এই গাইড থেকে একটি runnable Jupyter notebook তৈরি করে দেব (`model_training.ipynb`) যাতে প্রতিটি ধাপ cell-by-cell executable ও ভিজ্যুয়াল থাকবে। অথবা আমি নির্দিষ্ট dataset অনুযায়ী কোড কাস্টমাইজ করে দিতে পারি। কোনটা করবেন? 


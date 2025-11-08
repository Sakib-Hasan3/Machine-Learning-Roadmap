# Feature Selection (ফিচার সিলেকশন) — বাংলা গাইড

Feature Selection হলো সেই প্রক্রিয়া যার মাধ্যমে শেখার আগে বা শেখার সময় অপ্রয়োজনীয়, শক্তিশালী নয় এমন বা redundancy থাকা features বাদ দেয়া হয়। এটা model performance, interpretability, ও training time উন্নত করে।

---

## কেন Feature Selection দরকার?
- Overfitting কমাতে সাহায্য করে
- Computation ও storage কমায়
- Model interpretability বাড়ায়
- Multicollinearity কমায় (যেখানে প্রাসঙ্গিক)
- Noisy/irrelevant features সরিয়ে predictive power বাড়ায়

---

## প্রধান পদ্ধতি (Overview)
1. Filter methods
2. Wrapper methods
3. Embedded methods

নিচে প্রতিটির ব্যাখ্যা ও উদাহরণ দেয়া হলো।

---

## ১) Filter Methods (বাহ্যিক মানদণ্ড ভিত্তিক)
নির্বাচন independent ভাবে মেট্রিক (correlation, chi-square, mutual information ইত্যাদি) ব্যবহার করে করা হয় — মডেলের বাইরে।

- Correlation (সংখ্যাসূচক features):

```python
import pandas as pd
import numpy as np

# correlation matrix
corr = df.corr()
# drop highly correlated features
upper = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool))
to_drop = [c for c in upper.columns if any(upper[c].abs() > 0.9)]
df_reduced = df.drop(columns=to_drop)
```

- Variance Threshold (নিম্ন ভেরিয়েন্স ফিচার বাদ দেয়া):

```python
from sklearn.feature_selection import VarianceThreshold
sel = VarianceThreshold(threshold=0.01)
X_selected = sel.fit_transform(X)
```

- Univariate statistics (SelectKBest: chi2, f_classif, f_regression, mutual_info):

```python
from sklearn.feature_selection import SelectKBest, f_classif
selector = SelectKBest(score_func=f_classif, k=10)
X_new = selector.fit_transform(X, y)
```

সুবিধা: দ্রুত, model-agnostic।
অসুবিধা: feature interaction ধরতে পারে না।

---

## ২) Wrapper Methods (মডেল-ভিত্তিক অনুসন্ধান)
মডেল repeatedly train করে feature subsets মূল্যায়ন করে। সাধারণত ভাল ফল দেয় কিন্তু computationally ব্যয়বহুল।

- Recursive Feature Elimination (RFE):

```python
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

est = LogisticRegression(max_iter=500)
rfe = RFE(estimator=est, n_features_to_select=10, step=1)
X_rfe = rfe.fit_transform(X, y)
```

- Sequential Feature Selection (Forward/Backward):

```python
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.ensemble import RandomForestClassifier

est = RandomForestClassifier(n_estimators=100, random_state=42)
sfs = SequentialFeatureSelector(est, n_features_to_select=10, direction='forward')
X_sfs = sfs.fit_transform(X, y)
```

সুবিধা: interaction ধরতে পারে, ফলাফল সাধারণত ভাল।
অসুবিধা: ধীর, বড় feature-set এ খরচ বেশি।

---

## ৩) Embedded Methods (মডেল-এ অন্তর্ভুক্ত)
মডেল ট্রেনিংয়ের সময়ই feature selection ঘটে — যেমন regularization বা tree-based importance।

- Lasso (L1 regularization) — কিছু coefficient কে 0 করে দেয় (feature selection):

```python
from sklearn.linear_model import Lasso
from sklearn.feature_selection import SelectFromModel

lasso = Lasso(alpha=0.01)
sfm = SelectFromModel(lasso).fit(X, y)
X_lasso = sfm.transform(X)
```

- Tree-based feature importance (RandomForest, GradientBoosting):

```python
from sklearn.ensemble import RandomForestClassifier
est = RandomForestClassifier(n_estimators=200, random_state=42)
est.fit(X, y)
importances = est.feature_importances_
```

সুবিধা: দ্রুত, মডেল-নিয়ন্ত্রিত; অসুবিধা: কিছু মডেলে interpretability কম হতে পারে।

---

## বোনাস টেকনিক: Stability selection ও Permutation importance
-- Stability selection: resampling (subsampling) করে বারবার selection করে স্থায়িত্ব দেখা হয়।
-- Permutation importance: একটি feature shuffle করে model performance কমলে সেটা গুরুত্বপূর্ণ।

```python
from sklearn.inspection import permutation_importance
res = permutation_importance(est, X_test, y_test, n_repeats=10, random_state=42)
sorted_idx = res.importances_mean.argsort()
```

---

## VIF (Variance Inflation Factor) — Multicollinearity চেক
VIF ব্যবহার করে বোঝা যায় কোন feature গুলো multicollinearity তে অবদান রাখছে।

```python
import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor

X_numeric = df.select_dtypes(include='number').drop(columns=['target'])
vif = pd.DataFrame()
vif['variable'] = X_numeric.columns
vif['VIF'] = [variance_inflation_factor(X_numeric.values, i) for i in range(X_numeric.shape[1])]
print(vif.sort_values('VIF', ascending=False))
```

নিয়মিক নির্দেশনা: VIF > 5 বা >10 হলে সতর্ক হওয়া উচিত।

---

## Practical workflow (চেকলিস্ট ও কোড)
1. EDA → missing, dtype, distribution, correlation
2. Filter step (low variance, high correlation drop, SelectKBest) — দ্রুত প্রথম কাট
3. Embedded/wrapper step (Lasso, RFE, tree importance) ও cross-validation
4. Final model validation (cross_val_score, permutation importance)

উদাহরণ pipeline (SelectKBest + model) :

```python
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.model_selection import cross_val_score, KFold
from sklearn.linear_model import Ridge
import numpy as np

pipe = Pipeline([
	('select', SelectKBest(score_func=f_regression, k=10)),
	('model', Ridge(alpha=1.0))
])

kfold = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(pipe, X, y, cv=kfold, scoring='neg_mean_squared_error')
print('CV RMSE:', np.sqrt(-scores).mean())
```

---

## Pitfalls ও Best Practices
- সবসময় cross-validation ব্যবহার করে feature selection validate করুন — না হলে selection-এর ফলে data leakage হতে পারে।
- Target-encoding করলে CV-ভিত্তিক scheme বা nested CV ব্যবহার করুন।
- High-cardinality categorical variables এ one-hot না করে mean/target encoding বা embeddings বিবেচনা করুন।
- Multicollinearity থাকলে VIF চেক করে redundant features বাদ দিন অথবা regularized model ব্যবহার করুন (Ridge)।
- Feature selection শেষে final model কে আলাদা hold-out সেটে যাচাই করুন।

---

## দ্রুত রেফারেন্স (কী বেছে নেবেন কখন)
- যদি model-agnostic ও দ্রুত চান → Filter methods
- যদি accuracy সর্বোচ্চ চান এবং computation অনুমতি থাকে → Wrapper methods
- যদি pipeline-এ simplicity ও speed চান → Embedded methods (Lasso, tree importance)

---

## সারণি — কাজের সারাংশ
- [ ] EDA করে শুরু করুন
- [ ] Low-importance/low-variance features বাদ দিন
- [ ] Correlated features মধ্যে থেকে একটিকে বেছে নিন
- [ ] Lasso বা tree importance দিয়ে embedded selection পরীক্ষা করুন
- [ ] RFE/Sequential selection করে পারফরম্যান্স যাচাই করুন
- [ ] Final model cross-validation ও hold-out validation চালান

---

আপনি চাইলে আমি একটি runnable Jupyter notebook (`feature_selection.ipynb`) তৈরি করে দেব যাতে এই পদ্ধতিগুলোতে hands-on উদাহরণ এবং visualization থাকবে। আপনি কি চান আমি সেটা তৈরি করব? 


# EDA ও Feature Engineering (বাংলা গাইড)

এই ডকুমেন্টে Exploratory Data Analysis (EDA) এবং Feature Engineering—দুইটি গুরুত্বপূর্ণ ধাপের বাংলা ব্যাখ্যা, কার্যকরী কোড স্নিপেট ও best-practices দেওয়া হয়েছে। এগুলো মেশিন লার্নিং মডেল তৈরির আগে করা অত্যাবশ্যক কাজ।

---

## অংশ ১: EDA (Exploratory Data Analysis)

EDA হলো ডেটা সম্পর্কে বোঝাপড়া করা — distribution, missing values, correlation, outliers, ও সম্পর্কসমূহ অন্বেষণ করা। সাধারণ ধাপগুলো:

1. ডেটা লোড ও প্রথম চেক
2. Summary statistics
3. Missing values বিশ্লেষণ
4. Distribution ও skewness চেক
5. Categorical feature analysis
6. Relationship & correlation (feature vs target, feature vs feature)
7. Outliers ও extreme values

### ১. ডেটা লোড ও শীর্ষ চেক

```python
import pandas as pd
df = pd.read_csv('data.csv')
df.head()
df.info()
```

### ২. Summary statistics

```python
df.describe(include='all').T
```

### ৩. Missing values বিশ্লেষণ

```python
missing = df.isna().sum().sort_values(ascending=False)
missing[missing > 0]
```

ভিজ্যুয়াল চেক:

```python
import missingno as msno
msno.matrix(df)
msno.heatmap(df)
```

### ৪. Distribution ও skewness

সংখ্যাসূচক ফিচারের জন্য হিস্টোগ্রাম ও KDE প্লট:

```python
import seaborn as sns
import matplotlib.pyplot as plt

num_cols = df.select_dtypes(include='number').columns
for c in num_cols:
	plt.figure()
	sns.histplot(df[c].dropna(), kde=True)
	plt.title(c)
```

skewness = df[num_cols].skew().sort_values(ascending=False)
skewness
```

লগ বা Box-Cox transform দিয়ে skew ঠিক করা যায় যদি দরকার হয়।

### ৫. Categorical feature analysis

```python
cat_cols = df.select_dtypes(include=['object','category']).columns
for c in cat_cols:
	print(c)
	print(df[c].value_counts(normalize=True).head())
	print('-'*40)
```

ভিজ্যুয়াল: বার প্লট

```python
for c in cat_cols:
	plt.figure(figsize=(6,3))
	sns.countplot(y=c, data=df, order=df[c].value_counts().index)
	plt.title(c)
```

### ৬. Correlation এবং সম্পর্ক বিশ্লেষণ

সংখ্যাসূচক ফিচারের মধ্যে correlation heatmap:

```python
plt.figure(figsize=(10,8))
sns.heatmap(df[num_cols].corr(), annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Correlation Matrix')
```

Feature vs Target:

```python
for c in num_cols:
	plt.figure()
	sns.scatterplot(x=df[c], y=df['target'])
	plt.title(f'{c} vs target')
```

Categorical vs Target (classification):

```python
for c in cat_cols:
	display(pd.crosstab(df[c], df['target'], normalize='index'))
```

### ৭. Outliers শনাক্তকরণ

Boxplot বা IQR পদ্ধতি দিয়ে outliers দেখা যায়:

```python
for c in num_cols:
	plt.figure()
	sns.boxplot(x=df[c])
	plt.title(c)
```

IQR ভিত্তিক কাটা/ক্যাপ করা যেতে পারে (see clean_dataset.md)।

---

## অংশ ২: Feature Engineering

Feature Engineering হচ্ছে নতুন উপযুক্ত features তৈরি করে মডেলকে আরও শক্তিশালী করা। সাধারণ কৌশলগুলো:

1. Encoding categorical variables
2. Scaling numeric features
3. Binning / Discretization
4. Interaction & Polynomial features
5. Date/time features
6. Text features (TF-IDF, embeddings)
7. Dimensionality reduction (PCA)
8. Feature selection (Filter/Wrapper/Embedded)

প্রতিটি উপায় সহ উদাহরণ নীচে দেওয়া হল।

### ১. Categorical encoding

- One-Hot Encoding (কম কার্ডিনালিটি):

```python
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(handle_unknown='ignore', sparse=False)
ohe.fit_transform(df[['city']])
```

- Ordinal Encoding (ordered categories):

```python
from sklearn.preprocessing import OrdinalEncoder
ord_enc = OrdinalEncoder()
df['quality_ord'] = ord_enc.fit_transform(df[['quality']])
```

- Target/Mean Encoding (high-cardinality):

```python
mean_enc = df.groupby('user_id')['target'].mean()
df['user_target_mean'] = df['user_id'].map(mean_enc)
```

সতর্কতা: target encoding করলে information leakage এড়াতে cross-validation ভিত্তিক encoding ব্যবহার করুন।

### ২. Scaling

- StandardScaler (mean=0, std=1) — Linear models ও gradient-based algorithms-এ দরকার
- MinMaxScaler — neural networks বা bounded range প্রয়োজন হলে
- RobustScaler — outliers-এ রবারস্ট

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])
```

পাইপলাইনে সেটা fit কেবল train-এ করুন।

### ৩. Binning / Discretization

```python
df['age_bin'] = pd.cut(df['age'], bins=[0,18,35,60,100], labels=False)
```

Categoricalভাবে use করে decision trees বা interaction capture করতে পারেন।

### ৪. Interaction ও Polynomial features

```python
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2, interaction_only=False, include_bias=False)
X_poly = poly.fit_transform(X_num)
```

সতর্কতা: degree বেশি হলে features দ্রুত বেড়ে যায় (curse of dimensionality)।

### ৫. Date/time থেকে features

```python
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['dayofweek'] = df['date'].dt.dayofweek
df['is_weekend'] = df['dayofweek'].isin([5,6]).astype(int)
```

Time series-এ lag, rolling mean, expanding features খুব কার্যকর।

### ৬. Text features

```python
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(max_features=5000)
X_text = tfidf.fit_transform(df['review_text'])
```

এবং পরে sparse matrix কে model pipeline-এ মিলিয়ে ব্যবহার করা যাবে।

### ৭. Dimensionality reduction (PCA)

```python
from sklearn.decomposition import PCA
pca = PCA(n_components=0.95)
X_reduced = pca.fit_transform(X_num)
```

PCA ব্যবহার করে correlated numeric ফিচারগুলোর redundancy কমান।

### ৮. Feature selection

কয়েকটি পদ্ধতি:

- Filter methods: correlation threshold, Chi-square (categorical), mutual information
- Wrapper methods: Recursive Feature Elimination (RFE)
- Embedded methods: 모델-বেসড importance (Tree-based, Lasso)

উদাহরণ — SelectKBest:

```python
from sklearn.feature_selection import SelectKBest, f_regression
selector = SelectKBest(score_func=f_regression, k=10)
X_new = selector.fit_transform(X_num, y)
```

উদাহরণ — RFE:

```python
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier
est = RandomForestClassifier(n_estimators=50, random_state=42)
rfe = RFE(est, n_features_to_select=10)
X_rfe = rfe.fit_transform(X, y)
```

Feature importance দেখার উদাহরণ:

```python
est.fit(X, y)
importances = est.feature_importances_
```

---

## অংশ ৩: Practical pipeline (EDA → FE → Modeling)

নিচে একটি typical pipeline উদাহরণ (sklearn Pipeline & ColumnTransformer) দেয়া হলো:

```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import Ridge

num_transformer = Pipeline([
	('imputer', SimpleImputer(strategy='median')),
	('scaler', StandardScaler())
])

cat_transformer = Pipeline([
	('imputer', SimpleImputer(strategy='most_frequent')),
	('ohe', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer([
	('num', num_transformer, num_cols),
	('cat', cat_transformer, list(cat_cols))
])

pipe = Pipeline([
	('pre', preprocessor),
	('model', Ridge(alpha=1.0))
])

pipe.fit(X_train, y_train)
```

এইভাবে আপনার preprocessing reproducible ও safe থাকে (no data leakage)।

---

## অংশ ৪: Tips, Pitfalls ও Best Practices

- সর্বদা EDA-তে domain knowledge ব্যবহার করুন — সব correlation মানে causation নয়।
- Preprocessing steps (impute/scale/encode) অবশ্যই train-এ fit করে test-এ transform করুন।
- High-cardinality categorical ফিচারে one-hot ব্যবহার না করে target encoding বা embedding বিবেচনা করুন।
- Outliers-কে wholesale drop না করে context অনুযায়ী হ্যান্ডেল করুন।
- Feature selection এর আগে baseline model তৈরি করুন।
- Feature engineering iterative প্রক্রিয়া — cross-validation এ পরীক্ষা করে দেখুন কি কাজ করছে।

---

## শেষ কথা ও চেকলিস্ট

- [ ] Data loaded and inspected
- [ ] Missing values analyzed and imputed appropriately
- [ ] Datatypes converted correctly (dates, categories)
- [ ] Outliers identified & handled
- [ ] Useful features created (date parts, interactions, aggregates)
- [ ] Encoding & scaling applied within pipeline
- [ ] Feature selection / dimensionality reduction considered
- [ ] Model trained with cross-validation

এটি একটি সার্বিক রেফারেন্স; যদি আপনি চান আমি আপনার নির্দিষ্ট dataset-এর উপর ভিত্তি করে একটি `eda_feature.ipynb` তৈরি করে runnable কোড, ভিজ্যুয়াল এবং ফলাফলও দেখিয়ে দিতে পারি।


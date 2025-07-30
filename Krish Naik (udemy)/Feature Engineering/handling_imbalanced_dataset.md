# Handling Imbalanced Dataset - বাংলা টিউটোরিয়াল

## ভূমিকা
Imbalanced dataset হচ্ছে এমন একটি dataset যেখানে বিভিন্ন class এর sample সংখ্যায় ব্যাপক পার্থক্য রয়েছে। উদাহরণস্বরূপ, fraud detection এ 99% normal transaction এবং 1% fraudulent transaction থাকতে পারে।

## প্রাথমিক সেটআপ

### Library Import এবং Data Preparation

```python
import numpy as np
import pandas as pd

# set random seed for reproducibility
np.random.seed(123)

# create a dataframe with two classes
n_samples = 1000
class_0_rate = 0.9
n_class_0 = int(n_samples * class_0_rate)
n_class_1 = n_samples - n_class_0
```

**কোড ব্যাখ্যা:**
- `import numpy as np` - NumPy library import করা numerical operations এর জন্য
- `import pandas as pd` - Pandas library import করা DataFrame manipulation এর জন্য  
- `np.random.seed(123)` - Random seed set করা reproducible results এর জন্য
- `n_samples = 1000` - মোট sample সংখ্যা 1000 define করা
- `class_0_rate = 0.9` - Class 0 এর percentage 90% (majority class)
- `n_class_0 = int(n_samples * class_0_rate)` - Class 0 এর sample সংখ্যা = 900
- `n_class_1 = n_samples - n_class_0` - Class 1 এর sample সংখ্যা = 100

### Class সংখ্যা যাচাই

```python
n_class_0, n_class_1  # Output: (900, 100)
```

এখানে আমরা দেখতে পাচ্ছি যে class 0 এ 900টি sample এবং class 1 এ 100টি sample আছে। এটি একটি imbalanced dataset।

## Imbalanced Dataset তৈরি করা

### Class-wise DataFrame তৈরি

```python
# create my dataframe with imbalaced dataset
class_0 = pd.DataFrame({
    'feature_1': np.random.normal(loc=0, scale=1, size=n_class_0),
    'feature_2': np.random.normal(loc=0, scale=1, size=n_class_0),
    'target': [0]* n_class_0
})

class_1 = pd.DataFrame({
    'feature_1': np.random.normal(loc=0, scale=1, size=n_class_1),
    'feature_2': np.random.normal(loc=0, scale=1, size=n_class_1),
    'target': [1]* n_class_1
})
```

**কোড ব্যাখ্যা:**
- `class_0 = pd.DataFrame({` - Class 0 এর জন্য DataFrame তৈরি
- `'feature_1': np.random.normal(loc=0, scale=1, size=n_class_0)` - Feature 1 এর জন্য 900টি normal distribution values
- `'feature_2': np.random.normal(loc=0, scale=1, size=n_class_0)` - Feature 2 এর জন্য 900টি normal distribution values  
- `'target': [0]* n_class_0` - Target column এ 900টি 0 value
- একইভাবে class_1 এর জন্য 100টি sample তৈরি করা হয়েছে

### Complete Dataset তৈরি

```python
df = pd.concat([class_0, class_1]).reset_index(drop=True)
```

**ব্যাখ্যা:** দুইটি class এর DataFrame কে একসাথে জোড়া দিয়ে complete dataset তৈরি এবং index reset করা।

### Data Exploration

```python
df.head()  # প্রথম 5টি row দেখা
df.tail()  # শেষ 5টি row দেখা  
df['target'].value_counts()  # Class distribution: 0: 900, 1: 100
```

## Upsampling Technique

Upsampling হচ্ছে minority class এর sample বাড়িয়ে majority class এর সাথে balance করার পদ্ধতি।

### Class আলাদা করা

```python
df_minority = df[df['target'] == 1]  # Minority class (100 samples)
df_majority = df[df['target'] == 0]  # Majority class (900 samples)
```

**ব্যাখ্যা:**
- `df_minority` - Target value 1 যেসব row আছে (100টি sample)
- `df_majority` - Target value 0 যেসব row আছে (900টি sample)

### Upsampling Implementation

```python
from sklearn.utils import resample

df_minority_upsampled = resample(df_minority, 
                                replace=True, 
                                n_samples=len(df_majority), 
                                random_state=42)
```

**কোড ব্যাখ্যা:**
- `from sklearn.utils import resample` - Scikit-learn থেকে resample function import
- `df_minority_upsampled = resample(df_minority,` - Minority class resample করা
- `replace=True,` - Replacement সহ sampling (same data point multiple times নেওয়া যাবে)
- `n_samples=len(df_majority),` - Majority class এর সমান sample (900টি)
- `random_state=42` - Reproducible results এর জন্য

### Upsampled Data যাচাই

```python
df_minority_upsampled.shape  # Output: (900, 3)
df_minority_upsampled.head()  # First few rows দেখা
```

### Balanced Dataset তৈরি

```python
df_upsampled = pd.concat([df_majority, df_minority_upsampled])
print(f"Upsampled dataset shape: {df_upsampled.shape}")  # (1800, 3)
df_upsampled['target'].value_counts()  # Both classes: 900 each
```

**ফলাফল:** এখন উভয় class এ 900 করে sample আছে, মোট 1800 samples।

## Downsampling Technique

Downsampling হচ্ছে majority class এর sample কমিয়ে minority class এর সাথে balance করার পদ্ধতি।

### Downsampling Implementation

```python
df_majority_downsampled = resample(df_majority, 
                                  replace=False, 
                                  n_samples=len(df_minority), 
                                  random_state=42)
```

**কোড ব্যাখ্যা:**
- `df_majority_downsampled = resample(df_majority,` - Majority class resample করা
- `replace=False,` - Replacement ছাড়া sampling (একই data point দুইবার নেওয়া হবে না)
- `n_samples=len(df_minority),` - Minority class এর সমান sample (100টি)
- `random_state=42` - Reproducible results

### Downsampled Data যাচাই

```python
df_majority_downsampled.shape  # Output: (100, 3)
df_majority_downsampled.head()  # First few rows দেখা
```

### Balanced Dataset তৈরি

```python
df_downsampled = pd.concat([df_majority_downsampled, df_minority])
print(f"Downsampled dataset shape: {df_downsampled.shape}")  # (200, 3)
df_downsampled['target'].value_counts()  # Both classes: 100 each
```

**ফলাফল:** এখন উভয় class এ 100 করে sample আছে, মোট 200 samples।

## SMOTE (Synthetic Minority Oversampling Technique)

SMOTE একটি advanced technique যা synthetic data তৈরি করে minority class এর জন্য। এটি existing data points এর মধ্যে interpolation করে নতুন synthetic samples তৈরি করে।

### SMOTE Implementation

```python
from imblearn.over_sampling import SMOTE

# SMOTE technique apply করা
smote = SMOTE(random_state=42)
X = df[['feature_1', 'feature_2']]  # Features
y = df['target']  # Target variable

X_smote, y_smote = smote.fit_resample(X, y)
```

**কোড ব্যাখ্যা:**
- `from imblearn.over_sampling import SMOTE` - Imbalanced-learn library থেকে SMOTE import
- `smote = SMOTE(random_state=42)` - SMOTE object তৈরি
- `X = df[['feature_1', 'feature_2']]` - Feature columns আলাদা করা
- `y = df['target']` - Target column আলাদা করা
- `X_smote, y_smote = smote.fit_resample(X, y)` - SMOTE apply করে synthetic data তৈরি

### SMOTE Results তুলনা

```python
print(f"Original dataset shape: {X.shape}")  # (1000, 2)
print(f"SMOTE dataset shape: {X_smote.shape}")  # (1800, 2)
print(f"Original class distribution: {pd.Series(y).value_counts().to_dict()}")  # {0: 900, 1: 100}
print(f"SMOTE class distribution: {pd.Series(y_smote).value_counts().to_dict()}")  # {0: 900, 1: 900}
```

## তিনটি Technique এর তুলনা

| Technique | Original Shape | Final Shape | Pros | Cons |
|-----------|---------------|-------------|------|------|
| **Upsampling** | (1000, 3) | (1800, 3) | Simple, Fast | Overfitting এর সম্ভাবনা |
| **Downsampling** | (1000, 3) | (200, 3) | Simple, Fast | Data loss হয় |
| **SMOTE** | (1000, 2) | (1800, 2) | Synthetic data, No overfitting | Computationally expensive |

## কখন কোন Technique ব্যবহার করবেন

### Upsampling ব্যবহার করুন যখন:
- আপনার কাছে পর্যাপ্ত computational resources আছে
- Dataset size বড় করতে চান
- Simple solution চান

### Downsampling ব্যবহার করুন যখন:
- Dataset অনেক বড় এবং computational resources কম
- Training time কমাতে চান
- Data loss নিয়ে সমস্যা নেই

### SMOTE ব্যবহার করুন যখন:
- High-quality synthetic data চান
- Overfitting avoid করতে চান
- Best performance চান (usually)

## সারসংক্ষেপ

Imbalanced dataset handle করার জন্য তিনটি প্রধান technique রয়েছে:

1. **Upsampling**: Minority class এর sample duplicate করে বাড়ানো
2. **Downsampling**: Majority class এর sample কমানো  
3. **SMOTE**: Synthetic minority samples তৈরি করা

প্রতিটি technique এর নিজস্ব সুবিধা এবং অসুবিধা আছে। আপনার specific use case এবং dataset এর উপর ভিত্তি করে সঠিক technique বেছে নিতে হবে।

## আরও Advanced Techniques

- **ADASYN** (Adaptive Synthetic Sampling)
- **Borderline-SMOTE**
- **SMOTE + ENN** (Edited Nearest Neighbours)
- **SMOTE + Tomek Links**

এই techniques গুলো আরও sophisticated approaches যা specific scenarios এ ভাল কাজ করে।

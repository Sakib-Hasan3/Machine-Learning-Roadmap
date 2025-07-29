# One Hot Encoding - বাংলা টিউটোরিয়াল

## সূচিপত্র
1. [One Hot Encoding কি?](#one-hot-encoding-কি)
2. [কেন প্রয়োজন?](#কেন-প্রয়োজন)
3. [Step by Step Implementation](#step-by-step-implementation)
4. [Advanced Options](#advanced-options)
5. [Best Practices](#best-practices)
6. [তুলনা: Label Encoding vs One Hot Encoding](#তুলনা-label-encoding-vs-one-hot-encoding)

---

## One Hot Encoding কি?

One Hot Encoding হলো একটি preprocessing technique যা categorical data কে binary columns এ convert করে। প্রতিটি unique category এর জন্য আলাদা column তৈরি হয় যেখানে:
- **1** মানে সেই category present
- **0** মানে সেই category absent

**উদাহরণ:**
```
Original:     One Hot Encoded:
Category      Category_A  Category_B  Category_C
A             1           0           0
B             0           1           0
C             0           0           1
```

---

## কেন প্রয়োজন?

### ❌ Label Encoding এর সমস্যা:
```python
# Label Encoding
['A', 'B', 'C'] → [0, 1, 2]
# Model মনে করে: A < B < C (artificial ordering)
```

### ✅ One Hot Encoding এর সমাধান:
```python
# One Hot Encoding
A → [1, 0, 0]
B → [0, 1, 0]  
C → [0, 0, 1]
# কোনো artificial ordering নেই
```

---

## Step by Step Implementation

### Step 1: Library Import

```python
import pandas as pd
```

**ব্যাখ্যা:**
- `pandas` library import করা হচ্ছে data manipulation এর জন্য
- `pd` alias ব্যবহার করা হচ্ছে সংক্ষেপে লেখার জন্য

### Step 2: Sample Data তৈরি

```python
data = {'Category': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C']}
```

**ব্যাখ্যা:**
- একটি dictionary তৈরি করা হচ্ছে
- 'Category' column এ তিনটি unique values: 'A', 'B', 'C'
- মোট 9টি entries যাতে প্রতিটি category 3 বার repeat হয়েছে

### Step 3: DataFrame তৈরি

```python
df = pd.DataFrame(data)
df.head()
```

**লাইন বাই লাইন ব্যাখ্যা:**
- `df = pd.DataFrame(data)` - Dictionary থেকে pandas DataFrame তৈরি
- `df.head()` - প্রথম 5 rows display করা

**Output:**
```
   Category
0         A
1         B
2         C
3         A
4         B
```

### Step 4: Basic One Hot Encoding

```python
one_hot_encoded_df = pd.get_dummies(df, columns=['Category'])
one_hot_encoded_df
```

**ব্যাখ্যা:**
- `pd.get_dummies()` - pandas এর built-in one hot encoding function
- `columns=['Category']` - যে column encode করতে হবে

**Output:**
```
   Category_A  Category_B  Category_C
0           1           0           0
1           0           1           0
2           0           0           1
3           1           0           0
4           0           1           0
5           0           0           1
6           1           0           0
7           0           1           0
8           0           0           1
```

**ফলাফল:**
- Original 'Category' column সরে গেছে
- 3টি নতুন binary column তৈরি হয়েছে
- প্রতিটি row এ শুধু একটি column এ 1, বাকি সব 0

---

## Advanced Options

### Option 1: Custom Prefix ব্যবহার

```python
one_hot_encoded_df = pd.get_dummies(df, columns=['Category'], prefix='Dummy')
one_hot_encoded_df
```

**ব্যাখ্যা:**
- `prefix='Dummy'` - column names এর জন্য custom prefix
- Better readability এবং meaningful names

**Output:**
```
   Dummy_A  Dummy_B  Dummy_C
0        1        0        0
1        0        1        0
2        0        0        1
...
```

**সুবিধা:**
- Column names আরো clear এবং descriptive
- Multiple categorical columns থাকলে confusion এড়ানো যায়

### Option 2: Drop First Column (Recommended)

```python
one_hot_encoded_df = pd.get_dummies(df, columns=['Category'], prefix='Dummy', drop_first=True)
one_hot_encoded_df
```

**ব্যাখ্যা:**
- `drop_first=True` - প্রথম dummy column drop করে
- **কেন প্রয়োজন?** Dummy Variable Trap এড়ানোর জন্য

**Output:**
```
   Dummy_B  Dummy_C
0        0        0  # এর মানে A
1        1        0  # এর মানে B
2        0        1  # এর মানে C
3        0        0  # এর মানে A
4        1        0  # এর মানে B
...
```

**Logic:**
- যদি `Dummy_B=0` এবং `Dummy_C=0` → Category = 'A'
- যদি `Dummy_B=1` এবং `Dummy_C=0` → Category = 'B'
- যদি `Dummy_B=0` এবং `Dummy_C=1` → Category = 'C'

### Step 5: Original Data Verification

```python
df.head()
```

**ব্যাখ্যা:**
- Original DataFrame আবার check করা
- Confirm করা যে original data unchanged
- One hot encoding নতুন DataFrame তৈরি করে, original modify করে না

---

## Best Practices

### 1. কখন One Hot Encoding ব্যবহার করবেন?

✅ **ব্যবহার করুন যখন:**
- Non-ordinal categorical data আছে
- Categories এর মধ্যে কোনো natural ordering নেই
- Linear models (Linear Regression, Logistic Regression) ব্যবহার করছেন

❌ **ব্যবহার করবেন না যখন:**
- Ordinal data আছে (High cardinality)
- অনেক unique categories আছে (>10-15)
- Tree-based models ব্যবহার করছেন (Random Forest, XGBoost)

### 2. Dummy Variable Trap

```python
# ❌ ভুল approach (3 columns)
Category_A  Category_B  Category_C
1           0           0
0           1           0
0           0           1

# ✅ সঠিক approach (2 columns)
Category_B  Category_C
0           0  # Automatically A
1           0  # B
0           1  # C
```

**কেন drop_first=True?**
- Perfect multicollinearity এড়ানো
- Model performance improve করা
- Overfitting reduce করা

### 3. High Cardinality Handle করা

```python
# যদি অনেক categories থাকে
unique_categories = df['Category'].nunique()
if unique_categories > 10:
    # Consider other encoding techniques
    # - Target Encoding
    # - Frequency Encoding
    # - Binary Encoding
    pass
```

---

## তুলনা: Label Encoding vs One Hot Encoding

| বৈশিষ্ট্য | Label Encoding | One Hot Encoding |
|---------|----------------|------------------|
| **Output Format** | Single column (integers) | Multiple binary columns |
| **Ordering** | Creates artificial ordering | No ordering |
| **Memory Usage** | Low | Higher |
| **Suitable for** | Ordinal data | Non-ordinal data |
| **Model Types** | Tree-based models | Linear models |
| **High Cardinality** | Handles well | Not recommended |

### Example Comparison:

```python
# Original Data
categories = ['Red', 'Green', 'Blue', 'Red', 'Green']

# Label Encoding
# Red=0, Green=1, Blue=2
# [0, 1, 2, 0, 1]
# সমস্যা: Red < Green < Blue (ভুল assumption)

# One Hot Encoding
# Red → [1,0,0], Green → [0,1,0], Blue → [0,0,1]
# [[1,0,0], [0,1,0], [0,0,1], [1,0,0], [0,1,0]]
# সুবিধা: কোনো ordering নেই
```

---

## Advanced Techniques

### 1. Multiple Columns একসাথে Encode করা

```python
# Multiple categorical columns
df_multi = pd.DataFrame({
    'Color': ['Red', 'Green', 'Blue'],
    'Size': ['Small', 'Medium', 'Large']
})

# Encode both columns
encoded = pd.get_dummies(df_multi, columns=['Color', 'Size'], drop_first=True)
```

### 2. Scikit-learn OneHotEncoder

```python
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(drop='first', sparse=False)
encoded_array = encoder.fit_transform(df[['Category']])
```

### 3. Custom Handling for Unknown Categories

```python
# Training data
train_categories = ['A', 'B', 'C']

# Test data with unknown category
test_data = ['A', 'B', 'D']  # 'D' is unknown

# Handle unknown categories
test_data_cleaned = ['A' if x in train_categories else 'Unknown' for x in test_data]
```

---

## Real-world Example

```python
# E-commerce dataset
data = {
    'Product_Category': ['Electronics', 'Clothing', 'Books', 'Electronics', 'Clothing'],
    'Customer_Segment': ['Premium', 'Regular', 'Premium', 'Regular', 'Premium'],
    'Sales': [1000, 500, 200, 1200, 800]
}

df = pd.DataFrame(data)

# One Hot Encoding for ML model
df_encoded = pd.get_dummies(df, 
                           columns=['Product_Category', 'Customer_Segment'],
                           prefix=['Product', 'Customer'],
                           drop_first=True)

print("Encoded DataFrame:")
print(df_encoded)
```

---

## সারসংক্ষেপ

One Hot Encoding একটি powerful technique যা:

🎯 **Non-ordinal categorical data handle করে**  
🎯 **Artificial ordering এর সমস্যা সমাধান করে**  
🎯 **Linear models এর জন্য ideal**  
🎯 **Interpretable results দেয়**  

**মনে রাখার বিষয়:**
- High cardinality data এর জন্য suitable নয়
- Memory usage বেশি হতে পারে
- সবসময় `drop_first=True` ব্যবহার করুন
- Data এর nature অনুযায়ী encoding technique choose করুন

---

**পরবর্তী পদক্ষেপ:** Target Encoding, Frequency Encoding এবং অন্যান্য advanced encoding techniques শিখুন।

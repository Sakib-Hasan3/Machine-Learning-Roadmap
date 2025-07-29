# Label Encoder - বাংলা টিউটোরিয়াল

## সূচিপত্র
1. [Label Encoding কি?](#label-encoding-কি)
2. [Manual Label Encoding](#manual-label-encoding)
3. [Sklearn Label Encoder](#sklearn-label-encoder)
4. [তুলনা](#তুলনা)
5. [ব্যবহারের ক্ষেত্র](#ব্যবহারের-ক্ষেত্র)
6. [সতর্কতা](#সতর্কতা)

---

## Label Encoding কি?

Label Encoding হলো একটি preprocessing technique যা categorical data (text labels) কে numerical data (integers) তে convert করে। Machine Learning algorithms সাধারণত numerical data নিয়ে কাজ করে, তাই categorical data কে numbers এ convert করা প্রয়োজন।

**উদাহরণ:**
- `['classA', 'classB', 'classC']` → `[0, 1, 2]`

---

## Manual Label Encoding

### ডেটা প্রস্তুতি

```python
classes = ['classA', 'classB', 'classC', 'classD']

instances = ['classA','classB','classC','classD','classA','classB','classC','classD','classA','classB']
```

**লাইন বাই লাইন ব্যাখ্যা:**
- `classes = ['classA', 'classB', 'classC', 'classD']` - চারটি unique class/category define করা হচ্ছে
- `instances = ['classA','classB',...,'classB']` - একটি list তৈরি করা হচ্ছে যাতে বিভিন্ন classes এর instances আছে (total 10টি items)

### Encoding Dictionary তৈরি

```python
label_to_int ={label: index for index, label in enumerate(classes)}
```

**ব্যাখ্যা:**
- Dictionary comprehension ব্যবহার করে একটি mapping তৈরি করা হচ্ছে
- `enumerate(classes)` প্রতিটি class এর জন্য index এবং value return করে
- **কিভাবে কাজ করে:** `enumerate(['classA', 'classB', 'classC', 'classD'])` → `(0, 'classA'), (1, 'classB'), (2, 'classC'), (3, 'classD')`
- **Result:** `{'classA': 0, 'classB': 1, 'classC': 2, 'classD': 3}`

### Labels কে Numbers এ Convert করা

```python
encoded_labels = [label_to_int[label] for label in instances]
print(encoded_labels)
```

**ব্যাখ্যা:**
- List comprehension ব্যবহার করে instances এর প্রতিটি label কে integer এ convert করা
- `label_to_int[label]` dictionary থেকে corresponding integer value নেওয়া
- `print(encoded_labels)` - converted integers print করা
- **Output:** `[0, 1, 2, 3, 0, 1, 2, 3, 0, 1]`

### Decoding (Numbers থেকে Labels এ ফিরে যাওয়া)

```python
int_to_label = {index: label for index, label in enumerate(classes)}
decoded_labels = [int_to_label[index] for index in encoded_labels]
print(encoded_labels)
print(decoded_labels)
```

**লাইন বাই লাইন ব্যাখ্যা:**
- `int_to_label = {index: label for index, label in enumerate(classes)}` - Reverse mapping তৈরি করা (integer থেকে label এ ফিরে যাওয়ার জন্য)
- **Result:** `{0: 'classA', 1: 'classB', 2: 'classC', 3: 'classD'}`
- `decoded_labels = [int_to_label[index] for index in encoded_labels]` - Encoded integers কে আবার original labels এ convert করা
- `print(encoded_labels)` - Encoded values: `[0, 1, 2, 3, 0, 1, 2, 3, 0, 1]`
- `print(decoded_labels)` - Decoded values: `['classA', 'classB', 'classC', 'classD', 'classA', 'classB', 'classC', 'classD', 'classA', 'classB']`

---

## Sklearn Label Encoder

### Library Import

```python
from sklearn.preprocessing import LabelEncoder
```

**ব্যাখ্যা:**
- Sklearn library থেকে LabelEncoder class import করা হচ্ছে
- এটি professional-grade label encoding tool

### Encoder Object তৈরি এবং Encoding

```python
label_encoder= LabelEncoder()
encoded_labels = label_encoder.fit_transform(instances)
print(encoded_labels)
```

**লাইন বাই লাইন ব্যাখ্যা:**
- `label_encoder= LabelEncoder()` - LabelEncoder object তৈরি করা
- `encoded_labels = label_encoder.fit_transform(instances)` - একসাথে fit এবং transform করা:
  - **fit()**: Unique labels learn করা এবং mapping তৈরি করা
  - **transform()**: Labels কে integers এ convert করা
- `print(encoded_labels)` - Encoded array print করা
- **Output:** `[0 1 2 3 0 1 2 3 0 1]` (numpy array format)

### Inverse Transform (Decoding)

```python
original_labels = label_encoder.inverse_transform(encoded_labels)
print(encoded_labels)
print(original_labels)
```

**লাইন বাই লাইন ব্যাখ্যা:**
- `original_labels = label_encoder.inverse_transform(encoded_labels)` - Encoded integers কে আবার original labels এ convert করা
- `print(encoded_labels)` - Encoded values: `[0 1 2 3 0 1 2 3 0 1]`
- `print(original_labels)` - Original labels: `['classA' 'classB' 'classC' 'classD' 'classA' 'classB' 'classC' 'classD' 'classA' 'classB']`

---

## তুলনা

| বৈশিষ্ট্য | Manual Approach | Sklearn LabelEncoder |
|---------|------------------|---------------------|
| **Code Length** | বেশি | কম |
| **Error Handling** | Manual | Built-in |
| **Performance** | Slower | Optimized |
| **Flexibility** | High | Standard |
| **Industry Standard** | No | Yes |
| **Memory Usage** | Higher | Optimized |

### Manual Approach এর সুবিধা:
✅ সম্পূর্ণ control  
✅ Custom logic implement করা যায়  
✅ Learning purpose এর জন্য ভালো  

### Manual Approach এর অসুবিধা:
❌ বেশি code লিখতে হয়  
❌ Error prone  
❌ Performance কম  

### Sklearn Approach এর সুবিধা:
✅ Industry standard  
✅ Optimized performance  
✅ Built-in error handling  
✅ কম code  
✅ Robust এবং tested  

### Sklearn Approach এর অসুবিধা:
❌ Limited customization  
❌ Additional dependency  

---

## ব্যবহারের ক্ষেত্র

### ১. Machine Learning Preprocessing
```python
# Categorical features এর জন্য
education = ['High School', 'Bachelor', 'Master', 'PhD']
# → [0, 1, 2, 3]
```

### ২. Data Analysis
```python
# Survey responses
satisfaction = ['Poor', 'Fair', 'Good', 'Excellent']
# → [0, 1, 2, 3]
```

### ৩. Deep Learning
```python
# Image classifications
classes = ['cat', 'dog', 'bird', 'fish']
# → [0, 1, 2, 3]
```

---

## সতর্কতা

### ⚠️ Ordinal Relationship সমস্যা

Label Encoding একটি **ordinal relationship** তৈরি করে:
- `0 < 1 < 2 < 3`
- Model মনে করতে পারে যে `classD` (3) > `classA` (0)

### ❌ কখন ব্যবহার করবেন না:

```python
# Non-ordinal categorical data
colors = ['Red', 'Green', 'Blue']
# Red < Green < Blue - এটি logically সঠিক নয়
```

### ✅ কখন ব্যবহার করবেন:

```python
# Ordinal categorical data
grades = ['F', 'D', 'C', 'B', 'A']
# F < D < C < B < A - এটি logically সঠিক
```

### 🔧 Alternative Solution:

Non-ordinal data এর জন্য **One-Hot Encoding** ব্যবহার করুন:

```python
from sklearn.preprocessing import OneHotEncoder

# One-Hot Encoding
colors = ['Red', 'Green', 'Blue']
# Red → [1, 0, 0]
# Green → [0, 1, 0]  
# Blue → [0, 0, 1]
```

---

## Best Practices

### 1. সঠিক Method নির্বাচন
- **Ordinal data** → Label Encoding
- **Non-ordinal data** → One-Hot Encoding

### 2. Production Code এ
- Sklearn LabelEncoder ব্যবহার করুন
- Manual approach শুধু learning এর জন্য

### 3. Data Validation
```python
# Unknown labels handle করা
try:
    encoded = label_encoder.transform(['new_class'])
except ValueError:
    print("Unknown label encountered!")
```

### 4. Save/Load Encoder
```python
import joblib

# Save encoder
joblib.dump(label_encoder, 'label_encoder.pkl')

# Load encoder
loaded_encoder = joblib.load('label_encoder.pkl')
```

---

## সারসংক্ষেপ

Label Encoding একটি essential preprocessing technique যা:

🎯 **Categorical data কে numerical data তে convert করে**  
🎯 **Machine Learning models এর জন্য data prepare করে**  
🎯 **Memory efficient এবং processing friendly**  

তবে সঠিক context এ ব্যবহার করা গুরুত্বপূর্ণ। Ordinal relationship না থাকলে One-Hot Encoding consider করুন।

---

**মনে রাখবেন:** সব categorical data একইভাবে handle করা যায় না। Data এর nature বুঝে সঠিক encoding technique নির্বাচন করুন।

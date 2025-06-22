# 📘 Pandas দিয়ে JSON ফাইল নিয়ে সম্পূর্ণ কাজ (বাংলা নোট)

এই নোটে Python এবং Pandas ব্যবহার করে JSON ফাইলের উপর যেকোনো ধরনের অপারেশন কিভাবে করতে হয় তা ধাপে ধাপে দেখানো হয়েছে।

---

## ✅ Step 1: JSON ফাইল পড়া (Read JSON)

```python
import pandas as pd

# JSON ফাইল পড়া
df = pd.read_json('data.json')

# প্রিন্ট করা
print(df)
```

---

## ✅ Step 2: Nested JSON ফ্ল্যাট করা

```python
import json
from pandas import json_normalize

with open('data.json') as f:
    data = json.load(f)

# nested JSON কে ফ্ল্যাট করা
df = json_normalize(data)
```

---

## ✅ Step 3: কলাম যাচাই করা

```python
print(df.columns)
```

---

## ✅ Step 4: নির্দিষ্ট কলাম দেখানো

```python
print(df['name'])
print(df[['name', 'city']])
```

---

## ✅ Step 5: ফিল্টার করা (Filtering)

```python
# যাদের বয়স ২৫ এর বেশি
df[df['age'] > 25]

# যাদের ইংরেজি নম্বর ৮৫ এর বেশি
df[df['english'] > 85]
```

---

## ✅ Step 6: নতুন কলাম যোগ করা

```python
df['total'] = df['math'] + df['english']
df['average'] = df['total'] / 2
```

---

## ✅ Step 7: apply() দিয়ে শর্ত ভিত্তিক ক্যাটাগরি তৈরি

```python
df['category'] = df['math'].apply(lambda x: 'Topper' if x >= 90 else 'Average')
```

---

## ✅ Step 8: missing value পূরণ

```python
df['city'] = df['city'].fillna("Unknown")
```

---

## ✅ Step 9: string ফরম্যাট পরিবর্তন

```python
df['name'] = df['name'].str.lower()
```

---

## ✅ Step 10: JSON থেকে CSV ফাইল তৈরি

```python
df.to_csv("data.csv", index=False)
```

---

## ✅ Step 11: JSON এ সেভ করা

```python
df.to_json("new_data.json", orient='records', indent=4)
```

---

## ✅ Step 12: JSON-এর বিভিন্ন ফরম্যাট (orient)

| ফরম্যাট | ব্যবহার |
|---------|---------|
| records | list of dicts (প্রচলিত) |
| index   | index ভিত্তিক |
| split   | আলাদা অংশে বিভক্ত (index, columns, data) |
| table   | schema সহ |
| columns | dict of columns |

```python
df.to_json("data_records.json", orient="records")
df.to_json("data_split.json", orient="split")
```

---

## 🏁 উপসংহার:

- `read_json()` → JSON পড়তে
- `json_normalize()` → nested JSON ফ্ল্যাট করতে
- `to_json()` → JSON ফাইলে লিখতে
- `fillna()`, `apply()`, `str.lower()` → ডেটা পরিষ্কার করতে

এই নোটটি অনুসরণ করে আপনি যে কোনো ধরনের JSON ডেটা প্রক্রিয়াজাত করতে পারবেন Pandas দিয়ে।

---

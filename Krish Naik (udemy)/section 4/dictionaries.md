# 📘 Python Dictionary — সম্পূর্ণ বাংলা নোট

---

## 🔹 Dictionary কী?

**Dictionary** হলো পাইথনের একটি ডেটা স্ট্রাকচার যা **key-value pair** আকারে ডেটা সংরক্ষণ করে।

🔑 প্রতিটি key এর সাথে একটি নির্দিষ্ট value যুক্ত থাকে।

📌 এটি **unordered** এবং **mutable** — মানে উপাদান যোগ, মুছে ফেলা, পরিবর্তন করা যায়।

---

## ✅ Dictionary তৈরি করার নিয়ম

```python
student = {
    "name": "Sakib",
    "age": 22,
    "dept": "CSE"
}
```

🎯 আউটপুট:
```
{'name': 'Sakib', 'age': 22, 'dept': 'CSE'}
```

📘 ব্যাখ্যা:
- প্রতিটি key এবং value `:` দিয়ে আলাদা করা হয়
- key-value pair গুলো `,` দিয়ে আলাদা করা হয়
- `{}` ব্রেস ব্যবহার করা হয়

---

## 🔹 Dictionary Access (মান বের করা)

```python
print(student["name"])      # Sakib
print(student.get("age"))   # 22
```

📌 `[]` দিয়ে access করলে key না থাকলে `KeyError` দিবে  
📌 `.get()` দিয়ে access করলে key না থাকলে `None` রিটার্ন করবে

---

## 🔹 মান পরিবর্তন

```python
student["age"] = 23
```

---

## 🔹 নতুন মান যোগ করা

```python
student["university"] = "PSTU"
```

---

## 🔹 Dictionary এর Loop

```python
for key in student:
    print(key, ":", student[key])
```

অথবা:

```python
for key, value in student.items():
    print(key, value)
```

---

## 🔹 Built-in Methods

### ✅ keys()
```python
print(student.keys())
# dict_keys(['name', 'age', 'dept'])
```

### ✅ values()
```python
print(student.values())
# dict_values(['Sakib', 23, 'CSE'])
```

### ✅ items()
```python
print(student.items())
# dict_items([('name', 'Sakib'), ('age', 23), ('dept', 'CSE')])
```

### ✅ update()
```python
student.update({"age": 24, "dept": "EEE"})
```

### ✅ pop()
```python
student.pop("dept")
```

### ✅ popitem()
```python
student.popitem()  # শেষ item সরিয়ে দেয় (Python 3.7+)
```

### ✅ clear()
```python
student.clear()
```

---

## 🔹 Dictionary Comprehension

```python
squares = {x: x**2 for x in range(5)}
print(squares)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

---

## 🔹 Nested Dictionary

```python
students = {
    "sakib": {"age": 22, "dept": "CSE"},
    "rahim": {"age": 23, "dept": "BBA"}
}

print(students["rahim"]["dept"])  # BBA
```

---

## 🔹 Key থাকতে কিনা চেক করা

```python
if "age" in student:
    print("Age exists")
```

---

## 🔹 Dictionary থেকে List

```python
keys = list(student.keys())
values = list(student.values())
items = list(student.items())
```

---

## 📌 Dictionary vs List vs Set vs Tuple

| Feature       | Dictionary            | List              | Tuple            | Set             |
|---------------|------------------------|-------------------|------------------|-----------------|
| Syntax        | `{}` + key:value       | `[]`              | `()`             | `{}`            |
| Ordered       | ✅ (Python 3.7+)        | ✅                | ✅                | ❌              |
| Mutable       | ✅                      | ✅                | ❌               | ✅              |
| Duplicate Key | ❌ (একই key দুইবার হয় না) | ✅                | ✅                | ❌              |
| Indexed       | ❌ (Key দিয়ে Access)     | ✅                | ✅                | ❌              |

---

## ✅ কখন Dictionary ব্যবহার করবেন?

- ✅ যখন প্রতিটি মানের সাথে একটি নাম (key) যুক্ত করতে চান
- ✅ যখন ডেটা তে structure এবং meaning রাখতে চান
- ✅ যখন দ্রুত lookup দরকার key দিয়ে

---

## 📝 উপসংহার:

- Dictionary হলো key-value pair ডেটা রাখার জন্য সবচেয়ে শক্তিশালী ও জনপ্রিয় স্ট্রাকচার
- এটি অনেক দ্রুত কাজ করে এবং খুবই গুরুত্বপূর্ণ real-world application-এ
- ব্যবহার সহজ, কিন্তু nested বা বড় dictionary-তে loop বা structure বুঝে কাজ করতে হয়

---


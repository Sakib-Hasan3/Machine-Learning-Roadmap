
# 🔷 Python Data Structures: Set, Dictionary, Tuple

A beginner-friendly guide to understanding and using **Set**, **Dictionary**, and **Tuple** in Python. Explained in Bengali (বাংলা) with syntax and examples.

---

## 🔷 **সেট (Set)**  
**সেট** হলো এক ধরনের ডেটা স্ট্রাকচার যা **ইউনিক (unique)** এবং **আনঅর্ডারড (unordered)** এলিমেন্ট ধারণ করে।

### ✅ সেট তৈরি:
```python
my_set = {1, 2, 3}  
set2 = set([4, 5, 6])
```

### ✅ এলিমেন্ট যোগ:
```python
my_set.add(4)
```

### ✅ এলিমেন্ট মুছা:
```python
my_set.remove(2)       # এলিমেন্ট না থাকলে error দিবে  
my_set.discard(2)      # এলিমেন্ট না থাকলে কিছু হবে না
```

### ✅ সেট অপারেশন:
```python
a = {1, 2, 3}  
b = {3, 4, 5}

a.union(b)                # {1, 2, 3, 4, 5}  
a.intersection(b)         # {3}  
a.difference(b)           # {1, 2}  
a.symmetric_difference(b) # {1, 2, 4, 5}
```

---

## 🔷 **ডিকশনারি (Dictionary)**  
**ডিকশনারি** হলো **key-value pairs** এর সংগ্রহ, যা **অর্ডারড (ordered)** এবং **মিউটেবল (mutable)**।

### ✅ ডিকশনারি তৈরি:
```python
my_dict = {"name": "Alice", "age": 25}
```

### ✅ অ্যাক্সেস:
```python
my_dict["name"]      # Output: Alice  
my_dict.get("age")   # Output: 25
```

### ✅ আপডেট ও নতুন ভ্যালু যোগ:
```python
my_dict["age"] = 26           # আপডেট  
my_dict["city"] = "Paris"     # নতুন key যোগ
```

### ✅ রিমুভ:
```python
del my_dict["name"]     # নির্দিষ্ট key মুছে ফেলা  
my_dict.pop("age")      # key ও value রিমুভ  
my_dict.clear()         # সবকিছু মুছে ফেলে
```

### ✅ লুপিং:
```python
for key, value in my_dict.items():  
    print(key, value)
```

---

## 🔷 **টাপল (Tuple)**  
**টাপল** হলো **অর্ডারড (ordered)** এবং **ইমিউটেবল (immutable)** কালেকশন।

### ✅ টাপল তৈরি:
```python
my_tuple = (1, 2, 3)  
single = (5,)  # একক টাপল তৈরি করতে কমা দিতে হয়
```

### ✅ অ্যাক্সেস:
```python
my_tuple[0]      # Output: 1
```

### ✅ অপারেশন:
```python
len(my_tuple)          # টাপলের দৈর্ঘ্য  
my_tuple.count(2)      # 2 কয়বার আছে  
my_tuple.index(3)      # 3 কোন ইনডেক্সে আছে
```

### ✅ স্লাইসিং:
```python
my_tuple[1:3]     # Output: (2, 3)
```

### ✅ নেস্টেড টাপল:
```python
nested = (1, (2, 3), 4)  
nested[1][0]      # Output: 2
```

---

📘 Made with ❤️ to help you learn Python more easily in your native language.

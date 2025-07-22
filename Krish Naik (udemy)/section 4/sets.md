# 🧠 Python Set — বাংলা নোট

---

## 🔹 Set কী?

**Set** হলো পাইথনের একটি **unordered** এবং **unindexed** ডেটা স্ট্রাকচার, যা **unique (অদ্বিতীয়)** উপাদান রাখে।

📌 অর্থাৎ — কোনো উপাদান একাধিকবার রাখা যাবে না।

---

## 🔹 Set তৈরি করার নিয়ম

```python
my_set = {1, 2, 3, 4}
print(my_set)
```

🎯 আউটপুট:
```
{1, 2, 3, 4}
```

📘 ব্যাখ্যা: `{}` ব্রেস ব্যবহার করে set তৈরি করা হয়। প্রত্যেকটি মান ইউনিক হয়।

---

## 🔹 মিশ্র ডেটা টাইপেও set বানানো যায়

```python
mixed = {1, "hello", 3.14, True}
print(mixed)
```

---

## 🔹 Duplicates অটোমেটিক বাদ পড়ে

```python
s = {1, 2, 2, 3, 3, 3}
print(s)
```

🎯 আউটপুট:
```
{1, 2, 3}
```

---

## 🔹 Empty Set তৈরি করার সঠিক উপায়

```python
empty = set()
print(type(empty))  # <class 'set'>
```

📌 ⚠️ `{}` দিলে সেটা **dictionary** হয়, set না।

---

## 🔹 Set এ Loop চালানো

```python
for item in {'a', 'b', 'c'}:
    print(item)
```

📌 Set এর মধ্যে উপাদান **unsorted** থাকে, তাই ক্রম থাকে না।

---

## 🔹 উপাদান যোগ ও মুছে ফেলা

### ➤ উপাদান যোগ করতে:
```python
s = {1, 2}
s.add(3)
```

### ➤ একাধিক উপাদান যোগ করতে:
```python
s.update([4, 5])
```

### ➤ উপাদান মুছে ফেলতে:
```python
s.remove(2)   # Error দিবে যদি না থাকে
s.discard(5)  # Error দিবে না, চুপচাপ বাদ দিবে
```

---

## 🔹 Set Operations (Union, Intersection ইত্যাদি)

### ✅ Union → সব উপাদান (unique সহ)

```python
A = {1, 2, 3}
B = {3, 4, 5}
print(A.union(B))   # {1, 2, 3, 4, 5}
```

### ✅ Intersection → মিল আছে এমন উপাদান

```python
print(A.intersection(B))  # {3}
```

### ✅ Difference → A-তে আছে, B-তে নেই

```python
print(A.difference(B))  # {1, 2}
```

### ✅ Symmetric Difference → যেগুলো একটাই set-এ আছে

```python
print(A.symmetric_difference(B))  # {1, 2, 4, 5}
```

---

## 🔹 Subset & Superset

```python
A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))   # True
print(B.issuperset(A)) # True
```

---

## 🔹 Set মেথডগুলোর সংক্ষেপ

| মেথড | কাজ |
|------|-----|
| `add()` | একটি উপাদান যোগ করে |
| `update()` | একাধিক উপাদান যোগ করে |
| `remove()` | উপাদান সরায়, না থাকলে error |
| `discard()` | উপাদান সরায়, না থাকলে চুপচাপ |
| `union()` | দুটি সেটের মিলিত উপাদান |
| `intersection()` | দুটি সেটের মিল থাকা উপাদান |
| `difference()` | একটিতে আছে, অন্যটিতে নেই |
| `symmetric_difference()` | আলাদা আলাদা উপাদান |
| `issubset()` | একটি set কি অন্যটির উপসেট? |
| `issuperset()` | একটি set কি অন্যটির সুপারসেট? |
| `clear()` | সম্পূর্ণ খালি করে দেয় |

---

## 🔹 Set এর Limitations

- ❌ Indexing করা যায় না
- ❌ Ordered না — উপাদান কোথায় থাকবে, নির্দিষ্ট নয়
- ✅ তবে iteration করা যায়

---

## ✅ কখন set ব্যবহার করবেন?

- ✅ যখন **unique** উপাদান দরকার
- ✅ যখন **membership test (in / not in)** দ্রুত করতে হয়
- ✅ যখন **set operations** দরকার হয় (union, intersection, etc.)

---

## 📌 উপসংহার:

- ✅ Set দ্রুত এবং ইউনিক উপাদানের জন্য উপযুক্ত
- ✅ লিস্ট থেকে ডুপ্লিকেট বাদ দিতে set ব্যবহার করা হয়
- ⚠️ তবে ইনডেক্স না থাকায় শুধুমাত্র নির্দিষ্ট ধরণের সমস্যার জন্য উপযোগী

---


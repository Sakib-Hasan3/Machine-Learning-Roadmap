# 🧠 Python List এবং List Comprehension — বাংলা নোট

---

## 🔹 লিস্ট (List) কী?

**লিস্ট** হলো পাইথনের একটি ডেটা স্ট্রাকচার, যেখানে একাধিক মান (value) একসাথে রাখা যায়। এটি **mutable** অর্থাৎ পরিবর্তনযোগ্য।

### ✅ উদাহরণ:
```python
names = ['sakib', 'sami']
print(names)
```

🎯 আউটপুট:
```
['sakib', 'sami']
```

📘 ব্যাখ্যা:
- 'sakib', 'sami' → লিস্টের উপাদান
- ইনডেক্স ০, ১ → যেগুলো দিয়ে উপাদান অ্যাক্সেস করা যায়

---

## 🔹 মিশ্র লিস্ট (Mixed List)
```python
mixed_list = [1, 2, 3, 'sakib']
print(mixed_list)
```

🎯 আউটপুট:
```
[1, 2, 3, 'sakib']
```

📘 ব্যাখ্যা: লিস্টে ভিন্ন টাইপের ডেটা (int ও string) একসাথে রাখা যেতে পারে।

---

## 🔹 লিস্ট অ্যাক্সেস (Indexing & Slicing)
```python
fruits = ['apple', 'banana', 'cherry']
print(fruits[0])     # 'apple'
print(fruits[1:])    # ['banana', 'cherry']
print(fruits[-1])    # 'cherry'
```

📘 ব্যাখ্যা:
- fruits[0] → প্রথম উপাদান
- fruits[1:] → ১ থেকে শেষ পর্যন্ত
- fruits[-1] → শেষ উপাদান

---

## 🔹 লিস্ট পরিবর্তন (Modify List)
```python
fruits[0] = 'orange'
print(fruits)
```

🎯 আউটপুট:
```
['orange', 'banana', 'cherry']
```

📘 ব্যাখ্যা: লিস্ট mutable, তাই উপাদান পরিবর্তন করা যায়।

---

## 🔹 লিস্ট মেথড (List Methods)
```python
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')        # শেষে যোগ করে
fruits.insert(1, 'banana')     # নির্দিষ্ট পজিশনে বসায়
fruits.remove('banana')        # প্রথম 'banana' মুছে ফেলে
popped = fruits.pop()          # শেষ উপাদান সরিয়ে রিটার্ন করে
index = fruits.index('cherry') # 'cherry' এর অবস্থান
fruits.sort()                  # উপাদান সাজায়
fruits.clear()                 # লিস্ট খালি করে
```

📘 ব্যাখ্যা: প্রতিটি মেথড লিস্টের উপর সরাসরি কাজ করে।

---

## 🔹 লিস্ট স্লাইসিং (Slicing)
```python
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[2:5])     # [3, 4, 5]
print(numbers[:5])      # [1, 2, 3, 4, 5]
print(numbers[5:])      # [6, 7, 8, 9, 10]
print(numbers[-5:-2])   # [6, 7, 8]
print(numbers[::2])     # [1, 3, 5, 7, 9]
print(numbers[::-1])    # রিভার্স
```

📘 ব্যাখ্যা: লিস্টের নির্দিষ্ট অংশ বা ধাপ দিয়ে একাধিক উপাদান কাটা যায়।

---

## 🔹 লিস্টে লুপ চালানো (Iterating)

### ➤ সাধারণ লুপ:
```python
for item in numbers:
    print(item)
```

### ➤ ইনডেক্সসহ লুপ:
```python
for index, number in enumerate(numbers):
    print(index, number)
```

📘 ব্যাখ্যা: enumerate() ইনডেক্স ও মান একসাথে দেয়।

---

## 🔷 লিস্ট কমপ্রিহেনশন (List Comprehension)

---

### ✅ ১. সাধারণ রূপ
```python
squares = [x**2 for x in range(10)]
print(squares)
```

🎯 আউটপুট:
```
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

📘 ব্যাখ্যা: প্রতিটি সংখ্যার স্কয়ার করে নতুন লিস্ট তৈরি।

---

### ✅ ২. শর্তসহ (Conditional)
```python
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)
```

🎯 আউটপুট:
```
[0, 2, 4, 6, 8]
```

📘 ব্যাখ্যা: কেবল জোড় সংখ্যা রাখা হচ্ছে।

---

### ✅ ৩. if-else সহ
```python
labels = ['even' if x % 2 == 0 else 'odd' for x in range(5)]
print(labels)
```

🎯 আউটপুট:
```
['even', 'odd', 'even', 'odd', 'even']
```

📘 ব্যাখ্যা: সংখ্যাকে শ্রেণিবদ্ধ করছে।

---

### ✅ ৪. Nested Comprehension
```python
lst1 = [[1, 2, 3], [4, 5, 6]]
lst2 = ['a', 'b']
pairs = [(x, y) for x in lst1 for y in lst2]
print(pairs)
```

🎯 আউটপুট:
```
[([1, 2, 3], 'a'), ([1, 2, 3], 'b'), ([4, 5, 6], 'a'), ([4, 5, 6], 'b')]
```

📘 ব্যাখ্যা: দুটি লিস্টের সব কম্বিনেশন তৈরি।

---

### ✅ ৫. ফাংশন কল সহ
```python
words = ['hello', 'world', 'python']
caps = [word.upper() for word in words]
lengths = [len(word) for word in words]
print(caps)
print(lengths)
```

🎯 আউটপুট:
```
['HELLO', 'WORLD', 'PYTHON']
[5, 5, 6]
```

📘 ব্যাখ্যা: `upper()` এবং `len()` ফাংশন প্রতিটি উপাদানে প্রয়োগ করা হয়েছে।

---

## ✅ List Comprehension Syntax Summary

```python
[expression for item in iterable]
[expression for item in iterable if condition]
[true_expr if condition else false_expr for item in iterable]
[expression for item1 in iterable1 for item2 in iterable2]
```

---

## 📌 টিপস:

- ✅ List Comprehension কোডকে সংক্ষিপ্ত ও পরিষ্কার করে তোলে।
- ⚠️ তবে জটিল লজিক থাকলে `for` লুপ ব্যবহার করাই ভালো।

---

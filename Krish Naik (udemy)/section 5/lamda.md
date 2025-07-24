#  Python Lambda Functions (with Examples in Bangla)

##  Lambda Function কী?

**Lambda Function** হলো Python-এর একটি ছোট, একলাইনের, নামহীন ফাংশন। এগুলো সাধারণত তখন ব্যবহার করা হয়, যখন দ্রুত একবারের জন্য ফাংশন দরকার হয় এবং সেই কাজটি খুবই ছোট হয়।

---

## ✅ Lambda Function-এর গঠন (Syntax)

```python
lambda parameter1, parameter2, ... : expression
````

এটি আসলে নিচের মতো সাধারণ `def` ফাংশনের ছোট সংস্করণ:

```python
def add(a, b):
    return a + b
```

⏬ একেই Lambda ফাংশনে লেখা যায়:

```python
lambda a, b: a + b
```

---

## ✅ উদাহরণসমূহ

### ১. দুই সংখ্যার যোগফল

```python
add = lambda a, b: a + b
print(add(5, 3))  # Output: 8
```

---

### ২. একটি সংখ্যার স্কয়ার

```python
square = lambda x: x ** 2
print(square(6))  # Output: 36
```

---

### ৩. বড় সংখ্যাটি রিটার্ন করো

```python
maximum = lambda a, b: a if a > b else b
print(maximum(10, 20))  # Output: 20
```

---

### ৪. list এর প্রতিটি উপাদানের স্কয়ার (map এর মাধ্যমে)

```python
lst = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, lst))
print(squares)  # Output: [1, 4, 9, 16, 25]
```

---

### ৫. শুধুমাত্র জোড় সংখ্যাগুলো বের করো (filter)

```python
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6]
```

---

### ৬. list কে নামের দৈর্ঘ্য অনুসারে sort করো

```python
names = ['Sakib', 'Tamim', 'Afif', 'Mushfiq']
sorted_names = sorted(names, key=lambda x: len(x))
print(sorted_names)  # Output: ['Afif', 'Sakib', 'Tamim', 'Mushfiq']
```

---

### ৭. dictionary list কে বয়স অনুসারে sort করো

```python
students = [
    {'name': 'Sakib', 'age': 22},
    {'name': 'Tamim', 'age': 19},
    {'name': 'Mushfiq', 'age': 25}
]

sorted_students = sorted(students, key=lambda x: x['age'])
print(sorted_students)
```

📤 Output:

```python
[
 {'name': 'Tamim', 'age': 19},
 {'name': 'Sakib', 'age': 22},
 {'name': 'Mushfiq', 'age': 25}
]
```

---

## 🧠 Lambda Function কখন ব্যবহার করবো?

* এক লাইনের ছোট ফাংশন দরকার হলে
* `map()`, `filter()`, `reduce()` এর সঙ্গে
* list, dict বা tuple কে sort/filter করতে

---

## ✅ সারাংশ টেবিল

| ব্যবহার         | ফর্মুলা                           |
| --------------- | --------------------------------- |
| সাধারণ যোগ      | `lambda a, b: a + b`              |
| স্কয়ার          | `lambda x: x ** 2`                |
| বড় সংখ্যা       | `lambda a, b: a if a > b else b`  |
| map এর সঙ্গে    | `map(lambda x: ..., list)`        |
| filter এর সঙ্গে | `filter(lambda x: ..., list)`     |
| sorted এর সঙ্গে | `sorted(list, key=lambda x: ...)` |

---

## ✨ Bonus: Direct Call করা Lambda

```python
print((lambda a, b: a + b)(2, 3))  # Output: 5
```

---


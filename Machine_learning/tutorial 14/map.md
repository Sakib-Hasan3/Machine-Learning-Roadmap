````markdown
# 🐍 Python `map()` ফাংশন ও ব্যবহার — বাংলা ব্যাখাসহ

## 🔹 `map()` ফাংশন কী?

`map()` হলো Python-এর একটি in-built (অন্তর্নির্মিত) ফাংশন, যা একটি নির্দিষ্ট ফাংশনকে একটি iterable (যেমন list, tuple ইত্যাদি)-এর প্রতিটি উপাদানের উপর প্রয়োগ করে।

**সিনট্যাক্স (Syntax):**

    map(function, iterable)

- `function`: যেটা iterable-এর প্রতিটি উপাদানের উপর প্রয়োগ হবে।
- `iterable`: যেটার উপাদানগুলোতে ফাংশনটি প্রয়োগ করা হবে (যেমন list)।

`map()` একটি **map object** রিটার্ন করে, যেটিকে `list()` বা `tuple()` দিয়ে রূপান্তর করে দেখতে হয়।

---

## 🔹 উদাহরণ: ৫ দিয়ে গুণ করার কোড

```python
def mul_five_times(number):
    return number * 5

num = [3, 4, 5, 6, 7, 8]
mapped_result = list(map(mul_five_times, num))
print(mapped_result)
````

---

## 🔍 লাইন-বাই-লাইন বাংলা ব্যাখ্যা

### ✅ ফাংশন ডিফাইন:

```python
def mul_five_times(number):
    return number * 5
```

> একটি ফাংশন তৈরি করা হলো যার নাম `mul_five_times`। এটি ইনপুট হিসেবে একটি সংখ্যা গ্রহণ করে সেটিকে ৫ দিয়ে গুণ করে রিটার্ন করে।

### ✅ লিস্ট তৈরি:

```python
num = [3, 4, 5, 6, 7, 8]
```

> কিছু সংখ্যা নিয়ে একটি লিস্ট তৈরি করা হয়েছে।

### ✅ map() ফাংশন ব্যবহার:

```python
mapped_result = list(map(mul_five_times, num))
```

> `mul_five_times()` ফাংশনটি `num` লিস্টের প্রতিটি উপাদানের উপর প্রয়োগ করা হয়েছে এবং রেজাল্টগুলোকে list এ রূপান্তর করা হয়েছে।

### ✅ রেজাল্ট প্রিন্ট:

```python
print(mapped_result)
```

> চূড়ান্ত ফলাফল প্রিন্ট করা হয়েছে।

---

## ✅ চূড়ান্ত আউটপুট:

```
[15, 20, 25, 30, 35, 40]
```

---

## 🧠 ছোট্ট তুলনা: `for loop` vs `map()`

### `for` লুপ দিয়ে:

```python
result = []
for i in num:
    result.append(mul_five_times(i))
```

### `map()` দিয়ে:

```python
result = list(map(mul_five_times, num))
```

> উভয় ক্ষেত্রেই একই রেজাল্ট আসবে, তবে `map()` কোডকে সংক্ষিপ্ত ও আরও Pythonic করে তোলে।

---

## ✍️ উপসংহার:

Python-এর `map()` ফাংশন শেখার মাধ্যমে তুমি বড় লিস্টের উপর দ্রুত এবং কম কোডে কাজ করতে পারো। এটা functional programming এর একটি সুন্দর উদাহরণ।

---


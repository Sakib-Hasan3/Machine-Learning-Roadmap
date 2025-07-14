# 🔍 Python `filter()` ফাংশন — বাংলা ব্যাখ্যাসহ

## 🧠 `filter()` ফাংশন কী?

`filter()` হলো Python-এর একটি **in-built (অন্তর্নির্মিত)** ফাংশন, যা একটি নির্দিষ্ট ফাংশন এবং একটি iterable (যেমন `list`, `tuple`, ইত্যাদি) গ্রহণ করে এবং সেই iterable-এর শুধুমাত্র **যেসব উপাদান নির্দিষ্ট শর্ত পূরণ করে**, সেগুলো রিটার্ন করে।

---

## 🧾 সিনট্যাক্স (Syntax)

```python
filter(function, iterable)
```

- `function`: একটি ফাংশন যা প্রত্যেক উপাদানে প্রয়োগ করা হবে এবং `True` বা `False` রিটার্ন করবে।
- `iterable`: যেকোনো iterable (যেমন `list`, `tuple`, `set`) যার উপাদানগুলো ফিল্টার করা হবে।

📌 `filter()` একটি **filter object** রিটার্ন করে, যেটিকে `list()`, `tuple()` ইত্যাদির মাধ্যমে কনভার্ট করে দেখা যায়।

---

## ✅ উদাহরণ ১: পজিটিভ নাম্বার ফিল্টার করা

```python
numbers = [-5, -2, 0, 3, 7, 10]

positive = list(filter(lambda x: x > 0, numbers))

print(positive)
```

**আউটপুট:**
```
[3, 7, 10]
```

---

## ✅ উদাহরণ ২: শুধু জোড় সংখ্যা বের করা

```python
nums = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, nums))

print(even)
```

**আউটপুট:**
```
[2, 4, 6]
```

---

## ✅ উদাহরণ ৩: `def` ব্যবহার করে ফাংশন দিয়ে ফিল্টার

```python
def is_even(n):
    return n % 2 == 0

nums = [10, 15, 20, 25]

result = list(filter(is_even, nums))

print(result)
```

**আউটপুট:**
```
[10, 20]
```

---

## 🧠 অতিরিক্ত টিপস:

- `filter()` মূল iterable-কে পরিবর্তন করে না, বরং নতুন একটি filter object তৈরি করে।
- এটি **lazy evaluation** ব্যবহার করে — অর্থাৎ, iterable-এর উপাদানগুলো একে একে প্রসেস করে, একসাথে নয়।
- এটি performance-efficient ও functional programming-এ গুরুত্বপূর্ণ ভূমিকা রাখে।

---

## 🔚 উপসংহার

যখনই আপনাকে একটি iterable-এর মধ্যে থেকে কিছু নির্দিষ্ট উপাদান বেছে নিতে হবে নির্দিষ্ট শর্তের ভিত্তিতে — তখন `filter()` ফাংশন একটি **পরিষ্কার, ছোট ও দ্রুত সমাধান** দেয়।

```python
# উদাহরণস্বরূপ:
list(filter(lambda x: x > 10, [4, 11, 8, 20]))
# রিটার্ন করবে: [11, 20]
```

এইভাবে Python-এ functional programming-এর শক্তি ব্যবহার করে আপনি আপনার কোডকে আরও সহজ ও কার্যকর করে তুলতে পারেন।

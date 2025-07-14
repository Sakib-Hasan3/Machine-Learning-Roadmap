# 📚 Python List Comprehension — বাংলা ব্যাখ্যাসহ

## 🔍 List Comprehension কী?

List comprehension হলো Python-এর একটি সংক্ষিপ্ত ও সুন্দর সিনট্যাক্স, যার মাধ্যমে একটি নতুন লিস্ট তৈরি করা যায় — অন্য iterable (যেমন list, range, string, ইত্যাদি)-এর উপাদানগুলো থেকে **filtering**, **transformation**, বা **looping** এর মাধ্যমে।

এটি `for` লুপের একটি সংক্ষিপ্ত ও কার্যকরী বিকল্প।

---

## 🧾 সিনট্যাক্স (Syntax)

```python
[expression for item in iterable if condition]
```

- `expression`: যেটা প্রতিটি আইটেমের উপর প্রয়োগ হবে।
- `item`: iterable-এর প্রতিটি উপাদান।
- `iterable`: list, range, string, tuple ইত্যাদি।
- `condition` (ঐচ্ছিক): শর্ত যা পূরণ হলে কেবলমাত্র সেই উপাদান লিস্টে থাকবে।

---

## ✅ উদাহরণ ১: সাধারণ তালিকা তৈরি

```python
squares = [x * x for x in range(1, 6)]
print(squares)
```

**আউটপুট:**
```
[1, 4, 9, 16, 25]
```

🔍 ব্যাখ্যা: ১ থেকে ৫ পর্যন্ত প্রতিটি সংখ্যার স্কয়ার নিয়ে একটি নতুন লিস্ট তৈরি হয়েছে।

---

## ✅ উদাহরণ ২: শুধুমাত্র জোড় সংখ্যা

```python
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)
```

**আউটপুট:**
```
[0, 2, 4, 6, 8]
```

🔍 ব্যাখ্যা: `range(10)` থেকে শুধুমাত্র জোড় সংখ্যা রাখা হয়েছে।

---

## ✅ উদাহরণ ৩: স্ট্রিং থেকে ভাওয়েল বাদ দিয়ে লিস্ট তৈরি

```python
text = "python"
no_vowels = [char for char in text if char not in 'aeiou']
print(no_vowels)
```

**আউটপুট:**
```
['p', 'y', 't', 'h', 'n']
```

---

## ✅ উদাহরণ ৪: Nested List Comprehension

```python
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print(flattened)
```

**আউটপুট:**
```
[1, 2, 3, 4, 5, 6]
```

🔍 ব্যাখ্যা: ২D তালিকাকে ১D লিস্টে রূপান্তর করা হয়েছে।

---

## ⚖️ তুলনা: `for` লুপ বনাম List Comprehension

### সাধারন for লুপ:
```python
squares = []
for x in range(1, 6):
    squares.append(x * x)
```

### List Comprehension:
```python
squares = [x * x for x in range(1, 6)]
```

🔍 একই কাজ — কিন্তু দ্বিতীয়টি অনেক **ছোট ও পড়তে সুবিধাজনক**।

---

## 🧠 উপকারিতা:

- কোড সংক্ষিপ্ত করে
- পড়তে সহজ
- পারফরম্যান্স উন্নত হয়
- Functional Programming এর সাথে সামঞ্জস্যপূর্ণ

---

## 🚫 সতর্কতা:

- Nested বা খুব জটিল list comprehension পড়তে কঠিন হতে পারে।
- readable না হলে `for` loop ব্যবহার করাই ভালো।

---

## 🔚 উপসংহার:

List comprehension হলো Python প্রোগ্রামিংয়ের একটি শক্তিশালী বৈশিষ্ট্য, যা আপনার কোডকে ছোট, পরিষ্কার ও কার্যকরী করে তোলে।

```python
# উদাহরণ:
[x.upper() for x in ['a', 'b', 'c'] if x != 'b']
# আউটপুট: ['A', 'C']
```

চর্চার মাধ্যমে আপনি আরও সুন্দরভাবে List Comprehension ব্যবহার করতে শিখে যাবেন!

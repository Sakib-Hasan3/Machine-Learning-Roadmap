# 🎯 Python Advanced String Formatting — বাংলা ব্যাখ্যাসহ

Python-এ স্ট্রিং ফরম্যাটিংয়ের মাধ্যমে আমরা স্ট্রিং-এর ভিতরে ভেরিয়েবল, সংখ্যা, ডেটা ইত্যাদি সুন্দরভাবে বসাতে পারি। Advanced formatting আপনাকে **অবস্থান, সংখ্যা নিয়ন্ত্রণ, alignment, padding, precision** ইত্যাদি সুবিধা দেয়।

---

## 🧾 ১. `.format()` Method ব্যবহার করে

```python
name = "Sakib"
age = 23

intro = "My name is {} and I am {} years old.".format(name, age)
print(intro)
```

🔹 আউটপুট:
```
My name is Sakib and I am 23 years old.
```

---

## 🧭 ২. পজিশনাল ও কীওয়ার্ড আর্গুমেন্ট

```python
# Positional
print("Hello {0}, you have {1} messages.".format("Sakib", 5))

# Keyword
print("Name: {name}, Age: {age}".format(name="Sakib", age=23))
```

---

## 📐 ৩. Alignment ও Padding

```python
# ^ = center, < = left, > = right
print("{:<10}".format("Left"))    # Left aligned
print("{:>10}".format("Right"))   # Right aligned
print("{:^10}".format("Center"))  # Center aligned
```

🔹 আউটপুট:
```
Left      
     Right
  Center  
```

---

## 🎯 ৪. Padding with Custom Characters

```python
print("{:*^10}".format("Hi"))   # Center with *
print("{:.^10}".format("Hi"))   # Center with .
```

🔹 আউটপুট:
```
****Hi****
....Hi....
```

---

## 📊 ৫. ফ্লোট নাম্বারের Precision Control

```python
pi = 3.14159265359

print("Pi value: {:.2f}".format(pi))  # শুধু ২ দশমিক পর্যন্ত
```

🔹 আউটপুট:
```
Pi value: 3.14
```

---

## 🪙 ৬. সংখ্যায় Leading Zeros

```python
num = 5

print("Number: {:03}".format(num))  # Output: 005
```

---

## 💱 ৭. Currency Format

```python
price = 1234.567

print("Price: ${:,.2f}".format(price))  # কমা ও দশমিকসহ
```

🔹 আউটপুট:
```
Price: $1,234.57
```

---

## 🔄 ৮. f-strings (Python 3.6+)

```python
name = "Hasan"
score = 95.6789

print(f"Student {name} scored {score:.1f} marks.")
```

🔹 আউটপুট:
```
Student Hasan scored 95.7 marks.
```

---

## 🧮 ৯. Expressions in f-strings

```python
x = 5
y = 10

print(f"{x} + {y} = {x + y}")
```

---

## 📅 ১০. Date Formatting with `datetime`

```python
from datetime import datetime

now = datetime.now()

print(f"Today is {now:%B %d, %Y}")  # July 14, 2025 এর মতো
```

---

## 🧠 উপসংহার

Advanced string formatting আপনাকে স্ট্রিং-এর ভিতর তথ্য বসাতে আরও **নিয়ন্ত্রণ, শৈলী ও স্পষ্টতা** দেয়। বিশেষ করে:

- সংখ্যা ও মান ফরম্যাট করা
- ডেটা সুন্দরভাবে সাজানো
- বড় রিপোর্ট বা টেবিল বানানো

শুধু `.format()` বা `f-string` জানলেই Python-এ পেশাদারভাবে আউটপুট তৈরি করা সম্ভব!

```python
name = "Python"
version = 3.10
print(f"{name:^10} | Version: {version:.2f}")
```

⏩ এই ফরম্যাটিং গুলো বিশেষভাবে দরকার পড়ে ওয়েব ডেভেলপমেন্ট, রিপোর্ট জেনারেশন, ডেটা প্রিন্টিং ও প্রেজেন্টেশনে।


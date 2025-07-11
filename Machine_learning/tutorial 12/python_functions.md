#  Python Functions Explained

## 🔹 ফাংশন তৈরি এবং কল করা

```python
def hello_world():
    print("hello welcome")
```

**ব্যাখ্যা:**
এখানে `hello_world()` একটি সাধারণ ফাংশন যা শুধু `"hello welcome"` প্রিন্ট করে। কোনো `return` নেই, তাই ভ্যালু ধরে রাখা যাবে না।

---

## 🔹 ফাংশন কল করে মান প্রিন্ট

```python
hello_world()
val = hello_world()
print(val)
```

**ব্যাখ্যা:**

* `hello_world()` কল করলে "hello welcome" স্ক্রিনে দেখা যাবে।
* `val = hello_world()` ফাংশন কিছু `return` না করায় `val` এর মান হবে `None`।
* `print(val)` প্রিন্ট করবে: `None`

---

## 🔹 return দিয়ে মান ফেরত দেওয়া

```python
def hello_world():
    return "hello welcome"

val = hello_world()
print(val)
```

**ব্যাখ্যা:**
এখানে `return` ব্যবহৃত হওয়ায় ফাংশন `"hello welcome"` পাঠিয়ে দেয়, যেটা `val` এ সংরক্ষিত হয় এবং `print(val)` তা দেখায়।

---

## 🔹 দুটি সংখ্যার যোগফল

```python
def add_numbers(a, b):
    return a + b

val = add_numbers(5, 10)
print(val)
```

**ব্যাখ্যা:**
`add_numbers()` দুটি সংখ্যার যোগফল করে `return` করে। এখানে ৫ + ১০ = ১৫, যা `val` এ যায় এবং প্রিন্ট হয়।

---

## 🔹 Positional এবং Keyword Arguments

```python
def hello(name, age):
    print("my name is {} and my age is {}".format(name, age))

hello('sakib', 30)
```

**ব্যাখ্যা:**

* `'sakib'` → `name`
* `30` → `age`
  উভয়টা যথাক্রমে **positional arguments** হিসেবে ব্যবহৃত হয়েছে।

---

## 🔹 \*args এবং \*\*kwargs ব্যবহার

```python
def hello(*args, **kwargs):
    print(args)
    print(kwargs)

hello("sakib", "hasan", age=30, dob=2000)
```

**ব্যাখ্যা:**

* `*args` → সব positional argument ধরে (tuple আকারে)
* `**kwargs` → সব keyword argument ধরে (dictionary আকারে)

আউটপুট হবে:

```
('sakib', 'hasan')
{'age': 30, 'dob': 2000}
```

---

## 🔹 List ও Dictionary Unpack করে পাঠানো

```python
lst = ['sakib', 'hasan']
dict_args = {"age": 30, "dob": 2000}
hello(*lst, **dict_args)
```

**ব্যাখ্যা:**

* `*lst` → list এর প্রতিটি মান `args` এ যাবে
* `**dict_args` → dictionary এর key-value গুলো `kwargs` হিসেবে যাবে

---

## 🔹 evenoddsum ফাংশন — জোড় ও বিজোড় যোগফল


```python
def evenoddsum(lst):
    even_sum = 0
    odd_sum = 0
    for i in lst:
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
    return even_sum, odd_sum
```

**ব্যাখ্যা:**
`return` লাইনটি এখন লুপের বাইরে, ফলে পুরো লিস্ট ঘুরে ফাংশন সঠিকভাবে কাজ করবে।

---

## 🔹 ফাংশন কল করে ফলাফল দেখা

```python
lst = [1, 2, 3, 4, 5, 6]
even, odd = evenoddsum(lst)
print("Even sum:", even)
print("Odd sum:", odd)
```

**আউটপুট:**

```
Even sum: 12
Odd sum: 9
```

---

## ✅ সংক্ষেপ:

| বিষয়       | ব্যাখ্যা                                 |
| ---------- | ---------------------------------------- |
| `print()`  | শুধু স্ক্রিনে দেখায়                      |
| `return`   | মান ফিরিয়ে দেয়, যা সংরক্ষণ/হিসেব করা যায় |
| `*args`    | একাধিক positional argument নেয়           |
| `**kwargs` | একাধিক keyword argument নেয়              |
| `*list`    | list unpack করে ফাংশনে পাঠানো হয়         |
| `**dict`   | dictionary unpack করে পাঠানো হয়          |

---



# 🐍 Python Iterables vs Iterators (বাংলায় ব্যাখ্যা সহ)

---

## 🔹 Iterable কী?

**Iterable** হল এমন কোনো অবজেক্ট যার উপর আপনি `for` লুপ চালাতে পারেন। যেমন: `list`, `tuple`, `string`, `set` ইত্যাদি।

**উদাহরণ:**

```python
my_list = [10, 20, 30]

for item in my_list:
    print(item)
```

🔸 এখানে `my_list` একটি **Iterable**, কারণ আমরা এর উপর `for` লুপ চালাতে পারছি।

---

## 🔹 Iterator কী?

**Iterator** হল এমন এক অবজেক্ট যেটি এক এক করে উপাদান দিতে পারে এবং `__next__()` মেথড ব্যবহার করে পরবর্তী উপাদান দেয়। এটি `iter()` ফাংশন দিয়ে তৈরি করা হয়।

**উদাহরণ:**

```python
my_list = [10, 20, 30]

my_iter = iter(my_list)  # list থেকে iterator বানানো

print(next(my_iter))  # 10
print(next(my_iter))  # 20
print(next(my_iter))  # 30
```

🔸 এখানে `my_iter` একটি **Iterator**, কারণ আমরা `next()` দিয়ে এক এক করে উপাদান পাচ্ছি।

---

## 🔸 Iterable ও Iterator এর মধ্যে পার্থক্য

| বৈশিষ্ট্য     | Iterable              | Iterator                       |
|---------------|-----------------------|--------------------------------|
| সংজ্ঞা         | যেটার উপর লুপ চালানো যায় | যেটি `next()` দিয়ে উপাদান দেয়     |
| মেথড থাকে      | `__iter__()`           | `__iter__()` এবং `__next__()`     |
| উদাহরণ         | list, tuple, set, dict, string | iter(list), file object ইত্যাদি |
| তৈরি হয়        | সরাসরি                 | `iter()` দিয়ে iterable থেকে       |

---

## 🔹 নিজস্ব Iterator তৈরি করার উদাহরণ

```python
class MyCounter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            num = self.current
            self.current += 1
            return num

# Iterator তৈরি
counter = MyCounter(1, 5)

for num in counter:
    print(num)
```

🔸 আউটপুট:
```
1
2
3
4
5
```

এখানে `MyCounter` ক্লাসটি একটি কাস্টম Iterator যেখানে আমরা `__iter__()` এবং `__next__()` ব্যবহার করেছি।

---

## 🟡 উপসংহার

- **Iterable** মানে যেটার উপর লুপ চালানো যায়।
- **Iterator** মানে যেটা `next()` দিয়ে উপাদান দেয়।
- `for` লুপ ব্যাকগ্রাউন্ডে নিজেই `iter()` ও `next()` ব্যবহার করে।
- আপনি নিজের iterator বানাতে চাইলে `__iter__()` এবং `__next__()` মেথড লিখতে হবে।

---



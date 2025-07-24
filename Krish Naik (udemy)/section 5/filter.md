# 🧠 Python `filter()` Function — বাংলা ব্যাখ্যাসহ

## 🔹 `filter()` ফাংশন কী?

`filter()` হলো পাইথনের একটি **বিল্ট-ইন ফাংশন**, যা একটি iterable (যেমন লিস্ট, টাপল) থেকে শুধুমাত্র সেই উপাদানগুলো বেছে নেয় যেগুলো একটি নির্দিষ্ট শর্ত (function) পূরণ করে।

---

## ✅ `filter()` এর সাধারণ সিনট্যাক্স:
```python
filter(function, iterable)
function: এমন একটি ফাংশন, যা প্রতিটি উপাদানের জন্য True বা False রিটার্ন করে।

iterable: যেকোনো পুনরাবৃত্তিযোগ্য ডেটা, যেমন লিস্ট, টাপল, সেট ইত্যাদি।

এটি filter object রিটার্ন করে, যেটিকে list() বা tuple() দিয়ে ব্যবহারযোগ্য করতে হয়।

🧪 উদাহরণ ১: শুধুমাত্র জোড় সংখ্যা ফিল্টার করা
python
Copy code
def even(num):
    return num % 2 == 0

lst = [1,2,3,4,5,6,7,8,9,10,11,12]

result = list(filter(even, lst))

print(result)  # Output: [2, 4, 6, 8, 10, 12]
🧪 উদাহরণ ২: lambda দিয়ে ৫-এর বেশি সংখ্যা বেছে নেওয়া
python
Copy code
numbers = [1,2,3,4,5,6,7,8,9]

greater_than_five = list(filter(lambda x: x > 5, numbers))

print(greater_than_five)  # Output: [6, 7, 8, 9]
🧪 উদাহরণ ৩: একাধিক শর্ত — জোড় সংখ্যা এবং ৫-এর বেশি
python
Copy code
numbers = [1,2,3,4,5,6,7,8,9]

even_and_greater_than_five = list(filter(lambda x: x > 5 and x % 2 == 0, numbers))

print(even_and_greater_than_five)  # Output: [6, 8]
🧪 উদাহরণ ৪: filter() ব্যবহার করে dictionary থেকে বয়স > ২৫ চেক করা
python
Copy code
people = [
    {'name': 'Krish', 'age': 32},
    {'name': 'Jack', 'age': 33},
    {'name': 'John', 'age': 25}
]

def age_greater_than_25(person):
    return person['age'] > 25

result = list(filter(age_greater_than_25, people))

print(result)
# Output: [{'name': 'Krish', 'age': 32}, {'name': 'Jack', 'age': 33}]
🔁 Bonus: উপরের একই কাজ lambda দিয়ে
python
Copy code
people = [
    {'name': 'Krish', 'age': 32},
    {'name': 'Jack', 'age': 33},
    {'name': 'John', 'age': 25}
]

result = list(filter(lambda person: person['age'] > 25, people))

print(result)
# Output: [{'name': 'Krish', 'age': 32}, {'name': 'Jack', 'age': 33}]
✅ উপসংহার:
filter() হলো পাইথনের একটি শক্তিশালী ফাংশন যা দিয়ে তুমি যেকোনো iterable থেকে শর্তসাপেক্ষে উপাদান বেছে নিতে পারো।

এটি lambda বা আলাদা ফাংশন উভয়ের সঙ্গেই কাজ করে।

বাস্তব জীবনে ডেটা ফিল্টার, ফর্ম যাচাই, রিপোর্ট তৈরি ইত্যাদিতে খুব কাজের।


## ফাংশন

ফাংশন প্রোগ্রামিং এর একটি অত্যন্ত গুরুত্বপূর্ণ অংশ। এটি একটি কোড ব্লক যা নির্দিষ্ট কাজ সম্পাদন করে এবং আউটপুট প্রদান করে। একটি ফাংশন কিছু ইনপুট গ্রহণ করে, প্রক্রিয়া করে এবং তারপর ফলাফল দেয়। ফাংশন ব্যবহারের মাধ্যমে কোডকে সহজ, পরিষ্কার এবং পুনরায় ব্যবহারযোগ্য করা যায়।

### 1. Return Statement

#### উদাহরণ ১: সাধারণ রিটার্ন স্টেটমেন্ট

```python
def multiply(a, b):
    return a * b

multiply(2, 3)
ব্যাখ্যা:
def multiply(a, b)::
এখানে multiply নামের একটি ফাংশন সংজ্ঞায়িত করা হয়েছে, যা দুটি প্যারামিটার (a এবং b) গ্রহণ করে।

return a * b:
ফাংশনের মধ্যে a এবং b এর গুণফল (multiplication) বের করা হচ্ছে এবং return কিওয়ার্ড দিয়ে সেই ফলাফল ফিরিয়ে দেয়া হচ্ছে।

return কিওয়ার্ডটি ফাংশনের execution শেষ করে এবং তার ফলাফল ফিরে আসে।

multiply(2, 3):
এখানে multiply ফাংশনটি কল করা হয়েছে, যেখানে প্যারামিটার হিসেবে 2 এবং 3 পাস করা হয়েছে।

এটি a * b = 6 প্রদান করবে, কিন্তু এই ফলাফলটি কোন ভেরিয়েবলে সংরক্ষণ না করলে তা স্ক্রীনে প্রদর্শিত হবে না।

আউটপুট:

result = multiply(2, 3)
print(result)  # আউটপুট: 6

2. Return Multiple Parameters
উদাহরণ ২: একাধিক মান রিটার্ন করা (Tuple)

def multiply(a, b):
    return a * b, a

multiply(2, 3)

ব্যাখ্যা:
def multiply(a, b)::
multiply নামের একটি ফাংশন সংজ্ঞায়িত করা হয়েছে, যা দুটি প্যারামিটার (a এবং b) গ্রহণ করে।

return a * b, a:
ফাংশনটি দুটি মান রিটার্ন করছে:

প্রথমটি a * b (গুণফল),

দ্বিতীয়টি হলো a এর মান।
এই দুটি মান tuple আকারে রিটার্ন হবে।

multiply(2, 3):
এখানে multiply ফাংশনটি কল করা হয়েছে, যেখানে a = 2 এবং b = 3 পাঠানো হয়েছে।
ফলস্বরূপ, ফাংশনটি a * b = 6 এবং a = 2 দুটি মান ফিরিয়ে দেবে, যা হবে: (6, 2)।

আউটপুট:

result = multiply(2, 3)
print(result)  # আউটপুট: (6, 2)

3. Return Statement: Multiple Values and Return Type
ফাংশনটি একাধিক মান ফিরিয়ে দিতে পারে। Tuple বা List এর মাধ্যমে একাধিক মান ফেরানো সম্ভব। উদাহরণ:

def calculate(a, b):
    return a + b, a - b, a * b, a / b

result = calculate(10, 5)
print(result)  # আউটপুট: (15, 5, 50, 2.0)
এখানে calculate ফাংশনটি চারটি মান রিটার্ন করছে (গণনা অনুযায়ী যোগ, বিয়োগ, গুণফল এবং ভাগফল)। ফলস্বরূপ, এটি একটি tuple আকারে রিটার্ন হবে।

4. Default Parameters
ফাংশনে যদি আপনি কোনো প্যারামিটার না দেন, তবে আপনি ডিফল্ট মান দিতে পারেন।
উদাহরণ:

def greet(name="Guest"):
    print(f"Hello {name}!")

greet("Krish")  # আউটপুট: Hello Krish!
greet()         # আউটপুট: Hello Guest!
এখানে, যদি কোনো আর্গুমেন্ট না দেওয়া হয়, তবে name প্যারামিটারের জন্য "Guest" মানটি ডিফল্ট হিসেবে নেওয়া হবে।

5. Variable Length Arguments
ফাংশনটি যদি অসংখ্য আর্গুমেন্ট গ্রহণ করতে চায়, তবে আপনি *args ব্যবহার করতে পারেন। এর মাধ্যমে আপনি একাধিক পজিশনাল আর্গুমেন্ট পাঠাতে পারবেন। উদাহরণ:

def print_numbers(*args):
    for number in args:
        print(number)

print_numbers(1, 2, 3, 4, 5)  # আউটপুট: 1, 2, 3, 4, 5
এখানে *args পজিশনাল আর্গুমেন্টগুলো একটি tuple আকারে গ্রহণ করছে।

6. Keywords Arguments
ফাংশনে কিওয়ার্ড আর্গুমেন্টগুলি ব্যবহার করলে আপনি key-value পেয়ার হিসেবে মান পাঠাতে পারেন। উদাহরণ:

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Krish", age="32", country="India")
এখানে **kwargs কিওয়ার্ড আর্গুমেন্টগুলো একটি ডিকশনারি আকারে গ্রহণ করছে এবং key: value পেয়ার হিসেবে স্ক্রীনে প্রিন্ট হচ্ছে।

আউটপুট:

name: Krish
age: 32
country: India

7. Positional and Keyword Arguments Combined
পজিশনাল এবং কিওয়ার্ড আর্গুমেন্ট একসাথে ব্যবহার করা যেতে পারে। উদাহরণ:

def print_details(*args, **kwargs):
    for val in args:
        print(f"Positional argument: {val}")
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(1, 2, 3, name="Krish", age="32")
এখানে, পজিশনাল আর্গুমেন্টগুলো args এ এবং কিওয়ার্ড আর্গুমেন্টগুলো kwargs ডিকশনারিতে চলে যাবে।

আউটপুট:

Positional argument: 1
Positional argument: 2
Positional argument: 3
name: Krish
age: 32

উপসংহার:
Return Statement: ফাংশনটি একক বা একাধিক মান ফিরিয়ে দিতে পারে।

Default Parameters: ফাংশনে কিছু প্যারামিটার ডিফল্ট মানের সাথে নির্ধারণ করা যেতে পারে।

Variable Length Arguments: *args ব্যবহার করে যে কোন সংখ্যক আর্গুমেন্ট গ্রহণ করা যায়।

Keyword Arguments: **kwargs ব্যবহার করে key-value পেয়ার আর্গুমেন্টগুলি গ্রহণ করা যায়।

Positional and Keyword Arguments: একই ফাংশনে পজিশনাল এবং কিওয়ার্ড আর্গুমেন্ট একসাথে ব্যবহার করা যায়।
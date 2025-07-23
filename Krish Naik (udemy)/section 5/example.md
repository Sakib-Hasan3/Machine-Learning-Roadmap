# উদাহরণ ১: তাপমাত্রা রূপান্তর
def convert_temperature(temp, unit):
    """এই ফাংশনটি তাপমাত্রাকে সেলসিয়াস থেকে ফারেনহাইট অথবা ফারেনহাইট থেকে সেলসিয়াসে রূপান্তরিত করে"""
    if unit == 'C':
        return temp * 9 / 5 + 32  # সেলসিয়াস থেকে ফারেনহাইট
    elif unit == 'F':
        return (temp - 32) * 5 / 9  # ফারেনহাইট থেকে সেলসিয়াস
    else:
        return None  # যদি সঠিক ইউনিট না দেওয়া হয়

# উদাহরণ ২: পাসওয়ার্ড শক্তির পরীক্ষা
def is_strong_password(password):
    """এই ফাংশনটি পরীক্ষা করে যে পাসওয়ার্ডটি শক্তিশালী কিনা"""
    if len(password) < 8:
        return False  # পাসওয়ার্ড যদি ৮ অক্ষরের কম হয়
    if not any(char.isdigit() for char in password):
        return False  # পাসওয়ার্ডে যদি কোনো ডিজিট না থাকে
    if not any(char.islower() for char in password):
        return False  # পাসওয়ার্ডে যদি কোনো ছোট অক্ষর না থাকে
    if not any(char.isupper() for char in password):
        return False  # পাসওয়ার্ডে যদি কোনো বড় অক্ষর না থাকে
    if not any(char in '!@#$%^&*()_+' for char in password):
        return False  # পাসওয়ার্ডে যদি কোনো স্পেশাল ক্যারেক্টার না থাকে
    return True  # সব শর্ত পূর্ণ হলে পাসওয়ার্ড শক্তিশালী

# উদাহরণ ৩: শপিং কার্টের মোট খরচ হিসাব করা
def calculate_total_cost(cart):
    total_cost = 0
    for item in cart:
        total_cost += item['price'] * item['quantity']  # প্রতিটি আইটেমের মূল্য এবং পরিমাণ গুণ করে মোট খরচ হিসাব করা
    return total_cost

# উদাহরণ ৪: স্ট্রিংটি পালিনড্রোম কিনা পরীক্ষা করা
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # সব অক্ষরকে ছোট করতে এবং স্পেস মুছে ফেলতে
    return s == s[::-1]  # স্ট্রিংটি উলটো করে তার সাথে তুলনা

# উদাহরণ ৫: রিকর্শন ব্যবহার করে ফ্যাক্টোরিয়াল হিসাব করা
def factorial(n):
    if n == 0:
        return 1  # ০ এর ফ্যাক্টোরিয়াল ১
    else:
        return n * factorial(n - 1)  # রিকর্শনাল কল

# উদাহরণ ৬: ফাইল থেকে শব্দের ফ্রিকোয়েন্সি গোনা
def count_word_frequency(file_path):
    word_count = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()  # লাইনের সব শব্দ আলাদা করা
            for word in words:
                word = word.lower().strip('.,!?;:"\\')  # শব্দের কাছ থেকে অযাচিত চিহ্ন সরিয়ে ফেলা
                word_count[word] = word_count.get(word, 0) + 1  # শব্দের সংখ্যা বাড়ানো
    return word_count

# উদাহরণ ৭: ইমেইল ঠিকানা যাচাই করা
import re

def is_valid_email(email):
    """এই ফাংশনটি চেক করে যে ইমেইলটি বৈধ কিনা"""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'  # ইমেইল প্যাটার্ন
    return re.match(pattern, email) is not None  # প্যাটার্নের সাথে মিল আছে কিনা

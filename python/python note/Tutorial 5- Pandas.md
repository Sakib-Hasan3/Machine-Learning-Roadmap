# 📊 Pandas – পাইথনের ডেটা বিশ্লেষণ লাইব্রেরি

**Pandas** হলো পাইথনের একটি ওপেন-সোর্স লাইব্রেরি যা ডেটা বিশ্লেষণ ও ম্যানিপুলেশনের জন্য ব্যবহৃত হয়। এটি মূলত দুইটি ডেটা স্ট্রাকচার নিয়ে কাজ করে:
- `Series` – এক মাত্রার লেবেলযুক্ত অ্যারে
- `DataFrame` – দুই মাত্রার লেবেলযুক্ত টেবিল

---

## 📦 ইন্সটলেশন

```bash
pip install pandas
🔧 Pandas ইম্পোর্ট করা
import pandas as pd
🧪 মূল ডেটা স্ট্রাকচার

1️⃣ Series – এক মাত্রিক

# একটি সিরিজ তৈরি করা
s = pd.Series([10, 20, 30])
print(s)

# কাস্টম ইনডেক্স সহ
s = pd.Series([100, 200, 300], index=['a', 'b', 'c'])
2️⃣ DataFrame – দুই মাত্রিক
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'Score': [85.5, 90.0, 88.0]
}
df = pd.DataFrame(data)
print(df)
📂 ডেটা ফাইল থেকে পড়া

df = pd.read_csv('data.csv')        # CSV ফাইল থেকে
df = pd.read_excel('data.xlsx')     # Excel ফাইল থেকে
df = pd.read_json('data.json')      # JSON ফাইল থেকে
🔍 ডেটা এক্সপ্লোর করা

df.head()          # প্রথম ৫টি সারি
df.tail()          # শেষ ৫টি সারি
df.info()          # সারাংশ তথ্য
df.describe()      # পরিসংখ্যানগত সারাংশ
df.columns         # কলামের নাম
df.shape           # সারি ও কলামের সংখ্যা
🔍 ডেটা নির্বাচন

df['Name']                 # একটি কলাম
df[['Name', 'Score']]      # একাধিক কলাম

df.loc[0]                  # লেবেল অনুযায়ী সারি
df.iloc[1]                 # ইনডেক্স অনুযায়ী সারি
✍️ ডেটা পরিবর্তন

df['Passed'] = df['Score'] > 80         # নতুন কলাম যোগ
df['Age'] = df['Age'] + 1               # কলাম আপডেট
🧼 ডেটা ফিল্টার করা

df[df['Score'] > 85]              # নির্দিষ্ট কন্ডিশনের সারি
df[(df['Age'] > 25) & (df['Score'] < 90)]  # একাধিক শর্ত
🔁 ডেটা সংরক্ষণ

df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx', index=False)
📚 রিসোর্স
অফিসিয়াল ডকুমেন্টেশন: https://pandas.pydata.org/docs/

১০ মিনিটে Pandas: https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html

✅ দ্রুত টিপস
df.columns ব্যবহার করে কলামের নামগুলো চেক করুন যাতে KeyError না আসে

df.head() ব্যবহার করে ডেটা দেখে নিন পরিবর্তনের আগে

ফিল্টার ও সিলেকশন একত্রে চেইন করে লিখলে কোড ক্লিন থাকে
"""

Write the note to a file
with open("README_BANGLA.md", "w", encoding="utf-8") as f:
f.write(readme_bangla)

print("✅ README_BANGLA.md ফাইলটি সফলভাবে তৈরি হয়েছে!")


---

📝 এই কোড রান করলে আপনার প্রজেক্ট ফোল্ডারে একটি সুন্দর `README_BANGLA.md` তৈরি হবে, যাতে Pandas-এর বাংলা টিউটোরিয়াল থাকবে।

আপনি চাইলে এটাকে PDF বা Jupyter Notebook আকারেও নিতে পারেন—শুধু জানিয়ে দিন!







# 🐼 Pandas দিয়ে CSV ফাইল পড়া (বাংলা নোটস)

## 🔰 `read_csv()` ফাংশন কী?

`read_csv()` হল Pandas লাইব্রেরির একটি ফাংশন, যার মাধ্যমে CSV (Comma Separated Values) ফাইল খুব সহজে DataFrame আকারে পড়া যায়।

```python
import pandas as pd

df = pd.read_csv('data.csv')
print(df.head())
🔍 গুরুত্বপূর্ণ প্যারামিটার ও বাংলা ব্যাখ্যা
প্যারামিটার	বাংলা অর্থ	উদাহরণ
filepath_or_buffer	CSV ফাইলের নাম/পথ	'data.csv'
sep	কলাম বিভাজক (ডিফল্ট ,)	sep='\t' (ট্যাব-আলাদা হলে)
header	কোন সারিটি কলাম হেডার	header=None
names	নিজস্ব কলাম নাম	names=['নাম', 'বয়স']
index_col	কোন কলামটিকে ইনডেক্স ধরা হবে	index_col=0
usecols	নির্দিষ্ট কলামগুলোই পড়া	usecols=['নাম', 'ঠিকানা']
dtype	কলামের টাইপ নির্ধারণ	dtype={'বয়স': int}
skiprows	শুরুতে কত লাইন বাদ দেবে	skiprows=2
nrows	কয়টি সারি পড়বে	nrows=50
na_values	কোন মানগুলো NaN ধরা হবে	na_values=['?', 'NA']
parse_dates	কোন কলামকে তারিখ হিসেবে পড়বে	parse_dates=['জন্মতারিখ']
encoding	ফাইলের এনকোডিং	encoding='utf-8' বা 'latin1'

🧪 কিছু উদাহরণ
✅ হেডার ছাড়া CSV ফাইল
df = pd.read_csv('data.csv', header=None)

✅ নিজস্ব কলাম নাম
df = pd.read_csv('data.csv', names=['নাম', 'বয়স', 'ঠিকানা'])

✅ নির্দিষ্ট কলাম পড়া
df = pd.read_csv('data.csv', usecols=['নাম', 'বয়স'])

✅ জন্মতারিখ পার্স করা
df = pd.read_csv('data.csv', parse_dates=['জন্মতারিখ'])

✅ প্রথম ৩ লাইন বাদ দিয়ে পড়া
df = pd.read_csv('data.csv', skiprows=3)

🚀 বড় CSV ফাইল নিয়ে কাজ করার কৌশল
🔸 চাঙ্ক আকারে CSV পড়া (chunking)
for chunk in pd.read_csv('big_data.csv', chunksize=10000):
    print(chunk.shape)

🔸 কম মেমোরি ব্যবহারের জন্য
df = pd.read_csv('data.csv', low_memory=False)

📁 উদাহরণ CSV ডেটা
আপনি চাইলে নিচের ছোট CSV ফাইল দিয়ে অনুশীলন করতে পারেন:
নাম,বয়স,জন্মতারিখ
রহিম,২৫,1998-01-01
করিম,৩০,1993-05-21
সাবিনা,২৮,1995-08-15

✅ লাইব্রেরি ইনস্টল (প্রয়োজন হলে)
pip install pandas

✨ সমাপ্তি
এই নোটসটি Pandas দিয়ে CSV ফাইল পড়ার জন্য বাংলা ভাষায় সহজ গাইড হিসেবে তৈরি করা হয়েছে। ডেটা অ্যানালাইসিস ও মেশিন লার্নিং শুরু করার জন্য এটি অত্যন্ত প্রয়োজনীয় একটি টুল।

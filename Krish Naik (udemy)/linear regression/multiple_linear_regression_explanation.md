# Multiple Linear Regression কোডের বাংলা ব্যাখ্যা

---

## ১. লাইব্রেরি ইম্পোর্ট
```python
import numpy as np 
import pandas as pd 
from sklearn.linear_model import LinearRegression
```
**ব্যাখ্যা:**
- `numpy` ও `pandas` ডেটা প্রসেসিংয়ের জন্য ব্যবহৃত হয়।
- `LinearRegression` স্কিকিট-লার্ন লাইব্রেরি থেকে, মডেল তৈরির জন্য।

---

## ২. ডেটা তৈরি
```python
data = {
    'Hours_Study': [2, 4, 6, 8, 10],
    'Attendance': [60, 70, 75, 85, 95],
    'Marks': [210, 250, 270, 300, 310]
}
```
**ব্যাখ্যা:**
- এখানে একটি ডিকশনারি আকারে ডেটাসেট তৈরি করা হয়েছে।
- Hours_Study: কত ঘন্টা পড়াশোনা করেছে
- Attendance: উপস্থিতির হার (%)
- Marks: পরীক্ষার নম্বর

---

## ৩. DataFrame তৈরি
```python
df=pd.DataFrame(data)
```
**ব্যাখ্যা:**
- pandas DataFrame বানানো হয়েছে, যাতে ডেটা সহজে বিশ্লেষণ করা যায়।

---

## ৪. ফিচার ও টার্গেট নির্বাচন
```python
X = df[['Hours_Study', 'Attendance']] # independent variables
y = df['Marks'] # dependent variable
```
**ব্যাখ্যা:**
- `X` হচ্ছে স্বাধীন ভেরিয়েবল (Hours_Study, Attendance)
- `y` হচ্ছে নির্ভরশীল ভেরিয়েবল (Marks)

---

## ৫. মডেল তৈরি ও ট্রেইন
```python
model = LinearRegression()
model.fit(X, y)
```
**ব্যাখ্যা:**
- Linear Regression মডেল তৈরি ও ডেটার উপর ট্রেইন করা হয়েছে।

---

## ৬. Intercept ও Coefficient বের করা
```python
print("Intercept (β0):", model.intercept_)
print("Coefficients (β1, β2):", model.coef_)
```
**ব্যাখ্যা:**
- Intercept (β0): যেখানে রেখা y-অক্ষ ছেদ করে
- Coefficients (β1, β2): প্রতিটি ফিচারের প্রভাব

---

## ৭. নতুন ডেটার জন্য পূর্বাভাস
```python
new_data = [[5, 80]]  # 5 ঘন্টা পড়াশোনা, 80% উপস্থিতি
prediction = model.predict(new_data)
print("Predicted Marks:", prediction)
```
**ব্যাখ্যা:**
- নতুন ডেটা (৫ ঘন্টা পড়া, ৮০% উপস্থিতি) দিয়ে পরীক্ষার নম্বর পূর্বাভাস করা হয়েছে।
- মডেল মূলত এই ফর্মুলা ব্যবহার করে: Marks = β0 + β1 × Hours_Study + β2 × Attendance

---

## ৮. সংক্ষেপে
- এই কোডের মাধ্যমে Multiple Linear Regression মডেল তৈরি, ট্রেইন এবং নতুন ডেটার জন্য পূর্বাভাস করা হয়।
- প্রতিটি ধাপের বাংলা ব্যাখ্যা এখানে দেওয়া হয়েছে।

---

*© 2025 - Multiple Linear Regression কোডের বাংলা ব্যাখ্যা*

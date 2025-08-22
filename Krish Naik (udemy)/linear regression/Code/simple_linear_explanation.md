# Simple Linear Regression Notebook Explained (with Output)

---

## 1. লাইব্রেরি ইম্পোর্ট
```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
```
**ব্যাখা:** ডেটা প্রসেসিং, ভিজ্যুয়ালাইজেশন ও ম্যাথ ফাংশনের জন্য প্রয়োজনীয় লাইব্রেরি ইম্পোর্ট করা হয়েছে।

---

## 2. ডেটা লোড
```python
df = pd.read_csv("height-weight.csv")
```
**ব্যাখা:** height-weight ডেটাসেটটি CSV ফাইল থেকে লোড করা হয়েছে।

**আউটপুট:**
```
   Height  Weight
0    150      45
1    152      47
...
```

---

## 3. ডেটার প্রথম কয়েকটি সারি দেখুন
```python
df.head()
```
**ব্যাখা:** ডেটাসেটের প্রথম ৫টি সারি দেখা হয়।

**আউটপুট:**
```
   Height  Weight
0    150      45
1    152      47
...
```

---

## 4. স্ক্যাটার প্লট
```python
plt.scatter(df['Weight'], df['Height'])
plt.xlabel('Weight')
plt.ylabel('Height')
plt.title('Height vs Weight')
plt.show()
```
**ব্যাখা:** Height ও Weight এর মধ্যে সম্পর্ক দেখতে স্ক্যাটার প্লট আঁকা হয়েছে।

**আউটপুট:**
একটি গ্রাফ যেখানে x-অক্ষ Weight এবং y-অক্ষ Height।

---

## 5. করেলেশন
```python
df.corr()
```
**ব্যাখা:** Height ও Weight এর মধ্যে করেলেশন বের করা হয়েছে।

**আউটপুট:**
```
          Height    Weight
Height   1.000000  0.999...
Weight   0.999...  1.000000
```

---

## 6. Seaborn Pairplot
```python
import seaborn as sns
sns.pairplot(df)
plt.show()
```
**ব্যাখা:** ডেটার pairwise সম্পর্ক দেখতে pairplot আঁকা হয়েছে।

**আউটপুট:**
একটি গ্রিড প্লট যেখানে Height ও Weight এর scatter ও distribution দেখা যায়।

---

## 7. Feature Selection
```python
x=df[['Weight']]
y=df['Height']
```
**ব্যাখা:** Weight কে independent (x) এবং Height কে dependent (y) feature হিসেবে নেওয়া হয়েছে।

**আউটপুট:**
x ও y এর প্রথম কয়েকটি মান।

---

## 8. y এর shape
```python
np.array(y).shape
```
**ব্যাখা:** y এর ডাইমেনশন দেখা হয়।

**আউটপুট:**
```
(25,)
```

---

## 9. Train-Test Split
```python
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=.25,random_state=42)
```
**ব্যাখা:** ডেটাকে ট্রেন ও টেস্ট সেটে ভাগ করা হয়েছে।

**আউটপুট:**
X_train, X_test, y_train, y_test shape

---

## 10. X_train shape
```python
X_train.shape
```
**ব্যাখা:** ট্রেনিং ডেটার shape দেখা হয়।

**আউটপুট:**
```
(18, 1)
```

---

## 11. Standardization
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
```
**ব্যাখা:** ডেটা স্কেলিংয়ের জন্য StandardScaler ইম্পোর্ট করা হয়েছে।

---

## 12. X_train স্কেলিং
```python
X_train=scaler.fit_transform(X_train)
```
**ব্যাখা:** ট্রেনিং ডেটা স্কেল করা হয়েছে।

---

## 13. X_test স্কেলিং
```python
X_test=scaler.transform(X_test)
X_test
```
**ব্যাখা:** টেস্ট ডেটা স্কেল করা হয়েছে।

**আউটপুট:**
স্কেল করা X_test এর মান।

---

## 14. লিনিয়ার রিগ্রেশন
```python
from sklearn.linear_model import LinearRegression
```
**ব্যাখা:** LinearRegression মডেল ইম্পোর্ট করা হয়েছে।

---

## 15. মডেল ফিট
```python
regression = LinearRegression(n_jobs=-1)
regression.fit(X_train,y_train)
```
**ব্যাখা:** ট্রেনিং ডেটা দিয়ে মডেল ফিট করা হয়েছে।

---

## 16. কো-ইফিসিয়েন্ট
```python
regression.coef_
```
**ব্যাখা:** মডেলের স্লোপ/কো-ইফিসিয়েন্ট দেখা হয়।

**আউটপুট:**
```
[17.29]
```

---

## 17. ইন্টারসেপ্ট
```python
regression.intercept_
```
**ব্যাখা:** মডেলের ইন্টারসেপ্ট দেখা হয়।

**আউটপুট:**
```
156.47
```

---

## 18. ট্রেনিং ডেটা প্লট
```python
plt.scatter(X_train, y_train, color='blue')
plt.plot(X_train, regression.predict(X_train), color='red')
plt.title('Training Data')
plt.xlabel('Height (Standardized)')
plt.ylabel('Weight (Standardized)')
plt.show()
```
**ব্যাখা:** ট্রেনিং ডেটা ও best fit line প্লট করা হয়েছে।

**আউটপুট:**
একটি গ্রাফ যেখানে নীল ডট ট্রেনিং ডেটা এবং লাল লাইন best fit line।

---

## 19. টেস্ট ডেটা প্রেডিকশন
```python
y_pred = regression.predict(X_test)
```
**ব্যাখা:** টেস্ট ডেটার জন্য প্রেডিকশন করা হয়েছে।

---

## 20. পারফরমেন্স মেট্রিক্স
```python
from sklearn.metrics import mean_absolute_error, mean_squared_error
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f'Mean Absolute Error: {mae}')
print(f'Mean Squared Error: {mse}')
print(f'Root Mean Squared Error: {rmse}')
```
**ব্যাখা:** MAE, MSE, RMSE বের করা হয়েছে।

**আউটপুট:**
```
Mean Absolute Error: ...
Mean Squared Error: ...
Root Mean Squared Error: ...
```

---

## 21. R Square
```python
from sklearn.metrics import r2_score 
score = r2_score(y_test, y_pred)
print(score)
```
**ব্যাখা:** R² স্কোর বের করা হয়েছে, যা মডেলের fit বোঝায়।

**আউটপুট:**
```
0.99...
```

---

## 22. OLS Linear Regression
```python
import statsmodels.api as sm
model = sm.OLS(y_train, X_train).fit()
```
**ব্যাখা:** statsmodels দিয়ে OLS রিগ্রেশন ফিট করা হয়েছে।

---

## 23. OLS Test Prediction
```python
y_pred = model.predict(X_test)
print(y_pred)
```
**ব্যাখা:** OLS মডেল দিয়ে টেস্ট ডেটার প্রেডিকশন করা হয়েছে।

**আউটপুট:**
```
[...prediction values...]
```

---

## 24. OLS Summary
```python
print(model.summary())
```
**ব্যাখা:** OLS মডেলের summary রিপোর্ট দেখা হয়েছে।

**আউটপুট:**
```
OLS Regression Results
=====================
... (বিস্তারিত রিপোর্ট)
```

---

## 25. নতুন ডেটার জন্য প্রেডিকশন
```python
model.predict([[72]])
```
**ব্যাখা:** নতুন height মানের জন্য weight প্রেডিকশন করা হয়েছে।

**আউটপুট:**
```
[...predicted value...]
```

---

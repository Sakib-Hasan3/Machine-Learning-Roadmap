# 📊 Seaborn Visualization নোটস (বাংলায়, ব্যাখা সহ)

## ✅ লাইব্রেরি ইমপোর্ট

```python
import seaborn as sns
import matplotlib.pyplot as plt
````

🔍 Seaborn হলো Python-এর একটি visualization লাইব্রেরি।
Matplotlib হলো গ্রাফ আঁকার জন্য বেসিক লাইব্রেরি — Seaborn তার ওপর ভিত্তি করে কাজ করে।

---

## ✅ ডেটাসেট লোড

```python
tips = sns.load_dataset("tips")
flights = sns.load_dataset("flights")
iris = sns.load_dataset("iris")
```

🔍 `load_dataset()` দিয়ে Seaborn থেকে ডেমো ডেটাসেট লোড করা হয়।

* `tips` → রেস্টুরেন্টের বিল ও টিপসের ডেটা
* `flights` → মাস ও বছর অনুযায়ী বিমানযাত্রীর সংখ্যা
* `iris` → ফুলের পাপড়ির মাপ ও প্রজাতি

---

## ✅ গ্রাফের স্টাইল সেটিং

```python
sns.set_style('whitegrid')
sns.set_context("paper")
sns.despine()
```

🔍

* `whitegrid` → ব্যাকগ্রাউন্ডে সাদা রঙ ও হালকা গ্রিড
* `paper` → ছোট ফন্ট, প্রিন্ট করার জন্য উপযোগী
* `despine()` → উপর ও ডানদিকের বর্ডার সরিয়ে দেয়

---

## ✅ Countplot (বার চার্ট)

```python
sns.countplot(data=tips, x='smoker')
sns.countplot(x='sex', data=tips, palette='Blues')
plt.figure(figsize=(12, 3))
sns.countplot(x='sex', data=tips)
```

🔍 একটি ক্যাটাগরিকাল ভেরিয়েবলের প্রতিটি মান কতবার ঘটেছে তা বার চার্টে দেখায়।
`palette='Blues'` মানে বারগুলো নীল রঙে দেখানো হবে।

---

## ✅ lmplot (রিগ্রেশন রেখা সহ Scatter Plot)

```python
sns.lmplot(x='total_bill', y='tip', data=tips)
sns.lmplot(x='total_bill', y='tip', data=tips, hue='smoker')
sns.lmplot(x='total_bill', y='tip', data=tips, col='sex')
sns.lmplot(x='total_bill', y='tip', data=tips, row='sex', col='time')
sns.lmplot(x='total_bill', y='tip', data=tips, row='time', col='sex', hue='smoker')
sns.lmplot(x='total_bill', y='tip', data=tips, aspect=4)
```

🔍 Scatter Plot-এর ওপর সোজা রিগ্রেশন লাইন আঁকে।

* `hue` → আলাদা রঙে গ্রুপ
* `row`, `col` → subplot-এ বিভক্ত করে
* `aspect=4` → চওড়া স্কেলের গ্রাফ

---

## ✅ Box, Violin, Swarm, Strip Plots

```python
sns.boxplot(x="day", y="total_bill", data=tips, hue='smoker', palette='Blues')
sns.violinplot(x="day", y="total_bill", data=tips, hue='smoker', split=True)
sns.swarmplot(x="day", y="total_bill", data=tips, hue='smoker')
sns.stripplot(x="day", y="total_bill", data=tips, hue='smoker', dodge=True, jitter=True)
```

🔍

* **Boxplot** → গড়, ছড়ানো, এবং outlier দেখা যায়
* **Violinplot** → boxplot + distribution
* **Swarmplot** → প্রতিটি পয়েন্টকে overlap ছাড়া দেখায়
* **Stripplot** → হালকা এলোমেলোভাবে পয়েন্ট ছড়িয়ে overlap কমায়

---

## ✅ Pairplot & PairGrid

```python
sns.pairplot(iris)

g = sns.PairGrid(iris)
g.map_diag(sns.histplot)
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot)
```

🔍

* `pairplot` → সব সংখ্যাসংক্রান্ত কলামের মধ্যে pairwise relationship দেখায়
* `PairGrid` → তুমি নিজে ঠিক করতে পারো কোন অংশে কোন প্লট থাকবে

  * `diag` → কোণে histogram
  * `upper` → উপর দিকে scatter
  * `lower` → নিচে density plot

---

## ✅ FacetGrid (বিভাগ অনুযায়ী subplot)

```python
g = sns.FacetGrid(tips, col='time', row='smoker')
g.map(sns.scatterplot, 'total_bill', 'tip')
```

🔍
FacetGrid দিয়ে `row` এবং `column` অনুযায়ী subplot বানানো যায়।
উদাহরণ: Lunch vs Dinner এবং Smoker vs Non-smoker মিলিয়ে একাধিক গ্রাফ।

---

## ✅ Displot, Histplot, Rugplot (Distribution Plot)

```python
sns.displot(tips["total_bill"], kde=True, bins=30)
sns.histplot(tips["total_bill"], kde=True, bins=30)
sns.rugplot(tips["total_bill"])
```

🔍

* **Displot** → histogram + KDE curve
* **Histplot** → histogram + line
* **Rugplot** → প্রতিটি পয়েন্টকে নিচে ছোট দাগ দিয়ে দেখায়

---

## ✅ Heatmap ও Clustermap (2D Data Visualization)

```python
fp = flights.pivot_table(index='month', columns='year', values='passengers')
sns.heatmap(fp, cmap='plasma', linewidth=0.5, annot=True, fmt=".0f")
sns.clustermap(fp, cmap='plasma')
```

🔍

* `pivot_table()` → মাস ও বছরের ভিত্তিতে যাত্রী সংখ্যা
* `heatmap` → ঘরে ঘরে যাত্রী সংখ্যা রঙে বোঝায়
* `clustermap` → একই রকম মাস/বছর গুচ্ছ (cluster) করে সাজায়

---


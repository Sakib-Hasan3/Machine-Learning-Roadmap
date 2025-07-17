## 🔹 Pyforest কী?

`pyforest` একটি Python লাইব্রেরি যা **স্বয়ংক্রিয়ভাবে জনপ্রিয় ডেটা সায়েন্স লাইব্রেরিগুলো ইম্পোর্ট করে নেয়**, শুধুমাত্র তখনই যখন আপনি সেগুলো ব্যবহার করেন।  
এর ফলে কোড **ক্লিন** হয় এবং **দ্রুত রান** করে।

এটি নিচের মতো লাইব্রেরিগুলোর **lazy import** সাপোর্ট করে:

- `pandas`  
- `numpy`  
- `matplotlib.pyplot`  
- `seaborn`  
- `sklearn`  
- `tensorflow`  
- `keras`  
- `xgboost`  
- `lightgbm`  
- `plotly`  
- এবং আরও অনেক...

---

## 🔸 Pyforest ইন্সটল করবেন যেভাবে

```bash
pip install pyforest
```

---

## 🔸 কিভাবে Pyforest ব্যবহার করবেন

আপনাকে আর আলাদা করে `import` লিখতে হবে না। আপনি সরাসরি লাইব্রেরির শর্টকাট ব্যবহার করলেই চলবে — `pyforest` ব্যাকগ্রাউন্ডে তা ইম্পোর্ট করে নেবে।

```python
# এখানে আলাদা করে import pandas as pd লিখতে হয়নি
df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
print(df)

# numpy ব্যবহার করছি সরাসরি
arr = np.array([1, 2, 3, 4])
print(arr.mean())

# matplotlib দিয়ে প্লট
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
```

`pyforest` নিজে থেকেই বুঝে নেয়:

- `pd` → `pandas`  
- `np` → `numpy`  
- `plt` → `matplotlib.pyplot`  
- `sns` → `seaborn`  
- `sklearn`, `xgboost`, `lgbm` ইত্যাদি

---

## ✅ Pyforest ব্যবহারের সুবিধা

- কোড অনেক **সিম্পল** ও **পরিষ্কার** হয়  
- লাইব্রেরি ইম্পোর্ট করতে হয় না বারবার  
- প্রোটোটাইপিং বা দ্রুত কাজের জন্য খুবই ভালো  
- Jupyter Notebook বা শেখানোর ক্ষেত্রে অসাধারণ

---

## ⚠️ সতর্কতা

- Pyforest সবচেয়ে ভালো কাজ করে **Jupyter Notebook** বা ছোট স্ক্রিপ্টে।  
- কিন্তু **প্রোডাকশন কোডে** সব লাইব্রেরি স্পষ্টভাবে `import` করা ভালো।

---



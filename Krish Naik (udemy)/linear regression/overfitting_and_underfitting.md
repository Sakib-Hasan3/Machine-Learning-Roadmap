# Overfitting এবং Underfitting — বাংলায় সহজ ব্যাখ্যা

---

## ১. Underfitting কী?

যখন কোনো মডেল ডেটার আসল pattern ধরতে পারে না, তখন সেটিকে **Underfitting** বলে।

### কারণ:
- মডেল অনেক simple
- যথেষ্ট সময় ট্রেনিং না করানো
- গুরুত্বপূর্ণ ফিচার বাদ পড়া

### লক্ষণ:
- ট্রেনিং ডেটাতে accuracy খারাপ
- টেস্ট ডেটাতেও accuracy খারাপ

### উদাহরণ:
ছাত্রের নাম দেখে নম্বর predict করতে চাইলে, নামের সাথে নম্বরের কোনো সম্পর্ক নেই — মডেল underfit হবে।

---

## ২. Overfitting কী?

যখন মডেল ট্রেনিং ডেটা অতিরিক্ত মুখস্থ করে ফেলে, তখন সেটাকে **Overfitting** বলে।

### কারণ:
- মডেল অনেক complex
- খুব বেশি ফিচার
- অনেক বেশি সময় ট্রেনিং

### লক্ষণ:
- ট্রেনিং ডেটাতে accuracy খুব ভালো
- টেস্ট/নতুন ডেটাতে accuracy খারাপ

### উদাহরণ:
ছাত্র শুধু আগের বছরের প্রশ্ন মুখস্থ করেছে। পরীক্ষায় হুবহু সেগুলো এলে ভালো করবে, নতুন প্রশ্ন এলে খারাপ করবে — Overfitting।

---

## ৩. Good Fit

- ট্রেনিং ডেটাতে ভালো accuracy
- টেস্ট ডেটাতেও ভালো accuracy
- মডেল আসল pattern শিখেছে, মুখস্থ করেনি

---

## ৪. ভিজ্যুয়াল ব্যাখ্যা

- **Underfitting** → লাইনটা খুব সোজা, ডেটার pattern ধরতে পারছে না
- **Overfitting** → লাইনটা সব পয়েন্টকে আঁকড়ে ধরেছে, smooth নয়
- **Good Fit** → লাইনটা smooth, বেশিরভাগ পয়েন্টের trend ধরেছে

---

## ৫. Overfitting ঠেকানোর উপায়

- Cross Validation
- Feature Selection (অপ্রয়োজনীয় ফিচার বাদ)
- Regularization (L1, L2 penalty)
- Pruning (Decision Tree)
- Dropout (Deep Learning)
- কম জটিল মডেল ব্যবহার

---

## সংক্ষেপে

- **Underfitting** = ডেটা শেখেনি
- **Overfitting** = ডেটা মুখস্থ করেছে
- **Good Fit** = ডেটার আসল pattern শিখেছে

---

*© 2025 - Overfitting এবং Underfitting বাংলা টিউটোরিয়াল*

# রিজ রিগ্রেশন (Ridge Regression)

রিজ রিগ্রেশন একটি linear regression-এর উন্নত সংস্করণ, যা multicollinearity (যখন একাধিক independent variable পরস্পরের সাথে সম্পর্কিত থাকে) সমস্যার সমাধানে ব্যবহৃত হয়।

---

## 📌 রিজ রিগ্রেশন কী?

রিজ রিগ্রেশন একটি regularization technique, যা linear regression model-এ একটি penalty term যোগ করে। এই penalty term হলো L2 norm (squared magnitude of coefficients)।

এর মূল উদ্দেশ্য:

- মডেলকে overfitting থেকে রক্ষা করা।
- multicollinearity সমস্যা কমানো।

---

## 📘 রিজ রিগ্রেশনের গাণিতিক ফর্মুলা

সাধারণ লিনিয়ার রিগ্রেশনের cost function:

$$
J(\theta) = \sum_{i=1}^{n}(y_i - \hat{y}_i)^2
$$

রিজ রিগ্রেশনে penalty term যুক্ত করে:

$$
J(\theta) = \sum_{i=1}^{n}(y_i - \hat{y}_i)^2 + \lambda \sum_{j=1}^{p} \theta_j^2
$$

এখানে:

- $\lambda$ (lambda) = regularization parameter
- $\theta_j$ = model-এর coefficients

---

## 🔍 কীভাবে কাজ করে?

- যখন lambda = 0, তখন Ridge Regression → সাধারণ Linear Regression।
- যখন lambda > 0, তখন coefficients গুলো ছোট হয়, কিন্তু একদম ০ হয় না।

এটি feature selection করে না, বরং সব feature-কে রাখে, কিন্তু ওজন (weight) ছোট করে দেয়।

---

## 🧠 কবে ব্যবহার করবেন?

- যখন আপনার dataset-এ multicollinearity রয়েছে।
- যখন আপনি overfitting এ সমস্যায় পড়েছেন।
- যখন আপনি সব feature রাখতে চান, কিন্তু তাদের প্রভাব নিয়ন্ত্রণ করতে চান।

---

## ✅ সুবিধা

- Overfitting কমায়
- Multicollinearity-এর সমস্যা হ্রাস করে
- Model-এর generalization ক্ষমতা বাড়ায়

---

## ⚠️ সীমাবদ্ধতা

- কিছু coefficient ছোট করলেও, একদম বাদ দেয় না (LASSO-র মতো না)
- ব্যাখ্যা কঠিন হতে পারে যখন অনেক feature থাকে

---

## 📊 উদাহরণ (সাধারণ):

ধরা যাক আপনার কাছে student-এর GPA পূর্বাভাস করার জন্য নিচের তথ্য আছে:

- ঘুমের সময়
- পড়ার সময়
- ফেসবুকে সময়
- টিভি দেখা

এইসব feature একে অপরের সাথে সম্পর্কিত হতে পারে। তখন ridge regression ব্যবহার করে আপনি একটি ভালো prediction মডেল তৈরি করতে পারেন যা overfitting কমাবে।

---

আপনি চাইলে আমি Python-এ একটি উদাহরণ কোড দিয়েও বুঝাতে পারি। জানালে তৈরি করে দেব।

# MSE, MAE, RMSE — বাংলায় সহজ ব্যাখ্যা

---

## ভূমিকা

মডেলের প্রতিটি ডেটা পয়েন্টের error বিশ্লেষণ করতে আমরা **Mean Squared Error (MSE)**, **Mean Absolute Error (MAE)** এবং **Root Mean Squared Error (RMSE)** ব্যবহার করি।

---

## ১. Mean Squared Error (MSE)

### সূত্র:
$$
MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

- প্রতিটি error (y – ŷ) স্কয়ার করে গড় বের করি।

### সুবিধা
1. **Differentiable everywhere** — gradient descent সহজ হয়।
2. **Convex function** — শুধু একটি Global Minima থাকে।
3. **Convergence faster** — দ্রুত সমাধানে পৌঁছায়।

### অসুবিধা
1. **Not robust to outliers** — outlier থাকলে error বেশি penalize হয়।
2. **Unit পরিবর্তিত হয়** — স্কয়ার করার ফলে ইউনিট বদলে যায়।

---

## ২. Mean Absolute Error (MAE)

### সূত্র:
$$
MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|
$$

- error-এর absolute মান ব্যবহার করি।

### সুবিধা
1. **Robust to outliers** — outlier থাকলেও error বেশি penalize হয় না।
2. **Same unit as output** — error-এর ইউনিট আসল আউটপুটের মতোই থাকে।

### অসুবিধা
1. **Not differentiable at zero** — zero পয়েন্টে slope বের করা যায় না।
2. **Slower convergence** — optimization তুলনামূলক বেশি সময় নেয়।

---

## ৩. Root Mean Squared Error (RMSE)

### সূত্র:
$$
RMSE = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}
$$

- এটি MSE-এর বর্গমূল।

### সুবিধা
1. **Same unit as output** — error-এর ইউনিট আসল আউটপুটের মতোই থাকে।
2. **Differentiable** — gradient descent-এ সহজে ব্যবহার করা যায়।

### অসুবিধা
1. **Not robust to outliers** — outlier থাকলে error অনেক বেড়ে যায়।

---

## কোনটা কখন ব্যবহার করব?

- **MSE** — দ্রুত convergence, differentiable, outlier সংবেদনশীল।
- **MAE** — outlier-এ robust, convergence ধীর।
- **RMSE** — ইউনিট একই থাকে, outlier-এ সংবেদনশীল।

**সাধারণত সবগুলো মেট্রিকস একসাথে ব্যবহার করে মডেলের পারফরম্যান্স বোঝা হয়।**

---

## ইন্টারভিউ প্রশ্নে

- **MSE কেন ব্যবহার করবেন?** — differentiable, convex function, দ্রুত convergence।
- **MAE কেন ব্যবহার করবেন?** — robust to outliers।
- **RMSE কেন ব্যবহার করবেন?** — আসল আউটপুটের ইউনিটে error দেয়, সহজে ব্যাখ্যা করা যায়।

---

*© 2025 - MSE, MAE, RMSE বাংলা টিউটোরিয়াল*

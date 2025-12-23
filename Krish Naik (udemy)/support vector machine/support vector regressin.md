# Support Vector Regression (SVR) — সহজ বাংলায়

SVR হলো SVM-এর regression সংস্করণ — এখানে লক্ষ্য হলো একটি এমন রেখা/কার্ভ শিখে নেওয়া যার চারপাশে একটি ε (epsilon)–tube থাকে: টিউবের ভেতরের ভুল গণনা করা হয় না, টিউবের বাইরে গেলে শাস্তি (penalty) লাগে।

---

## 1️⃣ SVR কী কাজ করে?

- Classification নয়, এটি regression করে (continuous value predict)
- উদাহরণ: বাড়ির দাম, তাপমাত্রা, CGPA/স্কোর প্রেডিকশন

---

## 2️⃣ মূল আইডিয়া: ε–tube

- মডেল একটি `f(x)` ফাংশন শিখে
- `|y - f(x)| ≤ ε` হলে loss = 0 (ভিতরে থাকলে ignore)
- `|y - f(x)| > ε` হলে tube-এর বাইরে — penalty শুরু

---

## 3️⃣ ε–Insensitive Loss

এক-পয়েন্টের loss:

$$
L(y, f(x)) =
\begin{cases}
0, & \text{যদি } |y - f(x)| \le \varepsilon \\
|y - f(x)| - \varepsilon, & \text{যদি } |y - f(x)| > \varepsilon
\end{cases}
$$

অর্থ: ε-এর ভিতরে prediction থাকলে কোনো শাস্তি নেই; বাইরে গেলেই শাস্তি শুরু।

---

## 4️⃣ SVR Cost Function (Primal)

উদ্দেশ্য (objective):

$$
\min_{w,\,b,\,\xi,\,\xi^*}\; \frac{1}{2}\,\lVert w\rVert^2 \; + \; C \sum_{i=1}^{n} (\xi_i + \xi_i^*)
$$

শর্ত (constraints):

$$
\begin{aligned}
y_i - (w\cdot x_i + b) &\le \varepsilon + \xi_i \\
(w\cdot x_i + b) - y_i &\le \varepsilon + \xi_i^* \\
\xi_i,\,\xi_i^* &\ge 0
\end{aligned}
$$

ব্যাখ্যা:
- `½‖w‖²`: ফাংশনকে simple/flat রাখে (overfitting কমায়)
- `\xi_i, \xi_i^*`: ε–tube এর উপরে/নিচের অতিরিক্ত error
- `C`: শাস্তির কঠোরতা (বড় C → কম ভুল সহ্য; ছোট C → বেশি সহ্য)

---

## 5️⃣ Kernel কেন দরকার?

Non-linear সম্পর্ক ধরতে kernel ব্যবহার করা হয়:
- Linear, Polynomial, RBF (খুব জনপ্রিয়), Sigmoid
- Kernel ট্রিক দিয়ে high-dimensional feature space এ linear fit ⇒ input space এ non-linear curve

---

## 6️⃣ SVC vs SVR (দ্রুত তুলনা)

| বিষয় | SVC | SVR |
|---|---|---|
| কাজ | Classification | Regression |
| Output | Class label | Continuous value |
| Loss | Hinge loss | ε–insensitive loss |

---

## 7️⃣ Python (scikit-learn) উদাহরণ

নিচে 1D ডেটাসেটে SVR চালানো, prediction curve আঁকা, এবং ε–tube দেখানোর উদাহরণ দেওয়া হলো।

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR

# 1) Synthetic 1D data
rs = np.random.RandomState(42)
X = np.linspace(-3, 3, 120).reshape(-1, 1)
true_f = np.sin(X).ravel()
y = true_f + rs.normal(scale=0.2, size=X.shape[0])

# 2) Model: RBF SVR
epsilon = 0.2
C = 10.0
svr = SVR(kernel='rbf', C=C, epsilon=epsilon, gamma='scale')
svr.fit(X, y)

# 3) Predict and plot
X_test = np.linspace(-3.5, 3.5, 400).reshape(-1, 1)
y_pred = svr.predict(X_test)

plt.figure(figsize=(7,5))
plt.scatter(X, y, s=25, color='tab:blue', edgecolor='k', alpha=0.7, label='data')
plt.plot(X_test, y_pred, color='k', lw=2, label='SVR prediction f(x)')
plt.fill_between(X_test.ravel(), y_pred - epsilon, y_pred + epsilon, color='orange', alpha=0.25, label='ε-tube')
plt.title(f"SVR (RBF) — C={C}, ε={epsilon}")
plt.legend()
plt.tight_layout()
plt.show()
```

পরিবর্তন করে `kernel='linear'` দিলে লিনিয়ার ফিট পাওয়া যাবে।

---

## 8️⃣ Tuning Guide: C, ε, γ

- C (regularization):
	- বড় C → ভুল কম সহ্য, জটিল ফিট, overfit ঝুঁকি
	- ছোট C → বেশি সহ্য, মসৃণ ফিট, ভালো generalization
- ε (tube width):
	- বড় ε → টিউব চওড়া, অনেক পয়েন্টে loss=0 → মসৃণ/সরল ফিট
	- ছোট ε → টিউব সরু → বেশি পয়েন্ট পেনাল্টি পাবে → curve ডেটা ঘেঁষে যাবে
- γ (RBF kernel width):
	- বড় γ → kernel খুব “লোকাল” → curve টা খাড়া/জটিল হতে পারে (overfit)
	- ছোট γ → kernel “wide” → curve মসৃণ (underfit ঝুঁকি)

প্র্যাকটিক্যালি GridSearchCV/RandomizedSearchCV দিয়ে `(C, ε, γ)` টিউন করা ভালো।

---

## 9️⃣ এক্সাম-রেডি শর্ট নোট

- Loss: ε–insensitive, $L = \max(0, |y - f(x)| - \varepsilon)$
- Primal: $\min \tfrac{1}{2}\lVert w\rVert^2 + C\sum(\xi_i+\xi_i^*)$ with ε-constraints
- Kernel: Linear/Poly/RBF; RBF বহুল ব্যবহৃত
- টিউনিং: C↑ ⇒ কম ভুল সহ্য; ε↑ ⇒ মসৃণ; γ↑ ⇒ জটিল
- Intuition: ε–tube ভেতরে error ফ্রি; বাইরে penalty

---

চাইলে আমি গ্রাফ জেনারেটর স্ক্রিপ্টও যোগ করেছি — ε–tube সহ প্লট PNG হিসেবে সেভ করবে। নিচে রান করার ধাপ দেওয়া হলো।

### রান নির্দেশনা (Windows PowerShell)

```powershell
pip install -r requirements.txt
python svr_plot.py
```

আউটপুট: `assets/svr_rbf_tube.png` ছবি তৈরি হবে।


# SVC (Support Vector Classifier) — Cost Function (সহজ বাংলা)

SVC এমন একটি মডেল যা একসাথে দুটো লক্ষ্য পূরণ করে:
- ভুল ক্লাসিফিকেশন কমানো (penalty/শাস্তি কম রাখা)
- ডিসিশন বাউন্ডারির মার্জিন যত বড় সম্ভব করা

নিচে ধাপে ধাপে ব্যাখ্যা করা হলো।

---

## 1️⃣ SVC Cost Function কী?

SVC-তে আমরা দুইটি জিনিস মিনিমাইজ করি:
1) মার্জিন ছোট করা মানে `‖w‖` ছোট রাখার চেষ্টা (মার্জিন বড় হয়)
2) ভুলের জন্য শাস্তি যোগ করা (slack/hinge loss)

---

## 2️⃣ Soft Margin SVC — Primal Form

উদ্দেশ্য (objective):

$$
\min_{w,\,b,\,\xi}\; \frac{1}{2}\,\lVert w\rVert^2\; +\; C\, \sum_{i=1}^{n} \xi_i
$$

শর্ত (constraints):

$$
y_i\, (w\cdot x_i + b) \;\ge\; 1 - \xi_i,\quad \xi_i \ge 0\;\;\forall i
$$

এখানে:
- `½‖w‖²`: মার্জিন বড় করার অংশ (‖w‖ যত ছোট, মার্জিন তত বড়)
- `\xi_i`: i-তম পয়েন্টের ভুলের পরিমাণ (slack)
- `C`: ভুলের শাস্তি কতটা কড়া হবে তার নিয়ন্ত্রক

`C` বড় হলে মডেল ভুল একদমই সহ্য করতে চায় → মার্জিন ছোট হতে পারে (overfitting ঝুঁকি)। `C` ছোট হলে কিছু ভুল মানে → মার্জিন সাধারণত বড় থাকে (better generalization)।

---

## 3️⃣ Hinge Loss দিয়ে একই কথা

একই অপ্টিমাইজেশনকে loss দিয়ে লেখা যায়। প্রথমে এক-পয়েন্টের hinge loss:

$$
\ell_i\;=\;\max\big(0,\; 1 - y_i\,[w\cdot x_i + b]\big)
$$

এখন মোট উদ্দেশ্য:

$$
\min_{w,\,b}\; \frac{1}{2}\,\lVert w\rVert^2\; +\; C \sum_{i=1}^{n} \ell_i
\quad\text{(বা, গড় নিলে }\; \frac{C}{n}\sum_i \ell_i\text{)}
$$

টীকা:
- Scikit-learn এর `LinearSVC` প্রায়শই squared hinge ব্যবহার করে: `max(0, 1 - y f(x))^2`
- `SVC(kernel='linear')` ডিফল্টে hinge loss-ই ব্যবহার করে।

---

## 4️⃣ Hard Margin (বিশেষ কেস)

ডেটা যদি সম্পূর্ণভাবে separable হয়, তখন slack দরকার নেই:

$$
\min_{w,\,b}\; \frac{1}{2}\,\lVert w\rVert^2\quad\text{s.t.}\quad y_i\,(w\cdot x_i + b)\ge 1
$$

বাস্তবে সম্পূর্ণ separability কমন না, তাই Soft Margin-ই বেশি ব্যবহৃত।

---

## 5️⃣ `C` (Penalty) দ্রুত মনে রাখার টেবিল

| C এর মান | কী বোঝায় |
|---|---|
| বড় `C` | ভুল প্রায় সহ্য করে না → ছোট মার্জিন/overfit ঝুঁকি |
| ছোট `C` | কিছু ভুল মানে → বড় মার্জিন/ভালো generalization |

---

## 6️⃣ গ্রাফিক্যাল ধারণা (intuition)

- ডিসিশন বাউন্ডারি হলো `w·x + b = 0` রেখা/সমতল।
- সাপোর্ট ভেক্টরের ঠিক উপরকার মার্জিন লাইন: `w·x + b = ±1`।
- মার্জিনের প্রস্থ: $\dfrac{2}{\lVert w\rVert}$। `‖w‖` ছোট হলে মার্জিন বড় হয়।
- ভুল/কঠিন পয়েন্টগুলো মার্জিন বা ভুল পাশে গেলে hinge loss বেড়ে যায়, যেটা উদ্দেশ্যে (objective) শাস্তি যোগ করে।

---

## 7️⃣ Python উদাহরণ (Soft Margin, Linear Kernel)

নিচের উদাহরণে একটি সিন্থেটিক ডেটাসেটে `SVC(kernel='linear')` ট্রেন করে মার্জিন, সাপোর্ট ভেক্টর, আর ডিসিশন বাউন্ডারি দেখানো হয়েছে।

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.svm import SVC

# 1) Data
X, y = make_blobs(n_samples=100, centers=2, random_state=42, cluster_std=1.2)
y = np.where(y == 0, -1, 1)  # labels in {-1, +1}

# 2) Model
clf = SVC(kernel='linear', C=1.0)
clf.fit(X, y)

w = clf.coef_[0]
b = clf.intercept_[0]
margin = 2.0 / np.linalg.norm(w)
print(f"Margin width = {margin:.3f}")

# 3) Plot decision boundary & margins
xx = np.linspace(X[:,0].min()-1, X[:,0].max()+1, 200)
yy = np.linspace(X[:,1].min()-1, X[:,1].max()+1, 200)
XX, YY = np.meshgrid(xx, yy)
Z = clf.decision_function(np.c_[XX.ravel(), YY.ravel()]).reshape(XX.shape)

plt.figure(figsize=(6,5))
plt.contourf(XX, YY, Z, levels=np.linspace(Z.min(), Z.max(), 25), cmap='coolwarm', alpha=0.2)
plt.contour(XX, YY, Z, levels=[-1, 0, 1], colors=['#999', 'k', '#999'], linestyles=['--', '-', '--'])

plt.scatter(X[y==-1,0], X[y==-1,1], c='tab:blue', edgecolor='k', label='-1')
plt.scatter(X[y==1,0],  X[y==1,1],  c='tab:orange', edgecolor='k', label='+1')
plt.scatter(clf.support_vectors_[:,0], clf.support_vectors_[:,1], s=120, facecolors='none', edgecolors='k', label='support vectors')

plt.title(f"Linear SVC (C=1.0) — margin ≈ {margin:.2f}")
plt.legend(loc='best')
plt.tight_layout()
plt.show()
```

চাইলে এই কোড দিয়ে `.savefig(...)` ব্যবহার করে ছবি সেভ করা যাবে। নিচে আলাদা স্ক্রিপ্ট দেওয়া হলো।

---

## 8️⃣ এক্সাম-রেডি শর্ট নোট

- লক্ষ্য: $\min\; \tfrac{1}{2}\lVert w\rVert^2 + C\sum_i \xi_i$; শর্ত: $y_i(w\cdot x_i+b)\ge 1-\xi_i,\;\xi_i\ge0$।
- Hinge loss: $\ell_i = \max(0, 1 - y_i f(x_i))$; উদ্দেশ্য: $\tfrac{1}{2}\lVert w\rVert^2 + C\sum_i \ell_i$।
- `C` বড় → ভুল কম সহ্য, মার্জিন ছোট (overfit ঝুঁকি)। `C` ছোট → কিছু ভুল সহ্য, মার্জিন বড় (ভালো generalization)।
- মার্জিন প্রস্থ: $2/\lVert w\rVert$; সাপোর্ট ভেক্টর: `f(x)=±1` লাইনের উপর।
- Hard margin: separable হলে `\xi` ছাড়াই $\min\; \tfrac{1}{2}\lVert w\rVert^2$ ও $y_i(w\cdot x_i+b)\ge 1$।

---

## 9️⃣ (ঐচ্ছিক) গ্রাফ জেনারেটর স্ক্রিপ্ট চালাতে চাইলে

এই ফোল্ডারে `svc_cost_plot.py` স্ক্রিপ্ট রাখা আছে (নিচে তৈরি করলে)। এটি `assets/svc_soft_margin.png` ছবি সেভ করবে।

চালানোর ধাপ (Python 3.9+ ধরে):

```bash
pip install -r requirements.txt
python svc_cost_plot.py
```

আউটপুট: `assets/svc_soft_margin.png` ফাইল।

---



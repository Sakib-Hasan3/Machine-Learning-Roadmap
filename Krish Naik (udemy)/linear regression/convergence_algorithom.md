# 🔄 Convergence Algorithm (কনভার্জেন্স অ্যালগরিদম) — বাংলায় সহজ ব্যাখ্যা

---

## 📘 কনভার্জেন্স কী?

মেশিন লার্নিং-এ **কনভার্জেন্স** (Convergence) মানে হলো — যখন কোনো অ্যালগরিদম (যেমন: Gradient Descent) বারবার আপডেট হতে হতে এমন এক অবস্থায় পৌঁছায়, যেখানে Cost Function আর খুব একটা কমছে না, অর্থাৎ সমাধান স্থিতিশীল (Stable) হয়ে গেছে।

---

## 🔹 কনভার্জেন্স অ্যালগরিদমের ধাপ

1. **শুরু:** প্রাথমিক মান (Initial value) দিয়ে শুরু
2. **Cost Function হিসাব:** বর্তমান মানে Cost Function কত, তা বের করা
3. **Parameter আপডেট:** অ্যালগরিদম অনুযায়ী (যেমন: Gradient Descent) নতুন মান হিসাব
4. **Check:** Cost Function আগের চেয়ে কমেছে কিনা দেখে
5. **Repeat:** Cost Function খুব কম পরিবর্তন হলে থেমে যায় (Converged)

---

## 🧮 উদাহরণ: Gradient Descent-এ কনভার্জেন্স

- আমরা চাই Cost Function যতটা সম্ভব কমানো
- প্রতিবার প্যারামিটার (θ) আপডেট করি:

$$
\theta_{new} = \theta_{old} - \alpha \cdot \nabla J(\theta_{old})
$$

- এখানে $\alpha$ হলো Learning Rate
- $\nabla J(\theta)$ হলো Cost Function-এর Gradient

### **কনভার্জেন্স কখন হয়?**
- যখন $|J(\theta_{new}) - J(\theta_{old})| < \epsilon$ (খুব ছোট)
- অর্থাৎ Cost Function আর কমছে না

---

## 📈 কনভার্জেন্স চেনার উপায়

- **Cost Function-এর মান প্লট করলে:**
  - শুরুতে দ্রুত কমে
  - শেষে সমতল (flat) হয়ে যায়
- **Gradient (ঢাল) খুব ছোট হলে:**
  - $|\nabla J(\theta)|$ ≈ 0
- **Iteration সংখ্যা:**
  - নির্দিষ্ট সংখ্যক iteration পর থেমে যায়

---

## 🎯 কনভার্জেন্সে কী সমস্যা হতে পারে?

- **Local Minima:** Cost Function ন্যূনতম হলেও সেটি Global নাও হতে পারে
- **Overshooting:** Learning Rate বেশি হলে সমাধান লাফিয়ে যায়
- **Slow Convergence:** Learning Rate কম হলে অনেক সময় লাগে

---

## 🛠️ ব্যবহার

- **Gradient Descent**
- **Newton's Method**
- **Stochastic Gradient Descent (SGD)**
- **Optimization Algorithms**

---

## ✅ উপসংহার

- কনভার্জেন্স মানে Cost Function স্থিতিশীল হওয়া
- ভালো অ্যালগরিদম দ্রুত ও সঠিকভাবে কনভার্জ করে
- Learning Rate, Initial Value, Cost Function-এর ধরন — সবকিছু কনভার্জেন্সে প্রভাব ফেলে

---

*© 2025 - Convergence Algorithm বাংলা টিউটোরিয়াল*

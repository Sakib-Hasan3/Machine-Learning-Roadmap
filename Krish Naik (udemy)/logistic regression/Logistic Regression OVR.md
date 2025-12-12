
# 🎯 **Logistic Regression — OVR (One Vs Rest) কী?**

যখন Logistic Regression দিয়ে **multi-class classification** করতে হয় (যেমন: 3 বা তার বেশি ক্লাস), তখন সবচেয়ে জনপ্রিয় পদ্ধতি হলো **OVR**।

OVR = প্রতিটি ক্লাসের জন্য আলাদা করে Binary Logistic Regression মডেল তৈরি করা।


![Image](https://media.geeksforgeeks.org/wp-content/uploads/20230330170812/Screenshot-2023-03-30-170740.png?utm_source=chatgpt.com)

![Image](https://miro.medium.com/v2/resize%3Afit%3A788/1%2Au9Kj9xXuGXiu8RJqwCGtig.png?utm_source=chatgpt.com)

---

# 🧠 **মূল ধারণা**

যদি আমাদের কাছে 3টি ক্লাস থাকে:
**A, B, C**

তাহলে Logistic Regression দিয়ে multi-class করার উপায়:

### 👉 A class আলাদা করে:

A vs (B, C)

### 👉 B class আলাদা করে:

B vs (A, C)

### 👉 C class আলাদা করে:

C vs (A, B)

➡ মোট ৩টি logistic regression model
➡ Each model → 1 probability output দেয়
➡ Highest probability → final predicted class

---

# 🧪 **গাণিতিক ব্যাখ্যা (Math Intuition)**

প্রতিটি ক্লাসের জন্য Binary Logistic Model:

[
P(y=k|x) = \sigma(w_k^T x + b_k)
]

Prediction rule:

[
\hat{y} = \arg\max_k P(y=k|x)
]

অর্থাৎ—যে ক্লাসের probability সবচেয়ে বেশি → সেটাই prediction।

---

# 🔥 **Example (Bangla Intuition)**

একটি ফল detect করতে হবে:

ক্লাস = {Apple, Mango, Banana}

মডেল 3টি probability দিল—

* P(Apple) = 0.18
* P(Mango) = 0.72
* P(Banana) = 0.10

➡ Prediction = **Mango**

---

# 🔍 OVR vs Softmax (Multinomial Logistic)

| বিষয়        | OVR (One vs Rest)           | Softmax (Multinomial) |
| ----------- | --------------------------- | --------------------- |
| Model       | K binary models             | One model             |
| Probability | Independent                 | Sum = 1               |
| Faster?     | ✔ Fast                      | ❌ Slower              |
| Accuracy    | Good                        | Better                |
| Use Case    | High-dim sparse data (text) | Normal data           |

Softmax mathematically superior,
OVR computationally simpler।

---

# 🟩 **Python Implementation — OVR Logistic Regression**

Sklearn default ভাবে অনেক solver-এ **OVR** ব্যবহার করে।

```python
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

model = LogisticRegression(multi_class='ovr', solver='liblinear')
model.fit(X, y)

print("Prediction:", model.predict([[5.1, 3.5, 1.4, 0.2]]))
print("Class probabilities:", model.predict_proba([[5.1, 3.5, 1.4, 0.2]]))
```

---

# 🟦 **OVR এর সুবিধা**

✔ Implement করা সহজ
✔ Train করা দ্রুত
✔ Model interpret করা সহজ
✔ High-dimensional data (text classification)-এ খুব কার্যকর
✔ Debugging সহজ (কোন ক্লাসে ভুল হচ্ছে বোঝা যায়)

---

# 🟥 **OVR এর সীমাবদ্ধতা**

❌ Probabilities sum-to-one নয়
❌ Some decision boundary overlap হতে পারে
❌ Multinomial softmax-এর তুলনায় কখনো accuracy কম হতে পারে
❌ K models = computational cost grows linearly

---

# 🧠 **Short Notes (Exam-friendly)**

* OVR = Each class vs All Others
* K classes → K binary logistic regression models
* Prediction = class with highest probability
* Faster than softmax but less mathematically elegant
* Useful in high-dimensional sparse data (NLP/text classification)

---





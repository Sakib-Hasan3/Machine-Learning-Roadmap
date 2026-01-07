# Random Forest Regression

🌳 Random Forest Regression কী?

---

![Image](https://cdn.prod.website-files.com/5e6f9b297ef3941db2593ba1/5f6315207ab68b113cf57b1c_Screenshot%202020-09-17%20at%2009.49.20.png)

![Image](https://www.researchgate.net/publication/303835073/figure/fig3/AS%3A377949833449472%401467121670301/The-flowchart-of-random-forest-RF-for-regression-adapted-from-Rodriguez-Galiano-et.png)

[Image](https://miro.medium.com/v2/resize%3Afit%3A1400/0%2AYEwFetXQGPB8aDFV)

**Random Forest Regression** হলো একটি **Ensemble Learning** পদ্ধতি, যেখানে

👉 অনেকগুলো **Decision Tree (Regression Tree)** একসাথে train করা হয়

👉 এবং সবগুলোর prediction-এর **average** নিয়ে final output দেওয়া হয়।

👉 এটি মূলত **Bagging (Bootstrap Aggregating)** এর উপর ভিত্তি করে তৈরি।

---

## 🧠 সহজ ভাষায় ধারণা

একটা tree ভুল করতে পারে ❌

কিন্তু 100টা tree একসাথে গড় করলে ভুল অনেক কমে যায় ✅

📌 **Final Prediction = সব tree এর prediction-এর গড় (mean)**

---

## ⚙️ Random Forest Regression কীভাবে কাজ করে?

### ধাপ–১: Bootstrap Sampling

- Original dataset থেকে **random sampling (with replacement)** করা হয়
- প্রতিটি tree আলাদা dataset পায়

### ধাপ–২: Multiple Decision Tree Train

- প্রতিটি dataset দিয়ে একটি করে **Regression Tree** train হয়
- প্রতিটি split এ **random subset of features** নেওয়া হয়

### ধাপ–৩: Prediction

- নতুন input দিলে →
- সব tree prediction দেয় →
- **Average = Final Output**

---

## 📐 Mathematical Intuition (সহজ)

ধরা যাক 5টা tree prediction দিলো:

```
Tree 1 → 52
Tree 2 → 55
Tree 3 → 50
Tree 4 → 53
Tree 5 → 54

```

👉 Final Prediction:

[

\frac{52 + 55 + 50 + 53 + 54}{5} = 52.8

]

---

## 🎯 Random Forest Regression কেন ব্যবহার করা হয়?

✔ Overfitting কমাতে

✔ High variance problem solve করতে

✔ Non-linear relationship ধরতে

✔ Feature scaling ছাড়াই কাজ করতে

---

## 🌟 Key Hyperparameters (খুব গুরুত্বপূর্ণ)

| Parameter | কাজ |
| --- | --- |
| `n_estimators` | কতগুলো tree হবে |
| `max_depth` | tree কতটা গভীর হবে |
| `min_samples_split` | split করার minimum sample |
| `min_samples_leaf` | leaf node এ minimum sample |
| `max_features` | প্রতিটি split এ কত feature নেওয়া হবে |

📌 **Tip:**

- `n_estimators ↑` → stability ↑
- `max_depth ↓` → overfitting ↓

---

## ✅ Random Forest Regression এর সুবিধা

✔ Overfitting কম

✔ High accuracy

✔ Outlier & noise robust

✔ Feature importance পাওয়া যায়

✔ Scaling দরকার হয় না

---

## ❌ অসুবিধা

❌ Model heavy (memory বেশি লাগে)

❌ Training slow (tree বেশি হলে)

❌ Explain করা single tree থেকে কঠিন

---

## 📊 Random Forest vs Linear Regression

| বিষয় | Linear Regression | Random Forest |
| --- | --- | --- |
| Relationship | Linear | Non-linear |
| Overfitting | Sensitive | Robust |
| Feature scaling | দরকার | দরকার নেই |
| Accuracy | Low–Medium | High |
| Interpretability | High | Medium |

---

## 🧪 কোথায় বেশি ব্যবহার হয়?

- House price prediction 🏠
- Sales forecasting 📈
- Weather prediction 🌦
- Medical cost estimation 🏥
- Stock-related regression (features-based) 📊

---

## 🧠 মনে রাখার কৌশল

👉 **Random Forest Regression =অনেক Decision Tree + Average = Stable Prediction**

---
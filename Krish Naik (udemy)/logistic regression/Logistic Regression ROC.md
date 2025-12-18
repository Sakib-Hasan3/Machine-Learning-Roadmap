# 📈 Logistic Regression – ROC Curve (বাংলায় সম্পূর্ণ ব্যাখ্যা)

![Image](https://www.researchgate.net/publication/317319166/figure/download/fig3/AS%3A513460494897152%401499429929073/The-ROC-curve-of-the-multivariate-logistic-regression-model-The-ROC-curve-illustrated.png?utm_source=chatgpt.com)

![Image](https://web.stanford.edu/class/sbio228/public/lectures/lec6/Lecture6/Data_Visualization/images/Roc_Curve_Examples.jpg?utm_source=chatgpt.com)

![Image](https://www.researchgate.net/profile/Nawal-Zaher/publication/317078706/figure/fig2/AS%3A662827173945346%401535041721394/ROC-curve-showing-TPR-against-FPR-for-different-decision-thresholds.png?utm_source=chatgpt.com)

![Image](https://www.researchgate.net/profile/Ali-Hamzeh-5/publication/225824136/figure/fig9/AS%3A668556215713803%401536407631415/ROC-Curve-for-TPR-vs-FPR.jpg?utm_source=chatgpt.com)

## 1️⃣ ROC Curve কী?

**ROC (Receiver Operating Characteristic) Curve** হলো একটি গ্রাফ
যা **Binary Classification Model** (যেমন Logistic Regression) কতটা ভালো কাজ করছে তা দেখায়।

👉 এটি **Threshold পরিবর্তনের সাথে সাথে Model-এর পারফরম্যান্স** দেখায়।

---

## 2️⃣ ROC Curve-এর Axis কী বোঝায়?

### 🔹 X-axis → FPR (False Positive Rate)

[
	ext{FPR} = \frac{FP}{FP + TN}
]

### 🔹 Y-axis → TPR (True Positive Rate) / Recall

[
	ext{TPR} = \frac{TP}{TP + FN}
]

---

## 3️⃣ Logistic Regression এ ROC কেন দরকার?

Logistic Regression:

* সরাসরি **0/1** দেয় না
* দেয় **Probability (0–1)**

➡️ Threshold (0.5, 0.4, 0.3 …) বদলালে:

* Recall বাড়ে / কমে
* False Positive বাড়ে / কমে

👉 ROC Curve সব Threshold একসাথে দেখায়

---

## 4️⃣ Threshold পরিবর্তনে কী হয়?

| Threshold    | Result               |
| ------------ | -------------------- |
| High (0.7)   | FP কম, FN বেশি       |
| Medium (0.5) | Balanced             |
| Low (0.3)    | Recall বেশি, FP বেশি |

➡️ ROC Curve এই Trade-off দেখায়

---

## 5️⃣ AUC (Area Under Curve) কী?

**AUC = ROC Curve-এর নিচের এলাকা**

| AUC Value | Meaning       |
| --------- | ------------- |
| 1.0       | Perfect Model |
| 0.9+      | Excellent     |
| 0.8–0.9   | Good          |
| 0.7–0.8   | Average       |
| 0.5       | Random Guess  |

➡️ AUC যত বেশি, Logistic Regression তত ভালো

---

## 6️⃣ Imbalanced Dataset এ ROC কেন গুরুত্বপূর্ণ?

❌ Accuracy misleading
✅ ROC-AUC threshold independent

👉 Imbalanced Dataset এ:

* Class distribution বদলালেও
* ROC-AUC স্থির থাকে

➡️ তাই **Logistic Regression + Imbalanced Data = ROC-AUC Best Metric**

---

## 7️⃣ Logistic Regression এ ROC Curve আঁকার ধাপ

### Step 1: Probability বের করা

```python
y_prob = model.predict_proba(X_test)[:,1]
```

### Step 2: ROC Calculation

```python
from sklearn.metrics import roc_curve, auc

fpr, tpr, thresholds = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)
```

### Step 3: Plot

```python
import matplotlib.pyplot as plt

plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
plt.plot([0,1],[0,1],'--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.legend()
plt.show()
```

---

## 8️⃣ ROC Curve কেমন হলে ভালো?

✅ Curve যদি:

* **Top-left corner-এর দিকে যায়**
* Diagonal line-এর উপরে থাকে

❌ খারাপ Model:

* Diagonal line-এর কাছাকাছি

---

## 9️⃣ ROC vs Precision-Recall Curve

| ROC Curve             | PR Curve                 |
| --------------------- | ------------------------ |
| Balanced Dataset ভালো | Highly Imbalanced-এ ভালো |
| FPR ব্যবহার করে       | Precision ব্যবহার করে    |
| General purpose       | Minority focus           |

👉 Fraud / Medical case এ PR Curve বেশি উপযোগী

---

## 🔟 Logistic Regression + ROC Interview Points ⭐

* ROC threshold independent
* AUC probability ranking মাপে
* Imbalanced Dataset এ ROC-AUC preferred
* Accuracy misleading
* ROC diagonal = random classifier

---

## 1️⃣1️⃣ সহজ ভাষায় Summary

> Logistic Regression ROC Curve হলো এমন একটি গ্রাফ যা বিভিন্ন Threshold-এ Model-এর Recall এবং False Positive Rate দেখায়। AUC যত বেশি, Model তত ভালো। Imbalanced Dataset-এর ক্ষেত্রে ROC-AUC Accuracy-এর চেয়ে অনেক বেশি নির্ভরযোগ্য।

---


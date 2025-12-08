

---

# 🔍 **Performance Metrics কী?**

Performance Metrics হলো এমন সব পরিমাপক মান, যা দিয়ে আমরা Machine Learning মডেলের **কোনটা ভালো, কোনটা খারাপ**—তা পরিমাপ করি।

* Classification → Accuracy, Precision, Recall, F1, ROC-AUC
* Regression → MSE, RMSE, MAE, R² Score
* Imbalanced data → Precision-Recall, F1, AUC-PR

---

![Image](https://2.bp.blogspot.com/-EvSXDotTOwc/XMfeOGZ-CVI/AAAAAAAAEiE/oePFfvhfOQM11dgRn9FkPxlegCXbgOF4QCLcBGAs/s1600/confusionMatrxiUpdated.jpg?utm_source=chatgpt.com)

![Image](https://ashutoshtripathicom.files.wordpress.com/2022/01/precision-recall-vs-roc-auc.png?w=840&utm_source=chatgpt.com)

---

# 🟦 **A. Classification Metrics (Binary + Multi-Class)**

## 1️⃣ **Confusion Matrix** (মূল ভিত্তি)

```
								Predicted
							| 1      | 0
Actual   1    | TP     | FN
				 0    | FP     | TN
```

* **TP** = True Positive
* **TN** = True Negative
* **FP** = False Positive
* **FN** = False Negative

---

## 2️⃣ **Accuracy**

[
Accuracy = \frac{TP + TN}{TP + TN + FP + FN}
]

কবে ব্যবহার করবেন → যখন dataset **balanced** থাকে।

Limit → imbalanced dataset-এ ভুল ব্যাখ্যা দেয়।

---

## 3️⃣ **Precision**

[
Precision = \frac{TP}{TP + FP}
]

"Predicted positives এর মধ্যে কতগুলো সত্যি?"

উদাহরণ: Spam detection → spam বললে সত্যিই spam কিনা?

---

## 4️⃣ **Recall (Sensitivity / TPR)**

[
Recall = \frac{TP}{TP + FN}
]

"Actual positives কতটুকু detect করতে পারছে?"

উদাহরণ: Disease detection → অসুস্থ রোগী বাদ পড়লে বড় সমস্যা।

---

## 5️⃣ **F1-Score (Harmonic Mean)**

[
F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}
]

Precision ও Recall-এর balanced score → imbalanced dataset-এ অত্যন্ত গুরুত্বপূর্ণ।

---

## 6️⃣ **Specificity (TNR)**

[
Specificity = \frac{TN}{TN + FP}
]

True negative portion।

---

## 7️⃣ **ROC Curve এবং AUC**

* ROC → TPR vs FPR curve
* AUC → Area Under Curve = Model-এর শক্তি

[
AUC = 0.5 \Rightarrow Random
AUC = 1.0 \Rightarrow Perfect model
]

Balanced dataset-এ খুব গুরুত্বপূর্ণ।

---

## 8️⃣ **Precision-Recall Curve (AUC-PR)**

Imbalanced dataset-এ ROC curve বিভ্রান্ত করে, PR curve বেশি informative।

---

## 9️⃣ **Log Loss (Cross Entropy Loss)**

[
Loss = -[y\log(p) + (1-y)\log(1-p)]
]

Probabilistic classifier (logistic, softmax)-এর official scoring metric।

---

---

# 🟩 **B. Multi-Class Classification Metrics**

## 1️⃣ **Macro / Micro / Weighted Averages**

* **Macro F1** → সব ক্লাসকে সমান ওজন
* **Micro F1** → overall TP/FP/FN
* **Weighted F1** → ক্লাস সাইজ অনুযায়ী ওজন

---

## 2️⃣ **Top-K Accuracy**

উদাহরণ: Image classification (ImageNet)

Model top-k prediction-এর মধ্যে সঠিক ক্লাস থাকলে সফল।

---

---

# 🟥 **C. Regression Metrics**

![Image](https://www.researchgate.net/publication/362260849/figure/tbl1/AS%3A1184487119552531%401659415144265/Values-of-MSE-RMSE-MAE-MAPE-and-R-2-for-the-eight-models.png?utm_source=chatgpt.com)

![Image](https://miro.medium.com/v2/resize%3Afit%3A1358/1%2A5fnmYVHLTC8mGxybHm4XkA.png?utm_source=chatgpt.com)

## 1️⃣ **MSE (Mean Squared Error)**

[
MSE = \frac{1}{n}\sum (y - \hat{y})^2
]

Errors → square → large error বেশি penalize করা হয়।

---

## 2️⃣ **RMSE (Root Mean Squared Error)**

[
RMSE = \sqrt{MSE}
]

Interpretation সহজ (same unit as target variable)।

---

## 3️⃣ **MAE (Mean Absolute Error)**

[
MAE = \frac{1}{n}\sum |y - \hat{y}|
]

Outlier-এ stable (better than MSE)।

---

## 4️⃣ **R² Score (Coefficient of Determination)**

[
R^2 = 1 - \frac{SS_{res}}{SS_{tot}}
]

* R² = 1 → perfect
* R² = 0 → খুব খারাপ
* R² negative হতে পারে → model total ব্যর্থ

---

## 5️⃣ **Adjusted R²**

Multiple features থাকলে বেশি informative।
Penalty দেয় — useless features যোগ করলেই score না বাড়ে।

---

---

# 🟧 **D. Clustering Metrics (Unsupervised)**

## 1️⃣ **Silhouette Score**

[
(-1 \text{ to } 1)
]

Higher → clusters far & clean।

## 2️⃣ **Davies–Bouldin Index**

Lower → better clustering।

## 3️⃣ **Calinski–Harabasz Index**

Higher → better separation।

---

---

# 🟦 কখন কোন মেট্রিক ব্যবহার করবেন?

| Problem Type                   | Best Metrics                  |
| ------------------------------ | ----------------------------- |
| Balanced Binary Classification | Accuracy, ROC-AUC             |
| Imbalanced Classification      | F1, Precision, Recall, AUC-PR |
| Medical diagnosis              | Recall, F1                    |
| Fraud detection                | Precision, Recall, AUC-PR     |
| Regression                     | RMSE, MAE, R²                 |
| Clustering                     | Silhouette, DBI               |

---


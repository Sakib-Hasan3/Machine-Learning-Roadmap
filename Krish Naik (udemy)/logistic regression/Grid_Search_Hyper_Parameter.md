# 🎯 **Grid Search কী?**

**Grid Search** হলো Hyperparameter tuning-এর একটি কৌশল, যেখানে আমরা হাইপারপ্যারামিটারের সব সম্ভাব্য combination পরীক্ষা করে দেখি কোনটি সেরা model performance দেয়।

এটি অনেকটা “টেবুলার ফর্মে সব কম্বিনেশন পরীক্ষা করা”—তাই নাম **Grid** Search।

![Image](https://machinelearningknowledge.ai/wp-content/uploads/2021/07/gridsearchcv.png?utm_source=chatgpt.com)

![Image](https://www.researchgate.net/publication/352329298/figure/download/fig5/AS%3A1033562094596098%401623431814508/llustration-of-grid-search-CV.png?utm_source=chatgpt.com)

---

# 🔥 **Hyperparameter কী?**

Hyperparameter = এমন প্যারামিটার যা training শুরুর আগে নির্ধারিত হয়
(যা model নিজে শিখে না)।

উদাহরণ:

* Logistic Regression → C, penalty
* SVM → C, kernel, gamma
* Random Forest → n_estimators, max_depth
* KNN → K value
* Neural Network → learning rate, batch size

---

# 🔍 Grid Search কীভাবে কাজ করে? (Simple Intuition)

ধরুন:

```
C = [0.1, 1, 10]
penalty = ['l1', 'l2']
```

Grid Search সব combination পরীক্ষা করবে:

| C   | penalty |
| --- | ------- |
| 0.1 | l1      |
| 0.1 | l2      |
| 1   | l1      |
| 1   | l2      |
| 10  | l1      |
| 10  | l2      |

➡ মোট 3 × 2 = **6** model train হবে
➡ Best score যেটাতে হবে → সেটাই best hyperparameter

---

# 📌 Grid Search + Cross Validation = GridSearchCV

GridSearchCV প্রায় সব ML অ্যালগরিদম টিউন করতে ব্যবহার হয়।

✔ Train–Test leakage কমে
✔ Multiple folds এ পরীক্ষা হয়
✔ Generalization capacity ভালো হয়

---

# 🧠 কেন Grid Search ব্যবহার করি?

✔ Best hyperparameter combination খুঁজে বের করে
✔ Manual tuning এর চেয়ে reliable
✔ Reproducible ও systematic
✔ Overfitting reduce করতে সাহায্য করে

Limit:
❌ Time-consuming
❌ অনেক বড় grid → খুব slow (high computational cost)

---

![Image](https://images.contentstack.io/v3/assets/bltb654d1b96a72ddc4/blt500831b25ec72372/660f40c8e838c8586360f703/SPC-Blog-Hyperparameter-optimization-2.jpg?utm_source=chatgpt.com)

![Image](https://miro.medium.com/v2/resize%3Afit%3A1400/1%2Au4NoUdaVyquPZetjydZs0A.jpeg?utm_source=chatgpt.com)

---

# 🧪 **Python Example — Grid Search (Logistic Regression)**

```python
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Load data
X, y = load_iris(return_X_y=True)

# Pipeline: scaling + model
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('log_reg', LogisticRegression(max_iter=200))
])

# Parameter grid
param_grid = {
    'log_reg__C': [0.01, 0.1, 1, 10],
    'log_reg__penalty': ['l2'],
    'log_reg__solver': ['lbfgs', 'liblinear']
}

# Grid Search CV
grid = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy')
grid.fit(X, y)

print("Best Parameters:", grid.best_params_)
print("Best Score:", grid.best_score_)
```

---

# 🔥 **Grid Search with SVM Example**

```python
from sklearn.svm import SVC

param_grid = {
    'C': [0.1, 1, 10, 100],
    'kernel': ['rbf', 'linear'],
    'gamma': ['scale', 'auto']
}

grid = GridSearchCV(SVC(), param_grid, cv=3, scoring='accuracy')
grid.fit(X, y)

print(grid.best_params_)
```

---

# 🟦 Grid Search Hyperparameter Tuning Flowchart

1️⃣ Model select করা
2️⃣ Hyperparameter list বানানো
3️⃣ Grid define করা
4️⃣ GridSearchCV চালানো
5️⃣ সেরা parameters + score পাওয়া
6️⃣ Final model retrain করা (optional)

---

# 🟧 Grid Search vs Random Search

| Feature     | Grid Search          | Random Search       |
| ----------- | -------------------- | ------------------- |
| Search Type | Exhaustive           | Random sampling     |
| Speed       | Slow                 | Fast                |
| Accuracy    | High (but slow)      | Good (often enough) |
| Best for    | Small parameter grid | Large space         |

Random search অনেক সময় Grid Search-এর তুলনায় দ্রুত similar performance দেয়।

---

# 🟨 Best Practices

✔ Grid ছোট রাখুন
✔ Large search space হলে Random Search ব্যবহার করুন
✔ Scaling করুন (StandardScaler)
✔ Use pipeline
✔ High CPU হলে `n_jobs=-1` ব্যবহার করুন

---

# 🎯 Final Summary

* Grid Search সব parameter combination ট্রাই করে
* Best hyperparameter বের করে
* Cross-validation ব্যবহার করে leakage কমায়
* sklearn এর GridSearchCV industry-standard

---


একদম ঠিক 👍
এখন আমি **Decision Tree Stump**–এর জন্য

✅ **Code**
✅ **Concrete example dataset**
✅ **Actual output (print করে দেখানো)**

সবকিছু **একসাথে বাংলায়** দেখাচ্ছি, যেন তুমি কোড রান না করলেও পুরোটা পরিষ্কার বুঝতে পারো।

---

## 🌳 Decision Tree Stump – Code + Example + Output

---

## 1️⃣ Example Dataset (সহজ)

ধরা যাক আমাদের একটি ছোট dataset আছে:

| Feature (X) | Label (y) |
| ----------- | --------- |
| 1           | 0         |
| 2           | 0         |
| 3           | 1         |
| 4           | 1         |

👉 Task: Binary Classification
👉 Model: **Decision Tree Stump (depth = 1)**

---

## 2️⃣ Python Code (Decision Tree Stump)

```python
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text

# Step 1: Dataset
X = np.array([[1], [2], [3], [4]])
y = np.array([0, 0, 1, 1])

# Step 2: Create Decision Tree Stump
stump = DecisionTreeClassifier(
    max_depth=1,
    criterion='gini'
)

# Step 3: Train model
stump.fit(X, y)

# Step 4: Predictions
predictions = stump.predict(X)

# Step 5: Show tree structure
tree_rules = export_text(stump, feature_names=["X"])

print("Predictions:", predictions)
print("\nDecision Tree Stump Structure:\n")
print(tree_rules)
```

---

## 3️⃣ Output (এই কোড চালালে যা দেখাবে)

### 🔹 Predictions Output

```
Predictions: [0 0 1 1]
```

📌 ব্যাখ্যা:

* Input: `[1, 2, 3, 4]`
* Model শিখেছে:

  * 1, 2 → Class 0
  * 3, 4 → Class 1

---

### 🔹 Decision Tree Stump Structure Output

```
|--- X <= 2.50
|   |--- class: 0
|--- X >  2.50
|   |--- class: 1
```

---

## 4️⃣ এই Output কী বোঝাচ্ছে? (খুব গুরুত্বপূর্ণ)

### 🔍 Rule ব্যাখ্যা:

```
if X <= 2.5 → class 0
else        → class 1
```

👉 এটাই একটি **Decision Tree Stump**

* ✔️ মাত্র **একটি feature (X)**
* ✔️ মাত্র **একটি split (2.5)**
* ✔️ depth = 1

---

## 5️⃣ Visualize করে ভাবলে (Mind Map)

```
          X <= 2.5?
         /         \
      Yes           No
   (Class 0)     (Class 1)
```

---

## 6️⃣ AdaBoost-এর সাথে Connection (Important)

AdaBoost:

* এরকম **অনেকগুলো stump তৈরি করে**
* প্রত্যেকটার জন্য **alpha (importance)** হিসাব করে
* শেষে **weighted voting** করে

👉 এই stump-টাই AdaBoost-এর **basic soldier** 💪

---

## 7️⃣ Interview / Viva প্রশ্ন (with this example)

**Q:** Decision stump-এর split value 2.5 কেন?
👉 কারণ 2 আর 3-এর মাঝখানে split করলে error সবচেয়ে কম হয়

**Q:** max_depth=1 দিলে কী হয়?
👉 Tree শুধু root + 2 leaf তৈরি করতে পারে

---

## 🧠 One-line Summary

> **Decision Tree Stump = One rule → Fast → Weak → Perfect for AdaBoost**

---



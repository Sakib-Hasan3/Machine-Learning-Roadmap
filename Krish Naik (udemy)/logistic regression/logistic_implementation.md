---

# 🧠 Part 1 — Logistic Regression Implementation (Pure Math + Intuition)

Logistic Regression মূলত ৩টি ধাপ অনুসরণ করে:

---

## **1️⃣ Hypothesis / Model Function**

[
h_\theta(x) = \sigma(z) = \frac{1}{1 + e^{-z}}
]

যেখানে
[
z = \theta^T x
]

Sigmoid output → probability of class = 1.

---

## **2️⃣ Cost Function (Binary Cross Entropy)**

[
J(\theta) = -\frac{1}{m}\sum_{i=1}^m
\Big[ y^{(i)}\log(h_\theta(x^{(i)})) +
(1-y^{(i)})\log(1-h_\theta(x^{(i)})) \Big]
]

---

## **3️⃣ Gradient Descent to learn parameters**

[
\theta_j := \theta_j - \alpha \frac{\partial J}{\partial \theta_j}
]

Derivative:

[
\frac{\partial J}{\partial \theta_j} = \frac{1}{m}\sum(h_\theta(x)-y)x_j
]

এটিই weight update rule।

---

---

# 🟦 Part 2 — Logistic Regression (Manual Implementation using NumPy)

নিচের কোড logistic regression-এর internal math — sigmoid, cost, gradient descent — পুরোপুরি স্ক্র্যাচ থেকে দেখায়।

```python
import numpy as np

# Sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Cost function
def compute_cost(X, y, theta):
    m = len(y)
    h = sigmoid(X.dot(theta))
    cost = -(1/m) * np.sum(y*np.log(h) + (1-y)*np.log(1-h))
    return cost

# Gradient descent
def gradient_descent(X, y, theta, alpha, iterations):
    m = len(y)
    cost_history = []

    for i in range(iterations):
        h = sigmoid(X.dot(theta))
        gradient = (1/m) * X.T.dot(h - y)
        theta -= alpha * gradient
        cost_history.append(compute_cost(X, y, theta))

    return theta, cost_history

# Example dataset
X = np.array([[1, 2],
              [1, 3],
              [2, 4],
              [3, 5]])

y = np.array([0, 0, 1, 1])

# Add intercept term
X = np.c_[(np.ones(X.shape[0])), X]

theta = np.zeros(X.shape[1])

alpha = 0.1
iterations = 1000

theta, cost_history = gradient_descent(X, y, theta, alpha, iterations)

print("Learned parameters:", theta)
print("Final cost:", cost_history[-1])
```

✔ এটি pure Logistic Regression implementation
✔ sklearn ছাড়াই সব কিছু নিজে করা হয়েছে
✔ gradient descent কীভাবে কাজ করে তা clear দেখা যায়

---

---

# 🟩 Part 3 — Logistic Regression Implementation using **sklearn**

এটি বাস্তবে সবচেয়ে বেশি ব্যবহৃত।

```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Example data
X = [[2.3, 1], [1.1, 0], [3.3, 1], [0.6, 0], [4.1, 1]]
y = [1, 0, 1, 0, 1]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
```

---

---

# 🟧 Part 4 — Logistic Regression Decision Boundary (Visualization)

```python
import matplotlib.pyplot as plt
import numpy as np

# Sample data
X1 = np.array([1, 2, 3, 4, 5])
X2 = np.array([2, 1, 4, 3, 5])
y = np.array([0, 0, 1, 1, 1])

# Plotting
plt.scatter(X1, X2, c=y)
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Data Points")

# Example boundary: w1*x1 + w2*x2 + b = 0
w1, w2, b = 1, -1, 0
x_vals = np.linspace(0, 6, 100)
y_vals = (-w1*x_vals - b) / w2
plt.plot(x_vals, y_vals)

plt.show()
```

---

---

# 🟨 Part 5 — Logistic Regression Implementation Flow

১) Data collection
২) Data preprocessing (missing, scaling optional)
৩) Add intercept term
৪) Sigmoid hypothesis
৫) Cost function
৬) Gradient computation
৭) Weight update
৮) Prediction = 1 if P ≥ 0.5
৯) Evaluate model (accuracy, precision, recall, F1)
১০) Visualization (optional)

---

---

# 🧠 Part 6 — Real-Life Example (Bangla)

একজন ছাত্রের Study_hours এবং Attendance দেখে সে পাস করবে কিনা তা predict করতে চাই।

Model বলল:

[
P(\text{Pass}|x)=0.78
]

→ যেহেতু 0.78 ≥ 0.5 → **Prediction = Pass**

Logistic Regression probabilities দিয়ে decision নেয়।

---

---


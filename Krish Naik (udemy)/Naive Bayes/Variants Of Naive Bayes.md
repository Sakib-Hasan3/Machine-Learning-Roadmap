# নাইভ বেইজ (Naive Bayes): ভ্যারিয়েন্ট, ফর্মুলা, উদাহরণ ও কোড

নাইভ বেইজ একটি জনপ্রিয় probabilistic classification algorithm যা Bayes’ Theorem-এর উপর ভিত্তি করে কাজ করে এবং ধরে নেয় যে সব feature একে–অপরের থেকে স্বাধীন (independent)। এটি দ্রুত, লাইটওয়েট এবং টেক্সটসহ নানা ধরনের ডেটায় ভালো ফল দেয়।

---

## 🔹 1. Gaussian Naive Bayes

👉 Continuous / সংখ্যাসূচক ডেটার জন্য

### কখন ব্যবহার করা হয়?

* যখন feature-এর মান real number হয় (উচ্চতা, ওজন, মার্কস, তাপমাত্রা ইত্যাদি)

### কীভাবে কাজ করে?

* ধরে নেয় যে প্রতিটি feature Gaussian (Normal) Distribution অনুসরণ করে

### উদাহরণ:

* একজন ছাত্র পাস করবে নাকি ফেল করবে → ইনপুট: মার্কস, উপস্থিতি

### সুবিধা:

✔ সহজ  
✔ ছোট ডেটাসেটে ভালো কাজ করে

---

## 🔹 2. Multinomial Naive Bayes

👉 Count-based / Text Data-এর জন্য

### কখন ব্যবহার করা হয়?

* যখন feature হলো frequency বা count  
* সাধারণত NLP / Text Classification-এ

### কীভাবে কাজ করে?

* শব্দ কয়বার এসেছে সেটার উপর ভিত্তি করে probability হিসাব করে

### উদাহরণ:

* Email → Spam নাকি Not Spam  
* ডকুমেন্ট → Sports / Politics / Tech

### সুবিধা:

✔ Text classification-এ খুব কার্যকর  
✔ Bag of Words, TF-IDF-এর সাথে ভালো কাজ করে

---

## 🔹 3. Bernoulli Naive Bayes

👉 Binary (0/1) ডেটার জন্য

### কখন ব্যবহার করা হয়?

* Feature শুধু হ্যাঁ/না বা 0/1

### কীভাবে কাজ করে?

* কোনো feature আছে কিনা সেটাই গুরুত্বপূর্ণ, কতবার আছে তা না

### উদাহরণ:

* শব্দ আছে (1) / নেই (0)  
* User ক্লিক করেছে (1) / করেনি (0)

### Multinomial vs Bernoulli:

| বিষয়          | Multinomial     | Bernoulli    |
| ------------- | --------------- | ------------ |
| Feature টাইপ  | Count           | Binary       |
| শব্দের সংখ্যা | গুরুত্বপূর্ণ    | না           |
| শব্দ আছে কিনা | কম গুরুত্বপূর্ণ | গুরুত্বপূর্ণ |

---

## 🔹 4. Complement Naive Bayes

👉 Imbalanced Dataset-এর জন্য উন্নত ভার্সন

### কেন দরকার?

* Multinomial Naive Bayes imbalanced data-তে ভালো কাজ করে না

### কীভাবে কাজ করে?

* নিজের ক্লাস বাদ দিয়ে বাকি ক্লাসগুলোর তথ্য ব্যবহার করে probability হিসাব করে (complement statistics)

### ব্যবহার:

* News classification  
* Sentiment analysis (positive/negative imbalance)

---

## 🔹 5. Categorical Naive Bayes

👉 Categorical Feature-এর জন্য

### কখন ব্যবহার করা হয়?

* Feature যদি সরাসরি category হয় (যেমন: Gender, Color, Department)

### উদাহরণ:

* Gender = Male / Female  
* Browser = Chrome / Firefox / Edge

### সুবিধা:

✔ Encoding ছাড়াও কাজ করতে পারে  
✔ Discrete categorical data-তে ভালো

---

## 🧮 গাণিতিক ফর্মুলা (Bayes + Naive অনুমান)

Bayes’ Theorem:

$$
P(C \mid \mathbf{x}) = \frac{P(\mathbf{x} \mid C)\,P(C)}{P(\mathbf{x})}
$$

Naive Independence Assumption:

$$
P(\mathbf{x} \mid C) = \prod_{i=1}^{d} P(x_i \mid C)
$$

Decision Rule (denominator স্থির ধরে):

$$
\hat{C} = \arg\max_C\; P(\mathbf{x}\mid C)\,P(C)
$$

Gaussian likelihood (feature \(x_i\) normal ধরা):

$$
P(x_i \mid C) = \frac{1}{\sqrt{2\pi\,\sigma^2_{C,i}}}\,\exp\Big( -\frac{(x_i - \mu_{C,i})^2}{2\,\sigma^2_{C,i}} \Big)
$$

Multinomial likelihood (+ Laplace smoothing):

$$
P(\mathbf{x}\mid C) \propto \prod_{i=1}^d \theta_{i\mid C}^{\;x_i},\quad
	heta_{i\mid C} = \frac{N_{i\mid C}+\alpha}{\sum_{j}N_{j\mid C}+\alpha d}
$$

Bernoulli likelihood:

$$
P(\mathbf{x}\mid C) = \prod_{i=1}^d \theta_{i\mid C}^{\;x_i}\,(1-\theta_{i\mid C})^{\;1-x_i}
$$

Complement NB: \(\theta\) অনুমান করা হয় class complement থেকে, যাতে rare/imbalanced শব্দের প্রভাব সুষম থাকে।

---

## 📘 Worked Example (Multinomial NB, ছোট টেক্সট)

ধরা যাক দুইটি ক্লাস: Spam (S) এবং Ham (H)। Vocabulary: [offer, win].

Training counts (Laplace smoothing \(\alpha=1\)):

* S: offer=8, win=6, total words=20  
* H: offer=2, win=1, total words=15

Probability estimates:

$$
	heta_{offer\mid S} = \frac{8+1}{20+1\cdot 2} = \frac{9}{22},\quad
	heta_{win\mid S} = \frac{6+1}{22} = \frac{7}{22}
$$

$$
	heta_{offer\mid H} = \frac{2+1}{15+2} = \frac{3}{17},\quad
	heta_{win\mid H} = \frac{1+1}{17} = \frac{2}{17}
$$

Prior (উদাহরণস্বরূপ): \(P(S)=P(H)=0.5\).

নতুন ইমেইল: "offer win win" ⇒ counts: offer=1, win=2.

Log-score (numerator):

$$
\log P(\mathbf{x}\mid S) + \log P(S) = \log\Big((9/22)^1\,(7/22)^2\Big) + \log 0.5
$$

$$
\log P(\mathbf{x}\mid H) + \log P(H) = \log\Big((3/17)^1\,(2/17)^2\Big) + \log 0.5
$$

এখানে Spam-এর স্কোর বেশি ⇒ শ্রেণীকরণ ফল: Spam.

---

## 🐍 Python (scikit-learn) কোড উদাহরণ

নিচের উদাহরণগুলো দ্রুত ট্রাই করার জন্য তৈরি। Python 3.x এবং scikit-learn ইন্সটল থাকা দরকার।

### 1) GaussianNB (সংখ্যাসূচক)

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = GaussianNB()
clf.fit(X_train, y_train)
pred = clf.predict(X_test)
print("GaussianNB accuracy:", accuracy_score(y_test, pred))
```

### 2) MultinomialNB (টেক্সট/কাউন্ট)

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

texts = [
	"win a lottery now",
	"limited time offer",
	"meeting notes project",
	"family dinner plan",
	"special win offer today",
	"project update meeting"
]
labels = [1, 1, 0, 0, 1, 0]  # 1=Spam, 0=Ham

vec = CountVectorizer()
X = vec.fit_transform(texts)
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.33, random_state=7)

clf = MultinomialNB(alpha=1.0)
clf.fit(X_train, y_train)
pred = clf.predict(X_test)
print("MultinomialNB accuracy:", accuracy_score(y_test, pred))
```

### 3) BernoulliNB (বাইনারি উপস্থিতি)

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score

texts = [
	"win a lottery now",
	"limited time offer",
	"meeting notes project",
	"family dinner plan",
	"special win offer today",
	"project update meeting"
]
labels = [1, 1, 0, 0, 1, 0]

vec = CountVectorizer(binary=True)
X = vec.fit_transform(texts)
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.33, random_state=7)

clf = BernoulliNB(alpha=1.0)
clf.fit(X_train, y_train)
pred = clf.predict(X_test)
print("BernoulliNB accuracy:", accuracy_score(y_test, pred))
```

### 4) ComplementNB (ইম্ব্যালেন্স টেক্সট)

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import ComplementNB
from sklearn.metrics import accuracy_score

texts = [
	"rare category news about quantum",
	"common sports update football",
	"rare physics breakthrough",
	"sports match highlights",
	"quantum computing advances",
	"football transfer rumour"
]
labels = [1, 0, 1, 0, 1, 0]  # 1=Rare (e.g., science), 0=Common (sports)

vec = CountVectorizer()
X = vec.fit_transform(texts)
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.33, random_state=42)

clf = ComplementNB(alpha=1.0)
clf.fit(X_train, y_train)
pred = clf.predict(X_test)
print("ComplementNB accuracy:", accuracy_score(y_test, pred))
```

### 5) CategoricalNB (ডিসক্রিট ক্যাটেগরি)

```python
import numpy as np
from sklearn.naive_bayes import CategoricalNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# উদাহরণ: [Gender, Browser, Color] সবগুলো integer-coded category
# Gender: 0=Male, 1=Female
# Browser: 0=Chrome, 1=Firefox, 2=Edge
# Color: 0=Red, 1=Blue, 2=Green

X = np.array([
	[0, 0, 1], [1, 1, 0], [0, 2, 2], [1, 0, 1], [0, 1, 0], [1, 2, 2],
	[0, 0, 0], [1, 1, 2], [0, 2, 1], [1, 0, 2]
])
y = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1])  # দুইটি ক্লাস

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)

clf = CategoricalNB(alpha=1.0)
clf.fit(X_train, y_train)
pred = clf.predict(X_test)
print("CategoricalNB accuracy:", accuracy_score(y_test, pred))
```

---

## 🔹 সারসংক্ষেপ টেবিল

| Variant        | Data টাইপ       | ব্যবহার ক্ষেত্র |
| -------------- | --------------- | --------------- |
| Gaussian NB    | Continuous      | Numeric data    |
| Multinomial NB | Count / Text    | NLP, Spam       |
| Bernoulli NB   | Binary          | Yes/No feature  |
| Complement NB  | Imbalanced Text | NLP             |
| Categorical NB | Categorical     | Category-based  |

---

## 🔑 Exam Short Notes

* Always use log-sum of probabilities to avoid underflow.  
* Laplace smoothing (α) helps zero-count problems in text.  
* GaussianNB assumes normality per feature; check basic skew/outliers.  
* Multinomial vs Bernoulli: count vs presence—NLP-তে ডেটার ধরন অনুযায়ী বাছাই।  
* ComplementNB imbalanced টেক্সটে অনেক সময় বেশি robust।  
* CategoricalNB integer-coded discrete category-তে সরাসরি কাজ করে।

---

### মনে রাখবে

* সব Naive Bayes fast & lightweight  
* Feature independence assumption বাস্তবে পুরোপুরি সত্য না হলেও ভালো কাজ করে


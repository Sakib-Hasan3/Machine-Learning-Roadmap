# Hyperparameter Tuning (হাইপারপ্যারামিটার টিউনিং) — বাংলা গাইড

Hyperparameter tuning হলো মডেলের বাইরের সেটিংস (যেমন learning rate, regularization strength, tree depth ইত্যাদি) ঠিক করে মডেলের পারফরম্যান্স সর্বোচ্চ করার প্রক্রিয়া। নিচে প্রয়োজনীয় ধারণা, পদ্ধতি, কোড উদাহরণ ও ভালো প্র্যাকটিস দেয়া হলো।

---

## ১. কী ভিন্নতা? Hyperparameters vs Parameters
- Parameters: মডেল ট্রেনিং এর সময় শেখা হয় (উদাহরণ: linear model-এর coef_)
- Hyperparameters: আগে থেকেই নির্ধারণ করতে হয়, মডেল ট্রেনিংয়ের আচরণ নিয়ন্ত্রণ করে (উদাহরণ: Ridge-এর alpha, RandomForest-এর n_estimators)

---

## ২. কেন টিউন করবেন?
- Better generalization (test-set performance বাড়ে)
- Overfitting বা underfitting কমায়
- Training speed ও model complexity নিয়ন্ত্রণ করে

---

## ৩. প্রধান পদ্ধতি

1) Grid Search (GridSearchCV)
2) Random Search (RandomizedSearchCV)
3) Bayesian Optimization (Optuna, scikit-optimize)
4) Hyperband / BOHB (resource-aware)
5) Manual search + domain knowledge

---

## ৪. GridSearchCV — Exhaustive search

```python
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge

pipe = Pipeline([...])  # preprocessing + model
param_grid = {
	'model__alpha': [0.001, 0.01, 0.1, 1.0, 10.0]
}

grid = GridSearchCV(pipe, param_grid, cv=5, scoring='neg_mean_squared_error', n_jobs=-1)
grid.fit(X_train, y_train)

print('Best params:', grid.best_params_)
print('Best CV score:', grid.best_score_)

# Use best estimator
best = grid.best_estimator_
```

সুবিধা: সহজ, নির্দিষ্ট রেঞ্জে exhaustive।

অসুবিধা: যদি search space বড় হয়, computationally অপ্রচলিত।

---

## ৫. RandomizedSearchCV — স্ট্যাটিস্টিক্যাল সার্চ

```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint, uniform

param_dist = {
	'model__n_estimators': randint(50, 500),
	'model__max_depth': randint(3, 20),
	'model__min_samples_split': randint(2, 20)
}

rnd = RandomizedSearchCV(pipe, param_distributions=param_dist, n_iter=50, cv=5, scoring='accuracy', n_jobs=-1, random_state=42)
rnd.fit(X_train, y_train)

print(rnd.best_params_, rnd.best_score_)
```

সুবিধা: বড় search space-এ দ্রুত, প্রায়ই Grid তুলনায় ভাল ফল দেয় কম খরচে।

---

## ৬. Bayesian Optimization (Optuna উদাহরণ)

Optuna বা skopt মডেল-ভিত্তিক অনুসন্ধান করে যা আগের রেজাল্ট থেকে শিখে পরবর্তী পয়েন্ট নির্বাচন করে — সাধারণত fewer evaluations এ ভালো ফল দেয়।

```python
import optuna
from sklearn.model_selection import cross_val_score

def objective(trial):
	alpha = trial.suggest_loguniform('alpha', 1e-4, 1e1)
	model = Ridge(alpha=alpha)
	score = cross_val_score(model, X_train, y_train, cv=5, scoring='neg_mean_squared_error').mean()
	return score

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=50)
print('Best params:', study.best_params)
```

Optuna supports pruning (early stopping) of poor trials and parallel execution.

---

## ৭. Nested Cross-Validation — unbiased performance estimate

যদি আপনি hyperparameter tuning ও model evaluation একসাথে করছেন, nested CV ব্যবহার করুন: inner CV টিউনিংয়ের জন্য, outer CV final evaluation-এর জন্য। এতে ওভারফিটিং এড়ায় এবং CV-estimate biased হয় না।

```python
from sklearn.model_selection import GridSearchCV, cross_val_score
from sklearn.model_selection import KFold

inner_cv = KFold(n_splits=5, shuffle=True, random_state=42)
outer_cv = KFold(n_splits=5, shuffle=True, random_state=1)

gs = GridSearchCV(pipe, param_grid, cv=inner_cv, scoring='neg_mean_squared_error')
nested_scores = cross_val_score(gs, X, y, cv=outer_cv, scoring='neg_mean_squared_error')
print('Nested CV RMSE:', np.sqrt(-nested_scores).mean())
```

---

## ৮. Practical tips for search space design

- Use log-scale for scale parameters (learning rate, alpha): suggest_loguniform
- For integers (trees, n_estimators), use randint
- Keep ranges wide initially, then narrow down
- Use fewer hyperparameters at once (hierarchical search)
- Consider conditional parameters (e.g., max_depth only if boosting_type == 'gbdt')

---

## ৯. Early stopping, warm-start, and resource-aware tuning

- আলাদা করে early stopping ব্যবহার করলে training time বাঁচে (XGBoost, LightGBM, CatBoost support it)
- Warm-start (some estimators) সাহায্য করে iterative tuning-এ
- Hyperband/BOHB resource-aware methods আছে যা দ্রুত দেখা দেয় ভালো ট্রেনিং-কস্ট বাঁচিয়ে

---

## ১০. Metric selection ও scoring

- টাস্ক-ভিত্তিক scoring নির্বাচন করুন (classification-এ ROC-AUC vs accuracy)।
- Imbalanced dataset-এ precision/recall বা PR-AUC প্রাধান্য দিন।

---

## ১১. Parallelism ও runtime considerations

- `n_jobs=-1` ব্যবহার করে CPU parallelization করতে পারেন (Grid/Random)
- তবে cross-validation *n_jobs* এবং estimator এর ভিতরের parallelism (n_jobs) conflict এড়াতে nested control রাখুন।
- ক্লাউড/cluster বা Ray Tune/Optuna যে parallel backends ব্যবহার করা যায় বড় কাজের জন্য।

---

## ১২. Reproducibility

- সব random_state/seed নির্ধারণ করুন
- Trials ও results লোগ করুন (Optuna এর study অথবা MLflow)

---

## ১৩. Example: Tuning RandomForest

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint

param_dist = {
	'model__n_estimators': randint(100, 1000),
	'model__max_depth': randint(3, 30),
	'model__min_samples_split': randint(2, 20),
	'model__max_features': ['sqrt', 'log2', None]
}

pipe = Pipeline([('pre', preprocessor), ('model', RandomForestClassifier(random_state=42))])
search = RandomizedSearchCV(pipe, param_distributions=param_dist, n_iter=50, cv=5, scoring='accuracy', n_jobs=-1, random_state=42)
search.fit(X_train, y_train)
print(search.best_params_, search.best_score_)
```

---

## ১৪. Logging & Experiment Tracking

- Use MLflow, Weights & Biases বা Optuna's integrated storage to track trials, parameters, and metrics.

```python
import mlflow
mlflow.start_run()
mlflow.log_params(search.best_params_)
mlflow.log_metric('best_score', search.best_score_)
mlflow.end_run()
```

---

## ১৫. Quick Checklist

- [ ] Define objective metric (task-appropriate)
- [ ] Choose search method (Grid/Random/Bayes)
- [ ] Design reasonable search space (log-scale for scale params)
- [ ] Use CV (or nested CV) to avoid biased estimates
- [ ] Use early stopping or pruning to save compute
- [ ] Track experiments and seed values
- [ ] Final evaluation on hold-out test set

---

আপনি চাইলে আমি একটি runnable Jupyter notebook (`hyperparameter_tuning.ipynb`) তৈরি করে দিতে পারি যেখানে Grid/Random/Optuna উদাহরণগুলো small dataset এ চালিয়ে দেখানো থাকবে — কোনটি চান? 


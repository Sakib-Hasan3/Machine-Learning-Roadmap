# Red Wine Quality EDA - বাংলা টিউটোরিয়াল

## ভূমিকা
এই notebook এ আমরা Red Wine Quality dataset এর উপর Exploratory Data Analysis (EDA) করব। এই dataset Portuguese "Vinho Verde" wine এর physicochemical properties এবং quality ratings নিয়ে কাজ করে।

## Dataset পরিচিতি

### Data Set Information
Portuguese "Vinho Verde" wine এর red এবং white variants এর dataset। Privacy এবং logistic issues এর কারণে শুধুমাত্র physicochemical (inputs) এবং sensory (output) variables উপলব্ধ। 

### Dataset এর বৈশিষ্ট্য:
- **Classification বা Regression task** হিসেবে ব্যবহার করা যায়
- **Imbalanced dataset** - normal wines বেশি, excellent বা poor wines কম
- **Outlier detection** algorithms ব্যবহার করে excellent/poor wines detect করা যায়
- **Feature selection** methods test করার সুযোগ আছে

### Attribute Information

#### Input Variables (Physicochemical Tests):
1. **Fixed Acidity** - Non-volatile acids (tartaric acid)
2. **Volatile Acidity** - Acetic acid, high levels = vinegar taste
3. **Citric Acid** - Freshness এবং flavor যোগ করে
4. **Residual Sugar** - Fermentation এর পর বাকি sugar
5. **Chlorides** - Salt এর পরিমাণ
6. **Free Sulfur Dioxide** - SO2 এর free form
7. **Total Sulfur Dioxide** - Free + bound forms of SO2
8. **Density** - Wine এর ঘনত্ব
9. **pH** - Acidity/alkalinity level (0-14 scale)
10. **Sulphates** - Wine additive, antimicrobial properties
11. **Alcohol** - Alcohol percentage

#### Output Variable (Sensory Data):
12. **Quality** - Score between 0 and 10 (subjective rating)

## Code Implementation এবং ব্যাখ্যা

### ১. Data Loading এবং Initial Exploration

```python
import pandas as pd
df=pd.read_csv('winequality-red.csv')
df.head()
```

**ব্যাখ্যা:**
- `import pandas as pd` - Data manipulation এর জন্য pandas library import
- `df=pd.read_csv('winequality-red.csv')` - CSV file থেকে data load করা
- `df.head()` - প্রথম 5টি row display করা

**Expected Output:**
```
   fixed acidity  volatile acidity  citric acid  residual sugar  chlorides  ...
0            7.4              0.70         0.00             1.9      0.076  ...
1            7.8              0.88         0.00             2.6      0.098  ...
2            7.8              0.76         0.04             2.3      0.092  ...
3           11.2              0.28         0.56             1.9      0.075  ...
4            7.4              0.70         0.00             1.9      0.076  ...
```

### ২. Dataset Summary

```python
## Summary of the dataset
df.info()
```

**ব্যাখ্যা:**
- Dataset এর structure এবং data types দেখানো
- Non-null values count এবং memory usage

**Expected Output:**
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1599 entries, 0 to 1598
Data columns (total 12 columns):
 #   Column                Non-Null Count  Dtype  
---  ------                --------------  -----  
 0   fixed acidity         1599 non-null   float64
 1   volatile acidity      1599 non-null   float64
 ...
 11  quality              1599 non-null   int64  
dtypes: float64(11), int64(1)
memory usage: 150.0 KB
```

### ৩. Descriptive Statistics

```python
## descriptive summary of the dataset
df.describe()
```

**ব্যাখ্যা:**
- সব numerical columns এর statistical summary
- Count, mean, std, min, quartiles, max values

**Key Insights:**
- **Fixed Acidity**: Mean 8.32, Range 4.6-15.9
- **Alcohol**: Mean 10.42%, Range 8.4-14.9%
- **Quality**: Mean 5.64, Range 3-8 (no 1,2,9,10 ratings)

### ৪. Dataset Dimensions

```python
df.shape
```

**Expected Output:** `(1599, 12)`
**ব্যাখ্যা:** 1599 wine samples, 12 features (11 inputs + 1 target)

### ৫. Column Names

```python
## List down all the columns names
df.columns
```

**Expected Output:**
```
Index(['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
       'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
       'pH', 'sulphates', 'alcohol', 'quality'], dtype='object')
```

### ৬. Target Variable Analysis

```python
df['quality'].unique()
```

**Expected Output:** `array([5, 6, 7, 4, 8, 3], dtype=int64)`
**ব্যাখ্যা:** Quality ratings 3-8 পর্যন্ত, কোন extreme values (1,2,9,10) নেই

## Data Quality Assessment

### ৭. Missing Values Check

```python
## Missing values in the dataset
df.isnull().sum()
```

**Expected Output:**
```
fixed acidity           0
volatile acidity        0
citric acid            0
residual sugar         0
chlorides              0
free sulfur dioxide    0
total sulfur dioxide   0
density                0
pH                     0
sulphates              0
alcohol                0
quality                0
dtype: int64
```

**ব্যাখ্যা:** কোন missing values নেই - clean dataset

### ৮. Duplicate Records Detection

```python
## Duplicate records
df[df.duplicated()]
```

**ব্যাখ্যা:** Duplicate rows identify করা data quality নিশ্চিত করার জন্য

### ৯. Data Cleaning

```python
## Remove the duplicates
df.drop_duplicates(inplace=True)
```

**ব্যাখ্যা:** 
- Duplicate rows remove করা
- `inplace=True` - original DataFrame modify করা

### ১০. Updated Dataset Size

```python
df.shape
```

**Expected Output:** `(1359, 12)` (approximately)
**ব্যাখ্যা:** ~240 duplicate rows removed

## Correlation Analysis

### ১১. Correlation Matrix

```python
## Correlation
df.corr()
```

**Key Correlations with Quality:**
- **Alcohol**: +0.476 (Strong positive)
- **Volatile Acidity**: -0.391 (Strong negative)
- **Sulphates**: +0.251 (Moderate positive)
- **Citric Acid**: +0.226 (Moderate positive)

### ১২. Correlation Heatmap

```python
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(),annot=True)
```

**ব্যাখ্যা:**
- Visual representation of correlations
- Color intensity = correlation strength
- `annot=True` - correlation values display করা
- `figsize=(10,6)` - plot size set করা

**Key Visual Insights:**
- Dark colors = Strong correlations
- Light colors = Weak correlations
- Red/Orange = Positive correlations
- Blue = Negative correlations

## Data Visualization এবং Pattern Analysis

### ১৩. Target Variable Distribution

```python
## Visualization
#conclusion- It is an imbalanced dataset
df.quality.value_counts().plot(kind='bar')
plt.xlabel("Wine Quality")
plt.ylabel("Count")
plt.show()
```

**Expected Distribution:**
- Quality 5: ~681 wines (50%)
- Quality 6: ~638 wines (47%)
- Quality 7: ~199 wines (15%)
- Quality 4: ~53 wines (4%)
- Quality 8: ~18 wines (1%)
- Quality 3: ~10 wines (<1%)

**ব্যাখ্যা:** Highly imbalanced dataset - বেশিরভাগ wines average quality (5-6)

### ১৪. Feature Distribution Analysis

```python
for column in df.columns:
    sns.histplot(df[column],kde=True)
```

**ব্যাখ্যা:**
- প্রতিটি feature এর distribution pattern দেখানো
- `kde=True` - Kernel Density Estimation curve যোগ করা
- Normal vs Skewed distributions identify করা

**Distribution Patterns:**
- **pH**: Near normal distribution
- **Alcohol**: Right-skewed distribution
- **Residual Sugar**: Highly right-skewed
- **Quality**: Discrete distribution (categorical)

### ১৫. Specific Feature Analysis

```python
sns.histplot(df['alcohol'])
```

**ব্যাখ্যা:** Alcohol content এর specific distribution analysis
- Range: 8.4% - 14.9%
- Most wines: 9-11% alcohol
- Right-skewed distribution

### ১৬. Multivariate Analysis

```python
#univariate,bivariate,multivariate analysis
sns.pairplot(df)
```

**ব্যাখ্যা:**
- **Univariate**: Diagonal এ histograms
- **Bivariate**: Off-diagonal এ scatter plots
- সব features এর pairwise relationships
- Linear/non-linear patterns identify করা

**Key Patterns:**
- Strong linear relationships: Fixed acidity vs Citric acid
- Non-linear patterns: Alcohol vs Quality
- Outliers identification possible

### ১৭. Categorical Analysis

```python
##categorical Plot
sns.catplot(x='quality', y='alcohol', data=df, kind="box")
```

**ব্যাখ্যা:**
- Quality level অনুযায়ী alcohol distribution
- Box plots show median, quartiles, outliers
- Category-wise comparison

**Key Insights:**
- Higher quality wines → Higher alcohol content
- Quality 8 wines: Highest median alcohol (~12%)
- Quality 3-4 wines: Lower alcohol content (~9-10%)

### ১৮. Multi-dimensional Relationship

```python
sns.scatterplot(x='alcohol',y='pH',hue='quality',data=df)
```

**ব্যাখ্যা:**
- তিনটি variables এর simultaneous relationship
- X-axis: Alcohol content
- Y-axis: pH levels
- Color coding: Quality ratings

**Pattern Analysis:**
- Higher alcohol + optimal pH → Better quality
- Quality clusters visible in certain regions
- Complex multi-dimensional relationships

## Key Findings এবং Insights

### 1. Dataset Characteristics
- **Size**: 1599 samples → 1359 after cleaning
- **Features**: 11 physicochemical properties
- **Target**: Quality ratings (3-8 scale)
- **Quality**: Clean data, no missing values

### 2. Data Distribution Patterns
- **Imbalanced Target**: 97% wines are quality 4-7
- **Normal Distribution**: pH, density
- **Right-skewed**: Alcohol, residual sugar, chlorides
- **Quality Distribution**: Bell-shaped, centered at 5-6

### 3. Strong Predictors of Quality
1. **Alcohol** (+0.476): Higher alcohol → Better quality
2. **Volatile Acidity** (-0.391): Lower acidity → Better quality
3. **Sulphates** (+0.251): Optimal sulphate levels important
4. **Citric Acid** (+0.226): Freshness contributes to quality

### 4. Feature Relationships
- **Fixed Acidity ↔ Citric Acid**: Strong positive correlation
- **Free SO2 ↔ Total SO2**: Expected strong correlation
- **Density ↔ Alcohol**: Negative correlation (physics)
- **pH ↔ Fixed Acidity**: Negative correlation (chemistry)

### 5. Quality Patterns
- **Premium Wines** (Quality 7-8): Higher alcohol, lower volatile acidity
- **Average Wines** (Quality 5-6): Moderate levels across features
- **Poor Quality** (Quality 3-4): Lower alcohol, higher volatile acidity

## Business Implications

### Wine Production Insights:
1. **Alcohol Content**: Target 11-13% for premium wines
2. **Acidity Management**: Control volatile acidity levels
3. **Sulphate Optimization**: Maintain optimal sulphate levels
4. **pH Balance**: Monitor acid-base balance

### Quality Prediction Potential:
- **High Predictability**: Alcohol and volatile acidity
- **Moderate Predictability**: Sulphates, citric acid
- **Complex Interactions**: Multiple feature combinations

### Marketing Strategies:
- **Premium Segment**: Focus on high-alcohol, low-volatile acidity wines
- **Mass Market**: Optimize cost vs quality for ratings 5-6
- **Quality Control**: Monitor key chemical parameters

## Technical Recommendations

### For Machine Learning Models:
1. **Feature Engineering**: Create interaction terms
2. **Scaling**: Normalize features with different ranges
3. **Class Imbalance**: Use SMOTE or weighted algorithms
4. **Feature Selection**: Focus on top correlated features

### For Further Analysis:
1. **Outlier Analysis**: Detect anomalous wines
2. **Clustering**: Group wines by chemical profiles
3. **Time Series**: If temporal data available
4. **Comparison**: Red vs White wine analysis

## সারসংক্ষেপ

এই EDA থেকে আমরা শিখেছি:

1. **Data Quality**: Clean এবং complete dataset
2. **Target Imbalance**: Classification challenges expected
3. **Key Drivers**: Alcohol এবং volatile acidity most important
4. **Complex Relationships**: Multiple factors influence quality
5. **Business Value**: Actionable insights for wine production

Red Wine Quality dataset একটি excellent example of real-world data science challenges - imbalanced classes, multiple correlated features, এবং domain-specific insights। এই analysis wine industry এবং machine learning উভয় perspective থেকে valuable।

## Next Steps

1. **Feature Engineering**: Create new meaningful features
2. **Model Building**: Try different algorithms
3. **Hyperparameter Tuning**: Optimize model performance
4. **Model Interpretation**: SHAP/LIME analysis
5. **Business Integration**: Deploy insights in production



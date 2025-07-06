# 🧠 Adult Census Income Classification

This project is focused on predicting whether a person earns more than \$50K a year using the [Adult Census Income Dataset](https://archive.ics.uci.edu/ml/datasets/adult). It involves complete data preprocessing, model evaluation, cross-validation, hyperparameter tuning, and performance comparison across several ML models.

---

## 📂 Dataset Overview

- **Source**: UCI Machine Learning Repository
- **Target**: `income` (binary classification — `>50K` vs `<=50K`)

---
## 🧹 Data Preprocessing 

To prepare the data for robust modeling, implemented a structured and repeatable preprocessing pipeline with the following steps:

### ✅ 1. Data Cleaning
- Replaced invalid placeholders (`'?'`, `99999`) with `NaN`.
- Dropped redundant columns like `fnlwgt`.
- Removed exact duplicate rows to reduce data noise.

### ✅ 2. Missing Value Imputation
- **Numerical Features**: Imputed using **mean strategy**.
- **Categorical Features**: Imputed using **most frequent category**.

### ✅ 3. Label Encoding
- Applied **Label Encoding** to all categorical variables 


### ✅ 4. Feature Scaling
- Applied **StandardScaler** to normalize numerical features:
  -`age`, `education-num`, `capital-gain`, `capital-loss`, `hours-per-week`
- This ensures features are on the same scale and models like KNN & Gradient Boosting perform optimally.


## 📈 Models Used

Each model was:
- Evaluated using **Stratified Cross-Validation**
- Tuned with **GridSearchCV**
- Assessed using **Accuracy**, **F1 Score**, and **ROC AUC**

| Model                      | Accuracy | F1 Score | ROC AUC |
|----------------------------|----------|----------|---------|
| ✅ LGBMClassifier           | 0.8716   | 0.7113   | 0.9263  |
| ✅ XGBClassifier            | 0.8708   | 0.7094   | 0.9263  |
| ✅ GradientBoosting        | 0.8708   | 0.7098   | 0.9259  |
| ✅ RandomForestClassifier   | 0.8615   | 0.6807   | 0.9132  |
| ✅ AdaBoostClassifier       | 0.8612   | 0.6877   | 0.9162  |
| ✅ DecisionTreeClassifier   | 0.8519   | 0.6759   | 0.8972  |
| ✅ KNeighborsClassifier     | 0.8354   | 0.6320   | 0.8821  |

---

## 🏆 Conclusion

- **LightGBM** was the best performer across all metrics.
- Boosting models clearly outperformed simpler models.
- KNN had the weakest performance and longest training time.

---

## 📦 Libraries Used

- `pandas`, `numpy`, `matplotlib`, `seaborn`
- `scikit-learn`
- `xgboost`, `lightgbm`, `catboost`

---

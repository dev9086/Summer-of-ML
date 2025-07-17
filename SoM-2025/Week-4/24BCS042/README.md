# 🧠 IRIS Data 

This project deals with iris data and predicts the outcome on basis of various models and using various techniques to attain max accuracy with less variance and bias 

---

## 📂 Dataset Overview

- **Source**: Sklearn Dataset

---

## 📦 Libraries Used

- `pandas`, `numpy`, `matplotlib`, `seaborn`
- `scikit-learn`
- `randomforest`,`knearest neighbour`
- `xgboost` , `adaboost`

---

## 🧹 Data Preprocessing 

To prepare the data for robust modeling, implemented a structured and repeatable preprocessing pipeline with the following steps:


### ✅ 1. Missing Value Imputation
- **Numerical Features**: Imputed using **mean strategy**.
- **Categorical Features**: Imputed using **most frequent category**.

### ✅ 2. Label Encoding
- Applied **Label Encoding** to all categorical variables 

### ✅ 3. Hypertuning
- Applied **GridSearchCV & RandomSearchCV** to get best parameters:


## 📈 Models Used

Each model was:
- Evaluated using **Stratified Cross-Validation**
- Tuned with **GridSearchCV & RandomSearchCV**
- Assessed using **Accuracy**, **F1 Score**, and **ROC AUC**


## 🏆 Conclusion

- RandomSearchCV and GridSearchCV increases model performance by selecting best parameters
- Boosting methods helps alot to increase model accuracy 

---


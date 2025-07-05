# Week 3 - SA-2025 GRADED ASSIGNMENT 🚀

## 📁 Project Title: Spaceship Titanic - Alternate Dimension Prediction

This is a machine learning project built around the **Spaceship Titanic** dataset from Kaggle. The objective is to predict which passengers were teleported to another dimension during a cosmic event. The task uses various classification models, focusing on **Logistic Regression** & **Support Vector Machines (SVM)**.

![Spaceship Titanic](https://www.gannett-cdn.com/-mm-/682bf77435754aee88576469063388a7d8b07c2a/c=0-150-1280-873/local/-/media/2017/02/01/Reno/RGJ/636215634914521096-image001.jpg?width=660&height=373&fit=crop&format=pjpg&auto=webp)

---

## 📊 Dataset

- **Source**: [Google Drive CSV](https://drive.google.com/file/d/1sbQ5WJ-KCPBrhT2YagtaARGoujCMpB8Q/view)
- **Records**: ~13,000 passengers
- **Features**: Includes passenger ID, home planet, cryo-sleep status, destination, cabin, age, and more.
- **Target**: `Transported` (Binary: True/False)

---

## 🎯 Objective

Build a classification model to accurately predict if a passenger was **transported** to an alternate dimension.

---

## ⚙️ Technologies Used

- Python
- Jupyter Notebook
- Libraries:
  - `pandas`, `numpy`, `matplotlib`
  - `scikit-learn`

---

## 🧠 Machine Learning Techniques

- **Preprocessing**:
  - Handling missing values
  - Label encoding
  - Feature scaling (`StandardScaler`)
- **Model Used**: Support Vector Machine (SVM)
- **Evaluation Metrics**:
  - Accuracy
  - ROC-AUC
  - Cross-validation
  - Classification report

---

## 📈 Model Performance (Logistic Regression)

| Metric            | Value                  |
|-------------------|------------------------|
| Accuracy          | `~0.79` (79.06%)       |
| ROC-AUC Score     | `~0.88`                |
| Cross-Validation (Average)  | `0.79` (cv=5) |
| F1-Score (Class 0) | 0.79                   |
| F1-Score (Class 1) | 0.79                   |

## 📈 Model Performance (SVM)

| Metric            | Value                  |
|-------------------|------------------------|
| Accuracy          | `~0.80` (79.91%)       |
| ROC-AUC Score     | `~0.86`                |
| Cross-Validation (Average) | `~0.79` (cv=5) |
| F1-Score (Class 0) | 0.80                   |
| F1-Score (Class 1) | 0.80                   |

---

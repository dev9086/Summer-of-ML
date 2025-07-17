# 💼 Census Income Classification – Week 4 (Graded Assignment)

This project performs **exploratory data analysis (EDA)** and preprocessing on the UCI "Adult" dataset to predict whether an individual's annual income exceeds $50,000.<br>
Also known as **Census dataset**.

## 📌 Problem Statement

> Predict whether an individual's income exceeds $50K/year based on census data.  
This is a **binary classification** task using the well-known ["Census Income" (Adult)](https://archive.ics.uci.edu/ml/datasets/adult) dataset.

## 📊 What’s Inside

The notebook `Week_4.ipynb` covers the following:

### ✅ Data Source
- UCI ML Repository:  
  - `adult.data` for training  
  - `adult.test` for testing

### 🧹 Data Preparation
- Assigning column names to match the dataset documentation
- Merging training and testing datasets for consistent EDA
- Handling missing or ambiguous values (e.g., `?`)
- Type conversions

### 🔍 Exploratory Data Analysis
- Univariate and bivariate analysis
- Visuals:
  - Histograms for age and hours-per-week
  - Count plots for categorical features
  - Box plots for income across various demographics
- Target distribution visualization (`<=50K` vs `>50K`)

### 🧠 Feature Insights
- Analyzing key relationships:
  - Education vs Income
  - Occupation vs Income
  - Gender-based income differences

## 📁 File Structure

```
.
├── Week_4.ipynb         # EDA & preprocessing notebook
└── README.md            # This file
```
# Bonus Linear Regression Project - CodeChef vs Codeforces Ratings

This notebook is a **bonus assignment** that applies linear regression to real-world data comparing **CodeChef** and **Codeforces** competitive programming ratings. It walks through exploratory data analysis, correlation, outlier removal, and prediction using gradient descent.

## 📘 Notebook Summary

The project explores:

- Importing and visualizing competitive programming rating data
- Statistical summaries and distribution plots
- Detecting and removing outliers using **IQR (Interquartile Range)**
- Correlation matrix and scatter plots
- Kernel Density Estimation (KDE) plots
- Histogram visualizations (before and after cleaning)
- Regression analysis using **Seaborn regplot**
- Manual implementation of **Gradient Descent**
- Computing **R² (Coefficient of Determination)**
- Predictive functions:
  - Convert CodeChef → Codeforces ratings
  - Convert Codeforces → CodeChef ratings

## 🧪 Technical Concepts Covered

- **Linear Regression**
- **Exploratory Data Analysis (EDA)**
- **IQR-based Outlier Detection**
- **Correlation Analysis**
- **Kernel Density Estimation (KDE)**
- **Gradient Descent Algorithm**
- **R² Score Evaluation**

## 🛠️ Technologies Used

- Python 3.7+
- NumPy
- Pandas
- Seaborn
- Matplotlib
- Jupyter Notebook

## 📁 File Structure

- `Week_2_(bonus).ipynb`: Main notebook containing code, plots, and analysis

## 🚀 How to Run

1. Clone the repository or download the notebook file
2. Open it using [Google Colab](https://colab.research.google.com/), Jupyter Notebook, or any compatible IDE
3. Install dependencies (if not already available):
   ```bash
   pip install numpy pandas matplotlib seaborn
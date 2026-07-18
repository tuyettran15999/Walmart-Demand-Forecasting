# Walmart Time Series Demand Forecasting
An end-to-end Data Science project that develops machine learning models to forecast weekly sales for Walmart stores. The project demonstrates the complete data science workflow, from data understanding and feature engineering to forecasting model development and business recommendations.

**Best Model:** XGBoost  
**Business Domain:** Retail Supply Chain & Demand Forecasting

**1. Project Overview**

This project develops an end-to-end demand forecasting pipeline to predict weekly sales for each Walmart Store–Department combination. The objective is to improve inventory planning, reduce stockouts, minimize excess inventory, and support data-driven retail decision-making.
The project follows a complete Data Science workflow, including data understanding, exploratory data analysis, feature engineering, baseline forecasting, machine learning model development, model evaluation, and business recommendations.

**2. Business Problem**

Accurate demand forecasting enables retailers to:
- Improve inventory planning
- Reduce stockouts and overstock situations
- Optimize workforce scheduling
- Support promotion and replenishment planning

**3. Dataset**

The project uses the **Walmart - Super Market Dataset** on Kaggle.
Three datasets are included:
- `train.csv`
- `features.csv`
- `stores.csv`

**4. Project Workflow**
- ✅ Data Understanding
- ✅ Exploratory Data Analysis
- ✅ Feature Engineering
- ✅ Baseline Forecasting
- ✅ Machine Learning Models
- ✅ Business Insights & Recommendations

**5. Repository Structure**
```
data/
notebooks/
src/
README.md
requirements.txt
```

**6. Methodology**

The forecasting pipeline includes:

- Data cleaning and dataset integration
- Exploratory data analysis
- Time-based feature engineering
- Lag and rolling statistical features
- Baseline forecasting models
- Machine learning model development
- Model evaluation using MAE and RMSE
- Business insights and recommendations

**7. Model Performance**

| Model | MAE | RMSE |
|------|------:|------:|
| Naive Forecast | 1718.51 | 3942.46 |
| Linear Regression | 2019.96 | 3986.24 |
| Ridge Regression | 2027.24 | 3985.36 |
| Random Forest | 1538.27 | 3406.64 |
| **XGBoost** | **1484.80** | **3168.98** |

**8. Key Business Insights**

- Historical sales are the strongest predictors of future demand.
- Short-term demand trends provide more predictive power than yearly seasonal patterns.
- Tree-based ensemble models outperform linear regression models.
- XGBoost achieved the best forecasting accuracy and was selected as the final forecasting model.

**9. Technologies**

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- XGBoost
- Jupyter Notebook

**10. Future Improvements**

- Incorporate additional external variables such as weather forecasts and competitor promotions.
- Explore deep learning approaches for long-term forecasting.
- Deploy the forecasting pipeline as an automated prediction system.

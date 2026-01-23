# Customer Churn Prediction Project

## Summary

This repository contains a Python-based machine learning project focused on predicting customer churn for a telecom company using historical customer data.

The project includes:

1. `churn_prediction`.ipynb – A detailed Jupyter Notebook that performs exploratory data analysis (EDA), feature engineering, logistic regression model training, and evaluation using ROC curve and AUC score.

Together, these files demonstrate a full supervised machine learning workflow from raw data exploration to model evaluation and interpretation.


## Dataset Overview

The dataset `telco_customer_churn.csv` contains information about telecom customers, including demographic details, service usage, and account information.

Key features include:

* `Churn (Target)`: Indicates if the customer has churned (Yes/No)

* `gender`: Customer gender

* `SeniorCitizen`: Whether the customer is a senior citizen

* `Partner`: Whether the customer has a partner

* `Dependents`: Whether the customer has dependents

* `tenure`: Number of months the customer has stayed with the company

* `PhoneService`, `InternetService`, `OnlineSecurity`, etc.: Service subscription indicators

* `MonthlyCharges`: Monthly account charges

* `TotalCharges`: Total account charges

These features are used to train a logistic regression model to predict customer churn.


## Tools Used

* python
* pandas
* numpy
* seaborn
* matplotlib
* scikit-learn

## Steps to run the project

### 1. Clone / Download the project
> Download the project folder and open a terminal in the root directory.

### 2. Create and activate virtual environment
```
     # On Windows
    python -m venv .venv
    venv\Scripts\activate
    
     # On Mac/Linux
    python3 -m venv .venv
    source .venv/bin/activate
```

### 3. Install required libraries
```
    pip install pandas numpy seaborn matplotlib scikit-learn
```

### 4. Prepare the dataset
> Ensure you have the car dataset file in the correct location:
```
    month 2/week 3/data/telco_customer_churn.csv 
```
> If you don't have the actual dataset, you can:
    > 1. Download a car dataset from [Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
    > 2. Update the file paths in the scripts to match your dataset location.

### 5. Steps to run the jupyter notebook M2-Week2.ipynb
```
    jupyter notebook churn_prediction.ipynb
```

## Project Workflow

1. Exploratory Data Analysis (EDA)

    * Checked data types and missing values

    * Converted numeric columns (`TotalCharges`) and handled missing values

    * Visualized distributions of categorical and numerical variables

    * Explored relationships between features and target variable (`Churn`)

2. Data Preparation

    * Dropped irrelevant columns (`customerID`)

    * Encoded categorical features using `LabelEncoder`

    * Split data into features (X) and target (y)

    * Performed train-test split (80% train, 20% test)

3. Model Building

    * Trained a Logistic Regression model on the training set

4. Model Evaluation

    * Evaluated model performance using ROC-AUC score

    * Plotted ROC Curve for classification performance
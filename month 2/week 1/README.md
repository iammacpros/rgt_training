# Loan Prediction Project

## Summary
This repository contains a Python-based machine learning project focused on predicting loan approval outcomes using historical loan application data.

The project includes:
1. `loan_prediction_analysis.ipynb` – A complete Python script that performs exploratory data analysis (EDA), feature engineering, model training, and evaluation using Decision Tree and Random Forest classifiers.

2. `loan_prediction_report.pdf` – A detailed report documenting the analysis process, model performance, evaluation metrics, visualizations, and insights derived from the loan prediction task.

Together, these files demonstrate a full supervised machine learning workflow from raw data exploration to model evaluation and interpretation.

## Dataset Overview

The dataset contains customer demographic, financial, and loan-related attributes used to predict loan approval status.

Key features include:

* `loan_status (Target)`: Loan approval status

* `person_age`: Applicant age

* `person_gender`: Applicant gender

* `person_income`: Applicant income

* `person_education`: Education level

* `person_emp_exp`: Years of employment experience

* `person_home_ownership`: Home ownership status

* `loan_intent`: Purpose of the loan

* `loan_amnt`: Loan amount requested

* `loan_int_rate`: Loan interest rate

* `loan_percent_income`: Loan amount as a percentage of income

* `cb_person_cred_hist_length`: Credit history length

These features are used to train classification models that predict whether a loan will be approved or rejected.

## Tools Used
* python 3.x
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

### 4. Prepare the Dataset
> Ensure you have the car dataset file in the correct location:
```
    month 2/week 1/data/loan_data.csv
```
> If you don't have the actual dataset, you can:
    > 1. Download a car dataset from [Kaggle](https://www.kaggle.com/datasets/taweilo/loan-approval-classification-data)
    > 2. Update the file paths in the scripts to match your dataset location.

### 5. Run the Loan prediction jupyter notebook
```
    jupyter notebook loan_prediction_analysis.ipynb

```

## Project Workflow

1. Exploratory Data Analysis (EDA)

    Visualized loan approval distribution

    Inspected numerical feature distributions and outliers

    Analyzed categorical feature distributions

    Generated correlation heatmap

    Explored age and loan amount distributions

2. Data Preparation

    Identified categorical and numerical features

    Applied one-hot encoding using pd.get_dummies

    Split data into features (X) and target (y)

    Performed train-test split (80% train, 20% test)

3. Model Building

    Decision Tree Classifier

    Random Forest Classifier (with class balancing)

4. Model Evaluation

    Accuracy score

    Confusion matrix

    Classification report (Precision, Recall, F1-Score)

    Feature importance analysis for both models
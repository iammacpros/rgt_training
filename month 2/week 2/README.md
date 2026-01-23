# Car Price Prediction Project
## Summary

This repository contains a Python-based machine learning project focused on predicting car selling prices using historical car listing data.

The project includes:

1. `price_prediction.ipynb` – A complete Jupyter Notebook that performs exploratory data analysis (EDA), feature engineering, model training, and evaluation using multiple regression models including Linear Regression, Ridge Regression, Random Forest Regressor, and Gradient Boosting Regressor.

Together, these files demonstrate a full supervised machine learning workflow from raw data exploration to model evaluation and interpretation.

## Dataset Overview
The dataset contains various features related to cars, including:

* `selling_price`: Car selling price (numerical)
* `year`: Manufacturing year (numerical)
* `engine`: Engine capacity (numerical)
* `max_power`: Maximum power (numerical)
* `fuel`: Fuel type (categorical)
* `seller_type`: Type of seller (categorical)
* `transmission`: Transmission type (categorical)
* `owner`: Ownership history (categorical)
* `mileage(km/ltr/kg)`: Mileage (numerical)
* `seats`: Number of seats (numerical)
* `km_driven`: Kilometers driven (numerical)

These attributes allow analysis of the key factors influencing car prices and form the basis for future predictive modeling tasks.

## Tool Used
* python 3.x
* pandas
* seaborn
* matplotlib
* numpy
* scikit-learn

## Steps to run the python file

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
    month 1/week 3/data/cardekho.csv
```
> If you don't have the actual dataset, you can:
    > 1. Download a car dataset from [Kaggle](https://www.kaggle.com/datasets/sukhmandeepsinghbrar/car-price-prediction-dataset)
    > 2. Update the file paths in the scripts to match your dataset location.

### 5. Steps to run the jupyter notebook M2-Week2.ipynb
```
    jupyter notebook price_prediction.ipynb
```

## Project Workflow

1. Data Preparation

    * Identified categorical and numerical features

    * Applied one-hot encoding using pd.get_dummies

    * Dropped irrelevant columns such as name

    * Split data into features (X) and target (y)

    * Performed train-test split (80% train, 20% test)

2. Model Building

    * Linear Regression

    * Ridge Regression

    * Random Forest Regressor

    * Gradient Boosting Regressor

3. Model Evaluation

    * Calculated performance metrics: Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), R² Score

    * Visualized Actual vs Predicted prices for each model
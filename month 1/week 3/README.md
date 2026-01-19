# Complete car data anaysis and visualizations

## Summary
This repository contains two files:

1. complete_data_visualization.py – A comprehensive Python script that loads the car dataset, performs data cleaning, removes outliers, and generates a wide range of visualizations to analyze car selling prices and related features.

2. complete_cardata_analysis_report.pdf – A detailed written report that explains the full data analysis process, visualizations, findings, and insights derived from the car price dataset.

Together, these files demonstrate an end-to-end exploratory data analysis (EDA) workflow, from raw data preparation to visual insight reporting.

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

## Steps to run the python file

### 1. Clone / Download the project
> Download the project folder and open a terminal in the root directory.

### 2. Create virtual environment
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
    pip install pandas numpy seaborn matplotlib
```

### 4. Prepare the dataset
> Ensure you have the car dataset file in the correct location:
```
    month 1/week 3/data/cardekho.csv
```
> If you don't have the actual dataset, you can:
    > 1. Download a car dataset from [Kaggle](https://www.kaggle.com/datasets/sukhmandeepsinghbrar/car-price-prediction-dataset)
    > 2. Update the file paths in the scripts to match your dataset location.

### 5. Run the data visualization script

```
    python basic_data_visualizations.py
```
> What it does:
```
    Data Cleaning:

        Handles missing values in seats, engine, max_power, and mileage(km/ltr/kg)

        Converts max_power to numeric format

        Applies median/mean imputation

        Removes outliers using the IQR method
```

```
    Visualizations Created:

        Line plot: Selling prices over the years

        Scatter plots:
            • Engine vs Selling Price
            • Max Power vs Selling Price

        Count plots:
            • Fuel type distribution
            • Transmission type distribution
            • Owner type distribution

        Bar charts:
            • Seller type vs Transmission (stacked)
            • Ownership distribution (horizontal)

        Pair plot: Relationships between numerical features

        Heatmap: Correlation matrix

        Histograms: Selling price and mileage distributions

        Boxplots: Distribution of numerical columns

        Violin plots: Price vs Seller Type & Owner Type

        Density plot: KM Driven vs Selling Price
```

## Note:
Each plot is displayed in its own window.
Close a plot window to proceed to the next visualization.
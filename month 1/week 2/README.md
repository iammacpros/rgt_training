# Car Data Analysis and Visualization

## Summary

This repository contains two Python scripts for automotive data analysis and visualization:

1. `basic_data_visualizations.py` – A comprehensive data cleaning and visualization script that loads a car dataset, handles missing values, and creates multiple visualization plots (line plots, scatter plots, bar charts, histograms, heatmaps, and boxplots) to analyze car selling prices and features.

2. `car_prices_histogram.py` – A focused script that loads the same car dataset and creates a histogram visualization specifically showing the distribution of car selling prices.

Both scripts demonstrate data cleaning techniques and various visualization methods using Python's data science libraries.

## Dataset Overview
This dataset contains various features related to cars, including the year of manufacture, selling price, kilometers driven, fuel type, seller type, transmission type, number of previous owners, mileage, and engine specifications. These attributes provide valuable insights into the factors influencing car prices and can be used to develop predictive models for estimating the selling price of cars.

The scripts expect a CSV file with at least these columns:

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

## Tool Used
* python 3.x
* pandas
* seaborn
* matplotlib

## Steps to run both files

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
    pip install pandas seaborn matplotlib
```

### 4. Prepare the dataset
> Ensure you have the car dataset file in the correct location:
```
    month 1/week 2/data/cardekho.csv
```
> If you don't have the actual dataset, you can:
    > 1. Download a car dataset from [Kaggle](https://www.kaggle.com/datasets/sukhmandeepsinghbrar/car-price-prediction-dataset)
    > 2. Update the file paths in the scripts to match your dataset location

### 5. Run the car prices histogram script
```
    python car_prices_histogram.py
```
> What it does:
```
* Loads the car dataset from cardekho.csv
* Creates a histogram of car selling prices
* Displays the distribution of car prices with 50 bins
* Shows grid lines for better readability
```

### 6. Run the comprehensive visualization script
```
    python basic_data_visualizations.py
```
> What it does:
```
* Data Cleaning:
  - Handles missing values in 'seats', 'engine', 'max_power', and 'mileage' columns
  - Uses median/mode/mean imputation based on data characteristics
  - Converts 'max_power' to numeric type

* Visualizations Created:
  - Line plot: Selling prices over the years
  - Scatter plots: Engine size vs selling price, Max power vs selling price
  - Count plots: Fuel type distribution, Transmission type distribution
  - Bar charts: Seller type vs transmission, Car ownership distribution
  - Pair plot: Relationships between all numerical features
  - Heatmap: Correlation matrix of numerical features
  - Histogram: Distribution of mileage values
  - Boxplots: Distribution of all numerical columns
```

## Note: 
Both scripts will display multiple matplotlib windows. Close each plot window to see the next one.

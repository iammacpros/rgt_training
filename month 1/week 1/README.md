# CSV Data Cleaning, Analysis & Fibonacci Sequence Squared

## Summary
This repository contains two Python scripts for different purposes:

1. csv_data_cleaning_analysis.py – A comprehensive data cleaning and analysis script that loads a CSV file, handles missing values, performs statistical analysis using NumPy, and calculates advanced metrics like covariance and eigenvalues.

2. numbers_squared.py – A simple mathematical script that generates a Fibonacci sequence of a given length and returns a list of the squared values of that sequence.

Both scripts demonstrate core Python programming, data manipulation, and mathematical operations.

## Tools Used
 * Python 3.x
 * pandas
 * numpy

## Steps to run both files

### 1. Clone / Downlaoad the Project
> Download the project folder and open a terminal in the root directory:

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
    pip install pandas numpy
```

### 4. Run the first exercise
```
    python numbers_squared.py
```
> What it does:
```
    * Generates the first 20 Fibonacci numbers
    * Prints the Fibonacci sequence
    * Squares each number in the sequence
    * Prints the squared values
```

### 5. Run the second script
> Make sure this file exists

 ```
    data/generated_data.csv
 ```
 
> Run the file:
 ``` 
    python csv_data_cleaning_analysis.py
 ```

> What it does:
 ```
    * Loads the dataset
    * Displays metadata and summary statistics
    * Handles missing values (mean imputation for numeric, mode for categorical)
    * Converts numeric data to a NumPy array
    * Performs statistical calculations (mean, median, std, covariance, eigenvalues)
    * Prints results to the console
 ```
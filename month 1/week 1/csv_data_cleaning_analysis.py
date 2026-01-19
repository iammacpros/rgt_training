# Importing Libraries
import pandas as pd

# Loading dataset
dataset = pd.read_csv(r"month 1\week 1\data\generated_data.csv")


def wrangle(data):

    # Importing Libraries
    # import pandas as pd
    import numpy as np

    # # Loading dataset
    # data = pd.read_csv("generated_data.csv")

    # Displaying first few rows in the data
    data.head()

    # Displaying information about the dataset
    data.info()

    # Displaying summary statistics about data
    print(data.describe())

    # Total rows and Total columns
    print("Rows: ", data.shape[0])

    print("Columns: ", data.shape[1])

    # checking for missing values
    print(data.isnull().sum())

    # Filling missing values
    numeric_cols = data.select_dtypes(include= [np.number]).columns
    print("numeric columns in dataset: ", numeric_cols)

    categorical_cols = data.select_dtypes(exclude= [np.number]).columns
    print("categorical columns in dataset: ",categorical_cols)

    ## filling missing values of numerical columns  by imputing mean
    data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())

    ## filling missing values of categorical columns  by imputing mode
    data[categorical_cols] = data[categorical_cols].fillna(data[categorical_cols].mode().iloc[0])

    # confirming whether missing values are filled
    print(data.isnull().sum())

    # NUMPY

    # converting numeric columns to numpy array
    numpy_array = data[numeric_cols].to_numpy()
    print(numpy_array[:10])

    # shape of the array
    print("shape of numpy array: ",numpy_array.shape)

    # Calculating mean of array
    numpy_array_mean = np.mean(numpy_array, axis= 0)
    print("mean of numpy array ; ",numpy_array_mean)

    # Calculating mediam of array
    numpy_array_median = np.median(numpy_array, axis= 0)
    print("median of numpy array: ",numpy_array_median)

    # Calculating standard deviation of array
    numpy_array_std = np.std(numpy_array, axis= 0)
    print("standard deviation of numpy array: ",numpy_array_std)

    # Values above the mean of a selected column
    column = numpy_array[:, 4]
    column_mean = np.mean(column)

    above_col_mean = column[column > column_mean]
    print(above_col_mean[:10])

    # Calculating covariance
    numpy_array_cov = np.cov(numpy_array, rowvar= False)
    print("covariance of numpy array: ",numpy_array_cov)

    # Calculating eigen values
    eigenvalues, eigenvectors = np.linalg.eig(numpy_array_cov)
    print(eigenvalues)




## Testing
wrangle(dataset)

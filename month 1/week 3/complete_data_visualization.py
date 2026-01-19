# importing libraries

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Loading Dataset

df = pd.read_csv("month 1\week 3\data\cardekho.csv")

df.head()
df.tail(10)
df.info()
df.isnull().sum()

# Data Cleaning
df['seats'] = df['seats'].fillna(df['seats'].median())
df['engine'] = df['engine'].fillna(df['engine'].median())
df['max_power'] = pd.to_numeric(df['max_power'], errors= 'coerce')
df['max_power'] = df['max_power'].fillna(df['max_power'].mean().round(2))
df['mileage(km/ltr/kg)'] = df['mileage(km/ltr/kg)'].fillna(df['mileage(km/ltr/kg)'].median())
df.isnull().sum()

# Inspecting and removing Outliers
numeric_cols = df.select_dtypes(include= [np.number]).columns
sns.boxplot(data = df[numeric_cols])
plt.title('Boxplots for All Numeric Columns')


## Removing outliers
df_new = df.copy()

for column in numeric_cols:
    Q1 = df_new[column].quantile(0.25)
    Q3 = df_new[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
df_new = df_new[(df_new[column] >= lower_bound) & (df_new[column] <= upper_bound)]

df = df_new


#data visualization

# histogram of selling price
plt.figure(figsize=(15, 10))
sns.histplot(df['selling_price'], bins=30, kde=True)
plt.title('Distribution of Selling Prices')
plt.xlabel('Selling Price')
plt.ylabel('Frequency')
plt.show()

# line plot on year vs selling price
plt.figure(figsize=(15, 10))
sns.lineplot(df, x= 'year', y = 'selling_price')
plt.title(' Selling Prices over the years')
plt.ylabel('Price (in millions)')
plt.xlabel('Years')
plt.show()

# scatter plot on engine vs selling price
plt.figure(figsize=(15, 10))
sns.scatterplot(data=df, x='engine', y='selling_price')
plt.title('Engine Size vs Selling Price')
plt.xlabel('Engine Capacity (CC)')
plt.ylabel('Selling Price')
plt.show()

# scatter plot on max power vs selling price
plt.figure(figsize=(15, 10))
sns.scatterplot(data=df, x='max_power', y='selling_price')
plt.title('Max Power vs Selling Price')
plt.xlabel('Max Power (BHP)')
plt.ylabel('Selling Price')
plt.show()

# count plot on fuel
plt.figure(figsize=(15, 10))
sns.countplot(df, x= 'fuel')
plt.title('Distribution of Fuel Types')
plt.xlabel('Fuel Type')
plt.ylabel('Number of Cars')
plt.show()

# stacked bar plot on seller type vs transmission
plt.figure(figsize=(15, 10))
crosstab = pd.crosstab(df['seller_type'], df['transmission'])
crosstab.plot(kind= 'bar', stacked= True)
plt.title('Seller Type vs Transmission Type')
plt.xlabel('Seller Type')
plt.ylabel('Number of Cars')
plt.show()

# horizontal bar plot on owner
plt.figure(figsize=(15, 10))
df['owner'].value_counts().plot(kind= 'barh')
plt.title('Car Ownership Distribution')
plt.xlabel('Number of Cars')
plt.ylabel('Owner Type')
plt.show()

# count plot on transmission
plt.figure(figsize=(15, 10))
sns.countplot(df, x= 'transmission', hue = 'transmission')
plt.title('Transmission Type Distribution')
plt.xlabel('Transmission Type')
plt.ylabel('Number of Cars')
plt.show()

# pair plot
numericals = ["mileage(km/ltr/kg)", "engine", "max_power", "seats", "km_driven", "selling_price"]
sns.pairplot(df, vars=numericals)
plt.suptitle('Pairwise Relationships Between Numerical Features', y=1.02)
plt.show()

# heatmap
plt.figure(figsize=(15, 10))
corr = df.corr(numeric_only= True)
sns.heatmap(corr, annot= True)
plt.title('Correlation Heatmap of Numerical Features')
plt.xlabel('Features')
plt.ylabel('Features')
plt.show()

#histogram of mileage
plt.figure(figsize=(15, 10))
sns.histplot(df, x= 'mileage(km/ltr/kg)', bins= 50, kde= True)
plt.title('Distribution of Mileage')
plt.xlabel('Mileage (km/ltr/kg)')
plt.ylabel('Frequency')
plt.show()

# boxplot of all numerical columns
plt.figure(figsize=(15, 10))
numericals = ["mileage(km/ltr/kg)", "engine", "max_power", "seats", "km_driven", "selling_price"]
sns.boxplot(data=df[numericals])
plt.title('Boxplots for All Numeric Columns')
plt.xlabel('Numerical Features')
plt.ylabel('Value Distribution')
plt.show()

# boxplot of selling price vs fuel
plt.figure(figsize=(15, 10))
sns.boxplot(data=df, x='fuel', y='selling_price')
plt.title('Selling Price Distribution by Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Selling Price')
plt.show()

# violin plot of selling price vs seller type
plt.figure(figsize=(15, 10))
sns.violinplot(data=df, x='seller_type', y='selling_price')
plt.title('Selling Price Distribution by Seller Type')
plt.xlabel('Seller Type')
plt.ylabel('Selling Price')
plt.show()

# violin plot of selling price vs owner
plt.figure(figsize=(15, 10))
sns.violinplot(data=df, x='owner', y='selling_price')
plt.title('Selling Price Distribution by Owner Type')
plt.xlabel('Owner Type')
plt.ylabel('Selling Price')
plt.show()

# density plot of km driven vs selling price
plt.figure(figsize=(15, 10))
sns.kdeplot(data=df, x='km_driven', y='selling_price', fill=True)
plt.title('Density of KM Driven vs Selling Price')
plt.xlabel('Kilometers Driven')
plt.ylabel('Selling Price')
plt.show()

# line plot of average selling price over the years
plt.figure(figsize=(15, 10))
yearly_avg = df.groupby('year')['selling_price'].mean()
sns.lineplot(x=yearly_avg.index, y=yearly_avg.values)
plt.title('Average Selling Price Over the Years')
plt.xlabel('Year')
plt.ylabel('Average Selling Price')
plt.show()

# count plot on owner
plt.figure(figsize=(15, 10))
sns.countplot(data=df, x='owner')
plt.title('Owner Type Distribution')
plt.xlabel('Owner Type')
plt.ylabel('Number of Cars')
plt.show()




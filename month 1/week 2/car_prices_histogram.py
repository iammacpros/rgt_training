# Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Loading dataset
df = pd.read_csv("month 1\week 2\data\cardekho.csv")

def plot_price_histogram(data):
    plt.figure(figsize=(10,6))
    plt.hist(data['selling_price'], bins = 50, color = 'blue', edgecolor = 'black', alpha=0.7)
    plt.title('Distribution of Car Prices')
    plt.xlabel('Prices')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

plot_price_histogram(df)
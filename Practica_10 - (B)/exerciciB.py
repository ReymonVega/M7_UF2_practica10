import pandas as pd
import matplotlib.pyplot as plt

def total_population(df):
    return df.groupby('City')['Population'].sum()

def density_km2(df):
    return df.groupby('City')['Density KM2'].sum()

def density_m2(df):
    return df.groupby('City')['Density  M2'].sum()

def plot_pie(df, column):
    data = df.groupby('City')[column].sum()
    data.plot(kind='pie', autopct='%.1f%%', legend=True)
    plt.axis('equal')
    plt.show()
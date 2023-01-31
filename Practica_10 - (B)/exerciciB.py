import pandas as pd

def population_by_city(df):
    population = df.groupby('City')['Population'].sum().sort_values(ascending=False)
    return population

def density_km2_by_city(df):
    density_km2 = df.groupby('City')['Density KM2'].mean().sort_values(ascending=False)
    return density_km2

def density_m2_by_city(df):
    density_m2 = df.groupby('City')['Density M2'].mean().sort_values(ascending=False)
    return density_m2
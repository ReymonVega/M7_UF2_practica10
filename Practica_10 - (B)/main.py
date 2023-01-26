import pandas as pd
import matplotlib.pyplot as plt
from exerciciB import population_by_city, density_km2_by_city, density_m2_by_city

def main():
    # Cargar el archivo .csv en un DataFrame
    df = pd.read_csv('parteB.csv')

    # Obtener las 10 ciudades con mayor población
    top_10_cities = df.sort_values(by='Population', ascending=False).head(10)


    # Mostrar la población total por ciudad
    population = population_by_city(top_10_cities)
    population.plot.pie(autopct='%1.1f%%')
    plt.title('Población total por ciudad')
    # plt.show()
    print(population)

    # Mostrar la densidad por KM2 por ciudad
    density_km2 = density_km2_by_city(top_10_cities)
    density_km2.plot.pie(autopct='%1.1f%%')
    plt.title('Densidad por KM2 por ciudad')
    # plt.show()

    # Mostrar la densidad por M2 por ciudad
    density_m2 = density_m2_by_city(top_10_cities)
    density_m2.plot.pie(autopct='%1.1f%%')
    plt.title('Densidad por M2 por ciudad')
    # plt.show()

main()
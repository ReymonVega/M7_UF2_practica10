import pandas as pd
import exerciciB as f

df = pd.read_csv('List of cities proper by population density11.csv')

def main():
    total_pop = f.total_population(df)
    print(total_pop)
    f.plot_pie(total_pop, 'Population')

    density_km = f.density_km2(df)
    print(density_km)
    f.plot_pie(density_km, 'Density KM2')

    density_m = f.density_m2(df)
    print(density_m)
    f.plot_pie(density_m, 'Density  M2')

if __name__ == "__main__":
    main()
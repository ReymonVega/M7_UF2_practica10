import matplotlib.pyplot as plt
import exerciciA as ex
def main(df):
    countries = ['Afghanistan', 'China', 'Italy', 'Spain', 'France',
                 'Germany', 'Russia', 'United Kingdom', 'Brazil', 'India']


    # Llamamos a la primera función
    cases_per_month = ex.casosTotalPorMes(df, countries)
    # Resultados
    plt.figure()
    for country in countries:
        cases_per_month[cases_per_month['location'] == country].plot(x='Month', y='total_cases', label=country)
    plt.legend()
    plt.show()

    # Llamamos a la segunda función
    deaths_per_month_city = ex.muertesTotalesPorCiudad(df, countries)
    # Resultados
    plt.figure()
    for country in countries:
        deaths_per_month_city[deaths_per_month_city['location'] == country].plot(x='Month', y='total_deaths', label=country)
    plt.legend()
    plt.show()

    # Llamamos a la tercera función
    deaths_per_month_country = ex.numerosDeMuertesPais(df, countries)
    # Resultados
    plt.figure()
    for country in countries:
        deaths_per_month_country[deaths_per_month_country['location'] == country].plot(x='Month', y='reproduction_rate', label=country)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    df = ex.read_data("df_covid19_countries.csv")
    main(df)
import pandas as pd


# Función para leer los Datos
def read_data(data:str):
    df = pd.read_csv(data, parse_dates=['date'])
    df['Month'] = df['date'].dt.month
    return df

# Function 1: Cantidad de casos por mes Paises
# 1 función que muestre, por país (coger 10 países), la cantidad de casos total por mes
def casosTotalPorMes(df, countries):
    cases_per_month = df.groupby(['location', 'Month'])['total_cases'].sum().reset_index()
    cases_per_month = cases_per_month[cases_per_month['location'].isin(countries)]
    return cases_per_month

# Function 2: Total deaths per month by city
# 1 función que muestre, las muertes totales por mes por ciudad (coger 10 ciudades)
def muertesTotalesPorCiudad(df, countries):
    deaths_per_month = df.groupby(['location', 'Month'])['total_deaths'].sum().reset_index()
    deaths_per_month = deaths_per_month[deaths_per_month['location'].isin(countries)]
    return deaths_per_month

# Function 3: Number of deaths per month per country
# 1 función que muestre la “reproduction rate” por mes por país (coger 10 países)
def numerosDeMuertesPais(df, countries):
    deaths_per_month = df.groupby(['location', 'Month'])['reproduction_rate'].sum().reset_index()
    deaths_per_month = deaths_per_month[deaths_per_month['location'].isin(countries)]
    return deaths_per_month
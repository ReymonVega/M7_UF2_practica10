
import pandas as pd

# 1 funció que mostri, per país (agafar 10 països), la quantitat de casos total per mes

def perPais():
    df = pd.read_csv('df_covid19_countries.csv', header=0)

    contagios = df['total_cases']
    contagios_maximos = contagios.max()
    print(contagios_maximos)

perPais()
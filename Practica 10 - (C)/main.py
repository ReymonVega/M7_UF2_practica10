import pandas as pd
import matplotlib.pyplot as plt

# Cargar el csv
df = pd.read_csv("test.csv")


samples = [3, 13, 34, 56, 70, 85, 110, 120, 210, 400]
df = df.loc[samples]

# Funcion POT CLOCK
def plot_clock_speed(df):
    clock_speeds = df[["id", "clock_speed"]].set_index("id")
    clock_speeds.plot(kind="bar", legend=False)
    plt.xlabel("Mobile ID")
    plt.ylabel("Clock Speed")
    plt.show()

# Función para trazar megapíxeles por móvil (ID)
def plot_megapixels(df):
    megapixels = df[["id", "px_height", "px_width"]].set_index("id")
    megapixels["megapixels"] = megapixels["px_height"] * megapixels["px_width"]
    megapixels = megapixels[["megapixels"]]
    megapixels.plot(kind="bar", legend=False)
    plt.xlabel("Mobile ID")
    plt.ylabel("Megapixels")
    plt.show()

# Función para trazar la energía de la batería por móvil (ID)
def plot_battery_power(df):
    battery_power = df[["id", "battery_power"]].set_index("id")
    battery_power.plot(kind="bar", legend=False)
    plt.xlabel("Mobile ID")
    plt.ylabel("Battery Power")
    plt.show()

# Función principal para llamar a las otras tres funciones
def plot_all(df):
    plot_clock_speed(df)
    plot_megapixels(df)
    plot_battery_power(df)

plot_all(df)
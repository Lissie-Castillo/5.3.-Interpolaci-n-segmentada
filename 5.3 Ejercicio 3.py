import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Datos experimentales del vehículo
velocidad = np.array([40, 60, 80, 100, 120, 140])  # Velocidad (km/h)
consumo = np.array([6.5, 5.8, 5.5, 5.7, 6.2, 7.0])  # Consumo (L/100 km)

# Interpolaciones
lineal_interp = interp1d(velocidad, consumo, kind='linear')
cuadratica_interp = interp1d(velocidad, consumo, kind='quadratic')
cubica_interp = interp1d(velocidad, consumo, kind='cubic')

# Puntos intermedios donde evaluar
puntos_eval = np.arange(40, 141, 10)

print("Comparación de consumo interpolado en velocidades intermedias:")
print(f"{'Velocidad (km/h)':<20}{'Lineal (L/100km)':>20}{'Cuadrática':>15}{'Cúbica':>15}")
for v in puntos_eval:
    y_lin = lineal_interp(v)
    y_quad = cuadratica_interp(v)
    y_cubic = cubica_interp(v)
    print(f"{v:<20.1f}{y_lin:>20.2f}{y_quad:>15.2f}{y_cubic:>15.2f}")

# Para graficar
x_vals = np.linspace(min(velocidad), max(velocidad), 300)
y_lineal = lineal_interp(x_vals)
y_cuadratica = cuadratica_interp(x_vals)
y_cubica = cubica_interp(x_vals)

# Gráfica
plt.figure(figsize=(9, 6))
plt.scatter(velocidad, consumo, color='red', label='Datos experimentales')
plt.plot(x_vals, y_lineal, '--', color='blue', label='Interpolación lineal')
plt.plot(x_vals, y_cuadratica, '-.', color='green', label='Interpolación cuadrática')
plt.plot(x_vals, y_cubica, '-', color='purple', label='Interpolación cúbica')
plt.xlabel('Velocidad del vehículo (km/h)')
plt.ylabel('Consumo de combustible (L/100 km)')
plt.title('Interpolación del Consumo de Combustible en función de la Velocidad')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
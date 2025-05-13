import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Datos experimentales del motor
distancia = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])  # Distancia (cm)
temperatura = np.array([250, 220, 180, 150, 130, 125])  # Temperatura (°C)

# Interpolaciones
lineal_interp = interp1d(distancia, temperatura, kind='linear')
cuadratica_interp = interp1d(distancia, temperatura, kind='quadratic')
cubica_interp = interp1d(distancia, temperatura, kind='cubic')

# Puntos intermedios donde evaluar
puntos_eval = np.arange(0.0, 5.1, 0.5)

print("Comparación de temperatura interpolada en puntos intermedios:")
print(f"{'Distancia (cm)':<15}{'Lineal (°C)':>15}{'Cuadrática (°C)':>20}{'Cúbica (°C)':>15}")
for x in puntos_eval:
    y_lin = lineal_interp(x)
    y_quad = cuadratica_interp(x)
    y_cubic = cubica_interp(x)
    print(f"{x:<15.1f}{y_lin:>15.2f}{y_quad:>20.2f}{y_cubic:>15.2f}")

# Para graficar
x_vals = np.linspace(min(distancia), max(distancia), 200)
y_lineal = lineal_interp(x_vals)
y_cuadratica = cuadratica_interp(x_vals)
y_cubica = cubica_interp(x_vals)

# Gráfica
plt.figure(figsize=(9, 6))
plt.scatter(distancia, temperatura, color='red', label='Datos experimentales')
plt.plot(x_vals, y_lineal, '--', color='blue', label='Interpolación lineal')
plt.plot(x_vals, y_cuadratica, '-.', color='green', label='Interpolación cuadrática')
plt.plot(x_vals, y_cubica, '-', color='purple', label='Interpolación cúbica')
plt.xlabel('Distancia en el cilindro (cm)')
plt.ylabel('Temperatura (°C)')
plt.title('Interpolación Segmentada de Temperatura en un Motor')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
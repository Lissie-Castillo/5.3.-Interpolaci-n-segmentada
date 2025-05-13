import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Datos de la viga
longitud = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])  # Longitud (m)
deflexion = np.array([0.0, -1.5, -2.8, -3.0, -2.7, -2.0])  # Deflexión (mm)

# Interpolaciones
lineal_interp = interp1d(longitud, deflexion, kind='linear')
cuadratica_interp = interp1d(longitud, deflexion, kind='quadratic')
cubica_interp = interp1d(longitud, deflexion, kind='cubic')

# Puntos intermedios donde comparar resultados
puntos_eval = np.arange(0.0, 5.1, 0.5)

print("Comparación de deflexión interpolada en puntos intermedios:")
print(f"{'Longitud (m)':<12}{'Lineal':>12}{'Cuadrática':>15}{'Cúbica':>12}")
for x in puntos_eval:
    y_lin = lineal_interp(x)
    y_quad = cuadratica_interp(x)
    y_cubic = cubica_interp(x)
    print(f"{x:<12.1f}{y_lin:>12.3f}{y_quad:>15.3f}{y_cubic:>12.3f}")

# Para graficar
x_vals = np.linspace(min(longitud), max(longitud), 200)
y_lineal = lineal_interp(x_vals)
y_cuadratica = cuadratica_interp(x_vals)
y_cubica = cubica_interp(x_vals)

# Gráfica
plt.figure(figsize=(9, 6))
plt.scatter(longitud, deflexion, color='red', label='Datos experimentales')
plt.plot(x_vals, y_lineal, '--', color='blue', label='Interpolación lineal')
plt.plot(x_vals, y_cuadratica, '-.', color='green', label='Interpolación cuadrática')
plt.plot(x_vals, y_cubica, '-', color='purple', label='Interpolación cúbica')
plt.xlabel('Longitud (m)')
plt.ylabel('Deflexión (mm)')
plt.title('Interpolación Segmentada de la Deflexión de una Viga')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

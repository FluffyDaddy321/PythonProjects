
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import Rbf

# Исходные анные
X = np.array([1, 2, 4, 5, 7])
y = np.array([0, 1, 22, 0, 8])

# Определение радиуса
epsilon = 2

# Построение интерполятора с использованием RBF
rbf_interpolator = Rbf(X, y, function='multiquadric', epsilon=epsilon)

# Вычисление значения функции в точке x* = 1.5
x_star = 1.5
y_star = rbf_interpolator(x_star)

# Печать результата
print(f"Значение интерполированной функции в точке x* = {x_star}: {y_star}")

# Построение графика интерполяции
x_vals = np.linspace(1, 7, 100)
y_vals = rbf_interpolator(x_vals)

plt.plot(x_vals, y_vals, label='Интерполированный RBF')
plt.grid(True)
plt.scatter(X, y, color='blue', label='Исходные значении')
plt.title('Интерполяция с помощью RBF')
plt.legend()
plt.show()


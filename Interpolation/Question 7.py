import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from scipy.optimize import fsolve

# Исходные данные
x = np.array([1, 2, 3, 5])
y = np.array([-6, 0, 7, -6])
# Построение кубического сплайна
cubic_spline = CubicSpline(x, y)

# Функция для поиска корней
def find_roots(spline, x_min, x_max, num_intervals=100):
    roots = []
    interval_size = (x_max - x_min) / num_intervals
    for i in range(num_intervals):
        x_start = x_min + i * interval_size
        x_end = x_start + interval_size
        root = fsolve(spline, (x_start + x_end) / 2)
        if x_start <= root <= x_end:
            roots.append(root[0])
    return np.unique(roots)

# Нахождение корней сплайна
roots = find_roots(cubic_spline, x[0], x[-1])
print("Корни B-сплайна 3-й степени:", roots)

# Создаем массив x для построения сплайна
x_plot = np.linspace(x[0], x[-1], 100)

# Вычисляем значения сплайна
y_plot = cubic_spline(x_plot)

# Построение графика
plt.scatter(x, y, color='blue', label='SOURCE DATA')
plt.grid (True)
plt.plot(x_plot, y_plot, label='Cubic Spline')
plt.scatter(roots, cubic_spline(roots), color='red', label='Roots of the spline')
plt.legend()
plt.xlabel('X')
plt.ylabel('')
plt.title('Кубический сплайн и корни')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splrep, splev
# Исходные данные
x = np.array([1, 2, 4, 5, 7])
y = np.array([0, 1, 22, 0, 8])
# Создание кубических B-сплайнов

tck = splrep(x, y, k=3)
# Вычисление значений сплайнов в точках x*=1.5 и x*=8.5

x_val1 = 1.5
x_val2 = 8.5
y_val1 = splev(x_val1, tck)
y_val2 = splev(x_val2, tck, ext=0)  # Используем ext=0 для продолжения сплайна за пределами интервала данных
print(f"Значение сплайна в точке x* = {x_val1}: y* = {y_val1:.2f}")
print(f"Значение сплайна в точке x* = {x_val2}: y* = {y_val2:.2f}")
# Вычисление первой производной
dy_star_1 = splev(x_val1, tck, der=1)
dy_star_2 = splev(x_val2, tck, der=1, ext=0)  # Используем ext=0 для продолжения сплайна за пределами интервала данных
# Вычисление второй производной
d2y_star_1 = splev(x_val1, tck, der=2)
d2y_star_2 = splev(x_val2, tck, der=2, ext=0)  # Используем ext=0 для продолжения сплайна за пределами интервала данных
print(f"Значение первой производной в точке x* = {x_val1}: dy/dx = {dy_star_1:.2f}")
print(f"Значение первой производной в точке x* = {x_val2}: dy/dx = {dy_star_2:.2f}")
print(f"Значение второй производной в точке x* = {x_val1}: d2y/dx2 = {d2y_star_1:.2f}")
print(f"Значение второй производной в точке x* = {x_val2}: d2y/dx2 = {d2y_star_2:.2f}")
# Создаем массив x для построения сплайна, включая точку x_star_2
x_plot = np.linspace(min(x), x_val2, 100)
# Вычисляем значения сплайна
y_plot = splev(x_plot, tck, ext=0)  # Используем ext=0 для продолжения сплайна за пределами интервала данных

# Построение графика
plt.scatter(x, y, color='red', label='Исходные данные')
plt.plot(x_plot, y_plot, label='Кубический B-сплайн')
plt.scatter([x_val1, x_val2], [y_val1, y_val2], color='green', label='Значения в x*')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Кубический B-сплайн')
plt.show()

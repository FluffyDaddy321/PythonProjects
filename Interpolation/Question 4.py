import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
#Вводим данных
x = np.array([1, 0.25, 6, 7])
y = np.array([-1, 6, 18, 0])

#Создание функций с помощью библммотеку interpld
quadratic_interp = interp1d(x, y, kind='quadratic')
cubic_interp = interp1d(x, y, kind='cubic')

#Вычисление значений функции в точках x=3, 4 и x=4.4
x_new = np.array([3, 4, 4.4])
# Вычисление значений с использованием квадратичной интерполяции
y_quadratic = quadratic_interp(x_new)
# Вычисление значений с использованием кубической интерполяции
y_cubic = cubic_interp(x_new)
print("В точках x=3, 4, 4.4 с квадратичной интерпояции:")
print(y_quadratic)
print("В точках x=3, 4, 4.4 с кубической интерполяции:")
print(y_cubic)
# Создание графика
# Создание сетки для построения графика
x_plot = np.linspace(min(x), max(x), 100)
# Вычисление значений интерполяции на сетке
y_quadratic_plot = quadratic_interp(x_plot)
y_cubic_plot = cubic_interp(x_plot)
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='red', label='Исходные данные')
plt.plot(x_plot, y_quadratic_plot, label='Квадратичная интерполяция')
plt.plot(x_plot, y_cubic_plot, label='Кубическая интерполяция')
#В которых вычислялись значения
plt.scatter(x_new, y_quadratic, color='green', label='Значения (квадратичная)')
plt.scatter(x_new, y_cubic, color='orange', label='Значения (кубическая)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Интерполяция функции')
plt.legend()
plt.grid(True)
plt.show()

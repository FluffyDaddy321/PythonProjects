import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

#Вводим данные:
x = np.array([1, 2, 4])
y = np.array([4, 7, 25])

# Создание кубического сплайна с естественными граничными условиями
spline = CubicSpline(x, y, bc_type='natural')
# Создаем массив x для построения сплайна
x_plot = np.linspace(min(x), max(x), 100)
# Вычисляем значения сплайна
y_plot = spline(x_plot)
# Построение графика
plt.scatter(x, y, color='green', label='Source Data')
plt.plot(x_plot, y_plot, label='Cubic Spline')
plt.grid()
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Spline')
plt.show()
# Коэффициенты сплайна на интервалах
coeffs = spline.c

# Уравнения сплайнов на интервалах [1, 2] и [2, 4]
for i in range(len(x) - 1):
  a, b, c, d = coeffs[:, i] 
  # Выводим коэфф. 
  print(f"Уравнение сплайна на интервале [{x[i]}, {x[i+1]}]:")
  print(f"y = {a:.4f}(x - {x[i]})^3 + {b:.4f}(x - {x[i]})^2 + {c:.4f}(x - {x[i]}) + {d:.4f}")

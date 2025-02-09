import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splrep, splev
# Вводим данные
x = np.array([1, 2.7, 3, 4, 5])
y = np.array([-2, 1, 0, 9, 7])


# Сортировка точек по x
sorted_indices = np.argsort(x)
x_sorted = x[sorted_indices]
y_sorted = y[sorted_indices]

# Создание B-сплайнов 2-й и 3-й степени 
tck_2 = splrep(x_sorted, y_sorted, k=2)  
tck_3 = splrep(x_sorted, y_sorted, k=3)  
# Для построения сплайнов
x_plot = np.linspace(min(x_sorted), max(x_sorted), 100)

y_plot_2 = splev(x_plot, tck_2)
y_plot_3 = splev(x_plot, tck_3)
# Построение графиков
plt.scatter(x_sorted, y_sorted, color='blue', label='Исходные данные')
plt.plot(x_plot, y_plot_2, label='B-сплайн 2-й степени')
plt.plot(x_plot, y_plot_3, label='B-сплайн 3-й степени')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('B-сплайны II и III степени')
plt.show()

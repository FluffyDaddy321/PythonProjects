import numpy as np
#Вводим исходные данные
x_values = np.array([-1, 1, 3, 4])
y_values = np.array([8, 9, 6, 7])
#Предсатавим матрицу коэффициентов для уравнения
A = np.vstack([x_values**3,x_values**2,x_values, np.ones(len(x_values))]).T
#Находим и печатаем решение
coeff = np.linalg.solve(A, y_values)
print("Coefficients of the polynomials:")
print(coeff)
#Для вычисления значения полинома
def polynomial(x):
    return coeff[0]*x**3 + coeff[1]*x**2 + coeff[2]*x + coeff[3]
#Нахождение решения в заданных точках
x_data = np.array([-2,0.5])
y_data = polynomial(x_data)

print("\n At the points x = [-2, 0.5], the values are:")
print (y_data)
import numpy as np
from scipy.optimize import root
import matplotlib.pyplot as plt

def equation_find(x):
    c1,c2,c3 = x
    eq1 = c1*np.log(2) + 4*c2*np.exp(-1) + 8*c3 - 4
    eq2 = c1*np.log(3) + 9*c2*np.exp(-1.5) + 27*c3 - 0
    eq3 = c1*np.log(12) + 144*c2*np.exp(-6) + 1728*c3 -24
    return [eq1, eq2,eq3]
    
x0 = np.array([1,1,1])

solution = root(equation_find,x0)
c1,c2,c3 = solution.x

def func(x):
    return c1*np.log(x) + c2*x**2*np.exp(-0.5*x) + c3*x**3

x_values = np.array([2,3,12])
y_values = np.array([4,0,24])


x_plot = np.linspace(1, 20, 100)
y_plot = func(x_plot)

#Строим графику
plt.plot(x_values, y_values, 'ob', label = "Исходные данные")
plt.plot(x_plot ,y_plot, '-', label = "Аппроксимация")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

print ("Коэффициенты: ")
print (c1, c2, c3)
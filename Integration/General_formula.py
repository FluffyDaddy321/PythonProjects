import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson

#Rectangular method
def rectangular_rule(f_values, dx, method = "midpoint"):
    if method == "left":
        return np.sum(f_values[:-1])*dx
    elif method == "right":
        return np.sum(f_values[1:])*dx
    elif method == "midpoint":
        midpoints = (f_values[:-1]+f_values[1:])/2
        return np.sum(midpoints)*dx
    else:
        raise ValueError("Method must be 'left','right' or 'midpoint'")
    
#Trapezium rule

def trapezium_rule(f_values,dx):
    return (dx/2)*(f_values[0]+2*np.sum(f_values[1:-1]+f_values[-1]))

a = 7
b = 14.1
n = 10
x_values = np.linspace(a,b,n+1)
f_values = np.sqrt((x_values)**2+9)
dx = (b-a)/n

rect_left = rectangular_rule(f_values,dx,method="left")
rect_right = rectangular_rule(f_values,dx,method="right")
rect_midpoint = rectangular_rule(f_values,dx,method="midpoint")
trap_result = trapezium_rule(f_values, dx)
simp_result = simpson(f_values, x=x_values)

print("Integration Results:")
print(f"Rectangular Rule(Left):{rect_left:.10f}")
print(f"Rectangular Rule(Right):{rect_right:.10f}")
print(f"Rectangular Rule(Midpoint):{rect_midpoint:.10f}")
print(f"Trapezium Rule:{rect_left:.10f}")
print(f"Simpson's Rule:{rect_left:.10f}")

fig, ax = plt.subplots(figsize= (10,6))
#Our function
x_fine = np.linspace(a,b,11)
ax.plot(x_fine,np.sqrt((x_fine)**2 +9),label = "sqrt((x_values)**2+9)", color="blue")

#Rectangle function
for i in range(n):
    x_start = x_values[i]
    x_end = x_values[i+1]
    y_mid = (f_values[i] + f_values[i+1])/2 
    ax.fill_between([x_start,x_end],[y_mid,y_mid], color = "green", alpha = 0.3, step="mid")
#trapezoid function
for i in range (n):
    ax.plot([x_values[i], x_values[i+1]],[f_values[i],f_values[i+1]], color = "orange",alpha = 0.3)

#Customize the plot
ax.set_title("Integration Approximation Methods")
ax.set_xlabel("X")
ax.set_ylabel("F(X)")
ax.legend(["sqrt((x_values)^2+9)", "Midpoint Rectangles","Trapezium Rule Lines"], loc = "upper right")
plt.grid()
plt.show()
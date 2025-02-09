import numpy as np
import matplotlib as plt
from scipy.integrate import simpson 


def rectangular_rule(f_values, dx, method="midpoint"):
    if method == "left":
        return np.sum(f_values[:-1]) * dx
    elif method == "right":
        return np.sum(f_values[1:]) * dx
    elif method == "midpoint":
        midpoints = (f_values[:-1] + f_values[1:]) / 2
        return np.sum(midpoints) * dx
    else:
        raise ValueError("Method must be 'left', 'right', or 'midpoint'.")

def trapezium_rule(f_values, dx):

    return (dx / 2) * (f_values[0] + 2 * np.sum(f_values[1:-1]) + f_values[-1])
 # Define the function and interval
a = 6              # Lower limit
b = 11.1           # Upper limit
n = 10              # Number of intervals
x_values = np.linspace(a, b, n + 1)  # Equally spaced x points
f_values = [7.61577310586391,8.27309494687448,8.93847861775146,9.61024973660935,
10.2871570416709,10.9682496324619, 11.6527936564585,12.3402147469159,13.030057559351,13.7219568575331]       # Function values 
dx = (b - a) / n                    # Step size

# Calculate integrals using different methods
rect_integral_left = rectangular_rule(f_values, dx, method="left")
rect_integral_right = rectangular_rule(f_values, dx, method="right")
rect_integral_midpoint = rectangular_rule(f_values, dx, method="midpoint")
trapezium_integral = trapezium_rule(f_values, dx)
simpsons_integral = simpson(f_values, x=x_values)

# Print results
print("Integration results:")
print(f"Rectangular Rule (Left): {rect_integral_left:.6f}")
print(f"Rectangular Rule (Right): {rect_integral_right:.6f}")
print(f"Rectangular Rule (Midpoint): {rect_integral_midpoint:.6f}")
print(f"Trapezium Rule: {trapezium_integral:.6f}")
print(f"Simpson's Rule: {simpsons_integral:.6f}")
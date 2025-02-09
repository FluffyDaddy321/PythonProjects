import scipy.optimize
import numpy as np
import matplotlib.pyplot as plt

x_values = np.array ([-1, 1, 3, 4])
y_values = np.array ([8, 9, 6, 7])

def polynomial(t, a, b, c, d):
    return a*t**3+b*t**2+c*t+d
def graph(z):
    a = z[0]
    b = z[0]
    c = z[0]
    d = z[0]
    f = np.zeros(4)
    for i in range(len(x_values)):
        f[i] = polynomial(x_values[i],a,b,c,d)-y_values[i]
        return f

z = scipy.optimize.fsolve(graph,[0.267,-1.3,0.2333,9.8])
print ("The solution to the system of equations is: a = %.6f b= %.6f, c = %.6f, d = %.6f "%
       (z[0],z[1],z[2],z[3]))
print("The values of the left part of the first equation are %.12f" %graph(z)[0])
print("The values of the left part of the second equation are %.12f" %graph(z)[1])
print("The values of the left part of the third equation are %.12f" %graph(z)[2])
print("The values of the left part of the fourth equation are %.10f" %graph(z)[3])
print("The equation of the curve Y = (%.6f)x^3 + %.6fx^2+ %.6fx + %.6g" %(z[0],z[1],z[2],z[3]))

p1 = -2; q = polynomial(p1,z[0],z[1],z[2],z[3])
p2 = 0.5; r = polynomial(p2,z[0],z[1],z[2],z[3])

print("The value of the function at point %.1f equals %.6f"% (p1,q))
print("The value of the function at point %.1f equals %.6f"% (p2,r))
fig = plt.figure()
#ax = fig.add_subplot(111)
a1,b1 =  min(x_values), max(x_values)
x1 = np.linspace(a1,b1,10)
plt.grid()
plt.plot(x_values,y_values,'ob',label = "SOURCE DATA")
plt.plot(x1, polynomial(x1,z[0],z[1],z[2],z[3]), linewidth = 1, c = 'k', label = "Approx. curve")
plt.plot(p1,q,"*r",ms = 10, label = "solution 1")
plt.plot(p2,r,"*b",ms = 10, label = "solution 2")
plt.legend()
plt.show()




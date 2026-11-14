# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:
# Noah Castillo
# Alex Alvarez
# Anthony Reyes
# Section: 102 MO2
# Assignment: LAB: Topic 11 (Team)
# Date: 11/13/2026

import numpy as np
import matplotlib.pyplot as plt
# Part 1
x = np.linspace(-2, 2, 100)

yf2 = (1 / (4*2))*x**2
yf6 = (1 / (4*6))*x**2

plt.plot(x,yf2, color='red',linewidth = 2)
plt.plot(x,yf6, color='blue', linewidth = 6)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Parabola plots with varying focal length')
plt.show()
# Part 2
x = np.linspace(-4, 4 , 25)

y = (2*x**3)+(3*x**2)-(11*x)-6
plt.plot(x,y, color= 'yellow', linewidth = 0,marker = "*")
plt.show()
# Part 3
x = np.linspace(-2*(np.pi), 2*(np.pi) , 100)
ysin = np.sin(x)
ycos = np.cos(x)

plt.figure()
plt.title("Plot of cos(x) and sin(x)")
plt.subplot(211)
plt.ylabel("ycos(x)")
plt.plot(x,ycos, color = "red")
plt.legend(loc= "lower right" )

plt.subplot(212)
plt.ylabel("ysin(x)")
plt.plot(x, ysin , color = "black")
plt.legend(loc= "upper right")
plt.tight_layout()
plt.show()

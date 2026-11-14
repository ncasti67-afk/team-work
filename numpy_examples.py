
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
from math import *


# Part created for A
a = np.array([[0 , 1, 2, 3],[4, 5 , 6 , 7],[8, 9, 10, 11]])# Starting array
print(f"A = {a}")


# Part created for B
b = a.flatten() # Makes it from 2D to 1D 
b = b[:8]
b = b.reshape(4, 2)
print(f"B = {b}")

# Part created for C
c = a.flatten()
c = c[:6]
c = c.reshape(3,2)
print(f"C = {c}")

# Part created for D
d = np.array([[ 102  ,164  ,226],[ 294 , 468  ,642],[ 486 , 772 ,1058]])
print(f"D = {d}")

# Part created for D^T
data=  d.transpose()
print(f"D^T = {data}")

# Part created for E
e = np.sqrt(data)/2
print(f"E = {e}")

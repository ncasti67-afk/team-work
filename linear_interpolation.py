from math import *
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Jason Arteaga
# Noah Castillo
# Alex Alvarez
# Anthony Reyes
# Section: 102 MO2
# Assignment: LAB: Topic 2 (Team)
# Date: 9 3 2026

print("Part 1:")
x1 = 10
y1 = 2030
x2 = 55
y2 = 23030
slope=0
slope = (y2-y1)/(x2-x1)
x3 = 25
y = y1 + slope*(x3 -x1)
print("For t =", x3, "minutes, the position p =",y ,"kilometers")
print("Part 2:")
circumference = 2 * pi * 6745
x4=300
print("For t = 300 minutes, the position p =",y1 + slope * (x4 -x1)%circumference, "kilometers")
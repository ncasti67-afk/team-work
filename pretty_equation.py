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
# Date: 9 16 2026

# This program inputs values into the quadratic formula
A,B,C = [int(input(f"Please enter the coefficient {x}: ")) for x in "ABC"]

equation = ""

if A != 0:
    if A == 1:
        equation += "x^2"
    elif A == -1:
        equation += "- x^2"
    else:
        equation += f"{ A}x^2"

if B != 0:
    if equation:
        equation += " + " if B > 0 else " - "
    elif B < 0:
        equation += "-"

    if abs(B) != 1:
        equation += str(abs(B))
    equation += "x"

if C != 0:
    if equation:
        equation += " + " if C > 0 else " - "
    elif C < 0:
        equation += "-"
    equation += str(abs(C))

if not equation:
    equation = "0"

print(f"The quadratic equation is {equation} = 0")
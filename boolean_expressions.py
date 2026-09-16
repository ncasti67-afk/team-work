
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: NOAH CASTILLO
# JASON ARTEAGA
# ALEJANDRO ALVAREZ
# ANTHONY REYEZ
# Section: M02
# Assignment: LAB TOPIC 4 (TEAM)
# Date: 10/9/2026
############ Part A ############
# section comment A
a = input("Enter True or False for a: ").lower() in ("true", "t")
b = input("Enter True or False for b: ").lower() in ("true", "t")
c = input("Enter True or False for c: ").lower() in ("true", "t")

############ Parts B and C ############
# section comment for B and C
print(f"a and b and c: {a and b and c}")
print(f"a or b or c: {a or b or c}")

xor = (a and not b) or (not a and b)
odd_number = ((a and not b and not c) or
			  (not a and b and not c) or
			  (not a and not b and c) or
			  (a and b and c))
print(f"XOR: {xor}")
print(f"Odd number: {odd_number}")

############ Part D ############
# section comment D
complex_1 = ((not (a and not b) or (not c and b)) and not b
			 or (not a and b and not c) or (a and not b))
simple_1 = not b or (not a and not c)

complex_2 = (not ((b or not c) and (not a or not c))
			 or not (c or not (b and c))
			 or (a and not c) and
			 (not a or (a and b and c) or (a and ((b and not c) or not b))))
simple_2 = a or (not b and c)

print(f"Complex 1: {complex_1}")
print(f"Simple 1: {simple_1}")
print(f"Complex 2: {complex_2}")
print(f"Simple 2: {simple_2}")
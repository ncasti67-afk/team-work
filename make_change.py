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
# Making it equal to its varibale allows for python to assess the equations. 
payment = float(input("How much did you pay? "))
cost = float(input("How much did it cost? "))

payment_cents = int(round(payment * 100))
cost_cents = int(round(cost * 100))
change_cents = payment_cents - cost_cents

if change_cents < 0:
    print("You did not pay enough.")
else:
    quarters = change_cents // 25
    change_cents %= 25
    dimes = change_cents // 10
    change_cents %= 10
    nickels = change_cents // 5
    change_cents %= 5
    pennies = change_cents

    dollars = int((payment_cents - cost_cents) / 100)
    cents = (payment_cents - cost_cents) % 100

    print(f"You received ${dollars}.{cents:02d} in change. That is...")

    if quarters:
        print(f"{quarters} quarter{'s' if quarters != 1 else ''}")
    if dimes:
        print(f"{dimes} dime{'s' if dimes != 1 else ''}")
    if nickels:
        print(f"{nickels} nickel{'s' if nickels != 1 else ''}")
    if pennies:
        print(f"{pennies} {'penny' if pennies == 1 else 'pennies'}")

# An airline describes airfare as follows.
# A normal ticket's base cost is $300. Persons aged 60 or over have a base cost of $290.
# Children 2 or under have $0 base cost. A carry-on bag costs $10.
# A first checked bag is free, second is $25, and each additional is $50.
# Given inputs of age, carry-on (0 or 1), and checked bags (0 or greater), compute the total airfare.

passenger_age = int(input())
carry_ons = int(input())
checked_bags = int(input())
air_fare = 0

if passenger_age >= 60:
    air_fare = 290  # Senior
elif passenger_age <= 2:
    air_fare = 0  # Lap child
else:    # Regular: 2 < age < 60
    air_fare = 300

if carry_ons > 0:
    air_fare += 10

if checked_bags == 2:
    air_fare += 25
elif checked_bags >= 3:
    air_fare += 25 + (checked_bags - 2) * 50  # 2nd bag is $25. Each bag beyond 2nd is $50
# Note: 0 or 1 bags is $0, so no adjustment to airfare

print(air_fare)

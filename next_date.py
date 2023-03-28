# Many websites let users make reservations (hotel, car, flights, etc.). When a user selects a date, the next day is often automatically selected (for hotel checkout, car return, flight return, etc.). Given a date in the form of three integers, output the next date. If the input is 1 15 2017, the output should be 1 16 2017. If the input is 8 31 2017, the output should be 9 1 2017. Ignore leap years.
#
# Hints:
#
# Group the months based on number of days. Then create an if-else statement for each case.
#
# Note that 12 (December) is a special case; after the last day, the next month is 1 (January) and is the next year.

user_month, user_day, user_year = map(int, input().split())

if (user_month == 12) and (user_day == 31):  # Last day of year
    next_month = 1
    next_day = 1
    next_year = user_year + 1
elif (user_month in [1, 3, 5, 7, 8, 10]) and (user_day == 31):
    next_month = user_month + 1
    next_day = 1
    next_year = user_year
elif (user_month in [4, 6, 9, 11]) and (user_day == 30):
    next_month = user_month + 1
    next_day = 1
    next_year = user_year
elif (user_month == 2) and (user_day == 28):
    next_month = user_month + 1
    next_day = 1
    next_year = user_year
else:  # Normal case, just increment day
    next_month = user_month
    next_day = user_day + 1
    next_year = user_year

print(next_month, next_day, next_year)

# 24-hour time (also known in the U.S. as military time) is widely used around the world. Time is expressed as hours since midnight. The day starts at 00:00, and ends at 23:59. Write a program that converts am/pm time to 24-hour time. The input is two numbers and a string. If the input is 2 30 pm, the output should be 14:30. If the input is 12 01 am, the output should be 00:01.
#
# Hints:
#
# Think of how each hour should be handled. 12 00 am -12 59 am becomes what? 8 00 am becomes what? 12 00 pm? 1 00 pm? Group the hours into cases that should be handled similarly (e.g., 1 00 am to 11 00 am are handled the same).
#
# Declare variables for hoursAmPm, minAmPm, and hours24. Note that minutes for 24-hour time remain the same as for am/pm, so no extra variable is needed.
#
# Use an if-else statement to detect each case, and set the hours24 appropriately.
#
# When outputting hour24, check if the hour is 0-9 (just check for < 10). If so, output a "0". So 7 will be output as 07. Do the same when outputting the minutes.

hour_am_pm, min_am_pm, am_pm = input().split()

if (hour_am_pm == "12") and (am_pm == "am"):  # Special case for first hour
    hour_24 = "00"
elif (am_pm == "pm") and (hour_am_pm != "12"):  # Add 12 for 1 pm and higher (not for 12 pm).
    hour_24 = str(int(hour_am_pm) + 12)  # Ex: 2 pm becomes 14
else:  # must be 1 am to 11 am, so hour stays the same (e.g., 9 am stays 9 am)
    hour_24 = hour_am_pm

if len(hour_24) < 2:  # Prepend a "0", such as 02:30
    hour_24 = "0" + hour_24

if len(min_am_pm) < 2:  # Prepend a "0", such as 12:01
    min_am_pm = "0" + min_am_pm

print(hour_24 + ":" + min_am_pm)

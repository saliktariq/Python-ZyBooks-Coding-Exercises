# Given a total amount of inches, convert the input into a readable output in feet and inches.
#
# Ex: If the input is:
#
# 55
# the output should be:
#
# 4'7"

# Type your code here.
totalInches = int(input())
feet = totalInches // 12
inches = totalInches - feet*12
print(str(feet) + "'" + str(inches) + "\"" )


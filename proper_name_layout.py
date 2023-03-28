# Many documents require a specific format for listing a person's name. Assume you are given a person's full name (ie. first name, middle name, and last name). Output the full name in the following format: "lastName, firstName middleInitial.".
#
# Ex: If the input is:
#
# John Jane Doe
# the output should be:
#
# Doe, John J.

first_name = input()
middle_name = input()
last_name = input()

print(last_name + ", " + first_name + " " + middle_name[0] + ".")

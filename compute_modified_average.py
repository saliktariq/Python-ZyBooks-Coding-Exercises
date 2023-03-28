# Compute the average of a list of user-entered integers representing rolls of two dice. The list ends when 0 is entered. Integers must be in the range 2 to 12 (inclusive); integers outside the range don't contribute to the average. Output the average, and the number of valid and invalid integers (excluding the ending 0). If only 0 is entered, output 0. The output may be a floating-point value. Ex: If the user enters 8 12 13 0, the output is:
#
# Average: 10
# Valid: 2
# Invalid: 1

valid_sum = 0
valid_num = 0
invalid_num = 0
user_int = int(input())
average_num = 0.0

while user_int != 0:
    if 2 <= user_int <= 12:  # Valid
        valid_sum += user_int
        valid_num += 1
    else:  # Invalid
        invalid_num += 1

    user_int = int(input())

if valid_num > 0:  # Avoid dividing by 0
    average_num = valid_sum / valid_num

print("Average:", average_num)
print("Valid:", valid_num)
print("Invalid:", invalid_num)

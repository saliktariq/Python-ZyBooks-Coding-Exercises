# Commas make large integers easier to read. Ex: 145,020 is easier to read than 145020. Write a function that takes an integer, and returns a string representation of that number with commas appropriately inserted. If the input if 145020, the function returns string "145,020".

def digit_to_char(single_digit):
    # Given int 0, 1, ..., 9, returns ASCII character '0', '1', ..., '9'.
    digit_as_char = chr(ord('0') + single_digit)
    return digit_as_char


def num_to_string_with_commas(user_num):
    curr_num = user_num
    num_as_string = ""
    pos_count = 0  # Every 3, insert a comma

    while curr_num > 0:
        if pos_count == 3:
            num_as_string = ',' + num_as_string
            pos_count = 1  # 1 (not 0), because we're going to add a digit
        else:
            pos_count += 1

        curr_digit = curr_num % 10  # Gets the rightmost digit. Ex: 569 % 10 is 9.
        curr_digit_as_char = digit_to_char(curr_digit)  # Ex: 9 becomes character '9'
        num_as_string = curr_digit_as_char + num_as_string
        curr_num //= 10  # Shifts the number right one digit. Ex: 569 // 10 is 56.

    if user_num == 0:
        num_as_string = '0'

    return num_as_string


# Driver code
user_num = int(input())
result_string = num_to_string_with_commas(user_num)
print(result_string)

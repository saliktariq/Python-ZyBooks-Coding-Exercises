# Given a vector of digits (0-9) for a decimal number, write a function that returns a single integer. The 0'th element is the decimal number's one's place. If the vector's elements are 9, 6, 2, the function returns integer 269.

def digits_to_num(digits_list):
    curr_weight = 1
    total_num = 0

    for digit in reversed(digits_list):
        total_num += digit * curr_weight
        curr_weight *= 10

    return total_num


# Driver code
digits_list = list(map(int, input().split()))
result_num = digits_to_num(digits_list)
print(result_num)

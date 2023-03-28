# A user will enter an initial number, followed by that number of integers. Output those integers' sum. Repeat until the initial number is 0 or negative. Ex: If the user enters 3 9 6 1 0, the output is:
#
# 16
# Ex: If the user enters 3 9 6 1 2 5 3 0, the output is:
#
# 16
# 8

num_ints = int(input())

while num_ints > 0:
    ints_sum = 0
    for i in range(num_ints):
        user_int = int(input())
        ints_sum += user_int
    print(ints_sum)

    num_ints = int(input())


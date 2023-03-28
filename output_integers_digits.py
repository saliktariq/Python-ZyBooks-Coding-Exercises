# Given an input positive integer, output each digit on its own line, starting with the rightmost digit. Ex: If the input is 935, the output is:
#
# 5
# 3
# 9

userInt = int(input())
divisor = userInt

while divisor != 0:
    print(divisor % 10) # Outputs rightmost digit
    divisor = divisor // 10 # Shifts the integer right by one digit

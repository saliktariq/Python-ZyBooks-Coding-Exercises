# A binary number's digits are only 0's and 1's, with each digit's weight
# being an increasing power of 2. Ex: 110 is
# 1*22 + 1*21 + 0*20 = 1*4 + 1*2 + 0*1 = 4 + 2 + 0 = 6.
# A user enters an 8-bit binary number as 1's and 0's separated by spaces.
# Then compute and output the decimal equivalent. Ex: For input 0 0 0 1 1 1 1 1,
# the output is:
# 31
# (16 + 8 + 4 + 2 + 1)

binaryNum = [0] * 8
digitWeight = 1
decimalSum = 0

# Get user's binary number. Store leftmost bit in element 7, rightmost in 0.
for i in range(7, -1, -1):
    binaryNum[i] = int(input())

# Compute decimal equivalent
for i in range(8):
    decimalSum += binaryNum[i] * digitWeight
    digitWeight *= 2

print(decimalSum)

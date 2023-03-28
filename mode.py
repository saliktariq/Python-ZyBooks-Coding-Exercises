# The "mode" is a statistical summary of data (as are min, max, and average) representing the most commonly-occurring value. Given 10 integers ranging from 0 to 99, output the mode and its frequency. If the input is 1 1 1 1 2 2 9 8 7 6, the output is:
#
# 1 4
# If any integer is outside 0-99, output an error. If an input is 105, the output is:
#
# Invalid input: 105 is not in 0-99

userValues = [0] * 10
i = 0
curVal = 0 # Improves code readability below
valCounts = [0] * 100
maxCount = 0
maxCountIndex = 0

for i in range(10):
    userValues[i] = int(input())

# valCounts list was auto-initialized to all 0's. No need to explicitly initialize here
for i in range(10):
    curVal = userValues[i]
    if (curVal < 0) or (curVal > 99):
        print("Invalid input: ", curVal, " is not in 0-99")
        exit()

    valCounts[curVal] += 1

maxCount = valCounts[0] # Max count seen so far
maxCountIndex = 0      # Index of max count seen so far
for i in range(100):  # Note to 100, not 10
    if valCounts[i] > maxCount:
        maxCount = valCounts[i]
        maxCountIndex = i

print(maxCountIndex, maxCount)

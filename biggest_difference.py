# Write a program that outputs the biggest difference (absolute value)
# between any successive pair of numbers in a list. Such a list might represent
# daily stock market prices or daily temperatures, so the difference represents
# the biggest single-day change.
# The input is the list size, followed by the numbers.
# If the input is 5 60 63 68 61 59, the output is 7.

listSize = int(input())

maxDiff = 0
prevNum = None
for i in range(listSize):
    currNum = int(input())
    if i > 0:
        currDiff = abs(currNum - prevNum)
        if currDiff > maxDiff:
            maxDiff = currDiff
    prevNum = currNum

print(maxDiff)

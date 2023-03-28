# Reversing a vector is a common task. One approach copies to a second vector
# in reverse, then copies the second vector back to the first. However, to save space,
# reversing a vector without using a second vector is sometimes preferable.
# Write a function that reverses a given vector, without using a second vector.
# If the original vector's values are 2 5 9 7, the vector after reversing is 7 9 5 2.

listNums = []
while True:
    try:
        currNum = int(input())
        listNums.append(currNum)
    except:
        break

listSize = len(listNums)
for i in range(listSize // 2):
    # Swap item from first half with item from second half
    tmp = listNums[i]
    listNums[i] = listNums[listSize - i - 1]
    listNums[listSize - i - 1] = tmp

for i in range(listSize):
    print(listNums[i], end=" ")
print()

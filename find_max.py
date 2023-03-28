# Traversing a vector to find the max (or min) is common.
# Given a vector of integers, output the maximum integer found in the vector.
# If the input is 4 3 8 2 6, the output is 8.

numItems = int(input())

listItems = []
for i in range(numItems):
    currItem = int(input())
    listItems.append(currItem)

maxItem = listItems[0]
for i in range(numItems):
    if listItems[i] > maxItem:
        maxItem = listItems[i]

print(maxItem)
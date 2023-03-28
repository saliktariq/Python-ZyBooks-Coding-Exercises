# A common statistic of interest is the longest sequence of some pattern in
# a list of items. For example, in football, one may be interested in the longest
# sequence of consecutive complete passes. Given a list in which each item is
# either the letter "I" (for an incomplete pass) or a number (for a completed pass),
# output the length of the longest sequence of complete passes.
# The list is preceded by the number of items. Given 8 4 15 9 I 30 2 I 20,
# the output is 3 (because the longest sequence of complete passes is 4 15 9).

numItems = int(input())
listItems = []

for i in range(numItems):
    currItem = input()
    listItems.append(currItem)

longestSeqLength = 0
currSeqLength = 0

for i in range(numItems):
    if listItems[i] == "I":
        currSeqLength = 0
    else:
        currSeqLength += 1
        if currSeqLength > longestSeqLength:
            longestSeqLength = currSeqLength

print(longestSeqLength)

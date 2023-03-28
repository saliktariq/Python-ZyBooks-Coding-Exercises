# A publisher may allow a reader to select a subset of chapters to purchase.
# Given 15 integers that are 0 or 1 indicating whether or not to include
# chapters 1 to 15, output the selection using shorthand for ranges of 3 or more
# (11, 12, 13 becomes 11-13). If the input is 1 1 1 1 0 1 0 1 1 0 1 1 1 0 0,
# the output should be: 1-4 6 8 9 11-13 If no chapters are selected, output:
# None For simplicity, follow every term including the last by one space (and end with newline).

chptList = [False] * 16  # Valid chapters are 1-15. 1 means include, 0 exclude. Element 0 unused.
includeChpt = False
atLeastOne = False

# Get the chapter selections
for i in range(1, 16):
    includeChpt = bool(input())
    if includeChpt:
        chptList[i] = True
    else:
        chptList[i] = False

# Output the chapter selections, using ranges like 2-4 for ranges of 3-or-more
i = 1
while i <= 15:
    if chptList[i]:  # Output this number
        print(i, end='')
        atLeastOne = True
        if (i <= 13) and chptList[i+1] and chptList[i+2]:  # Possible 3-or-more range
            # Find end of range
            j = i + 2  # Last 1 seen so far in the range
            while (j <= 14) and chptList[j+1]:  # Range continues...
                j += 1  # ...so extend the range
            print('-', j, end=' ')
            i = j + 1  # Set i to end of range, so next while loop iteration will start at the next number
        else:
            print(' ', end='')  # No 3-or-more range, so just output a space after the number
        i += 1
    else:
        i += 1

if not atLeastOne:  # No chapters were selected
    print('None', end=' ')
print()  # Print a newline to end the output

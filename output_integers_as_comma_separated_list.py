# Given a list of integers, output those integers separated by a comma and space, except for the last which should be followed by a period (and newline). The first integers indicates how many integers are in the subsequent list.
# If the input is 4 1 7 3 5, the output should be: 1, 7, 3, 5.

numInts = int(input())
for i in range(numInts):
    if i > 0:
        print(", ", end="")
    currInt = int(input())
    print(currInt, end="")
print(".")


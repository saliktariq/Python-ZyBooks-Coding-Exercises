# A state's Department of Motor Vehicles needs a program to generate license plate numbers. A license plate number consists of three letters followed by three digits, as in CBJ523. (So "number" is a bit inaccurate, but that's the standard word used for license plates). The plate numbers are given out in sequence, so given the current number, the program should output the next number. If the input is CBJ523, the output should be CBJ524. If the input is CBJ999, the output should be CBK000. For the last number ZZZ999, the next is AAA000.
#
# Hints:
#
# Treat each character individually.
#
# Initially, don't try to create an "elegant" solution. Just consider each of the six places one at a time, starting from the right.
#
# For each place, if less than the max for that place ('9' for digits, 'Z' for letters), just increment that place. Note that you can just type c = c + 1 to get the next higher character for a digit like '5' or for a letter like 'K').
#
# If a place is at the max, set it with the '0' or 'A', and then set a boolean variable to true to indicate a "carry" is needed. (If a carry isn't needed, set to false).
#
# With the above process, you'll have 6 separate if-else statements.

plate_number = input()
c1, c2, c3 = plate_number[0], plate_number[1], plate_number[2]
i1, i2, i3 = plate_number[3], plate_number[4], plate_number[5]
carry_needed = False

# Check each place starting from the right. If less than max, just increment it.
# If at max, set to start val, set carry true.

# Place 6
if i3 < '9':
    i3 = chr(ord(i3) + 1)
else:
    i3 = '0'
    carry_needed = True

# Place 5
if carry_needed:
    if i2 < '9':
        i2 = chr(ord(i2) + 1)
        carry_needed = False
    else:
        i2 = '0'
        carry_needed = True

# Place 4
if carry_needed:
    if i1 < '9':
        i1 = chr(ord(i1) + 1)
        carry_needed = False
    else:
        i1 = '0'
        carry_needed = True

# Place 3
if carry_needed:
    if c3 < 'Z':
        c3 = chr(ord(c3) + 1)
        carry_needed = False
    else:
        c3 = 'A'
        carry_needed = True

# Place 2
if carry_needed:
    if c2 < 'Z':
        c2 = chr(ord(c2) + 1)
        carry_needed = False
    else:
        c2 = 'A'
        carry_needed = True

# Place 1
if carry_needed:
    if c1 < 'Z':
        c1 = chr(ord(c1) + 1)
        carry_needed = False
    else:
        c1 = 'A'
        carry_needed = True

print(c1 + c2 + c3 + i1 + i2 + i3)

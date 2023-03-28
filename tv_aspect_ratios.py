# A TV's size indicates the TV's diagonal.
# Thus, one 60" TV could have a different width and height than another 60" TV,
# both yielding a 60" diagonal. For a given TV diagonal, output a table listing
# possible widths and heights, each row increasing width by 1 inch. Only list rows
# where width is greater than height. Define diagonal, width, and height variables
# as doubles, but note that width will only take on rounded values like 20.0, 21.0,
# etc.

import math

tvDiagonal = int(input())

for tvWidth in range(1, tvDiagonal):
    tvHeight = math.sqrt(tvDiagonal**2 - tvWidth**2)
    if tvWidth > tvHeight:
        print(tvWidth, tvHeight)

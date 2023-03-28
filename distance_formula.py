# Map/GPS applications commonly compute the distance between two points.
# A point may be a coordinate on an x-y plane like (1.5, 2.0).
# The distance formula is d = √((x2 - x1)2 + (y2 - y1)2)
# (basically, Pythagorean's Theorem). Given two points, output the distance between them.
# If the input is (1.5, 2.0) (4.5, 6.0), the output is 5.

import math

c = input()  # Skip (
x1 = float(input())
c = input()  # Skip ,
y1 = float(input())
c = input()  # Skip )
c = input()  # Skip (
x2 = float(input())
c = input()  # Skip ,
y2 = float(input())

dist_points = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(dist_points)

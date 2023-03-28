# Write a function called MaxFive that returns the maximum of five integer
# parameters.
# Ex: MaxFive(3, 5, 1, 0, 2) returns 5.

def MaxFive(a, b, c, d, e):
    maxFound = a
    if b > maxFound:
        maxFound = b
    if c > maxFound:
        maxFound = c
    if d > maxFound:
        maxFound = d
    if e > maxFound:
        maxFound = e
    return maxFound

v, w, x, y, z = map(int, input().split())
maxVal = MaxFive(v, w, x, y, z)
print(maxVal)

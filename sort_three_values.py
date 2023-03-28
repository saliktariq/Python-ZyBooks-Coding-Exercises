# Write a function Ascend3 with three integer reference parameters,
# that sorts the values into ascending order. Ex: If x = 5, y = 2, and z = 7,
# after the call Ascend3(x, y, z),
# the new values will be x = 2, y = 5, and z = 7.

def Ascend3(a, b, c):
    lowVal, midVal, highVal = 0, 0, 0

    if a <= b <= c:
        lowVal = a
        midVal = b
        highVal = c
    elif a <= c <= b:
        lowVal = a
        midVal = c
        highVal = b
    elif b <= a <= c:
        lowVal = b
        midVal = a
        highVal = c
    elif b <= c <= a:
        lowVal = b
        midVal = c
        highVal = a
    elif c <= a <= b:
        lowVal = c
        midVal = a
        highVal = b
    elif c <= b <= a:
        lowVal = c
        midVal = b
        highVal = a

    a, b, c = lowVal, midVal, highVal


x, y, z = map(int, input().split())
Ascend3(x, y, z)
print(x, y, z)

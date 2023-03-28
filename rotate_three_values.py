# Given three function parameters p1, p2, p3, rotate the values to the right. Rotate means to shift each item to the item on the right, with the rightmost item rotating around to become the leftmost item. If initial values are 2 4 6, final values are 6 2 4.

def rotate_right_3(p1, p2, p3):
    tmp = p3
    p3 = p2
    p2 = p1
    p1 = tmp
    return p1, p2, p3

n1 = int(input())
n2 = int(input())
n3 = int(input())

n1, n2, n3 = rotate_right_3(n1, n2, n3)

print(n1, n2, n3)

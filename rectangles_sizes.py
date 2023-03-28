# Suppose a graphics program needs a function to indicate whether one rectangle is smaller than another rectangle. A rectangle is specified by its upper-left coordinate and bottom-right coordinate. If the first rectangle is (1, 1) and (2,3), and the second is (0,0) and (10,10), the function returns true.

def first_rectangle_smaller(r1xul, r1yul, r1xbr, r1ybr, r2xul, r2yul, r2xbr, r2ybr):
    r1_area = abs(r1xul - r1xbr) * abs(r1yul - r1ybr)  # Area is width * height
    r2_area = abs(r2xul - r2xbr) * abs(r2yul - r2ybr)
    return r1_area < r2_area


# Driver code
r1xul, r1yul, r1xbr, r1ybr = map(int, input().split())
r2xul, r2yul, r2xbr, r2ybr = map(int, input().split())

print(first_rectangle_smaller(r1xul, r1yul, r1xbr, r1ybr, r2xul, r2yul, r2xbr, r2ybr))

# Rideshare companies like Uber or Lyft track the x,y coordinates of drivers
# and customers on a map. If a customer requests a ride, the company's app estimates
# the minutes until the nearest driver can arrive. Write a function that,
# given the x and y coordinates of a customer and the three nearest drivers,
# returns the estimated pickup time. Assume drivers can only drive in the x or y
# directions (not diagonal) and each mile takes 2 minutes to drive.
# All values are integers.

def absVal(a):
    if a < 0:
        return -a
    else:
        return a


# All x, y coordinates are in miles from the origin 0, 0.
def PickupMinutes(userX, userY, d1X, d1Y, d2X, d2Y, d3X, d3Y):
    # Compute distances
    dist1 = absVal(userX - d1X) + absVal(userY - d1Y)
    dist2 = absVal(userX - d2X) + absVal(userY - d2Y)
    dist3 = absVal(userX - d3X) + absVal(userY - d3Y)

    # Determine minimum distance
    minDist = dist1
    if dist2 < minDist:
        minDist = dist2
    if dist3 < minDist:
        minDist = dist3

    # Calculate and return time (2 min per mile)
    return 2 * minDist


# Get input from user
userX, userY = map(int, input().split())
d1X, d1Y = map(int, input().split())
d2X, d2Y = map(int, input().split())
d3X, d3Y = map(int, input().split())

# Output result
print(PickupMinutes(userX, userY, d1X, d1Y, d2X, d2Y, d3X, d3Y))

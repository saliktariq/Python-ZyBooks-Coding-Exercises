# Programs commonly perform simulations of physical scenarios like cars
# in traffic, or people waiting at stores. A store wants to understand customer
# waiting time. A list provides the number of customers that arrive every minute for
# 10 minutes. The program should output the length of the line at each minute,
# assuming one clerk serves each customer and takes 1 minute to complete service.
# If the input is 2 0 0 2 1 0 0 0 1 0, the output should be 2 1 0 2 2 1 0 0 1 0
# (At minute 0, 2 customers arrived in line. At minute 1, 1 of those has been served,
# reducing the line to 1. At minute 2, that customer was served, reducing the line to 0).
# Output a space after each output integer,
# including the last (followed by newline).

def SimulateLine(customerArrivals):
    lineLength = 0

    # Perform simulation for 10 steps (simulating 10 minutes)
    for arrival in customerArrivals:
        if lineLength > 0:
            lineLength -= 1  # Each minute, the clerk finishes serving 1 customer
        lineLength += arrival  # This many new customers arrived into line
        print(lineLength, end=' ')
    print()


# Get customer arrival data
customerArrivals = list(map(int, input().split()))

SimulateLine(customerArrivals)

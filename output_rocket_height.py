# Suppose a launched toy rocket's height is computed as h = vi*t - 5t2. vi is the initial velocity, and t is time in seconds since the launch (starting at 0). Write a program to read the initial velocity, then output the time and the rocket's height once per second. Stop when the height would be negative, meaning the rocket hit the ground (don't print the negative). Assume all values are integers. Ex: For input 20, the output is:
#
# 0 0
# 1 15
# 2 20
# 3 15
# 4 0

rocket_height = 0
initial_velocity = int(input())
time_since_launch = 0

while rocket_height >= 0:
    print(time_since_launch, rocket_height)
    time_since_launch += 1
    rocket_height = initial_velocity*time_since_launch - 5*time_since_launch*time_since_launch

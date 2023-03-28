# Write a function ActivityCalories that takes a string indicating an activity (sit, walk, run, bike, swim) and duration in minutes (integer), and returns the estimated calories expended (double). Calories per minute for a 150 lb person (source):
#
# sit: 1.4 walk: 5.4 run: 13.0 bike: 6.8 swim: 8.7
#
# If the input is sit 2, the output is 2.8.

def ActivityCalories(activityDone, minutesSpent):
    caloriesPerMinute = 0.0

    if activityDone == "sit":
        caloriesPerMinute = 1.4
    elif activityDone == "walk":
        caloriesPerMinute = 5.4
    elif activityDone == "run":
        caloriesPerMinute = 13.0
    elif activityDone == "bike":
        caloriesPerMinute = 6.8
    elif activityDone == "swim":
        caloriesPerMinute = 8.7

    return caloriesPerMinute * minutesSpent


userActivity, userMinutes = input().split()
userMinutes = int(userMinutes)
print(ActivityCalories(userActivity, userMinutes))

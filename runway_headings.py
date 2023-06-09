# Airport runways are numbered using a 2-digit number, like 09. The meaning generally is that planes taking off or landing on that runway will be facing 090 or 90 degrees rotated right from north, namely facing east. Given a runway number (integer), output the degrees followed by the closest direction indication (north, northeast, east, southeast, south, southwest, west, or northwest). If the input is 03, the output is: 30 degrees (northeast).
#
# Hints:
#
# First just read the input number, multiply by 10 to yield runwayDeg.
#
# Next, create an if-else statement to compare runwayDeg's value with ranges for each direction. For north, the value should be within -22.5 and +22.5. For northeast, the value should be between 45 - 22.5 and 45 + 22.5. And so on.
#
# Based on the range in which the value falls, update a string variable with the direction. Then after the if-else, have a single output statement that outputs "270 degrees (north)" or whatever value and direction are correct.
#
# Don't forget that ranges use &&. An expression detecting a value x is between 1 and 10 is (x > 1) && (x < 10).
#
# Because the input is an integer which is multiplied by 10 to yield runwayDeg, the comparisons with floating-point values like 22.5 will never result in equality. Hence, the ranges don't have to account for such quality.


runway_num = int(input())
runway_deg = runway_num * 10
runway_direction = ""

# Determine closest direction. Ranges are heading +/- 22.5.
if (-22.5 < runway_deg <= 22.5):
    runway_direction = "north"
elif (22.5 < runway_deg <= 67.5):
    runway_direction = "northeast"
elif (67.5 < runway_deg <= 112.5):
    runway_direction = "east"
elif (112.5 < runway_deg <= 157.5):
    runway_direction = "southeast"
elif (157.5 < runway_deg <= 202.5):
    runway_direction = "south"
elif (202.5 < runway_deg <= 247.5):
    runway_direction = "southwest"
elif (247.5 < runway_deg <= 292.5):
    runway_direction = "west"
elif (292.5 < runway_deg <= 337.5):
    runway_direction = "northwest"

print(runway_deg, "degrees (", runway_direction, ")", sep="")

# Given your current grade as the input, write a program to help you determine what score you need to get on a final to get an A (90% or higher) in a class. The syllabus states that the final is worth 40% of the overall grade.
#
# The input is an integer.
#
# The output should be a percentage rounded to one decimal place. Ex: 85.5%

current_grade = float(input())

current_points = current_grade * 0.6
points_needed = 90 - current_points
grade_on_final = points_needed / 40

print("{:.1%}".format(grade_on_final))

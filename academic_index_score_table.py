# Many universities calculate a weighted sum of an applicant's high school
# GPA and standardized test scores, whose value (called an Academic Index Score or AIS)
# must exceed a minimum threshold to be considered for admission.
# Ex: AIS = 2.5 * (GPA / 4.0) * 100 + (test_score / 1600) * 100 must be at least 270.
# Write a program that, given a threshold, prints a table indicating the
# minimum GPA / test score combinations that meet the threshold. Use doubles for
# all values. Each row is GPA then test score. GPA should range from 3.0 to 4.0 in
# increments of 0.1.


aisMinimum = float(input())

for rowGPA in [3.0 + i/10.0 for i in range(11)]:
    rowTestScore = 1600.0 * (aisMinimum / 100.0) - 1600.0 * 2.5 * (rowGPA / 4.0)
    print(rowGPA, rowTestScore)



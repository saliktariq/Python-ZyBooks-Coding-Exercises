# A user inputs the name of a shape (square or triangle). The program outputs the shape using asterisks. For input square, the output is:
#
# ***
# * *
# ***
# If the input is triangle, the output is:
#
#   *
#  * *
# *****

user_shape = input()

if user_shape == "square":
    print("***")
    print("* *")
    print("***")
elif user_shape == "triangle":
    print("  *")
    print(" * *")
    print("*****")

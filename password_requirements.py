# Websites commonly require a password that satisfies several requirements. Write a program that checks if an input string satisfies the following (error message is shown for each)
#
# At least 8 characters (Too short)
# At least one letter (Missing letter)
# At least one number (Missing number)
# At least one of these special characters: !, #, % (Missing special)
# Output OK, or all related error messages (in above order). If the input string is "Hello", the output is:
#
# Too short
# Missing number
# Missing special

userText = input()
lengthOK = False
hasLetter = False
hasNumber = False
hasSpecial = False

if len(userText) >= 8:
    lengthOK = True

for c in userText:
    if c.isalpha():  # At least one letter found
        hasLetter = True
    elif c.isdigit():  # At least one number found
        hasNumber = True
    elif c in ['!', '#', '%']:
        hasSpecial = True

if lengthOK and hasLetter and hasNumber and hasSpecial:  # All requirements met
    print("OK")
else:
    if not lengthOK:
        print("Too short")
    if not hasLetter:
        print("Missing letter")
    if not hasNumber:
        print("Missing number")
    if not hasSpecial:
        print("Missing special")

# Various websites like Wikipedia or IMDB list not just a person's birthdate
# but also the person's current age. Given a person's birthdate and current date,
# output the person's age in years. The custom is to round down.
# If the input is 7 1 2000 2 15 2015, the output is 14
# (because the person hasn't yet reached their 15th birthday).
# A person less than 1 has age 0.

def GetAge(birthMonth, birthDay, birthYear, currMonth, currDay, currYear):
    currAge = currYear - birthYear
    # Determine if need to reduce by 1 if birthday not yet reached
    if currMonth < birthMonth:  # Birth month not yet reached, reduce by 1
        currAge = currAge - 1
    elif currMonth == birthMonth:
        if currDay < birthDay:  # In birth month, but birthday not yet reached
            currAge = currAge - 1

    return currAge


# Get input from user
birthMonth, birthDay, birthYear = map(int, input().split())
currMonth, currDay, currYear = map(int, input().split())

# Output result
print(GetAge(birthMonth, birthDay, birthYear, currMonth, currDay, currYear))

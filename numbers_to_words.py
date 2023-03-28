# Sometimes numbers are converted to words, like in a wedding invitation. So 23 becomes "twenty three". Write a function DigitToWord that takes a single digit number from 0-9 and returns that number's word: 0 is zero, 1 is one, 2 is two, etc (if the number is outside 0-9, return "error"). Write another function TensDigitToWord that takes a single digit number from 2-9, and returns that number's word when it appears in the tens digit: 2 is twenty, 3 is thirty, etc. If the number is outside 2-9, return "error". Finally, write a function TwoDigitNumToWords that takes a two-digit number from 20-99 and returns that number in words. Your main program should get a user's integer, call TwoDigitNumToWords, and output the resulting string. If the input is 23, the output should be "twenty three".
#
# Do not do any error checking of the input. Note that your program does not support all numbers. 0-19 will yield error output, for example.

def DigitToWord(digitIn):
    if digitIn == 0:
        wordOut = ""
    elif digitIn == 1:
        wordOut = "one"
    elif digitIn == 2:
        wordOut = "two"
    elif digitIn == 3:
        wordOut = "three"
    elif digitIn == 4:
        wordOut = "four"
    elif digitIn == 5:
        wordOut = "five"
    elif digitIn == 6:
        wordOut = "six"
    elif digitIn == 7:
        wordOut = "seven"
    elif digitIn == 8:
        wordOut = "eight"
    elif digitIn == 9:
        wordOut = "nine"
    else:
        wordOut = "error"
    return wordOut


def TensDigitToWord(digitIn):
    if digitIn == 0:
        wordOut = "error"
    elif digitIn == 1:
        wordOut = "error"
    elif digitIn == 2:
        wordOut = "twenty"
    elif digitIn == 3:
        wordOut = "thirty"
    elif digitIn == 4:
        wordOut = "forty"
    elif digitIn == 5:
        wordOut = "fifty"
    elif digitIn == 6:
        wordOut = "sixty"
    elif digitIn == 7:
        wordOut = "seventy"
    elif digitIn == 8:
        wordOut = "eighty"
    elif digitIn == 9:
        wordOut = "ninety"
    else:
        wordOut = "error"
    return wordOut


def TwoDigitNumToWords(numIn):
    onesDigit = numIn % 10
    tensDigit = numIn // 10

    return TensDigitToWord(tensDigit) + " " + DigitToWord(onesDigit)


# Get input from user
userNum = int(input())

# Output result
print(TwoDigitNumToWords(userNum))

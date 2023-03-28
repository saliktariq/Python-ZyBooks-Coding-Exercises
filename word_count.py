# Many text processing tools like Microsoft Word or Google Docs will count the number
# of "words" in text. A word is a sequence of any characters other than a space.
# Write a program that reads an input line of text, and outputs the number of words
# in that text. If the input is "I have a bike." then the output is 4.

userText = input()

wordCount = 0
inWord = False
for char in userText:
    if char == ' ':
        inWord = False
    elif not inWord:
        wordCount += 1
        inWord = True
    else:
        pass

print(wordCount)



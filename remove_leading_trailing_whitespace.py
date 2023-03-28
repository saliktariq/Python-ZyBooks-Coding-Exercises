# Users may type or copy-paste in a text box of a web form, perhaps a name like "Joe Smith". The user sometimes has whitespace before or after the text, like " Joe Smith ". A program typically strips such leading and trailing whitespace. Given a string, create a new string that lacks any leading or trailing spaces. Given " Joe Smith ", the new string should be "Joe Smith". Be sure to handle the case of the user entering only whitespace, or entering nothing, which each should yield an empty string "".


userText = input()
cleanedText = ""
i = 0
j = len(userText) - 1

# Find first non-space character
while i < len(userText) and userText[i] == " ":
    i += 1

if i == len(userText):
    print(cleanedText)
    exit()

# Find last non-space character
while j >= 0 and userText[j] == " ":
    j -= 1

# Copy just characters from i to j to new string
for n in range(i, j + 1):
    cleanedText += userText[n]

print(cleanedText)

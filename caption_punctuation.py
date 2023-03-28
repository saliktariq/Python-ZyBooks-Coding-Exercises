# A user is asked to type a caption for a photo in a web form's text field. If the caption didn't end with a punctuation mark (. ! ?), a period should automatically be added. A common error is to end with a comma, which should be replaced by a period. Another common error is to end with two periods, which should be changed to one period (however, ending with three periods (or more) indicates elipses so should be kept as is). The corrected caption is output.
#
# If the input is "I like pie", the output is "I like pie." If the input is "I like pie!", the output remains "I like pie!" If the input is "Coming soon…", the output remains "Coming soon…"

user_caption = input()

last_index = len(user_caption) - 1
last_char = user_caption[last_index]

if last_char in ['!', '?']:
    # Caption OK; do nothing
    pass
elif last_char == ',':
    user_caption = user_caption[:last_index] + '.'  # Replace ending , (common mistake) by .
elif last_char != '.':  # Not ! ? , . so append .
    user_caption += '.'
elif last_index > 0 and last_char == '.' and user_caption[last_index - 1] == '.':  # Two periods
    if last_index > 1 and user_caption[last_index - 2] == '.':  # Three periods?
        # Caption OK (ends with elipses ... Do nothing)
        pass
    else:  # Ends with two periods; remove one
        user_caption = user_caption[:-1]

print(user_caption)

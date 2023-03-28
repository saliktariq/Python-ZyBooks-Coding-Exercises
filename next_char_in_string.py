# Write a function that, given a string, index, and character, returns the index of the first occurrence of the character starting
# the search at the index. If not found, return -1. If the inputs are "Hello-friends", 3, and 'e', the function returns 9 (indexing the
# 'e' in friends).

def find_next_char_in_string(s, start_index, c):
    char_found = False

    for i in range(start_index, len(s)):
        if s[i] == c:
            char_found = True
            break

    if char_found:
        return i
    else:
        return -1


input_string = input()
start_index = int(input())
search_char = input()

print(find_next_char_in_string(input_string, start_index, search_char))

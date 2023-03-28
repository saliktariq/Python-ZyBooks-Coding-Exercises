# Write a function that returns the index of the next occurrence of a substring in a string. Inputs are the string, start index, and substring. If not found, return -1. Do not use built-in string functions. If the input is "heyhey-friend", 1, "hey", the output is 3 (where the second "hey" starts).

def find_next_substr(s, start_index, substr):
    found_at_index = -1

    for i in range(start_index, len(s) - len(substr) + 1):
        substr_same = True

        for j in range(len(substr)):
            if s[i + j] != substr[j]:
                substr_same = False
                break

        if substr_same:
            found_at_index = i
            break

    return found_at_index


input_string = input()
start_index = int(input())
search_string = input()

print(find_next_substr(input_string, start_index, search_string))

# An earlier problem introduced guitar tabs. In this problem, the user can enter a sequence of chords, and the program should output the tabs in sequence. The first input is the number of chords to follow. If the input is 4 G C G D, the output should be:
#
# e|-3-0-3-2-
# B|-0-1-0-3-
# G|-0-0-0-2-
# D|-0-2-0-0-
# A|-2-3-2---
# E|-3---3---

e_string = "e|-"
B_string = "B|-"
G_string = "G|-"
D_string = "D|-"
A_string = "A|-"
E_string = "E|-"
num_chords = int(input())

for i in range(num_chords):
    user_chord = input()
    if user_chord == "G":
        e_string += "3-"
        B_string += "0-"
        G_string += "0-"
        D_string += "0-"
        A_string += "2-"
        E_string += "3-"
    elif user_chord == "C":
        e_string += "0-"
        B_string += "1-"
        G_string += "0-"
        D_string += "2-"
        A_string += "3-"
        E_string += "--"
    elif user_chord == "D":
        e_string += "2-"
        B_string += "3-"
        G_string += "2-"
        D_string += "0-"
        A_string += "--"
        E_string += "--"

print(e_string)
print(B_string)
print(G_string)
print(D_string)
print(A_string)
print(E_string)

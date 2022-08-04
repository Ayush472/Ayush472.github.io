import string

list = ["", "", "", "", "", "", "", "", "_"]

t = 1
a = input("Enter player-1 Name = ")
b = input("Enter player-2 Name = ")

while t < 10:

    if t % 2 == 0:
        pos = int(input("Enter your position = "))

        if list[pos - 1] == '_':
            list[pos - 1] = 'X'
        else:
            t = t - 1
            print("You Idiot!! Already Occupied")
    else:
        pos = int(input("Enter your position = "))

        if list[pos - 1] == '_':
            list[pos - 1] = 'O'
        else:
            t = t - 1
            print("You Idiot!! Already Occupied")

    print("After ", t, " =")
    print(list[0], list[1], list[2])
    print(list[3], list[4], list[5])
    print(list[6], list[7], list[8])

    t = t + 1

    if list[0] == list[1] and list[1] == list[2] and list[0] == 'O':
        print(a, " wins !!!!! ")
        t = 15
    elif list[0] == list[3] and list[3] == list[6] and list[0] == 'O':
        print(a, "wins !!!!! ")
        t = 15
    elif list[0] == list[4] and list[4] == list[8] and list[0] == 'O':
        print(a, " wins !!!!! ")
        t = 15
    elif list[1] == list[4] and list[4] == list[7] and list[1] == 'O':
        print(a, " wins !!!!! ")
        t = 15
    elif list[2] == list[5] and list[5] == list[8] and list[2] == 'O':
        print(a, " wins !!!!! ")
        t = 15
    elif list[2] == list[4] and list[4] == list[6] and list[2] == 'O':
        print(a, " wins !!!!! ")
        t = 15
    elif list[3] == list[4] and list[4] == list[5] and list[3] == 'O':
        print(a, " wins !!!!! ")
        t = 15
    elif list[6] == list[7] and list[7] == list[8] and list[6] == 'O':
        print(a, " wins !!!!! ")
        t = 15
    elif list[0] == list[1] and list[1] == list[2] and list[0] == 'X':
        print(b, " wins !!!!! ")
        t = 15
    elif list[0] == list[3] and list[3] == list[6] and list[0] == 'X':
        print(b, " wins !!!!! ")
        t = 15
    elif list[0] == list[4] and list[4] == list[8] and list[0] == 'X':
        print(b, " wins")
        t = 15
    elif list[1] == list[4] and list[4] == list[7] and list[1] == 'X':
        print(b, " wins !!!!! ")
        t = 15
    elif list[2] == list[5] and list[5] == list[8] and list[2] == 'X':
        print(b, " wins !!!!!")
        t = 15
    elif list[2] == list[4] and list[4] == list[6] and list[2] == 'X':
        print(b, " wins !!!!!")
        t = 15
    elif list[3] == list[4] and list[4] == list[5] and list[3] == 'X':
        print(b, " wins !!!!! ")
        t = 15

if t == 10:
    print("Match Tie!!!!")
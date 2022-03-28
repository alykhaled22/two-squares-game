"""""
     *pseudo code:
     1-make gameboard
     2-define function move, to print x in the cell the player will choose
     3-define function is_draw to check when the game is tie
     4-define function is_winner to check is any player won
     5-take palyer1 move and make sure it is a valid number
     6-check if the choosen cell is umpty
     7-print player1 move on board
     8-check if it is draw or player1 won
     9-take player2 move and make sure it is a valid number
     10-check if the choosen cell is umpty
     11-print player2 move on board
     12-check if it is draw or player2 won


"""""

table = ["1", "2", "3", "4",\
         "5", "6", "7", "8",\
         "9", "10", "11", "12",\
         "13", "14", "15", "16"]


def print_table():
    print("==" * 17)
    for i in range(0, 16):
        print("|", '{:>2}'.format(table[i]), end="  |  ")
        if i == 3 or i == 7 or i == 11:
            print()
    print()
    print("==" * 17)
    print()


def move(x, y):
    table[table.index(x)] = "X"
    table[table.index(y)] = "X"


def is_draw():
    if table.count("X") == len(table):
        return "DRAW"


def is_winner():
    for i in range(len(table)-1):
        if table[i] != "X" and table[i + 1] != "X":
            return False

    for i in range(0, len(table) - 4):
        if table[i] != "X" and table[i + 4] != "X":
            return False

    return True


print_table()

while True:
    while True:
        try:
            print("Player 1's Move: ", end="")
            x, y = input().split()
            break
        except ValueError:
            print("INVALID INPUT!")

    while abs(int(x) - int(y)) != 4 and abs(int(x) - int(y)) != 1:
        print("Please Enter two adjacent Squares Only!")
        print_table()
        print("Player 1's Move: ", end="")
        x, y = input().split()


    while table[int(x)-1] == "X" or table[int(y)-1] == "X":
        print("Ops!, It seems that One of the Chosen Squares are already Busy")
        print_table()
        print("Please, Enter Empty Squares Only")
        print("Player 1's Move: ", end="")
        x, y = input().split()

    move(x, y)
    print_table()
    if is_draw():
        print("DRAW")
        break
    elif is_winner():
        print("Player 1 WIN!")
        break

    while True:
        try:
            print("Player 2's Move: ", end="")
            x, y = input().split()
            break
        except ValueError:
            print("INVALID INPUT!")

    while abs(int(x) - int(y)) != 4 and abs(int(x) - int(y)) != 1:
        print("Please Enter two adjacent Squares Only!")
        print_table()
        print("Player 2's Move: ", end="")
        x, y = input().split()

    while table[int(x) - 1] == "X" or table[int(y) - 1] == "X":
        print("Ops!, It seems that One of the Chosen Squares are already Busy")
        print_table()
        print("Please, Enter Empty Squares Only")
        print("Player 2's Move: ", end="")
        x, y = input().split()

    move(x, y)
    print_table()

    if is_draw():
        print("DRAW!")
        break
    elif is_winner():
        print("Player 2 WIN!")
        break


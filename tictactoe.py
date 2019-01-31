# Initialize game board
game = [0, 1, 2,
        3, 4, 5,
        6, 7, 8]


# Function to print game board
def show_board():
    print game[0], "|", game[1], "|", game[2]
    print "---------"
    print game[3], "|", game[4], "|", game[5]
    print "---------"
    print game[6], "|", game[7], "|", game[8]


# Display game board
show_board()


# Function to check lines
def check_line(char, pos1, pos2, pos3):
    if game[pos1] == char and game[pos2] == char and game[pos3] == char:
        return True


# Function to check board
def check_board(char):
    if check_line(char, 0, 1, 2) or \
            check_line(char, 3, 4, 5) or \
            check_line(char, 6, 7, 8) or \
            check_line(char, 0, 4, 8) or \
            check_line(char, 2, 4, 6) or \
            check_line(char, 0, 3, 6) or \
            check_line(char, 1, 4, 7) or \
            check_line(char, 2, 5, 8):
        return True
    else:
        return False


# Check whether board is full or not
def check_not_full():
    if game[0] == 0 or game[1] == 1 or game[2] == 2 or game[3] == 3 or game[4] == 4 or game[5] == 5 or game[6] == 6 or \
            game[7] == 7 or game[8] == 8:
        return True
    else:
        return False


# take user inputs
def player_input(s):
    player = raw_input(s)
    player = int(player)
    return player


while True:
    if check_not_full():
        while True:
            p1 = player_input("enter spot for player 1: ")
            if game[p1] != "X" and game[p1] != "O":
                game[p1] = "X"
                show_board()
                if check_board("X"):
                    print ("!!!!!!!!!! Player 1 wins !!!!!!!!!!")
                    break
                break
            else:
                print "spot already taken"
    else:
        print "Match Draw"
        break

    if check_not_full():
        while True:
            p2 = player_input("enter spot for player 2: ")
            if game[p2] != "X" and game[p2] != "O":
                game[p2] = "O"
                show_board()
                if check_board("O"):
                    print ("!!!!!!!!!! Player 2 wins !!!!!!!!!!")
                    break
                break
            else:
                print "spot already taken"

    else:
        print "Match Draw"
        break

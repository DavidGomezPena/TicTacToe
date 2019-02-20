#This is the main function
def main():
    #These two integers are how the player will pick where they should put their X or O
    cord1 = 0
    cord2 = 0

    board = [["#", "#", "#"],
             ["#", "#", "#"],
             ["#", "#", "#"], ]

    print("Welcome to Tic tac Toe")
    start = input("To Proceed to play this totally orginal game that no one has ever made. Type GO ")
    if start == "GO" or start == "go":
        get_Letter(board, cord1, cord2)
    else:
        print("That is an Invaild Input")
    return


#This function askes the player if they want to be X or be an O
def get_Letter(board, cord1, cord2):
    round = 0
    letter = input("Player One. Which letter do you want to be?(Choose X or O) ")
    if letter == "O" or letter == "o":
        print("You choose O ")
        #p1 is used to see which letter to use
        p1 = 0
        print_Board(board, p1, cord1, cord2, round)
    if letter == "X" or letter == "x":
        print("You choose X ")
        p1 = 1
        print_Board(board, p1, cord1, cord2, round)
        return

#This function prints the board 
def print_Board(board, p1, cord1, cord2, round):
    letters = ["O", "X"]

    if round > 0:
        board[cord1][cord2] = letters[p1]


    print(board[0][0] + "|" + board[1][0] + "|" + board[2][0])
    print("______")
    print(board[0][1] + "|" + board[1][1] + "|" + board[2][1])
    print("______")
    print(board[0][2] + "|" + board[1][2] + "|" + board[2][2])
    playerInput(board, cord1, cord2, p1, letters, round)

    return

#This function asks the user where they want to put their letter. 
def playerInput(board, cord1, cord2, p1, letters, round):
    #This part of the code checks the round and switches the letter for the other person
    if round > 0:
        if p1 == 0:
            p1 = 1
        else:
            p1 = 0

    cord1 = int(input("Enter the coordinates where you want to put an " + letters[p1] + ". Ex:1 0"))
    cord2 = int(input())
    round += 1
    #This part of the function calls the checkBoard function to see if anyone has won after the second round is done.
    if round > 2:
        checkBoard(board, p1, letters)
    print_Board(board, p1, cord1, cord2, round)
    return
#This function checks the board to see if anyone has won


def checkBoard(board, p1, letters):
    if board[0][0] == board[0][1] == board[0][2]:
        print("")
        print("Player " + letters[p1] + " Has WON")
        return
    if board[1][0] == board[1][1] == board[1][2]:
        print("")
        print("Player " + letters[p1] + " Has WON")
        return
    if board[2][0] == board[2][1] == board[2][2]:
        print("")
        print("Player " + letters[p1] + " Has WON")
        return

    if board[0][0] == board[1][0] == board[2][0]:
        print("")
        print("Player " + letters[p1] + " Has WON")
        return
    if board[0][1] == board[1][1] == board[2][1]:
        print("")
        print("Player " + letters[p1] + " Has WON")
        return
    if board[0][2] == board[1][2] == board[2][2]:
        print("")
        print("Player " + letters[p1] + " Has WON")
        return
    if board[0][0] == board[1][1] == board[2][2]:
        print("")
        print("Player " + letters[p1] + " Has WON")
        return
    if board[2][0] == board[1][1] == board[0][2]:
        print("")
        print("Player " + letters[p1] + " Has WON")
        return

    return


main()

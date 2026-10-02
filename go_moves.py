board= []
row= []

def set_board():
    for row in range(0,9):
        for column in range(0,9):
            print(board[row][column], end= "")
        print(end="\n")
for i in range(0,9):
    row= []
    for i in range(0,9):
        row.append(".")
    board.append(row)

set_board()# calls on the board that we just made with all the lopps
player= 1 # makes sure that we know which players turn it is
new_board= []
answer = input(f"Enter your letter-num player {player}: ") # since player was initally set to 1 it will always start by asking player 1 to go
answer.split()

letters=["A", "B", "C", "D", "E", "F", "G", "H", "I"] # we decided to go with using letters-nums because it seemed easier than spliting numbers
while answer != "stop": # once user inputs stop the program will end
    if not(answer in new_board):
        if(answer[0] in letters):
            new_board.append(answer) # stores the players input for the next board
            answer.split()
            row_num=(letters.index(answer[0])) # converts it into an interger based on where on the list the letter is
            column_num=(int(answer[1]) -1)
            if player == 1:
                board[row_num][column_num] = "●" # replaces the . with ● based on the row and column
                player +=1
            else:
                board[row_num][column_num] = "*"
                player -= 1 # we use + and - 1 so that it changes between player 1 and 2 so there is no confusion
            set_board()
            answer = input(f"Enter your letter-num player {player}: ")
    else:
        print(f"There is already a stone there.")
        answer= input(f"Try again player {player}: ")
# this code was make presuming the user would input a capital letter from A to I and a postive number from 1 - 9

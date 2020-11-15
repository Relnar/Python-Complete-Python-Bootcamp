import os
from subprocess import call


def resetGame():
    global player1Turn
    player1Turn = True
    global gameWon
    gameWon = False
    global board
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    global numberOfTurns
    numberOfTurns = len(board) * len(board[0])


def getPlayerTurn():
    global player1Turn
    return 1 if player1Turn else 2


def gameIsADraw():
    global numberOfTurns
    return numberOfTurns <= 0


def validateInput(numberstr):
    number = 0
    if numberstr.isdigit():
        number = int(numberstr)
        return (number in range(1, 11), number)
    return (False, -1)


def getBoardValue(index):
    global board
    return board[index // 3][index % 3]


def setBoardValue(index):
    global board
    board[index // 3][index % 3] = playerValue()


def playerValue():
    global player1Turn
    return "X" if player1Turn else "O"


def checkGameWon(number):
    global board

    # 1  2  3
    # 4  5  6
    # 7  8  9
    row = number // 3
    col = number % 3

    playerVal = playerValue()

    # Horizontal match
    if board[(row + 1) % 3][col] == playerVal and \
            board[(row + 2) % 3][col] == playerVal:
        return True
    # Vertical match
    elif board[row][(col + 1) % 3] == playerVal and \
            board[row][(col + 2) % 3] == playerVal:
        return True
    # Elements on a diagonal are always odd
    elif ((number + 1) % 2) != 0:
        number += 1
        if number == 1:
            return playerVal == board[1][1] and playerVal == board[2][2]
        if number == 3:
            return playerVal == board[1][1] and playerVal == board[2][0]
        if number == 5:
            return ((playerVal == board[0][0] and playerVal == board[2][2]) or \
                    (playerVal == board[2][0] and playerVal == board[0][2]))
        if number == 7:
            return playerVal == board[1][1] and playerVal == board[0][2]
        if number == 9:
            return playerVal == board[1][1] and playerVal == board[0][0]

    return False


def chooseNumber(number):
    global gameWon
    if number > 0 and number <= len(board) * len(board[0]) and \
            gameIsADraw() == False and \
            gameWon == False:
        boardValue = getBoardValue(number - 1)
        if boardValue != 'O' and boardValue != 'X':
            setBoardValue(number - 1)
            gameWon = checkGameWon(number - 1)
            if gameWon:
                return True

            global numberOfTurns
            numberOfTurns -= 1
            global player1Turn
            player1Turn = not player1Turn
            return True

    return False


def clearConsole():
    # check and make call for specific operating system
    _ = call('clear' if os.name == 'posix' else 'cls', shell=True)


def displayBoard():
    clearConsole()
    global board
    for rownumber, row in enumerate(board):
        print("   |   |")
        print(f" {row[0]} | {row[1]} | {row[2]}")
        print("   |   |")
        if rownumber < len(row) - 1:
            print("-----------")


def main():
    resetGame()

    displayBoard()

    global gameWon
    while gameWon == False and gameIsADraw() == False:
        number = 0
        invalidInput = True
        while invalidInput:
            print(f"Player {getPlayerTurn()}, choose number: ")
            numberstr = input()
            result = validateInput(numberstr)
            invalidInput = not result[0]
            number = result[1]

        if chooseNumber(number):
            displayBoard()

    if gameIsADraw():
        print("Game is a draw.")
    else:
        print(f"Player {getPlayerTurn()} won !")


if __name__ == "__main__":
    main()

def readField(fileName):
    with open(fileName, 'r') as f:
        field = [list(line.strip()) for line in f]
    return field

def ifMaximizingChrists(field):
    countX = 0
    countO = 0
    for i in range(3):
        for j in range(3):
            if field[i][j] == 'X':
                countX += 1
            elif field[i][j] == 'O':
                countO += 1
    if countX == countO:
        return True
    else:
        return False

def movesAvailable(field):
    count = 0
    for i in range(3):
        for j in range(3):
            if (field[i][j] == '-'):
                count += 1
    return count

def checkWin(field, player):
    for i in range(3):
        if all(field[i][j] == player for j in range(3)) or \
           all(field[j][i] == player for j in range(3)):
                return True
    if field[0][0] == field[1][1] == field[2][2] == player or field[0][2] == field[1][1] == field[2][0] == player:
        return True
    return False

    
def minimax(field, depth, isMaximizingNow, maximizingPlayer):
    minimizingPlayer = 'O' if (maximizingPlayer == 'X') else 'X'

    if checkWin(field, maximizingPlayer):
        return {'score': 10} 
    elif checkWin(field, minimizingPlayer):
        return {'score': -10}
    elif depth == 0:
        return {'score': 0}

    if isMaximizingNow:
        bestScore = -10000 
        move = None 
        for i in range(3):
            for j in range(3):
                if field[i][j] == '-':
                    field[i][j] = maximizingPlayer 
                    score = minimax(field, depth - 1, False, maximizingPlayer)['score'] 
                    field[i][j] = '-' 
                    if score > bestScore:
                        bestScore = score
                        move = i * 3 + j 
        return {'score': bestScore, 'move': move}
    else:
        bestScore = 10000 
        move = None 
        for i in range(3):
            for j in range(3):
                if field[i][j] == '-': 
                    field[i][j] = minimizingPlayer 
                    score = minimax(field, depth - 1, True, maximizingPlayer)['score']  
                    field[i][j] = '-' #
                    if score < bestScore:
                        bestScore = score
                        move = i * 3 + j
        return {'score': bestScore, 'move': move} 
    
def findBestMove(field):
    isChrists = ifMaximizingChrists(field) 
    maximizingPlayer = 'X' if isChrists else 'O'
    return minimax(field, movesAvailable(field), True, maximizingPlayer) 

def printField(field):
    bestMove = findBestMove(field)['move'] 
    field[bestMove // 3][bestMove % 3] = 'X' if ifMaximizingChrists(field) else 'O'  
    for i in range(len(field)): 
        for j in range(len(field[i])):
            print(field[i][j], end='')
        print("")
    if (checkWin(field, 'X')): 
        print("X Win")
    elif (checkWin(field, 'O')): 
        print("O Win")
    elif (movesAvailable(field) == 0): 
        print("Draw")
    

def main():
    fname = input("Enter the name of the file(with .txt), in which the board is located: ")
    field = readField(fname)
    printField(field)

main()
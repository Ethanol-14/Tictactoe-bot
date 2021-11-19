def superscript(n):
    out = ""
    while(n>0):
        v = n%10
        if(v==1):
            out = "\u00b9" + out
        elif(v==2 or v==3):
            out = chr(ord("\u00b0")+v) + out
        else:
            out = chr(ord("\u2070")+v) + out
        n //= 10
    return out
    
def printBoard(board):
    for i in range(len(board)):
        if(board[i] == ""):
            print(superscript(i+1),end="")
        else:
            print(board[i],end="")
        
        if(i%3<2):
            print("",end="|")
        elif(i<len(board)-1):
            print("\n-+-+-")
        else:
            print()

def getRow(board, row):
    row = row*3
    return [board[row], board[row+1], board[row+2]]

def getCol(board, col):
    return [board[col], board[col+3], board[col+6]]

def getDia(board, dia):
    if dia == 1:
        return [board[6], board[4], board[2]]
    else:
        return [board[0], board[4], board[8]]

def isWinner(line):
    if line[0] == line[1] and line[0] == line[2]:
        if line[0] != "":
            return True
    return False

def determineWinner(board):
    count = 0
    while count < 3:
        if isWinner(getRow(board, count)):
            return getRow(board, count)[0]
        if isWinner(getCol(board, count)):
            return getCol(board, count)[0]
        count = count+1
    if isWinner(getDia(board, 1)):
        return getDia(board, 1)[0]
    if isWinner(getDia(board, 0)):
        return getDia(board, 0)[0]
    return ""

def whoWonAlgo(board):
    count = 0
    while count < 3:
        if isWinner(getRow(board, count)):
            if getRow(board, count)[0] == "X":
                return 1
            else:
                return -1
        if isWinner(getCol(board, count)):
            if getCol(board, count)[0] == "X":
                return 1
            else:
                return -1
        count = count+1
    if isWinner(getDia(board, 1)):
        if getDia(board, 1)[0] == "X":
            return 1
        else:
            return -1
    if isWinner(getDia(board, 0)):
        if getDia(board, 0)[0] == "X":
            return 1
        else:
            return -1
        
    for x in board:
        if x == "":
            return 2
    return 0

def getValidInput(board):
    userInput = 0
    while userInput < 1 or userInput > 9 or board[userInput-1] != "":
        print("Enter a valid tile number from 1 to 9")
        userInput = input()
        try:
            userInput = int(userInput)
        except ValueError:
            userInput = 0
        userInput = int(userInput)
    return userInput-1

def findBestMove(board, playingAsX):
    bestMove = -1

    if playingAsX:
        bestScore = -2
        for x in range(9):
            if board[x] == "":
                board[x] = "X"
                evaluation = minimax(board, 0, False)
                board[x] = ""
                if evaluation > bestScore:
                    bestScore = evaluation
                    bestMove = x
        return bestMove
    else:
        bestScore = 2
        for x in range(9):
            if board[x] == "":
                board[x] = "O"
                evaluation = minimax(board, 0, True)
                board[x] = ""
                if evaluation < bestScore:
                    bestScore = evaluation
                    bestMove = x
        return bestMove
        
def minimax(board, depth, isMaxing):
    result = whoWonAlgo(board)
    if result != 2:
        #print("Depth: "+str(depth)+", Eval: "+str(result))
        #printBoard(board)
        return result
    
    if isMaxing:
        bestScore = -2
        for x in range(9):
            if board[x] == "":
                board[x] = "X"
                evaluation = minimax(board, depth+1, False)
                board[x] = ""
                if evaluation > bestScore:
                    bestScore = evaluation                    
        return bestScore
    else:
        bestScore = 2
        for x in range(9):
            if board[x] == "":
                board[x] = "O"
                evaluation = minimax(board, depth+1, True)
                board[x] = ""
                if evaluation < bestScore:
                    bestScore = evaluation
        return bestScore

algoIsX = False

while(True):
    
    board = [""]*9
    turn = True
    count = 1
    algoIsX = not algoIsX
    
    while(True):
        printBoard(board)
        #GET INPUT
        if(turn):
            print("\nPlayer X's turn")
            if algoIsX:
                t = findBestMove(board, True)
            else:
                t = getValidInput(board)
        else:
            print("\nPlayer O's turn")
            if algoIsX:
                t = getValidInput(board)
            else:
                t = findBestMove(board, False)
        #print("input worked")
        #SET THE BOARD VALUE based on t above
        if(turn):
            board[t] = "X"
        else:
            board[t] = "O"
        #print("turn worked")
        #DETERMINE WINNER IF ANY
        win = determineWinner(board)
        if(win!=""):
            print("\n")
            printBoard(board)
            print("\n")
            print("Player "+win+" won!!")
            break
        #print("win check worked")
        #CHECK IF TIE
        if(count==9):
            print("\n")
            printBoard(board)
            print("\n")
            print("The players drew.")
            break
        #print("tie check worked")
        print("\n\n")

        #print("turn:",turn,"\tt:",t,"\twin:",win,"\tcount:",count) #DELETE ONCE COMPLETED
        #input("..testing pause") #DELETE ONCE COMPLETED

        count += 1
        turn = not(turn)

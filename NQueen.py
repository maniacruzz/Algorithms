def printBoard(board,N):
    for i in range(N):
        for j in range(N):
            print(board[(i,j)],end="   ")
        print()

def isSafe(row,col,rowlookup,slashmatrix,slashlookup,backslashmatrix,backslashlookup):
    if rowlookup[row] or slashlookup[slashmatrix[(row,col)]] or backslashlookup[backslashmatrix[(row,col)]]:
        return False
    return True

def findNQueenUtil(board,N,col,rowlookup,slashmatrix,slashlookup,backslashmatrix,backslashlookup):
    if col>=N:
        return True

    for row in range(N):
        if isSafe(row,col,rowlookup,slashmatrix,slashlookup,backslashmatrix,backslashlookup):
            board[(row,col)]=1
            rowlookup[row]=True
            slashlookup[slashmatrix[(row,col)]]=True
            backslashlookup[backslashmatrix[(row,col)]]=True

            if findNQueenUtil(board,N,col+1,rowlookup,slashmatrix,slashlookup,backslashmatrix,backslashlookup):
                return True

            board[(row,col)]=0
            rowlookup[row]=False
            slashlookup[slashmatrix[(row, col)]] = False
            backslashlookup[backslashmatrix[(row, col)]] = False

    return False

def findNQueen(N):
    board={}
    for i in range(N):
        for j in range(N):
            board[(i,j)]=0
    rowlookup=[False for i in range(N)]
    slashlookup=[False for i in range(2*N-1)]
    backslashlookup=[False for i in range(2*N-1)]

    slashmatrix={}
    backslashmatrix={}

    for i in range(N):
        for j in range(N):
            slashmatrix[(i,j)]=i+j
            backslashmatrix[(i,j)]=i-j+(N-1)

    if not findNQueenUtil(board,N,0,rowlookup,slashmatrix,slashlookup,backslashmatrix,backslashlookup):
        return False
    printBoard(board,N)
    return True

def main():
    N=20
    result=findNQueen(N)
    print(result)

if __name__=="__main__":
    main()
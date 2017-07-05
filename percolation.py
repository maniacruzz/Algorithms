
def isPercolationSuccessful(rows,cols,grid):
    startpoints=set([(0,i) for i in range(cols) if not grid[0][i]])
    endpoints=set([(rows-1,i) for i in range(cols) if not grid[rows-1][i]])
    seen=set()

    for r,c in startpoints:
        seen.add((r,c))
        if checkPercolation(r+1,c,grid,seen,endpoints):
            return True
    return False

def checkPercolation(r,c,grid,seen,endpoints):
    print((r,c))
    if (r,c) in endpoints:
        return True
    if ispassable(r,c,grid,seen):
        seen.add((r, c))
        #check down path
        if checkPercolation(r+1,c,grid,seen,endpoints):
            return True

        #check left path
        if checkPercolation(r,c-1,grid,seen,endpoints):
            return True

        #check right path
        if checkPercolation(r,c+1,grid,seen,endpoints):
            return True
    return False

def ispassable(r,c,grid,seen):
    if (r,c) in seen:
        return False
    if r<len(grid) and c<len(grid[0]):
        return not grid[r][c]
    return False

def main():
    grid=[[1, 1, 0, 0, 0, 1, 1, 0],
          [1, 0, 0, 0, 0, 0, 1, 0],
          [1, 1, 0, 0, 0, 0, 1, 1],
          [0, 1, 0, 1, 0, 1, 1, 1],
          [0, 1, 0, 1, 0, 1, 1, 1],
          [0, 1, 1, 1, 0, 1, 1, 1],
          [0, 1, 0, 0, 1, 0, 1, 0],
          [0, 1, 0, 0, 1, 0, 1, 0]]
    rows,cols=8,8
    result=isPercolationSuccessful(rows,cols,grid)
    print(result)

if __name__=="__main__":
    main()
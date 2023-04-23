"""
The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.

 
Find the minimal path sum from the left column to the right column in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
"""

with open("81-90/matrix82.txt") as file:
    matrix = []
    for line in file:
        matrix.append(list(map(int, line.split(","))))

def minimumPath(grid):
 
    # Dimensions of grid[][]
    N = len(grid)
    M = len(grid[0])
 
    # Stores minimum sum at each cell
    # sum[i][j] from cell sum[0][0]
    minimum = [[0 for _ in range(M)]
              for _ in range(N)]
 
    # Iterate to compute the minimum
    # minimum path in the grid
    for i in range(0, N):
        for j in range(0, M):
            
            if j == 0 and i == 0:
                minimum[i][j] = grid[i][j]
            
            else:
                # Update the minimum path 
                up = minimum[i-1][j] if minimum[i-1][j] != 0 else 10000000
                
                left = minimum[i][j-1] if minimum[i][j-1] != 0 else 10000000

                minimum[i][j] = (min(up + grid[i][j], left + grid[i][j]))

    # Return the minimum 
    return minimum[N-1][M-1]

print(minimumPath(matrix))
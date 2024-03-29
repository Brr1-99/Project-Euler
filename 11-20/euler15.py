"""
Starting in the top left corner of a 2*2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20*20 grid?
"""

grid = [[0 for i in range(21)] for j in range (21)]


for i in range(21):
    grid[i][0] = 1

for j in range(21):
    grid[0][j] = 1

for i in range(21):
    for j in range(21):
        grid[i][j] = grid[i-1][j] + grid[i][j-1]

print(f'The number of ways on a 20*20 grid is : {grid[20][20]/2}')
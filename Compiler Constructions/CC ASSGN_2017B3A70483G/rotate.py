def transpose(grid):
	for i in range(4):
		for j in range(i):
			grid[i][j],grid[j][i] = grid[j][i], grid[i][j]

def rotate90(grid):
	grid.reverse()
	transpose(grid)

def rotate90x(x,grid):
	for i in range(x):
		rotate90(grid)
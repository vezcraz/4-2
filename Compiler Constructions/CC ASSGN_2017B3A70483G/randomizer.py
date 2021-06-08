import random
def getRand(x):
	return random.randint(0,1000000)%x
def placeRandom(grid):
	pos_zeros=[]
	for i in range(4):
		for j in range(4):
			if grid[i][j]==0:
				pos_zeros.append((i,j))
	# print(pos_zeros)
	x, y = pos_zeros[getRand(len(pos_zeros))]
	vec = [2,4]
	grid[x][y]= vec[getRand(2)]
def getRandomInput():
	inp = ['w','s','a','d']
	return inp[getRand(4)]
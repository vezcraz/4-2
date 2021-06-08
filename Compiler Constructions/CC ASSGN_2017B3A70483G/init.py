from randomizer import placeRandom

def initializer(grid, idx):
	for i in range(4):
		tempGrid = []
		tempIdx = []
		for j in range(4):
			tempGrid.append(0)
			tempIdx.append((i+1,j+1))
		grid.append(tempGrid)
		idx.append(tempIdx)
	placeRandom(grid)
	placeRandom(grid)



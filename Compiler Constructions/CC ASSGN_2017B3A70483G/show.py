from stderrPrinter import *
import itertools
def display(grid):
	board  = grid
	for row in board:
		for el in row:
			if el==0:
				print('_', end = '     ')
			else:
				print(el, end='     ')
		print()
		print()

def displayErr(grid, cellToName):
	for i in range(4):
		for j in range(4):
			eprint(grid[i][j],end=' ')

	for i in range(1,5):
		for j in range(1,5):
			if len(cellToName[(i,j)])>0:
				sortedList = list(sorted(cellToName[(i,j)]))
				eprint(f'{i},{j}', end='')
				tempStr = ""
				for el in sortedList:
					tempStr+=f'{el},'
				eprint(tempStr[0:-1], end=' ')
	eprint()
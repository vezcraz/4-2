from rotate import *
import copy
from randomizer import placeRandom
from init import initializer #function to initialize board and scores
from show import * #funntion to display board and scores
import copy
from randomizer import placeRandom,getRandomInput #functions to randomize inputs

print("2048> Hi, I am the 2048-game Engine")
print("2048> The start state is:")

grid=[] #a dictionary to store a single state and its scores
idx=[]
initializer(grid, idx) #initializes the grid with two random values
display(grid)

nameSet = set()
cellToName = {}
for i in range(1,5):
	for j in range(1,5):
		cellToName[(i,j)]=set()
def makeMove( op): 	
	changes=0
	done = set()
	temp = copy.deepcopy(grid)
	for r in range(1,4):
		row=r
		while(row!=0):
			for i in range(4):
				x = idx[row][i]
				nx = idx[row-1][i]
				xSet = copy.deepcopy(cellToName[x])

				if ((row-1,i) in done) or ((row,i) in done) or grid[row][i]==0:
					continue
				elif grid[row-1][i]==0:
					grid[row-1][i]=grid[row][i]
					grid[row][i]=0
					cellToName[nx] = copy.deepcopy(xSet)
					cellToName[x] = set()

				elif grid[row][i]==grid[row-1][i] or op=="ADD":
					done.add((row-1,i))
					if op=="SUBTRACT":
						grid[row-1][i]  = 0
						for nam in cellToName[nx]:
							nameSet.remove(nam)
						for nam in cellToName[x]:
							nameSet.remove(nam)
						cellToName[nx]= set()
					elif op=="MULTIPLY":
						grid[row-1][i]  = grid[row-1][i]*grid[row][i]
						cellToName[nx]|=xSet
					elif op=="DIVIDE":
						grid[row-1][i]  = 1
						cellToName[nx]|=xSet
					else:
						grid[row-1][i]  = grid[row-1][i]+grid[row][i]
						cellToName[nx]|=xSet
					cellToName[x]=set()
					grid[row][i]=0
			row-=1

	if(temp==grid):
		return 0

	placeRandom(grid)
	return 1

rotBy = {"UP":0, "LEFT":1, "DOWN":2,"RIGHT":3}
def updateGrid(x, op):
	rotate90x(rotBy[x], grid)
	rotate90x(rotBy[x], idx)
	changed=makeMove( op)
	rotate90x(4-rotBy[x], grid)
	rotate90x(4-rotBy[x], idx)
	if(changed):
		print(f"2048> Thanks, {x.lower()} move done. Random tile added.")
		print("2048> The current state is: ")
		display(grid)
		displayErr(grid, cellToName)
	else:
		displayErr(grid, cellToName)

def valid(x,y): #check if the cell is inside the grid
	return x>=1 and x<=4 and y>=1 and y<=4

def assignCell(val,x,y):
	if(val>=0 and valid(x,y)):
		grid[x-1][y-1]=val
		if val==0:
			cellToName[(x,y)]=set()
		print("2048> Thanks, assignment done")
		print("2048> The current state is: ")
		display(grid)
		displayErr(grid, cellToName)
	elif(not valid(x,y)):
		print("2048> There is no tile like that. The tile co-ordinates must be in the range 1,2,3,4.")
		eprint(-1)
	elif(val<0):
		print("2048> Cannot assign a negative value to a cell.")
		eprint(-1)


keywords = set([
	'ADD',
	'SUBTRACT',
	'MULTIPLY',
	'DIVIDE',
	'LEFT',
	'RIGHT',
	'UP',
	'DOWN',
	'ASSIGN',
	'TO',
	'VAR',
	'IS',
	'VALUE',
	'IN',

])

def nameCell(x,y,st):
	if grid[x-1][y-1]==0:
		print("2048> Can't assign names to 0 valued cell")
		eprint(-1)
	elif st in keywords:
		print("2048> No, a keyword cannot be a variable name")
		eprint(-1)
	elif st in nameSet:
		print("2048> This name has already been used")
		eprint(-1)
	else:
		print("2048> Thanks, naming done")
		nameSet.add(st)
		cellToName[(x,y)].add(st)
		displayErr(grid,cellToName)

def findVal(x,y):
	if valid(x,y):
		print(f'2048> Value in {x},{y} is: {grid[x-1][y-1]}')
		displayErr(grid,cellToName)
	else:
		print(f'2048> There is no tile like that. The tile co-ordinates must be in the range 1,2,3,4.')
		eprint(-1)








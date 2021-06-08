import os
import copy
import random 
from randomizer import placeRandom,getRandomInput #functions to randomize inputs
from update import updateGrid, assignCell #functions to make moves and update
from show import display #funntion to display board and scores
from parser import parserObj

def getCommand():
	print("2048> Please type a command.")
	inp = input('----> ')
	return inp

while True:
	try:
		inp=getCommand()
	except EOFError:
		break
	except KeyboardInterrupt:
		break
	parserObj.parse(inp)
	
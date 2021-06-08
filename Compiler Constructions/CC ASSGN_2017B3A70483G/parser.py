import ply.lex as lex
import ply.yacc as yacc
from scanner import *
import sys
from update import *
from stderrPrinter import eprint
def p_evaluate(p):
	'''
	evaluate : exp_assign
			 | exp_move
			 | exp_naming
			 | exp_value
			 | no_stop
			 | empty
	'''

def p_exp_assign(p):
	'''
	exp_assign : assignment integer to integer comma integer stop
	'''
	p[0]= (p[2], p[4], p[6])
	run_assign(p[0])

def p_exp_move(p):
	'''
	exp_move : operation move stop
	'''
	p[0]= (p[1],p[2])
	run_move(p[0])

def p_exp_naming(p):
	'''
	exp_naming : var string is integer comma integer stop
			   | var operation is integer comma integer stop
			   | var move is integer comma integer stop
			   | var var is integer comma integer stop
			   | var is is integer comma integer stop
			   | var assignment is integer comma integer stop
	'''
	run_name((p[4],p[6],p[2]))

def p_exp_value(p):
	'''
	exp_value : value in integer comma integer stop

	'''
	run_value((p[3], p[5]))

def p_fullStop(p):
	'''
	no_stop : operation move
            | assignment integer to integer comma integer
            | var string is integer comma integer
            | value in integer comma integer
	'''
	print("2048> You need to end a command with a full-stop")
	eprint(-1)

def p_empty(p):
	'''
	empty :
	'''

def run_assign(p):
	val,x,y = p
	assignCell(val , x, y)

def run_move(p):
	op,direction = p
	updateGrid(direction,op)

def run_name(p):
	x,y,name = p
	nameCell(x,y,name)

def run_value(p):
	findVal(p[0],p[1])

def p_error(p):
	print("2048> Syntax Error")
	eprint(-1)

parserObj = yacc.yacc()


import ply.lex as lex
import ply.yacc as yacc
import sys
from stderrPrinter import eprint
# from update import updateGrid,
tokens = [
	'operation',
	'move',
	'assignment',
	'to',
	'integer',
	'stop',
	'comma',
	'is',
	'string',
	'var',
	'value',
	'in'
]

t_ignore = ' '
def t_operation(t):
	r'ADD|SUBTRACT|MULTIPLY|DIVIDE'
	return t

def t_move(t):
	r'UP|RIGHT|LEFT|DOWN'
	return t
	
def t_assignment(t):
	r'ASSIGN'
	return t
	
def t_stop(t):
	r'\.'
	return t
	
def t_comma(t):
	r'\,'
	return t

def t_var(t):
	r'VAR'
	return t

def t_value(t):
	r'VALUE'
	return t

def t_in(t):
	r'IN'
	return t

def t_is(t):
	r'IS'
	return t

def t_to(t):
	r'TO'
	return t
	
def t_integer(t):
	r'\d+'
	t.value = 	int(t.value)
	return t

def t_string(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*'
	t.type= 'string'
	return t

def t_error(t):
	print("2048> Tokenization error")
	eprint(-1)
	t.lexer.skip(100)


lexer = lex.lex()
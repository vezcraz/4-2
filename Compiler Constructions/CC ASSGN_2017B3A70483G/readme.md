#Compilation and Execution
Run makefile by entering the command `make`
Alternatively, ply library can be installed using `pip3 install ply` and then executing `python3 main.py`

#Files
- *main.py* : This is the driver code (The interpreter shell).
- *scanner.py* : This is the file which uses `ply.lex` module to tokenize the input.
- *parser.py* : This is the parser file which uses `ply.yacc` module to parse the input using grammar rules specified.
- *update.py* : This file handles all the functions to run after a match has been found in the grammar rules.
- *show.py* : Implements functions to display the grid in stdout and stderr as required.
- *stderrPrinter.py* : Implements function to print in stderr.
- *init.py* : Initializes the grid.
- *rotate.py* : Rotates the grid to reuse the function to make a move.

#Assumptions
- The start state has 2 random tiles placed on the grid
- Any two values can be added, however for other operators (subtract, multiply, divide) value of tiles must be same.
- When a row is like: [4,2,2,4] and `ADD LEFT.` is done, then the resultant row is [4,0,4,0] and not [4,4,0,0]

#Starting afresh:
Run `make clean` to remove the files needed for running the codes and start fresh.
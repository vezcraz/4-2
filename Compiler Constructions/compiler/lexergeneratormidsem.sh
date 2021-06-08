# This shell-script generates the lexer that is required to be designed
# in response to the mid-sem exam question given to
# the CS F363 Compiler Construction class of
# Birla Institute of Technology and Science Pilani (BITS Pilani)
# K K Birla Goa Campus, GOA INDIA
# in Semester II, 2020-21.
#
# It takes as input the seed parameter, an ID number.
# The target language to be scanned is a set of ID numbers
# related structurally to this ID number, and
# that structural relation fits into a regexp.
# That means, it is a regular lagnuage.
#
# This script invokes a C program that does the generation. Then it is compiled into a scanner exec.
#

echo flex -o mylexer$1.c mylexer$1.lex
flex -o mylexer$1.c mylexer$1.lex
echo Compiling the C program into an exec
echo gcc -Wall -o xmylexer$1 mylexer$1.c
gcc -Wall -o xmylexer$1 mylexer$1.c
echo Executing the built scanner exec
echo ./xmylexer$1 \< inputfile.txt
./xmylexer$1 < inputfile.txt

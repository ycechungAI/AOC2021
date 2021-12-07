# The first line of the input file is a comma-separated list of numbers.
# These numbers are the numbers that will be drawn from the board.
# The rest of the input file is a series of boards.
# Each board is separated by a blank line.
# Each board is a square matrix of characters.
# The characters are either "X", "O", or ".".
import numpy as np
from itertools import product

# The program iterates over each combination of the numbers in the first
# line and each board.
with open("input.txt") as fp:
	draws = list(map(int, fp.readline().split(",")))
	boards = [np.mat(board.replace("\n", ";")) 
	for board in fp.read()[1:-1].split("\n\n")]
	
# For each combination, the program masks the board.
# The program masks the board by setting the value of the board at each
# location where the number drawn is equal to the number on the board to
# "X" as well as "O".
# The program checks if the board has been masked such that the sum of
#  the masked board along the 0th axis is equal to 5.
# The program checks if the board has been masked such that the sum of
#  the masked board along the 1st axis is equal to 5.
for draw, board in product(draws, [np.ma.masked_array(board) for board in boards]):
	board.mask |= board.data == draw
	if np.any(board.mask.sum(0) == 5) or np.any(board.mask.sum(1) == 5):
	# Calculates the product of the masked board and the number drawn
		result = board.sum()*draw
		break
# print result
print(result)
